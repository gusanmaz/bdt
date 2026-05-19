"""Helpers for notebook → handbook HTML conversion."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
NB_DIR = TOOLS / "source" / "notebooks"


def load_notebook(name: str) -> list[dict]:
    data = json.loads((NB_DIR / name).read_text(encoding="utf-8"))
    return data["cells"]


def esc_code(source: str) -> str:
    return html.escape(source.rstrip("\n"))


def code_block(source: str, filename: str | None = None) -> str:
    fn = f' data-filename="{filename}"' if filename else ""
    return (
        f'    <div class="code-block" data-lang="python"{fn}>\n'
        f"      <pre><code>{esc_code(source)}</code></pre>\n"
        f"    </div>"
    )


def p(text: str) -> str:
    return f"    <p>{text}</p>"


def ul(items: list[str]) -> str:
    lines = ["    <ul>"]
    for item in items:
        lines.append(f"      <li>{item}</li>")
    lines.append("    </ul>")
    return "\n".join(lines)


def h1(text: str) -> str:
    return f"<h1>{text}</h1>"


def h2(text: str, id_: str) -> str:
    return f'    <h2 id="{id_}">{text}</h2>'


def h3(text: str, id_: str) -> str:
    return f'    <h3 id="{id_}">{text}</h3>'


def h4(text: str, id_: str) -> str:
    return f'    <h4 id="{id_}">{text}</h4>'


def addon(title: str, body: str) -> str:
    return f"""    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Ders notu — {title}</div>
      <p>{body}</p>
    </div>"""


def try_it(title: str, desc: str, code: str, filename: str) -> str:
    return f"""    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>{desc}</p>
      <div class="code-block" data-lang="python" data-filename="{filename}">
        <pre><code>{esc_code(code)}</code></pre>
      </div>
    </div>"""


def next_link(href: str, label: str) -> str:
    return f"""    <div class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</div>
      <p><a href="{href}">{label} →</a></p>
    </div>"""


def orig_line(en_url: str, en_label: str) -> str:
    return (
        f'    <p><em>Orijinal: <a href="{en_url}" target="_blank" '
        f'rel="noopener">{en_label}</a></em></p>'
    )


def build_from_notebook(
    notebook: str,
    tr_md: dict[int, str],
    code_names: dict[int, str] | None = None,
    inserts: dict[int, str] | None = None,
) -> str:
    """Build body HTML: markdown cells from tr_md, code from notebook."""
    cells = load_notebook(notebook)
    code_names = code_names or {}
    inserts = inserts or {}
    parts: list[str] = []
    for i, cell in enumerate(cells):
        if cell["cell_type"] == "markdown":
            if i in tr_md:
                parts.append(tr_md[i])
        else:
            src = "".join(cell["source"])
            parts.append(code_block(src, code_names.get(i, f"cell_{i:02d}.py")))
        if i in inserts:
            parts.append(inserts[i])
    return "\n\n".join(parts)
