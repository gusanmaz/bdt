#!/usr/bin/env python3
"""Generate Turkish Jupyter notebooks from handbook HTML chapter pages."""
from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters"
OUT = ROOT / "notebooks"

SECTIONS = [
    ("01-ipython", "00-introduction"),
    ("01-ipython", "01-help-and-documentation"),
    ("01-ipython", "02-keyboard-shortcuts"),
    ("01-ipython", "03-magic-commands"),
    ("01-ipython", "04-input-output-history"),
    ("01-ipython", "05-shell-commands"),
    ("01-ipython", "06-errors-and-debugging"),
    ("01-ipython", "07-timing-and-profiling"),
    ("01-ipython", "08-more-resources"),
    ("02-numpy", "00-introduction"),
    ("02-numpy", "01-understanding-data-types"),
    ("02-numpy", "02-basics-of-numpy-arrays"),
    ("02-numpy", "03-computation-ufuncs"),
    ("02-numpy", "04-aggregates"),
    ("02-numpy", "05-broadcasting"),
    ("02-numpy", "06-boolean-masks"),
    ("02-numpy", "07-fancy-indexing"),
    ("02-numpy", "08-sorting"),
    ("02-numpy", "09-structured-arrays"),
]

try:
    from pandas_sections import PANDAS_CHAPTER, PANDAS_SECTIONS

    SECTIONS.extend((PANDAS_CHAPTER, s["slug"]) for s in PANDAS_SECTIONS)
except ImportError:
    pass

try:
    from matplotlib_sections import MPL_CHAPTER, MPL_SECTIONS

    SECTIONS.extend((MPL_CHAPTER, s["slug"]) for s in MPL_SECTIONS)
except ImportError:
    pass

try:
    from sklearn_sections import SKLEARN_CHAPTER, SKLEARN_SECTIONS

    SECTIONS.extend((SKLEARN_CHAPTER, s["slug"]) for s in SKLEARN_SECTIONS)
except ImportError:
    pass

MAIN_RE = re.compile(
    r'<main\s+class="content handbook-content">(.*?)</main>',
    re.DOTALL | re.IGNORECASE,
)
TAG_RE = re.compile(r"<\s*(/\s*)?([a-zA-Z0-9:-]+)([^>]*)>", re.DOTALL)
ATTR_RE = re.compile(
    r'([a-zA-Z0-9:-]+)\s*=\s*("([^"]*)"|\'([^\']*)\'|([^\s"\'=<>`]+))'
)


def parse_attrs(raw: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for m in ATTR_RE.finditer(raw):
        key = m.group(1).lower()
        val = m.group(3) or m.group(4) or m.group(5) or ""
        attrs[key] = unescape(val)
    return attrs


def strip_tags(html: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return unescape(re.sub(r"\n{3,}", "\n\n", text)).strip()


def inline_md(html: str) -> str:
    html = re.sub(
        r"<code[^>]*>(.*?)</code>",
        lambda m: f"`{strip_tags(m.group(1))}`",
        html,
        flags=re.S | re.I,
    )
    html = re.sub(
        r"<strong[^>]*>(.*?)</strong>",
        lambda m: f"**{inline_md(m.group(1))}**",
        html,
        flags=re.S | re.I,
    )
    html = re.sub(
        r"<em[^>]*>(.*?)</em>",
        lambda m: f"*{inline_md(m.group(1))}*",
        html,
        flags=re.S | re.I,
    )
    html = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f"[{inline_md(m.group(2))}]({m.group(1)})",
        html,
        flags=re.S | re.I,
    )
    html = re.sub(
        r"<kbd[^>]*>(.*?)</kbd>",
        lambda m: f"`{strip_tags(m.group(1))}`",
        html,
        flags=re.S | re.I,
    )
    return strip_tags(html)


def extract_main(html: str) -> str:
    m = MAIN_RE.search(html)
    if not m:
        raise ValueError("main.handbook-content not found")
    return m.group(1)


def find_balanced(html: str, start: int) -> tuple[str, str, str, int]:
    """Return (tag, attrs_raw, inner, end_pos) for element starting at start."""
    open_m = TAG_RE.match(html, start)
    if not open_m or open_m.group(1):
        raise ValueError("expected open tag")
    tag = open_m.group(2).lower()
    attrs_raw = open_m.group(3) or ""
    pos = open_m.end()
    depth = 1
    inner_parts: list[str] = []
    while pos < len(html) and depth > 0:
        m = TAG_RE.search(html, pos)
        if not m:
            break
        if not m.group(1):
            t = m.group(2).lower()
            if t == tag:
                depth += 1
            inner_parts.append(html[pos : m.start()])
            pos = m.end()
            continue
        t = m.group(2).lower()
        inner_parts.append(html[pos : m.start()])
        pos = m.end()
        if t == tag:
            depth -= 1
    inner = "".join(inner_parts)
    return tag, attrs_raw, inner, pos


def iter_top_level_blocks(fragment: str):
    pos = 0
    n = len(fragment)
    while pos < n:
        while pos < n and fragment[pos].isspace():
            pos += 1
        if pos >= n:
            break
        if fragment[pos] != "<":
            end = fragment.find("<", pos)
            text = fragment[pos:end if end != -1 else n]
            if text.strip():
                yield ("text", text.strip())
            pos = end if end != -1 else n
            continue
        m = TAG_RE.match(fragment, pos)
        if not m or m.group(1):
            pos += 1
            continue
        tag, attrs_raw, inner, end = find_balanced(fragment, pos)
        attrs = parse_attrs(attrs_raw)
        yield ("element", tag, attrs, inner)
        pos = end


def code_from_block(inner: str, attrs: dict) -> tuple[str, str, bool]:
    lang = (attrs.get("data-lang") or "text").lower()
    readonly = attrs.get("data-readonly") == "true"
    filename = attrs.get("data-filename") or ""
    m = re.search(r"<pre[^>]*>\s*(?:<code[^>]*>)?(.*?)(?:</code>\s*)?</pre>", inner, re.S | re.I)
    text = unescape(m.group(1)) if m else strip_tags(inner)
    text = text.replace("\r\n", "\n").rstrip() + "\n"
    if filename and lang in ("python", "py") and not text.lstrip().startswith("#"):
        text = f"# {filename}\n{text}"
    return text, lang, readonly


def table_to_md(inner: str) -> str:
    rows = []
    for tr in re.finditer(r"<tr[^>]*>(.*?)</tr>", inner, re.S | re.I):
        cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr.group(1), re.S | re.I)
        if cells:
            row = [inline_md(c).replace("|", "\\|") for c in cells]
            rows.append("| " + " | ".join(row) + " |")
    if not rows:
        return ""
    if len(rows) > 1:
        ncols = rows[0].count("|") - 1
        rows.insert(1, "| " + " | ".join(["---"] * ncols) + " |")
    return "\n".join(rows)


