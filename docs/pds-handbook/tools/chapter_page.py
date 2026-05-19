#!/usr/bin/env python3
"""HTML page shell for PDS Handbook chapter sections."""
from __future__ import annotations

import html


def page_shell(
    *,
    title: str,
    chapter: str,
    section: str,
    source_en_url: str,
    source_en_label: str,
    body_html: str,
    preload_numpy: bool = False,
    preload_pandas: bool = False,
    preload_matplotlib: bool = False,
    preload_seaborn: bool = False,
    preload_sklearn: bool = False,
    pyodide: bool = True,
) -> str:
    data_attrs = []
    if preload_numpy or preload_pandas or preload_matplotlib or preload_seaborn or preload_sklearn:
        data_attrs.append('data-preload-numpy="true"')
    if preload_pandas or preload_seaborn or preload_sklearn:
        data_attrs.append('data-preload-pandas="true"')
    if preload_matplotlib or preload_seaborn or preload_sklearn:
        data_attrs.append('data-preload-matplotlib="true"')
    if preload_seaborn:
        data_attrs.append('data-preload-seaborn="true"')
    if preload_sklearn:
        data_attrs.append('data-preload-sklearn="true"')
    data_attr_str = (" " + " ".join(data_attrs)) if data_attrs else ""
    pyodide_script = (
        '\n  <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>'
        if pyodide
        else ""
    )
    if preload_seaborn:
        pyodide_label = "Python + NumPy + Pandas + Matplotlib + Seaborn"
    elif preload_sklearn:
        pyodide_label = "Python + NumPy + Pandas + Matplotlib + scikit-learn"
    elif preload_matplotlib:
        pyodide_label = "Python + NumPy + Matplotlib"
    elif preload_pandas:
        pyodide_label = "Python + NumPy + Pandas"
    elif preload_numpy:
        pyodide_label = "Python + NumPy"
    else:
        pyodide_label = "Python"
    status = ""
    if pyodide:
        status = f'''
<div class="pyodide-status">
  <span class="dot"></span>
  <span class="status-text">{pyodide_label} yükleniyor...</span>
</div>'''

    safe_title = html.escape(title)
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{safe_title} — PDS Handbook (TR)</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/style.css">
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/python.min.js"></script>{pyodide_script}
</head>
<body class="pds-handbook-site" data-depth="2" data-chapter="{chapter}" data-section="{section}"{data_attr_str}>

<header class="top-nav">
  <a href="../../index.html" class="nav-brand">📚 PDS Handbook (TR)</a>
  <div class="nav-links">
    <a href="#" data-handbook-course-link>← Büyük Veri Teknolojileri</a>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Koyu Mod</button>
  </div>
</header>

<div class="main-container handbook-page">
  <aside class="sidebar handbook-sidebar">
    <a href="../../index.html" class="handbook-back-link">← Kitap ana sayfası</a>
    <div class="toc-title">Bölümler</div>
    <div class="chapter-list handbook-chapter-list"></div>
    <div class="toc-title">Bu Bölümde</div>
    <div class="chapter-list handbook-section-list"></div>
    <div class="toc-title">Bu Sayfada</div>
    <nav></nav>
  </aside>

  <main class="content handbook-content">

    <div class="alert alert-info handbook-attribution">
      <div class="alert-title">📜 Orijinal kaynak</div>
      <p>Bu sayfa orijinal kitap bölümünün <strong>eksiksiz</strong> Türkçe uyarlamasıdır — atlanan başlık/kod yoktur.
      Zor yerlerde ek <span class="handbook-addon-tag">ders notu</span> ve
      <strong>🧪 Şimdi deneyin</strong> kutuları vardır.</p>
      <p>Orijinal (EN): <a href="{html.escape(source_en_url)}" target="_blank" rel="noopener">{html.escape(source_en_label)}</a>
      · <a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank" rel="noopener">Jupyter notebook</a></p>
    </div>

{body_html}
  </main>
</div>

<footer class="page-footer">
  <div class="footer-nav">
    <a href="#" data-nav-prev>← Önceki</a>
    <a href="../../index.html">Ana sayfa</a>
    <a href="#" data-nav-next>Sonraki →</a>
  </div>
  <p class="footer-text">Python Data Science Handbook — Jake VanderPlas · Türkçe ders uyarlaması</p>
</footer>

<button class="scroll-top" title="Yukarı çık">↑</button>
{status}

<script src="../../assets/nav.js"></script>
<script src="../../assets/script.js"></script>
</body>
</html>
'''
