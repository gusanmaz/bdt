#!/usr/bin/env python3
"""Load code cells from source notebooks."""
from __future__ import annotations

import json
import re
from pathlib import Path

NB = Path(__file__).parent / "source" / "notebooks"


def nb_code(name: str, idx: int) -> str:
    cells = json.loads((NB / name).read_text(encoding="utf-8"))["cells"]
    return "".join(cells[idx].get("source", [])).rstrip("\n")


def code_meta(code: str) -> tuple[str, bool]:
    """Return (lang, readonly) for handbook code-block."""
    if not code.strip():
        return "python", False
    if code.lstrip().startswith("!") or re.search(r"^%\w+", code, re.M):
        return "text", True
    if re.match(r"^#\s*(Following are commands|shell command)", code, re.I):
        return "text", True
    return "python", False
