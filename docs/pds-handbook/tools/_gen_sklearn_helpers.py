#!/usr/bin/env python3
from __future__ import annotations
import html


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def code_block(code: str, filename: str, lang: str = "python", readonly: bool = False) -> str:
    ro = ' data-readonly="true"' if readonly else ""
    body = esc(code.rstrip("\n"))
    return (
        f'    <div class="code-block" data-lang="{lang}" data-filename="{filename}"{ro}>\n'
        f"      <pre><code>{body}</code></pre>\n"
        f"    </div>\n"
    )


def figure(img: str, alt: str, caption: str = "") -> str:
    cap = f"\n      <figcaption>{caption}</figcaption>" if caption else ""
    return f"""    <figure class="handbook-figure">
      <img src="../../assets/images/{html.escape(img)}" alt="{html.escape(alt)}" width="700" loading="lazy">{cap}
    </figure>"""


def addon(title: str, body: str) -> str:
    return f"""    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Ders notu — {html.escape(title)}</div>
      {body}
    </div>
"""


def try_it(title: str, intro: str, code: str, filename: str) -> str:
    return f"""    <div class="try-it-box">
      <div class="try-it-title">🧪 {html.escape(title)}</div>
      <p>{intro}</p>
      {code_block(code, filename)}
    </div>
"""


def next_link(href: str, label: str) -> str:
    return f"""    <div class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</div>
      <p><a href="{href}">{html.escape(label)} →</a></p>
    </div>
"""
