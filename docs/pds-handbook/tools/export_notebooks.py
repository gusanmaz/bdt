#!/usr/bin/env python3
"""Export Turkish Jupyter notebooks from handbook HTML pages."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from html_to_notebook import export_all

if __name__ == "__main__":
    n = export_all()
    print(f"Done: {n} Turkish notebooks from HTML")