def alert_to_md(inner: str) -> str:
    title_m = re.search(r'class="alert-title"[^>]*>(.*?)</', inner, re.S | re.I)
    title = inline_md(title_m.group(1)) if title_m else "Not"
    if "Sonraki konu" in title:
        return ""
    parts = [inline_md(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", inner, re.S | re.I)]
    body = "\n\n".join(p for p in parts if p)
    lines = [f"> **{title}**", ">"]
    for line in body.splitlines():
        lines.append(f"> {line}" if line else ">")
    return "\n".join(lines)


def figure_to_md(inner: str) -> str:
    img = re.search(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"', inner, re.I)
    if not img:
        img = re.search(r"<img[^>]*src=\"([^\"]*)\"", inner, re.I)
        if not img:
            return ""
        src, alt = img.group(1), "Şekil"
    else:
        src, alt = img.group(1), img.group(2)
    cap_m = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", inner, re.S | re.I)
    md = f"![{alt}]({src})"
    if cap_m:
        md += f"\n\n*{inline_md(cap_m.group(1))}*"
    return md


def is_runnable_python(lang: str, readonly: bool, code: str) -> bool:
    if readonly or lang not in ("python", "py"):
        return False
    first = code.lstrip().splitlines()[0] if code.strip() else ""
    if first.startswith("%") or first.startswith("!") or first.startswith("%%"):
        return False
    return True


class CellBuilder:
    def __init__(self) -> None:
        self.cells: list[dict] = []
        self._md: list[str] = []

    def flush_md(self) -> None:
        if not self._md:
            return
        text = "\n\n".join(p for p in self._md if p.strip())
        if text.strip():
            self.cells.append(md_cell(text))
        self._md = []

    def add_md(self, text: str) -> None:
        if text.strip():
            self._md.append(text.strip())

    def add_code(self, code: str, lang: str, readonly: bool) -> None:
        self.flush_md()
        if is_runnable_python(lang, readonly, code):
            self.cells.append(code_cell(code))
        else:
            fence = lang if lang not in ("text", "plaintext") else ""
            note = ""
            if readonly and lang in ("python", "py"):
                note = "\n\n*(Jupyter/IPython veya özel ortam gerekir — web sayfasında salt okunur.)*"
            elif lang in ("bash", "shell", "sh"):
                note = "\n\n*(Kabuk komutu — terminal veya Jupyter `!` ile.)*"
            self.add_md(f"```{fence}\n{code.rstrip()}\n```{note}")
            self.flush_md()

    def finish(self) -> list[dict]:
        self.flush_md()
        return self.cells


def class_list(attrs: dict) -> set[str]:
    return set((attrs.get("class") or "").split())


def process_blocks(fragment: str, builder: CellBuilder, skip_h1: bool = False) -> None:
    for item in iter_top_level_blocks(fragment):
        if item[0] == "text":
            builder.add_md(item[1])
            continue
        _, tag, attrs, inner = item
        classes = class_list(attrs)

        if "handbook-attribution" in classes:
            continue
        if tag == "h1" and skip_h1:
            continue
        if tag == "h1":
            builder.add_md(f"# {strip_tags(inner)}")
            continue
        if tag == "h2":
            builder.add_md(f"## {strip_tags(inner)}")
            continue
        if tag == "h3":
            builder.add_md(f"### {strip_tags(inner)}")
            continue
        if tag == "h4":
            builder.add_md(f"#### {strip_tags(inner)}")
            continue
        if tag == "p":
            builder.add_md(inline_md(inner))
            continue
        if tag == "hr":
            builder.add_md("---")
            continue
        if tag in ("ul", "ol"):
            items = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.S | re.I)
            lines = []
            for i, li in enumerate(items, 1):
                prefix = f"{i}." if tag == "ol" else "-"
                lines.append(f"{prefix} {inline_md(li)}")
            builder.add_md("\n".join(lines))
            continue
        if "code-block" in classes:
            code, lang, readonly = code_from_block(inner, attrs)
            if code.strip():
                builder.add_code(code, lang, readonly)
            continue
        if "alert" in classes:
            md = alert_to_md(inner)
            if md:
                builder.add_md(md)
            continue
        if "try-it-box" in classes:
            title_m = re.search(r'class="try-it-title"[^>]*>(.*?)</', inner, re.S | re.I)
            title = strip_tags(title_m.group(1)) if title_m else "🧪 Şimdi deneyin"
            builder.add_md(f"### {title}")
            inner_clean = re.sub(
                r'<div[^>]*class="[^"]*try-it-title[^"]*"[^>]*>.*?</div>',
                "",
                inner,
                flags=re.S | re.I,
            )
            process_blocks(inner_clean, builder, skip_h1=False)
            continue
        if "table-wrapper" in classes or tag == "table":
            md = table_to_md(inner if tag != "table" else f"<table>{inner}</table>")
            if md:
                builder.add_md(md)
            continue
        if "handbook-figure" in classes or tag == "figure":
            md = figure_to_md(inner)
            if md:
                builder.add_md(md)
            continue
        if tag == "div":
            process_blocks(inner, builder, skip_h1=skip_h1)
            continue


def md_cell(source: str) -> dict:
    lines = source.split("\n")
    src = [line + "\n" for line in lines]
    if src:
        src[-1] = src[-1].rstrip("\n") + "\n"
    return {"cell_type": "markdown", "metadata": {"pds_handbook_tr": True}, "source": src}


def code_cell(source: str) -> dict:
    lines = source.split("\n")
    src = [line + "\n" for line in lines]
    return {
        "cell_type": "code",
        "metadata": {"pds_handbook_tr": True},
        "source": src,
        "outputs": [],
        "execution_count": None,
    }


def intro_cell(chapter: str, slug: str, title: str) -> dict:
    text = f"""# {title}

Bu notebook, PDS Handbook (TR) web sayfasının **Türkçe Jupyter karşılığıdır** — aynı açıklamalar, ders notları ve kod örnekleri.

| | |
|---|---|
| **Web sayfası** | `chapters/{chapter}/{slug}.html` |
| **Çalıştırma** | JupyterLab, VS Code veya Colab — hücreleri **yukarıdan aşağı** sırayla (`Shift+Enter`) |
| **Bağımlılık** | Kod hücreleri birbirine bağlıdır; hata alırsanız önce üsttekileri çalıştırın |

> **Kaynak:** Jake VanderPlas, *Python Data Science Handbook* — Türkçe ders uyarlaması
"""
    return md_cell(text)


def extract_title(fragment: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", fragment, re.S | re.I)
    return strip_tags(m.group(1)) if m else "Konu"


def html_to_notebook(html_path: Path, chapter: str, slug: str) -> dict:
    html = html_path.read_text(encoding="utf-8")
    main = extract_main(html)
    title = extract_title(main)
    builder = CellBuilder()
    process_blocks(main, builder, skip_h1=True)
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "pds_handbook_tr": {
                "chapter": chapter,
                "slug": slug,
                "html": f"chapters/{chapter}/{slug}.html",
            },
        },
        "cells": [intro_cell(chapter, slug, title)] + builder.finish(),
    }


def export_all() -> int:
    count = 0
    for chapter, slug in SECTIONS:
        html_path = CHAPTERS / chapter / f"{slug}.html"
        if not html_path.exists():
            print("MISSING", html_path.relative_to(ROOT))
            continue
        nb = html_to_notebook(html_path, chapter, slug)
        out_dir = OUT / chapter
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{slug}.ipynb"
        out_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        n_md = sum(1 for c in nb["cells"] if c["cell_type"] == "markdown")
        n_code = sum(1 for c in nb["cells"] if c["cell_type"] == "code")
        print(f"OK {out_path.relative_to(ROOT)}  ({n_md} md, {n_code} code)")
        count += 1
    return count


if __name__ == "__main__":
    n = export_all()
    print(f"Done: {n} Turkish notebooks from HTML")
