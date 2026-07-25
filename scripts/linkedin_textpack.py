#!/usr/bin/env python3
"""Fetch a public LinkedIn article and build an Omnighost TextPack."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import time
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser
from markdownify import markdownify

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)
ARTICLE_URL = re.compile(r"https?://(?:[\w-]+\.)?linkedin\.com/pulse/[^?#\"'\s<]+", re.I)


def clean_url(url: str) -> str:
    parts = urlsplit(url.strip())
    if parts.scheme not in {"http", "https"} or not parts.netloc.endswith("linkedin.com"):
        raise ValueError("Expected a linkedin.com http(s) URL")
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), "", ""))


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value[:100] or "linkedin-post"


def promote_section_headings(markdown: str) -> str:
    """Restore headings flattened by LinkedIn's schema.org articleBody.

    LinkedIn emits section labels as standalone short paragraphs rather than
    preserving their heading level. Real prose in these articles ends with
    sentence punctuation; section labels are short and either have no terminal
    punctuation or are phrased as a question.
    """
    paragraphs = markdown.split("\n\n")
    output = []
    for paragraph in paragraphs:
        text = paragraph.strip()
        words = text.split()
        is_plain_line = "\n" not in text and not text.startswith(("#", "-", ">", "!["))
        heading_shape = (
            2 <= len(words) <= 10
            and len(text) <= 90
            and (text.endswith("?") or text[-1:] not in ".!:;")
        )
        if is_plain_line and heading_shape:
            output.append(f"## {text}")
        else:
            output.append(paragraph)
    return "\n\n".join(output)


def fetch(session: requests.Session, url: str, *, binary: bool = False):
    response = session.get(url, timeout=45, allow_redirects=True)
    response.raise_for_status()
    if not binary:
        lowered = response.text.lower()
        if response.status_code == 999 or "authwall" in response.url or (
            "sign in" in lowered and "articlebody" not in lowered and len(response.text) < 50_000
        ):
            raise RuntimeError("LinkedIn returned a sign-in wall instead of the public article")
    return response


def jsonld_objects(soup: BeautifulSoup):
    for node in soup.select('script[type="application/ld+json"]'):
        try:
            raw = json.loads(node.string or node.get_text())
        except (json.JSONDecodeError, TypeError):
            continue
        queue = raw if isinstance(raw, list) else [raw]
        while queue:
            item = queue.pop(0)
            if isinstance(item, dict):
                yield item
                graph = item.get("@graph")
                if isinstance(graph, list):
                    queue.extend(graph)


def meta(soup: BeautifulSoup, *names: str) -> str:
    for name in names:
        node = soup.find("meta", attrs={"property": name}) or soup.find(
            "meta", attrs={"name": name}
        )
        if node and node.get("content"):
            return node["content"].strip()
    return ""


def extract(html: str, source_url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    data = {}
    for obj in jsonld_objects(soup):
        kind = obj.get("@type", "")
        kinds = kind if isinstance(kind, list) else [kind]
        if any(k in {"Article", "NewsArticle", "SocialMediaPosting"} for k in kinds):
            data = obj
            break

    # LinkedIn's JSON-LD "headline" is sometimes the opening paragraph rather
    # than the visible article title. The public page's h1 is authoritative.
    title = (
        (soup.h1.get_text(" ", strip=True) if soup.h1 else "")
        or meta(soup, "og:title", "twitter:title")
        or data.get("headline")
    )
    author_value = data.get("author", "")
    if isinstance(author_value, dict):
        author = author_value.get("name", "")
    elif isinstance(author_value, list):
        author = ", ".join(
            a.get("name", "") if isinstance(a, dict) else str(a) for a in author_value
        )
    else:
        author = str(author_value)
    author = author or meta(soup, "author") or "Slava Tykhonov"
    published = data.get("datePublished") or meta(
        soup, "article:published_time", "datePublished"
    )
    description = data.get("description") or meta(soup, "og:description", "description")
    cover = data.get("image") or meta(soup, "og:image", "twitter:image")
    if isinstance(cover, dict):
        cover = cover.get("url", "")
    elif isinstance(cover, list):
        cover = cover[0] if cover else ""

    body = data.get("articleBody", "")
    content_node = None
    selectors = (
        ".article-main__content",
        ".article-content",
        "[data-test-id='article-content']",
        "article",
    )
    for selector in selectors:
        candidate = soup.select_one(selector)
        if candidate and len(candidate.get_text(" ", strip=True)) > 500:
            content_node = candidate
            break

    images = []
    # Prefer schema.org articleBody when LinkedIn provides it: the surrounding
    # <article> element also contains its title, author card, avatar, follow
    # button, and publication chrome, none of which belongs in Ghost content.
    if body:
        paragraphs = [p.strip() for p in re.split(r"\n{1,}", body) if p.strip()]
        body_md = "\n\n".join(paragraphs)
        images = []
    elif content_node:
        for unwanted in content_node.select("script, style, nav, form, button"):
            unwanted.decompose()
        for img in content_node.find_all("img"):
            src = img.get("data-delayed-url") or img.get("data-src") or img.get("src")
            if src:
                absolute = urljoin(source_url, src)
                img["src"] = absolute
                images.append((absolute, img.get("alt", "").strip()))
        body_md = markdownify(str(content_node), heading_style="ATX", bullets="-")
    else:
        raise RuntimeError(
            "Could not locate the public article body. LinkedIn may have changed its HTML."
        )

    body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip()
    # Ghost's theme already renders title, excerpt, author, date, and feature
    # image. LinkedIn often wraps the prose in an <article> that begins with
    # those same presentation elements. Its og:description is the first real
    # paragraph, so use that as the strict content boundary.
    if description:
        start = body_md.find(description)
        if start > 0:
            body_md = body_md[start:].strip()
    body_md = promote_section_headings(body_md)
    # Do not download author avatars or other LinkedIn chrome removed above.
    images = [(url, alt) for url, alt in images if url in body_md]
    if len(re.sub(r"\s+", "", body_md)) < 500:
        raise RuntimeError("Extracted article body is suspiciously short; refusing partial output")

    return {
        "title": title.strip(),
        "author": author.strip(),
        "published": published,
        "description": description.strip(),
        "cover": str(cover),
        "body": body_md,
        "images": images,
        "source_url": source_url,
    }


def image_extension(content_type: str, url: str) -> str:
    known = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp", "image/gif": ".gif"}
    if content_type.split(";")[0] in known:
        return known[content_type.split(";")[0]]
    ext = Path(urlsplit(url).path).suffix.lower()
    return ext if ext in {".jpg", ".jpeg", ".png", ".webp", ".gif"} else ".jpg"


def download_image(session: requests.Session, url: str, assets: Path, index: int) -> str | None:
    try:
        response = fetch(session, url, binary=True)
        if not response.headers.get("content-type", "").startswith("image/"):
            return None
        digest = hashlib.sha256(response.content).hexdigest()[:10]
        name = f"image-{index:02d}-{digest}{image_extension(response.headers.get('content-type', ''), url)}"
        (assets / name).write_bytes(response.content)
        return name
    except requests.RequestException as exc:
        print(f"warning: could not download image {url}: {exc}", file=sys.stderr)
        return None


def build(url: str, out_root: Path, blog: str, tags: list[str]) -> Path:
    source_url = clean_url(url)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})
    article = extract(fetch(session, source_url).text, source_url)
    slug = slugify(article["title"])
    post_dir = out_root / slug
    assets = post_dir / "assets"
    dist = post_dir / "dist"
    assets.mkdir(parents=True, exist_ok=True)
    dist.mkdir(parents=True, exist_ok=True)

    for old in assets.iterdir():
        if old.is_file():
            old.unlink()

    replacements = {}
    candidates = []
    if article["cover"]:
        candidates.append((article["cover"], article["title"]))
    candidates.extend(article["images"])
    seen = set()
    for url_value, alt in candidates:
        if url_value in seen:
            continue
        seen.add(url_value)
        local = download_image(session, url_value, assets, len(seen))
        if local:
            replacements[url_value] = (local, alt)
        time.sleep(0.2)

    body = article["body"]
    for remote, (local, _) in replacements.items():
        body = body.replace(f"]({remote})", f"](assets/{local})")
    feature_image = ""
    if article["cover"] in replacements:
        feature_image = f"assets/{replacements[article['cover']][0]}"
        # LinkedIn commonly repeats its cover inside the article DOM. Ghost
        # renders feature_image separately, so remove every inline copy.
        body = re.sub(
            rf"!\[[^\]]*\]\({re.escape(feature_image)}\)\s*",
            "",
            body,
        ).strip()

    date = ""
    if article["published"]:
        try:
            date = date_parser.parse(article["published"]).date().isoformat()
        except (ValueError, TypeError):
            date = str(article["published"])
    frontmatter = {
        "title": article["title"],
        "author": article["author"],
        "date": date,
        "source": source_url,
        "tags": tags,
    }
    yaml_lines = ["---"] + [
        f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in frontmatter.items()
    ] + ["---", ""]
    markdown = "\n".join(yaml_lines)
    markdown += body.rstrip() + f"\n\n---\n\n[Originally published on LinkedIn]({source_url}).\n"
    (post_dir / "post.md").write_text(markdown, encoding="utf-8")

    metadata = {
        "title": article["title"],
        "author": article["author"],
        "published": date,
        "source_url": source_url,
        "slug": slug,
        "newsletter": "Croissant, Graphs and AI",
        "feature_image": feature_image,
    }
    (post_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    info = {
        "version": 2,
        "type": "net.daringfireball.markdown",
        "transient": False,
        "omnighost": {
            "blog": blog,
            "slug": slug,
            "tags": tags,
            "excerpt": article["description"],
            "source": source_url,
            "author": article["author"],
            "published_at": date,
        },
    }
    pack = dist / f"{slug}.textpack"
    with tempfile.TemporaryDirectory() as tmp:
        bundle = Path(tmp) / f"{slug}.textbundle"
        bundle_assets = bundle / "assets"
        bundle_assets.mkdir(parents=True)
        (bundle / "text.markdown").write_text(markdown, encoding="utf-8")
        (bundle / "info.json").write_text(
            json.dumps(info, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        for image in assets.iterdir():
            if image.is_file():
                shutil.copy2(image, bundle_assets / image.name)
        with zipfile.ZipFile(pack, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(bundle.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(Path(tmp)))
    with zipfile.ZipFile(pack) as archive:
        prefix = f"{slug}.textbundle/"
        if not archive.namelist() or any(not n.startswith(prefix) for n in archive.namelist()):
            raise RuntimeError("Invalid TextPack layout")

    output = {"slug": slug, "post_dir": str(post_dir), "textpack": str(pack), **metadata}
    Path(os.environ.get("GITHUB_OUTPUT", post_dir / "github-output.txt")).open("a").write(
        "\n".join(f"{k}={v}" for k, v in output.items()) + "\n"
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return pack


def discover(config_path: Path, out_root: Path, blog: str, tags: list[str]) -> list[str]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})
    urls = {clean_url(config["seed_url"])}
    for page_url in (config.get("newsletter_url"), config.get("seed_url")):
        if not page_url:
            continue
        try:
            html = fetch(session, page_url).text
        except Exception as exc:
            print(f"warning: discovery page failed: {page_url}: {exc}", file=sys.stderr)
            continue
        for match in ARTICLE_URL.findall(html.replace("\\/", "/")):
            urls.add(clean_url(match))

    built = []
    known_sources = {
        json.loads(p.read_text(encoding="utf-8")).get("source_url")
        for p in out_root.glob("*/metadata.json")
    }
    for candidate in sorted(urls):
        if candidate in known_sources:
            continue
        try:
            built.append(str(build(candidate, out_root, blog, tags)))
        except Exception as exc:
            print(f"warning: candidate failed: {candidate}: {exc}", file=sys.stderr)
    if not built:
        print("No new publicly discoverable editions.")
    return built


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs="?")
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--config", default="config.json")
    parser.add_argument("--out-root", default="posts")
    parser.add_argument("--blog", default="querygraph.ai")
    parser.add_argument("--tags", default="Slava Tykhonov;Croissant, Graphs and AI;AI")
    args = parser.parse_args()
    separator = ";" if ";" in args.tags else ","
    tags = [tag.strip() for tag in args.tags.split(separator) if tag.strip()]
    if args.discover:
        discover(Path(args.config), Path(args.out_root), args.blog, tags)
    elif args.url:
        build(args.url, Path(args.out_root), args.blog, tags)
    else:
        parser.error("provide a LinkedIn URL or --discover")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
