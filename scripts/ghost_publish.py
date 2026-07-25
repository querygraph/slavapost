#!/usr/bin/env python3
"""Create or update a Ghost post from a generated SlavaPost directory."""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import mimetypes
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote

import markdown
import requests


def b64url(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).rstrip(b"=").decode()


def token(admin_key: str) -> str:
    try:
        key_id, secret = admin_key.strip().split(":", 1)
        secret_bytes = bytes.fromhex(secret)
    except ValueError as exc:
        raise ValueError("GHOST_ADMIN_API_KEY must have the form id:hexsecret") from exc
    now = int(time.time())
    header = b64url(json.dumps({"alg": "HS256", "typ": "JWT", "kid": key_id}, separators=(",", ":")).encode())
    payload = b64url(json.dumps({"iat": now, "exp": now + 300, "aud": "/admin/"}, separators=(",", ":")).encode())
    signature = b64url(hmac.new(secret_bytes, f"{header}.{payload}".encode(), hashlib.sha256).digest())
    return f"{header}.{payload}.{signature}"


class Ghost:
    def __init__(self, url: str, admin_key: str):
        self.base = url.rstrip("/") + "/ghost/api/admin"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Ghost {token(admin_key)}",
                "Accept-Version": "v5.0",
                "User-Agent": "SlavaPost-GitHub-Action/1.0",
            }
        )

    def request(self, method: str, path: str, **kwargs):
        response = self.session.request(method, self.base + path, timeout=60, **kwargs)
        if not response.ok:
            detail = response.text[:1000]
            raise RuntimeError(f"Ghost {method} {path} failed ({response.status_code}): {detail}")
        return response.json()

    def find_existing(self, slug: str, source_url: str):
        data = self.request(
            "GET",
            "/posts/",
            params={"limit": "all", "formats": "html"},
        )
        posts = data.get("posts", [])
        # Source identity survives title/slug corrections and prevents a bad
        # first import from becoming a permanent duplicate.
        by_source = [
            post for post in posts
            if post.get("canonical_url", "").rstrip("/") == source_url.rstrip("/")
        ]
        if by_source:
            return by_source[0]
        by_slug = [post for post in posts if post.get("slug") == slug]
        return by_slug[0] if by_slug else None

    def find_user(self, name: str):
        data = self.request("GET", "/users/", params={"limit": "all"})
        exact = [
            user for user in data.get("users", [])
            if user.get("name", "").strip().casefold() == name.strip().casefold()
        ]
        if not exact:
            raise RuntimeError(
                f'Ghost staff author "{name}" was not found. Add this person '
                "under Ghost Settings → Staff, then rerun the workflow."
            )
        return exact[0]

    def upload(self, path: Path) -> str:
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        with path.open("rb") as handle:
            data = self.request(
                "POST",
                "/images/upload/",
                files={"file": (path.name, handle, mime)},
                data={"purpose": "image", "ref": str(path)},
            )
        return data["images"][0]["url"]

    def publish(self, payload: dict, existing: dict | None):
        if existing:
            payload["updated_at"] = existing["updated_at"]
            return self.request(
                "PUT",
                f"/posts/{existing['id']}/",
                params={"source": "html"},
                json={"posts": [payload]},
            )["posts"][0]
        return self.request(
            "POST", "/posts/", params={"source": "html"}, json={"posts": [payload]}
        )["posts"][0]


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)


def publish(post_path: Path, status: str, ghost_url: str, admin_key: str) -> dict:
    post_dir = post_path.parent
    metadata = json.loads((post_dir / "metadata.json").read_text(encoding="utf-8"))
    text = strip_frontmatter(post_path.read_text(encoding="utf-8"))
    ghost = Ghost(ghost_url, admin_key)

    uploaded = {}
    for relative in sorted(set(re.findall(r"\]\((assets/[^)\s]+)\)", text))):
        local = post_dir / relative
        if not local.is_file():
            raise RuntimeError(f"Referenced image is missing: {local}")
        uploaded[relative] = ghost.upload(local)
    feature_image = metadata.get("feature_image", "")
    if feature_image and feature_image not in uploaded:
        local = post_dir / feature_image
        if not local.is_file():
            raise RuntimeError(f"Feature image is missing: {local}")
        uploaded[feature_image] = ghost.upload(local)
    for relative, remote in uploaded.items():
        text = text.replace(f"]({relative})", f"]({remote})")

    html = markdown.markdown(
        text,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )
    existing = ghost.find_existing(metadata["slug"], metadata["source_url"])
    author = ghost.find_user(metadata["author"])
    excerpt = ""
    info_path = post_dir / "dist" / f"{metadata['slug']}.textpack"
    if info_path.exists():
        import zipfile

        with zipfile.ZipFile(info_path) as archive:
            bundle = f"{metadata['slug']}.textbundle/info.json"
            info = json.loads(archive.read(bundle))
            excerpt = info.get("omnighost", {}).get("excerpt", "")
    tags = [
        {"name": tag}
        for tag in ["Slava Tykhonov", "Croissant, Graphs and AI", "AI"]
    ]
    payload = {
        "title": metadata["title"],
        "slug": metadata["slug"],
        "html": html,
        "status": status,
        "tags": tags,
        "custom_excerpt": excerpt[:300] or None,
        "canonical_url": metadata["source_url"],
        "authors": [{"id": author["id"]}],
    }
    if feature_image:
        payload["feature_image"] = uploaded[feature_image]
        payload["feature_image_alt"] = metadata["title"]
    if status == "published" and metadata.get("published"):
        # LinkedIn exposes the calendar date but not a stable publication time.
        # Noon UTC preserves that date in Ghost across practical time zones.
        payload["published_at"] = f"{metadata['published']}T12:00:00.000Z"
    result = ghost.publish(payload, existing)
    output = {
        "id": result["id"],
        "slug": result["slug"],
        "status": result["status"],
        "url": result.get("url", ""),
        "updated": bool(existing),
    }
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as handle:
            for key, value in output.items():
                handle.write(f"ghost_{key}={str(value).lower() if isinstance(value, bool) else value}\n")
    print(json.dumps(output, indent=2))
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("post", type=Path, help="Generated posts/<slug>/post.md")
    parser.add_argument("--status", choices=["draft", "published"], default="published")
    args = parser.parse_args()
    ghost_url = os.environ.get("GHOST_ADMIN_URL", "")
    admin_key = os.environ.get("GHOST_ADMIN_API_KEY", "")
    if not ghost_url or not admin_key:
        parser.error("GHOST_ADMIN_URL and GHOST_ADMIN_API_KEY are required")
    publish(args.post, args.status, ghost_url, admin_key)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
