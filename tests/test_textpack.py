import importlib.util
import json
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "linkedin_textpack.py"
SPEC = importlib.util.spec_from_file_location("linkedin_textpack", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_clean_url_removes_tracking():
    assert MODULE.clean_url(
        "https://www.linkedin.com/pulse/example-slug?utm_source=share"
    ) == "https://www.linkedin.com/pulse/example-slug"


def test_slugify():
    assert MODULE.slugify("Europe’s AI Future: Different!") == "europes-ai-future-different"


def test_extract_jsonld_article():
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "A Useful Title",
        "author": {"@type": "Person", "name": "Slava Tykhonov"},
        "datePublished": "2026-07-24",
        "articleBody": "This is a sufficiently long paragraph. " * 40,
    }
    html = (
        '<html><head><script type="application/ld+json">'
        + json.dumps(article)
        + "</script></head><body></body></html>"
    )
    result = MODULE.extract(html, "https://www.linkedin.com/pulse/example")
    assert result["title"] == "A Useful Title"
    assert result["author"] == "Slava Tykhonov"
    assert "sufficiently long" in result["body"]
