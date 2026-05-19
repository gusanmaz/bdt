#!/usr/bin/env python3
"""Write a handbook chapter HTML file from a body fragment."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from chapter_page import page_shell

ROOT = Path(__file__).resolve().parent.parent

CHAPTERS = {
    # slug -> meta
    "01-ipython/00-introduction": {
        "title": "IPython: Sıradan Python'un Ötesinde",
        "chapter": "01-ipython",
        "section": "00-introduction",
        "url": "https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html",
        "label": "01.00 IPython Beyond Normal Python",
        "numpy": False,
    },
}


def write(slug: str, body: str, meta: dict):
    out = ROOT / "chapters" / f"{slug}.html"
    html = page_shell(
        title=meta["title"],
        chapter=meta["chapter"],
        section=meta["section"],
        source_en_url=meta["url"],
        source_en_label=meta["label"],
        body_html=body,
        preload_numpy=meta.get("numpy", False),
        pyodide=meta.get("pyodide", True),
    )
    out.write_text(html, encoding="utf-8")
    print("wrote", out)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: write_chapter.py <slug>  (reads body from stdin)")
        sys.exit(1)
    slug = sys.argv[1]
    meta = CHAPTERS.get(slug)
    if not meta:
        print("unknown slug", slug)
        sys.exit(1)
    write(slug, sys.stdin.read(), meta)
