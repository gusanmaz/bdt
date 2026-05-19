#!/usr/bin/env python3
"""Write a Scikit-Learn handbook chapter HTML file."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from chapter_page import page_shell
from sklearn_sections import SKLEARN_CHAPTER, SKLEARN_SECTIONS

ROOT = Path(__file__).resolve().parent.parent


def meta_for_slug(slug: str) -> dict:
    for sec in SKLEARN_SECTIONS:
        if sec["slug"] == slug:
            return sec
    raise KeyError(slug)


def write_chapter(slug: str, body: str) -> Path:
    sec = meta_for_slug(slug)
    out = ROOT / "chapters" / SKLEARN_CHAPTER / f"{slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    html = page_shell(
        title=sec["title"],
        chapter=SKLEARN_CHAPTER,
        section=slug,
        source_en_url=sec["en_url"],
        source_en_label=sec["en_label"],
        body_html=body,
        preload_sklearn=sec.get("preload_sklearn", True),
    )
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: write_sklearn_chapter.py <slug>  (body from stdin)")
        sys.exit(1)
    path = write_chapter(sys.argv[1], sys.stdin.read())
    print("wrote", path.relative_to(ROOT))
