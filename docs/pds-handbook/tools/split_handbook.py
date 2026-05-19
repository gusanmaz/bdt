#!/usr/bin/env python3
"""Generate per-section handbook pages.

Canonical content lives in chapters/*/*.html — edit those files directly.
This script was used for initial split from monolithic HTML; monolithic
ipython.html / numpy.html at repo root are now redirects only.
Re-run only after restoring full source to tools/source/.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

IPYTHON_MAP = [
    ("00-introduction", "ipython-giris", "IPython'a Giriş"),
    ("01-help-and-documentation", "yardim-dokumantasyon", "1.1 Yardım ve Dokümantasyon"),
    ("02-keyboard-shortcuts", "klavye-kisayollari", "1.2 Klavye Kısayolları"),
    ("03-magic-commands", "magic-komutlar", "1.3 Magic Komutlar"),
    ("04-input-output-history", "girdi-cikti-gecmisi", "1.4 Girdi ve Çıktı Geçmişi"),
    ("05-shell-commands", "shell-komutlari", "1.5 IPython ve Shell Komutları"),
    ("06-errors-and-debugging", "hatalar-debug", "1.6 Hatalar ve Hata Ayıklama"),
    ("07-timing-and-profiling", "profil-zamanlama", "1.7 Profil ve Kod Zamanlama"),
    ("08-more-resources", "kaynaklar", "1.8 Daha Fazla IPython Kaynağı"),
]

NUMPY_MAP = [
    ("00-introduction", "numpy-giris", "NumPy'ye Giriş"),
    ("01-understanding-data-types", "veri-tipleri", "2.1 Python'da Veri Tiplerini Anlamak"),
    ("02-basics-of-numpy-arrays", "dizi-temelleri", "2.2 NumPy Dizilerinin Temelleri"),
    ("03-computation-ufuncs", "ufuncs", "2.3 NumPy Dizilerinde Hesaplama: UFuncs"),
    ("04-aggregates", "agregasyonlar", "2.4 Agregasyonlar"),
    ("05-broadcasting", "broadcasting", "2.5 Broadcasting"),
    ("06-boolean-masks", "boolean-maske", "2.6 Karşılaştırma, Maskeler ve Boolean Mantık"),
    ("07-fancy-indexing", "fancy-indexing", "2.7 Fancy Indexing"),
    ("08-sorting", "siralama", "2.8 Dizi Sıralama"),
    ("09-structured-arrays", "yapilandirilmis", "2.9 Yapılandırılmış Diziler"),
]

SOURCE_URLS = {
    "01-help-and-documentation": "https://jakevdp.github.io/PythonDataScienceHandbook/01.01-help-and-documentation.html",
    "02-keyboard-shortcuts": "https://jakevdp.github.io/PythonDataScienceHandbook/01.02-shell-keyboard-shortcuts.html",
    "03-magic-commands": "https://jakevdp.github.io/PythonDataScienceHandbook/01.03-magic-commands.html",
    "04-input-output-history": "https://jakevdp.github.io/PythonDataScienceHandbook/01.04-input-output-history.html",
    "05-shell-commands": "https://jakevdp.github.io/PythonDataScienceHandbook/01.05-ipython-and-shell-commands.html",
    "06-errors-and-debugging": "https://jakevdp.github.io/PythonDataScienceHandbook/01.06-errors-and-debugging.html",
    "07-timing-and-profiling": "https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html",
    "08-more-resources": "https://jakevdp.github.io/PythonDataScienceHandbook/01.08-more-ipython-resources.html",
    "01-understanding-data-types": "https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html",
    "02-basics-of-numpy-arrays": "https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html",
    "03-computation-ufuncs": "https://jakevdp.github.io/PythonDataScienceHandbook/02.03-computation-on-arrays-ufuncs.html",
    "04-aggregates": "https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html",
    "05-broadcasting": "https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html",
    "06-boolean-masks": "https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html",
    "07-fancy-indexing": "https://jakevdp.github.io/PythonDataScienceHandbook/02.07-fancy-indexing.html",
    "08-sorting": "https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html",
    "09-structured-arrays": "https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html",
}


def extract_main(html: str) -> str:
    m = re.search(r'<main class="content handbook-content">(.*)</main>', html, re.DOTALL)
    if not m:
        raise ValueError("main not found")
    return m.group(1)


def split_sections(main: str, id_map: list[tuple[str, str, str]]) -> dict[str, str]:
    parts = {}
    for slug, anchor, title in id_map:
        pattern = rf'<h2 id="{re.escape(anchor)}">.*?(?=<hr>|$)'
        m = re.search(pattern, main, re.DOTALL)
        if not m:
            # last section may not have trailing hr
            pattern = rf'<h2 id="{re.escape(anchor)}">.*'
            m = re.search(pattern, main, re.DOTALL)
        if m:
            content = m.group(0).strip()
            # strip duplicate h2 id for cleaner single-page toc
            content = re.sub(rf'^<h2 id="{re.escape(anchor)}">', f'<h1>', content, count=1)
            content = content.replace('</h2>', '</h1>', 1)
            parts[slug] = content
        else:
            print(f"WARN: section {anchor} not found")
    return parts


def fidelity_banner(slug: str, title: str) -> str:
    src = SOURCE_URLS.get(slug, "https://jakevdp.github.io/PythonDataScienceHandbook/")
    return f'''
    <div class="alert alert-info handbook-attribution">
      <div class="alert-title">📜 Orijinal kaynak</div>
      <p>Bu sayfa <strong>{title}</strong> konusunun Türkçe uyarlamasıdır.
      Kitaptaki tüm kod örnekleri ve ana fikirler korunur; zor bölümlerde
      <span class="handbook-addon-tag">ders notu</span> ve
      <strong>🧪 Şimdi deneyin</strong> kutuları eklenmiştir.</p>
      <p>Orijinal (EN): <a href="{src}" target="_blank" rel="noopener">{slug.replace("-", " ").title()}</a>
      · <a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank" rel="noopener">Jupyter notebook</a></p>
    </div>
    '''


def page_template(
    *,
    title: str,
    chapter: str,
    section: str,
    body_content: str,
    slug: str,
    preload_numpy: bool = False,
    depth: int = 2,
) -> str:
    prefix = "../" * depth
    numpy_attr = ' data-preload-numpy="true"' if preload_numpy else ""
    pyodide = f'''
<div class="pyodide-status">
  <span class="dot"></span>
  <span class="status-text">Python{" + NumPy" if preload_numpy else ""} yükleniyor...</span>
</div>''' if chapter else ""
    extra_head = ""
    if preload_numpy:
        extra_head = '''
  <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>'''
    elif chapter == "01-ipython":
        extra_head = '''
  <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>'''

    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — PDS Handbook (TR)</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/style.css">
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/python.min.js"></script>{extra_head}
</head>
<body class="pds-handbook-site" data-depth="{depth}" data-chapter="{chapter}" data-section="{section}"{numpy_attr}>

<header class="top-nav">
  <a href="{prefix}index.html" class="nav-brand">📚 PDS Handbook (TR)</a>
  <div class="nav-links">
    <a href="#" data-handbook-course-link>← Büyük Veri Teknolojileri</a>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Koyu Mod</button>
  </div>
</header>

<div class="main-container handbook-page">
  <aside class="sidebar handbook-sidebar">
    <a href="{prefix}index.html" class="handbook-back-link">← Kitap ana sayfası</a>
    <div class="toc-title">Bölümler</div>
    <div class="chapter-list handbook-chapter-list"></div>
    <div class="toc-title">Bu Bölümde</div>
    <div class="chapter-list handbook-section-list"></div>
    <div class="toc-title">Bu Sayfada</div>
    <nav></nav>
  </aside>

  <main class="content handbook-content">
{fidelity_banner(slug, title) if slug and slug not in ("00-introduction", "index") else ""}
{body_content}
  </main>
</div>

<footer class="page-footer">
  <div class="footer-nav">
    <a href="#" data-nav-prev>← Önceki</a>
    <a href="{prefix}index.html">Ana sayfa</a>
    <a href="#" data-nav-next>Sonraki →</a>
  </div>
  <p class="footer-text">Python Data Science Handbook — Jake VanderPlas · Türkçe ders uyarlaması</p>
</footer>

<button class="scroll-top" title="Yukarı çık">↑</button>
{pyodide}

<script src="{prefix}assets/nav.js"></script>
<script src="{prefix}assets/script.js"></script>
</body>
</html>
'''


CHAPTER_META = {
    "01-ipython": ("Bölüm 1 — IPython", "Sıradan Python'un ötesinde — Jupyter ve IPython araçları"),
    "02-numpy": ("Bölüm 2 — NumPy", "Sayısal Python — diziler, vektörizasyon, maskeleme"),
}


def chapter_index(chapter_id: str, title: str, subtitle: str, sections: list, preload: bool) -> str:
    links = "\n".join(
        f'        <li><a href="{slug}.html">{sec_title}</a></li>'
        for slug, _, sec_title in sections
    )
    body = f'''
    <h1>{title}</h1>
    <p class="subtitle">{subtitle}</p>
    <p>Bu bölümdeki konular — kitaptaki sırayla:</p>
    <ul class="handbook-topic-list">
{links}
    </ul>
    <div class="alert alert-info handbook-attribution">
      <div class="alert-title">📜 Uyarlama ilkesi</div>
      <p>Orijinal PDS Handbook metnindeki <strong>tüm bölüm başlıkları, kod örnekleri ve örnek senaryolar</strong> korunur.
      Türkçe sürümde ek olarak ders notu kutuları, şimdi deneyin alıştırmaları ve zor kavramlar için genişletilmiş açıklamalar vardır.</p>
    </div>
    '''
    return page_template(
        title=title,
        chapter=chapter_id,
        section="",
        body_content=body,
        slug="index",
        preload_numpy=preload,
        depth=2,
    )


def process_file(src_name: str, chapter_id: str, section_map: list, preload: bool):
    html = (ROOT / src_name).read_text(encoding="utf-8")
    main = extract_main(html)
    # remove global attribution block from split content
    main = re.sub(
        r'<div class="alert alert-info handbook-attribution">.*?</div>\s*<hr>\s*',
        "",
        main,
        count=1,
        flags=re.DOTALL,
    )
    sections = split_sections(main, section_map)
    out_dir = ROOT / "chapters" / chapter_id
    out_dir.mkdir(parents=True, exist_ok=True)

    for slug, _, sec_title in section_map:
        if slug not in sections:
            continue
        content = sections[slug]
        # fix internal links from old monolithic paths
        content = content.replace('href="numpy.html"', f'href="../02-numpy/index.html"')
        content = content.replace('href="ipython.html"', f'href="../01-ipython/index.html"')
        content = content.replace("../ders-notlari/", "../../../ders-notlari/")
        page = page_template(
            title=sec_title,
            chapter=chapter_id,
            section=slug,
            body_content=content,
            slug=slug,
            preload_numpy=preload,
            depth=2,
        )
        (out_dir / f"{slug}.html").write_text(page, encoding="utf-8")
        print(f"  wrote {chapter_id}/{slug}.html")

    idx = chapter_index(
        chapter_id,
        *CHAPTER_META[chapter_id],
        section_map,
        preload,
    )
    (out_dir / "index.html").write_text(idx, encoding="utf-8")
    print(f"  wrote {chapter_id}/index.html")


def main():
    print("Splitting ipython.html...")
    process_file("ipython.html", "01-ipython", IPYTHON_MAP, preload=False)
    print("Splitting numpy.html...")
    process_file("numpy.html", "02-numpy", NUMPY_MAP, preload=True)
    print("Done.")


if __name__ == "__main__":
    main()
