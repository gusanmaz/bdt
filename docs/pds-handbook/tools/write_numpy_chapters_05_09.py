#!/usr/bin/env python3
"""Generate full Turkish HTML for NumPy chapters 05-09."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "chapters" / "02-numpy"

RAINFALL_MM_2015 = [
    0.0, 1.5, 0.0, 10.2, 8.1, 0.0, 0.0, 0.0, 0.3, 5.8, 1.5, 0.0, 0.0, 0.0, 9.7, 0.0, 26.2, 21.3, 0.5, 0.0,
    0.0, 0.8, 5.8, 0.5, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 1.5, 7.4, 1.3, 8.4, 26.2, 17.3, 23.6, 3.6, 6.1,
    0.3, 0.0, 1.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0, 4.6, 0.8, 0.0, 0.0, 0.0, 0.0, 4.1, 9.4, 18.3, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 2.5, 0.0, 2.0, 17.0, 55.9, 1.0, 0.8, 0.0, 0.0, 4.1, 3.8,
    1.0, 8.1, 7.6, 5.1, 0.0, 1.0, 0.0, 0.0, 1.8, 1.0, 5.1, 0.0, 1.5, 0.0, 0.0, 1.0, 0.5, 0.0, 0.0, 10.9,
    0.0, 0.0, 14.0, 3.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.6, 0.0, 3.0, 3.3, 1.3, 0.0, 0.3, 1.8, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 6.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.3, 4.1, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.6, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3,
    0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.6, 0.0, 30.5,
    0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 32.5, 10.2, 0.0, 5.8, 0.0, 0.0,
    0.0, 0.3, 5.3, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.8, 0.0, 0.0, 4.1, 0.0, 0.0, 0.0,
    0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.9, 0.0, 0.3, 28.7, 0.0, 4.6, 1.3, 0.0, 0.0,
    0.0, 0.3, 3.8, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 8.9, 6.9, 0.0, 3.3, 1.8, 19.3, 33.0, 26.2, 0.3, 0.8, 0.0,
    1.3, 0.0, 12.7, 6.6, 3.3, 1.3, 1.5, 9.9, 33.5, 47.2, 22.4, 2.0, 29.5, 1.5, 2.0, 0.0, 0.0, 0.0, 3.0, 7.1,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 12.2, 2.5, 12.7, 2.0, 15.7, 11.2, 27.4, 54.1, 13.5, 9.4, 0.3, 16.0, 1.3,
    0.0, 1.5, 3.6, 21.8, 18.5, 0.0, 4.3, 27.4, 4.6, 6.1, 2.5, 5.8, 0.0, 8.6, 1.5, 0.0, 0.0, 0.0,
]


def head(title, section, chapter_title, en_url, en_label):
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — PDS Handbook (TR)</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/style.css">
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/python.min.js"></script>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
</head>
<body class="pds-handbook-site" data-depth="2" data-chapter="02-numpy" data-section="{section}" data-preload-numpy="true">

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
      <p>Orijinal (EN): <a href="{en_url}" target="_blank" rel="noopener">{en_label}</a>
      · <a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank" rel="noopener">Jupyter notebook</a></p>
    </div>
    
<h1>{chapter_title}</h1>

    <p><em>Orijinal: <a href="{en_url}" target="_blank" rel="noopener">{en_label}</a></em></p>
"""


FOOT = """
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

<div class="pyodide-status">
  <span class="dot"></span>
  <span class="status-text">Python + NumPy yükleniyor...</span>
</div>

<script src="../../assets/nav.js"></script>
<script src="../../assets/script.js"></script>
</body>
</html>
"""


def code_block(code, filename, lang="python", readonly=False):
    ro = ' data-readonly="true"' if readonly else ""
    return f"""    <div class="code-block" data-lang="{lang}" data-filename="{filename}"{ro}>
      <pre><code>{code}</code></pre>
    </div>
"""


def write(path, content):
    (OUT / path).write_text(content, encoding="utf-8")
    print("wrote", path)


# --- Chapter 05 ---
ch05 = head(
    "2.5 Broadcasting (Yayınlama)",
    "05-broadcasting",
    "2.5 NumPy Dizilerinde Hesaplama: Broadcasting",
    "https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html",
    "05 Computation on Arrays: Broadcasting",
) + """
    <p><a href="03-computation-ufuncs.html">2.3 UFuncs</a> bölümünde NumPy'nin evrensel fonksiyonlarının yavaş Python döngülerini kaldırarak işlemleri <em>vektörize</em> ettiğini gördük. Bu bölüm <strong>broadcasting</strong> (yayınlama) kurallarını anlatır: farklı boyut ve şekillerdeki diziler arasında ikili işlemler (toplama, çıkarma, çarpma vb.) nasıl yapılır.</p>

    <h2 id="broadcasting-giris">Broadcasting'e Giriş</h2>

    <p>Aynı boyuttaki dizilerde ikili işlemler eleman eleman yapılır:</p>
""" + code_block("import numpy as np", "import_numpy.py") + code_block("""a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b""", "a_plus_b.py") + """
    <p>Broadcasting, farklı boyutlardaki dizilerle de bu tür işlemlere izin verir — örneğin bir skaleri (sıfır boyutlu dizi gibi düşünün) bir diziye ekleyebiliriz:</p>
""" + code_block("a + 5", "scalar_broadcast.py") + """
    <p>Bunu, <code>5</code> değerinin <code>[5, 5, 5]</code> dizisine “yayıldığı” ve sonuçların toplandığı bir işlem olarak düşünebilirsiniz.</p>

    <p>Aynı fikri daha yüksek boyutlu dizilere genişletebiliriz. Tek boyutlu bir diziyi iki boyutlu bir diziye eklediğimizde:</p>
""" + code_block("""M = np.ones((3, 3))
M""", "ones_matrix.py") + code_block("M + a", "matrix_plus_vector.py") + """
    <p>Burada tek boyutlu <code>a</code> dizisi, <code>M</code> ile şekil eşleşmesi için ikinci boyut boyunca <strong>yayınlanır</strong> (broadcast edilir).</p>

    <p>Daha karmaşık durumlarda her iki dizi de yayınlanabilir:</p>
""" + code_block("""a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)""", "broadcast_both.py") + code_block("a + b", "broadcast_both_result.py") + """
    <p>Daha önce tek bir değeri diğerinin şekline yaydığımız gibi, burada <em>hem</em> <code>a</code> hem <code>b</code> ortak bir şekle yayılır ve sonuç iki boyutlu bir dizidir!</p>

    <p>Bu örneklerin geometrisi aşağıdaki şekilde görselleştirilmiştir (kaynak: <a href="https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb#Broadcasting" target="_blank" rel="noopener">kitap ek kodu</a>, astroML dokümantasyonundan uyarlanmıştır):</p>

    <figure class="handbook-figure">
      <img src="../../assets/images/02.05-broadcasting.png" alt="NumPy broadcasting geometrisi: iki dizinin ortak şekle yayılması" width="700" loading="lazy">
      <figcaption>Şekil: Broadcasting görseli — açık kutular yayınlanan değerleri temsil eder (kaynak: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html" target="_blank" rel="noopener">PDS Handbook</a>)</figcaption>
    </figure>

    <p>Açık kutular yayınlanan değerleri temsil eder. Bellek açısından verimlilik endişesi doğurabilir; endişelenmeyin: NumPy broadcasting yayınlanan değerleri bellekte <em>gerçekten kopyalamaz</em>. Yine de broadcasting hakkında düşünürken bu zihinsel model faydalıdır.</p>

    <h2 id="broadcasting-kurallari">Broadcasting Kuralları</h2>

    <p>NumPy'da broadcasting iki dizi arasındaki etkileşimi belirlemek için katı kurallara uyar:</p>
    <ul>
      <li><strong>Kural 1:</strong> İki dizinin boyut sayısı farklıysa, daha az boyutlu olanın şekli sol taraftan (baştan) <code>1</code> ile doldurulur (<em>padding</em>).</li>
      <li><strong>Kural 2:</strong> Herhangi bir boyutta şekiller uyuşmuyorsa, o boyutta boyutu <code>1</code> olan dizi diğerinin boyutuna <em>gerilir</em> (stretch).</li>
      <li><strong>Kural 3:</strong> Herhangi bir boyutta boyutlar uyuşmuyorsa ve ikisi de <code>1</code> değilse hata oluşur.</li>
    </ul>

    <h3 id="ornek-1">Broadcasting Örneği 1</h3>

    <p>İki boyutlu bir diziye tek boyutlu bir dizi eklemek isteyelim:</p>
""" + code_block("""M = np.ones((2, 3))
a = np.arange(3)""", "ornek1_setup.py") + """
    <p>Şekiller:</p>
    <ul>
      <li><code>M.shape</code> → <code>(2, 3)</code></li>
      <li><code>a.shape</code> → <code>(3,)</code></li>
    </ul>
    <p>Kural 1: <code>a</code> daha az boyutlu; sol taraftan <code>1</code> ile doldurulur → <code>(1, 3)</code>. Kural 2: ilk boyut uyuşmaz; <code>1</code> → <code>2</code> gerilir. Son şekil: <code>(2, 3)</code>.</p>
""" + code_block("M + a", "ornek1_result.py") + """
    <h3 id="ornek-2">Broadcasting Örneği 2</h3>

    <p>Her iki dizinin de yayınlanması gereken durum:</p>
""" + code_block("""a = np.arange(3).reshape((3, 1))
b = np.arange(3)""", "ornek2_setup.py") + """
    <ul>
      <li><code>a.shape</code> → <code>(3, 1)</code></li>
      <li><code>b.shape</code> → <code>(3,)</code> → Kural 1 ile <code>(1, 3)</code></li>
      <li>Kural 2: her iki taraftaki <code>1</code> boyutları karşı tarafa gerilir → ikisi de <code>(3, 3)</code></li>
    </ul>
""" + code_block("a + b", "ornek2_result.py") + """
    <h3 id="ornek-3">Broadcasting Örneği 3</h3>

    <p>Uyumsuz iki dizi:</p>
""" + code_block("""M = np.ones((3, 2))
a = np.arange(3)""", "ornek3_setup.py") + """
    <p>İlk örneğe benzer ama <code>M</code> transpoze edilmiş gibi: <code>M.shape = (3, 2)</code>, <code>a</code> → <code>(1, 3)</code> → <code>(3, 3)</code>. Kural 3: ikinci boyut <code>2</code> vs <code>3</code> — uyumsuz!</p>
""" + code_block("""try:
    M + a
except ValueError as e:
    print("Hata:", e)""", "ornek3_error.py") + """
    <p>Kafa karışıklığı: <code>a</code>'yı sağ taraftan <code>1</code> ile doldurarak uyumlu hale getirebileceğinizi hayal edebilirsiniz — ama kurallar böyle çalışmaz! Sağ taraftan padding istiyorsanız açıkça yeniden şekillendirin (<a href="02-basics-of-numpy-arrays.html">2.2 NumPy Dizilerinin Temelleri</a>'ndeki <code>np.newaxis</code> ile):</p>
""" + code_block("a[:, np.newaxis].shape", "newaxis_shape.py") + code_block("M + a[:, np.newaxis]", "ornek3_fix.py") + """
    <p>Burada <code>+</code> operatörüne odaklandık; bu kurallar <em>herhangi bir</em> ikili ufunc için geçerlidir. Örneğin <code>logaddexp(a, b)</code> — <code>log(exp(a) + exp(b))</code> — daha hassas hesaplar:</p>
""" + code_block("np.logaddexp(M, a[:, np.newaxis])", "logaddexp.py") + """
    <p>Evrensel fonksiyonlar için bkz. <a href="03-computation-ufuncs.html">2.3 UFuncs</a>.</p>

    <h2 id="pratikte">Broadcasting Pratikte</h2>

    <p>Broadcasting, kitabın geri kalanında sık karşılaşacağınız birçok örneğin özünü oluşturur.</p>

    <h3 id="merkezleme">Bir Diziyi Ortalamadan Çıkarma</h3>

    <p>Veri biliminde yaygın bir örnek: satır veya sütun ortalamasını çıkarmak. 10 gözlem × 3 özelliklik bir dizi (Scikit-Learn veri temsili geleneği; bkz. kitap Bölüm 5):</p>
""" + code_block("""rng = np.random.default_rng(seed=1701)
X = rng.random((10, 3))""", "merkezleme_veri.py") + """
    <p>Her sütunun ortalaması (<code>axis=0</code>):</p>
""" + code_block("""Xmean = X.mean(0)
Xmean""", "merkezleme_ortalama.py") + """
    <p>Ortalamayı çıkararak merkezleme (broadcasting işlemi):</p>
""" + code_block("X_centered = X - Xmean", "merkezleme_cikar.py") + """
    <p>Doğrulama — merkezlenmiş dizinin sütun ortalamaları sıfıra yakın olmalı:</p>
""" + code_block("X_centered.mean(0)", "merkezleme_dogrula.py") + """
    <p>Makine hassasiyeti içinde ortalama artık sıfırdır.</p>

    <h3 id="2d-fonksiyon">İki Boyutlu Bir Fonksiyonu Çizme</h3>

    <p>Broadcasting, $z = f(x, y)$ gibi iki boyutlu fonksiyonları ızgara üzerinde hesaplamak için idealdir:</p>
""" + code_block("""# x ve y: 0–5 arası 50 adım
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
print("z.shape:", z.shape)
print("z min/max:", z.min(), z.max())""", "2d_fonksiyon.py") + """
    <p>Matplotlib ile bu iki boyutlu dizi görselleştirilebilir (kitap Bölüm 4 — <em>Density and Contour Plots</em>). Pyodide ortamında grafik yerine şekil ve değer aralığını yazdırıyoruz; tam kod:</p>
""" + code_block("""# Matplotlib ile (notebook ortamında):
# import matplotlib.pyplot as plt
# plt.imshow(z, origin='lower', extent=[0, 5, 0, 5])
# plt.colorbar()""", "2d_fonksiyon_plot.py", readonly=True) + """
    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin — 2D ızgara</div>
      <p>Yukarıdaki <code>x</code>, <code>y</code> ızgarasıyla <code>z = np.sin(x)**2 + np.cos(y)</code> hesaplayın; <code>z.shape</code> ve bir köşe değerini yazdırın.</p>
""" + code_block("""import numpy as np
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 2 + np.cos(y)
print(z.shape, z[0, 0])""", "deneme_2d.py") + """
    </div>

    <div class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</div>
      <p><a href="06-boolean-masks.html">2.6 Karşılaştırma, Maskeler ve Boolean Mantık →</a></p>
    </div>
""" + FOOT

write("05-broadcasting.html", ch05)

# --- Chapter 06 ---
rain_repr = repr(RAINFALL_MM_2015)
ch06 = head(
    "2.6 Karşılaştırma, Maskeler ve Boolean Mantık",
    "06-boolean-masks",
    "2.6 Karşılaştırma, Maskeler ve Boolean Mantık",
    "https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html",
    "06 Comparisons, Masks, and Boolean Logic",
) + """
    <p>Bu bölüm, NumPy dizilerindeki değerleri incelemek ve değiştirmek için Boolean maskelerin kullanımını ele alır. Maskeleme, belirli bir ölçüte göre değerleri çıkarmak, değiştirmek veya saymak istediğinizde devreye girer. NumPy'da Boolean maskeleme genellikle bu tür görevler için en verimli yoldur.</p>

    <h2 id="ornek-yagmurlu-gunler">Örnek: Yağmurlu Günleri Saymak</h2>

    <p>Bir yıl boyunca günlük yağış miktarını temsil eden bir veri dizisi düşünün. Orijinal kitapta 2015 yılı Seattle günlük yağış istatistikleri Pandas ile yüklenir (<a href="../03-pandas/index.html">Bölüm 3 — Pandas</a>). Pyodide ortamında aynı veri kümesini gömülü olarak kullanıyoruz — kaynak: <a href="https://github.com/vega/vega-datasets" target="_blank" rel="noopener">vega-datasets</a> <code>seattle-weather</code>, 2015 <code>precipitation</code> (mm).</p>
""" + code_block(f"""import numpy as np

# Seattle 2015 günlük yağış (mm) — kitaptaki veri kümesi (gömülü)
rainfall_mm = np.array({rain_repr})
len(rainfall_mm)""", "seattle_rainfall.py") + """
    <p>Dizi 365 değer içerir: 1 Ocak – 31 Aralık 2015 arası günlük yağış (milimetre).</p>

    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Ders notu — histogram</div>
      <p>Kitap bu verinin histogramını Matplotlib ile çizer (Bölüm 4). Çoğu gün yağış sıfıra yakındır — Seattle'ın yağmurlu ününe rağmen 2015'te ölçülen yağışın büyük kısmı düşük değerlerdedir. Histogram soruları (kaç yağmurlu gün? ortalama ne?) maskeleme ile çok daha verimli yanıtlanır.</p>
    </div>

    <p>Döngüyle tek tek saymak yerine NumPy karşılaştırma ufunc'ları ve maskeleme kullanacağız (<a href="03-computation-ufuncs.html">2.3 UFuncs</a>).</p>

    <h2 id="karsilastirma-ufunc">Karşılaştırma Operatörleri Ufunc Olarak</h2>

    <p><code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> gibi aritmetik operatörler eleman eleman çalışır. NumPy <code>&lt;</code>, <code>&gt;</code> gibi karşılaştırma operatörlerini de ufunc olarak uygular; sonuç her zaman Boolean tipli bir dizidir. Altı standart karşılaştırma operatörü mevcuttur:</p>
""" + code_block("x = np.array([1, 2, 3, 4, 5])", "comp_x.py") + code_block("x < 3   # küçüktür", "comp_lt.py") + code_block("x > 3   # büyüktür", "comp_gt.py") + code_block("x <= 3  # küçük eşit", "comp_le.py") + code_block("x >= 3  # büyük eşit", "comp_ge.py") + code_block("x != 3  # eşit değil", "comp_ne.py") + code_block("x == 3  # eşit", "comp_eq.py") + """
    <p>İki dizi arasında eleman eleman karşılaştırma ve bileşik ifadeler de mümkündür:</p>
""" + code_block("(2 * x) == (x ** 2)", "comp_compound.py") + """
    <p>Karşılaştırma operatörleri NumPy'da ufunc olarak uygulanır; <code>x &lt; 3</code> yazdığınızda dahili olarak <code>np.less(x, 3)</code> kullanılır. Özet tablo:</p>

    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Operatör</th><th>Eşdeğer ufunc</th><th>Operatör</th><th>Eşdeğer ufunc</th></tr></thead>
        <tbody>
          <tr><td><code>==</code></td><td><code>np.equal</code></td><td><code>!=</code></td><td><code>np.not_equal</code></td></tr>
          <tr><td><code>&lt;</code></td><td><code>np.less</code></td><td><code>&lt;=</code></td><td><code>np.less_equal</code></td></tr>
          <tr><td><code>&gt;</code></td><td><code>np.greater</code></td><td><code>&gt;=</code></td><td><code>np.greater_equal</code></td></tr>
        </tbody>
      </table>
    </div>

    <p>Aritmetik ufunc'lar gibi bunlar da her boyut ve şekildeki dizilerde çalışır. İki boyutlu örnek:</p>
""" + code_block("""rng = np.random.default_rng(seed=1701)
x = rng.integers(10, size=(3, 4))
x""", "comp_2d_x.py") + code_block("x < 6", "comp_2d_result.py") + """
    <p>Her durumda sonuç Boolean dizidir; NumPy bu sonuçlarla çalışmak için bir dizi kalıp sunar.</p>

    <h2 id="boolean-diziler">Boolean Dizilerle Çalışmak</h2>

    <p>Boolean dizi verildiğinde birçok yararlı işlem yapılabilir. Yukarıdaki iki boyutlu <code>x</code> ile devam edelim:</p>
""" + code_block("print(x)", "print_x.py") + """
    <h3 id="sayma">Girdi Sayma</h3>

    <p>Boolean dizideki <code>True</code> sayısını saymak için <code>np.count_nonzero</code> kullanılır:</p>
""" + code_block("# 6'dan küçük kaç değer?\nnp.count_nonzero(x < 6)", "count_nonzero.py") + """
    <p>Alternatif: <code>np.sum</code> — <code>False</code> → 0, <code>True</code> → 1:</p>
""" + code_block("np.sum(x < 6)", "sum_bool.py") + """
    <p><code>np.sum</code>'un avantajı, diğer agregasyon fonksiyonları gibi satır veya sütunlar boyunca da toplanabilmesidir:</p>
""" + code_block("# Her satırda 6'dan küçük kaç değer?\nnp.sum(x < 6, axis=1)", "sum_axis.py") + """
    <p>Herhangi bir veya tüm değerlerin <code>True</code> olup olmadığını hızlıca kontrol etmek için <code>np.any</code> veya <code>np.all</code>:</p>
""" + code_block("np.any(x > 8)    # 8'den büyük var mı?", "any_gt8.py") + code_block("np.any(x < 0)     # sıfırdan küçük var mı?", "any_lt0.py") + code_block("np.all(x < 10)    # hepsi 10'dan küçük mü?", "all_lt10.py") + code_block("np.all(x == 6)    # hepsi 6'ya eşit mi?", "all_eq6.py") + """
    <p><code>np.all</code> ve <code>np.any</code> belirli eksenler boyunca da kullanılabilir:</p>
""" + code_block("# Her satırdaki tüm değerler 8'den küçük mü?\nnp.all(x < 8, axis=1)", "all_axis.py") + """
    <div class="alert alert-warning handbook-addon">
      <div class="alert-title">⚠️ Ders notu — Python vs NumPy</div>
      <p>Python'un yerleşik <code>sum</code>, <code>any</code>, <code>all</code> fonksiyonları vardır (<a href="04-aggregates.html">2.4 Agregasyonlar</a>). Çok boyutlu dizilerde farklı sözdizimi kullanırlar ve beklenmeyen sonuç verebilirler. Bu örneklerde <code>np.sum</code>, <code>np.any</code>, <code>np.all</code> kullanın!</p>
    </div>

    <h3 id="boolean-operators">Boolean Operatörleri</h3>

    <p>20 mm'den az veya 10 mm'den fazla yağmurlu günleri saymak kolay; peki 10 mm ile 20 mm <em>arasında</em> kaç gün var? Python'un <strong>bit düzeyi mantık operatörleri</strong> <code>&amp;</code>, <code>|</code>, <code>^</code>, <code>~</code> kullanılır. NumPy bunları (genelde Boolean) diziler üzerinde eleman eleman ufunc olarak aşırı yükler:</p>
""" + code_block("np.sum((rainfall_mm > 10) & (rainfall_mm < 20))", "rain_range.py") + """
    <p>2015'te 10–20 mm arası yağışlı 16 gün vardır. Parantezler önemlidir — parantez olmadan operatör önceliği hatası oluşur:</p>
""" + code_block("""# HATALI — parantez yok:
# rainfall_mm > (10 & rainfall_mm) < 20""", "rain_precedence.py", readonly=True) + """
    <p>De Morgan kurallarıyla aynı sonuç farklı biçimde:</p>
""" + code_block("np.sum(~((rainfall_mm <= 10) | (rainfall_mm >= 20)))", "de_morgan.py") + """
    <p>Karşılaştırma ve Boolean operatörlerini birleştirmek geniş bir verimli mantıksal işlem yelpazesi sağlar. Bit düzeyi Boolean operatörleri tablosu:</p>

    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Operatör</th><th>Eşdeğer ufunc</th><th>Operatör</th><th>Eşdeğer ufunc</th></tr></thead>
        <tbody>
          <tr><td><code>&amp;</code></td><td><code>np.bitwise_and</code></td><td><code>|</code></td><td><code>np.bitwise_or</code></td></tr>
          <tr><td><code>^</code></td><td><code>np.bitwise_xor</code></td><td><code>~</code></td><td><code>np.bitwise_not</code></td></tr>
        </tbody>
      </table>
    </div>

    <p>Hava durumu verisiyle maskeleme + agregasyon örnekleri:</p>
""" + code_block("""print("Yağışsız gün sayısı:     ", np.sum(rainfall_mm == 0))
print("Yağışlı gün sayısı:      ", np.sum(rainfall_mm != 0))
print("10 mm üzeri günler:      ", np.sum(rainfall_mm > 10))
print("Yağmurlu ama < 5 mm:     ", np.sum((rainfall_mm > 0) & (rainfall_mm < 5)))""", "rain_stats.py") + """
    <h2 id="maskeler">Boolean Diziler Maske Olarak</h2>

    <p>Boolean diziler üzerinde doğrudan agregasyon yerine, daha güçlü kalıp: Boolean diziyi <strong>maske</strong> olarak kullanıp verinin alt kümelerini seçmek. <code>x</code> dizisine dönelim:</p>
""" + code_block("x", "x_again.py") + """
    <p>5'ten küçük tüm değerleri isteyelim:</p>
""" + code_block("x < 5", "mask_lt5.py") + """
    <p>Bu Boolean dizi üzerinde indeksleyerek değerleri <em>seçmek</em> — <strong>maskeleme</strong>:</p>
""" + code_block("x[x < 5]", "mask_select.py") + """
    <p>Dönen tek boyutlu dizi, maskenin <code>True</code> olduğu konumlardaki tüm değerleri içerir.</p>

    <p>Seattle yağış verisiyle istatistikler:</p>
""" + code_block("""# Yağmurlu günler maskesi
rainy = (rainfall_mm > 0)

# Yaz günleri (21 Haziran = 172. gün)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("2015 yağmurlu günlerde medyan yağış (mm):   ",
      np.median(rainfall_mm[rainy]))
print("2015 yaz günlerinde medyan yağış (mm):      ",
      np.median(rainfall_mm[summer]))
print("2015 yaz günlerinde maksimum yağış (mm):    ",
      np.max(rainfall_mm[summer]))
print("Yaz dışı yağmurlu günlerde medyan (mm):     ",
      np.median(rainfall_mm[rainy & ~summer]))""", "seattle_masks.py") + """
    <h2 id="and-or-vs">and/or Anahtar Kelimeleri vs &amp;/| Operatörleri</h2>

    <p>Sık karıştırılan nokta: <code>and</code>/<code>or</code> ile <code>&amp;</code>/<code>|</code> farkı. <code>and</code>/<code>or</code> nesnenin <em>bütünü</em> üzerinde çalışır; <code>&amp;</code>/<code>|</code> nesnenin <em>elemanları</em> üzerinde.</p>

    <p>Python'da sıfır olmayan tamsayılar <code>True</code> sayılır:</p>
""" + code_block("bool(42), bool(0)", "bool_int.py") + code_block("bool(42 and 0)", "and_int.py") + code_block("bool(42 or 0)", "or_int.py") + """
    <p>Tamsayılarda <code>&amp;</code>/<code>|</code> bit düzeyinde çalışır:</p>
""" + code_block("bin(42)", "bin42.py") + code_block("bin(59)", "bin59.py") + code_block("bin(42 & 59)", "bin_and.py") + code_block("bin(42 | 59)", "bin_or.py") + """
    <p>Boolean NumPy dizisinde <code>1 = True</code>, <code>0 = False</code> gibi düşünülür:</p>
""" + code_block("""A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
A | B""", "bool_arrays_or.py") + """
    <p>Ama dizilerde <code>or</code> kullanırsanız tüm dizinin truth value'su tanımsızdır — hata:</p>
""" + code_block("""# A or B  # ValueError: truth value of array is ambiguous""", "array_or_error.py", readonly=True) + """
    <p>Boolean ifadelerde <code>|</code> veya <code>&amp;</code> kullanın:</p>
""" + code_block("""x = np.arange(10)
(x > 4) & (x < 8)""", "range_mask.py") + """
    <p><code>and</code>/<code>or</code> ile denerseniz aynı <code>ValueError</code> oluşur:</p>
""" + code_block("""# (x > 4) and (x < 8)  # ValueError!""", "and_error.py", readonly=True) + """
    <p><strong>Özet:</strong> <code>and</code>/<code>or</code> tek Boolean değerlendirme; <code>&amp;</code>/<code>|</code> eleman eleman değerlendirme. Boolean NumPy dizilerinde neredeyse her zaman ikincisi istenen davranıştır.</p>

    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>1–100 arası dizide 3'e ve 5'e tam bölünen sayıları maske ile seçin.</p>
""" + code_block("""import numpy as np
x = np.arange(1, 101)
mask = (x % 3 == 0) & (x % 5 == 0)
print(x[mask])""", "deneme_bolunebilir.py") + """
    </div>

    <div class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</div>
      <p><a href="07-fancy-indexing.html">2.7 Fancy Indexing →</a></p>
    </div>
""" + FOOT

write("06-boolean-masks.html", ch06)

# --- Chapter 07 ---
ch07 = head(
    "2.7 Fancy Indexing",
    "07-fancy-indexing",
    "2.7 Fancy Indexing (Gelişmiş İndeksleme)",
    "https://jakevdp.github.io/PythonDataScienceHandbook/02.07-fancy-indexing.html",
    "07 Fancy Indexing",
) + """
    <p>Önceki bölümlerde basit indeksler (<code>arr[0]</code>), dilimler (<code>arr[:5]</code>) ve Boolean maskeler (<code>arr[arr &gt; 0]</code>) ile dizilerin bölümlerine erişmeyi gördük. Bu bölümde <strong>fancy indexing</strong> (veya <strong>vektörize indeksleme</strong>): tek skaler yerine <em>indeks dizisi</em> geçirerek birden çok elemana aynı anda erişim.</p>

    <h2 id="fancy-kesfet">Fancy Indexing'i Keşfetmek</h2>

    <p>Kavramsal olarak basit: birden fazla elemana erişmek için indeks dizisi geçirmek.</p>
""" + code_block("""import numpy as np
rng = np.random.default_rng(seed=1701)

x = rng.integers(100, size=10)
print(x)""", "fancy_x.py") + """
    <p>Üç farklı elemana erişmek:</p>
""" + code_block("[x[3], x[7], x[2]]", "fancy_manual.py") + """
    <p>Alternatif: tek bir liste veya indeks dizisi:</p>
""" + code_block("""ind = [3, 7, 4]
x[ind]""", "fancy_ind.py") + """
    <p>İndeks dizileri kullanıldığında sonucun şekli, <em>indekslenen dizinin</em> değil <em>indeks dizilerinin</em> şeklini yansıtır:</p>
""" + code_block("""ind = np.array([[3, 7],
                [4, 5]])
x[ind]""", "fancy_2d_ind.py") + """
    <p>Fancy indexing çok boyutlu dizilerde de çalışır:</p>
""" + code_block("""X = np.arange(12).reshape((3, 4))
X""", "fancy_X.py") + """
    <p>Standart indekslemede olduğu gibi ilk indeks satır, ikinci sütun:</p>
""" + code_block("""row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]""", "fancy_row_col.py") + """
    <p>İlk değer <code>X[0, 2]</code>, ikinci <code>X[1, 1]</code>, üçüncü <code>X[2, 3]</code>. İndeks eşleştirmesi <a href="05-broadcasting.html">2.5 Broadcasting</a> kurallarına uyar. Sütun vektörü + satır vektörü birleştirilirse iki boyutlu sonuç:</p>
""" + code_block("X[row[:, np.newaxis], col]", "fancy_broadcast_ind.py") + """
    <p>Her satır değeri her sütun vektörüyle eşleşir — aritmetik broadcasting'deki gibi:</p>
""" + code_block("row[:, np.newaxis] * col", "fancy_broadcast_demo.py") + """
    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Ders notu</div>
      <p>Fancy indexing'de dönüş değerinin şekli <strong>indekslerin yayınlanmış şeklini</strong> yansıtır, indekslenen dizinin şeklini değil.</p>
    </div>

    <h2 id="birlesik-indeksleme">Birleşik İndeksleme</h2>

    <p>Fancy indexing diğer indeksleme şemalarıyla birleştirilebilir:</p>
""" + code_block("print(X)", "print_X.py") + """
    <p>Fancy + basit indeks:</p>
""" + code_block("X[2, [2, 0, 1]]", "fancy_simple.py") + """
    <p>Fancy + dilimleme:</p>
""" + code_block("X[1:, [2, 0, 1]]", "fancy_slice.py") + """
    <p>Fancy + maskeleme:</p>
""" + code_block("""mask = np.array([True, False, True, False])
X[row[:, np.newaxis], mask]""", "fancy_mask.py") + """
    <p>Tüm bu seçenekler dizilere verimli erişim ve değiştirme için esnek bir araç seti sunar.</p>

    <h2 id="rastgele-noktalar">Örnek: Rastgele Nokta Seçimi</h2>

    <p>Fancy indexing'in yaygın kullanımı: matristen satır alt kümesi seçmek. $N \times D$ boyutlu matris — $D$ boyutlu $N$ nokta. İki boyutlu normal dağılımdan noktalar:</p>
""" + code_block("""mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rng.multivariate_normal(mean, cov, 100)
X.shape""", "random_points.py") + """
    <p>Kitap bu noktaları scatter plot ile gösterir (Bölüm 4 — Matplotlib). 20 rastgele nokta seçmek için tekrarsız 20 indeks:</p>
""" + code_block("""indices = np.random.choice(X.shape[0], 20, replace=False)
indices""", "random_indices.py") + code_block("""selection = X[indices]  # fancy indexing
selection.shape""", "random_selection.py") + """
    <p>Seçilen noktalar büyük dairelerle üst üste çizilebilir. Bu strateji veri kümesini hızlıca bölmede kullanılır — örneğin istatistiksel modellerde eğitim/test ayrımı (kitap Bölüm 5 — <em>Hyperparameters and Model Validation</em>).</p>

    <h2 id="fancy-atama">Fancy Indexing ile Değer Değiştirme</h2>

    <p>Erişimin yanı sıra değiştirme de mümkün:</p>
""" + code_block("""x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)""", "fancy_assign.py") + """
    <p>Herhangi bir atama operatörü:</p>
""" + code_block("""x[i] -= 10
print(x)""", "fancy_assign_op.py") + """
    <p>Tekrarlı indeksler beklenmedik sonuç verebilir:</p>
""" + code_block("""x = np.zeros(10)
x[[0, 0]] = [4, 6]
print(x)  # x[0] = 6 (4 kayboldu)""", "fancy_repeat1.py") + code_block("""i = [2, 3, 3, 4, 4, 4]
x[i] += 1
x  # x[3]=1, x[4]=1 — 2 ve 3 değil!""", "fancy_repeat2.py") + """
    <p><code>x[i] += 1</code> kısaltması <code>x[i] = x[i] + 1</code>. <code>x[i] + 1</code> bir kez hesaplanır, sonra atama yapılır — artırma değil atama tekrarlanır.</p>

    <p>Artırmanın her tekrarda uygulanmasını istiyorsanız ufunc'un <code>at</code> metodu:</p>
""" + code_block("""x = np.zeros(10)
np.add.at(x, i, 1)
print(x)  # x[3]=2, x[4]=3""", "add_at.py") + """
    <p><code>at</code> belirtilen indekslerde operatörü yerinde uygular. Benzer: ufunc'ların <code>reduceat</code> metodu — <a href="https://numpy.org/doc/stable/reference/ufuncs.html" target="_blank" rel="noopener">NumPy ufunc dokümantasyonu</a>.</p>

    <h2 id="binning">Örnek: Veriyi Kutulara Ayırma (Binning)</h2>

    <p>Fancy indexing fikirleriyle özel kutulu hesaplamalar yapılabilir. 100 değerin hangi kutuya düştüğünü bulmak:</p>
""" + code_block("""rng = np.random.default_rng(seed=1701)
x = rng.normal(size=100)

bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# Her x için uygun kutuyu bul
i = np.searchsorted(bins, x)

# Her kutuya 1 ekle
np.add.at(counts, i, 1)
print("counts:", counts)""", "binning_manual.py") + """
    <p><code>counts</code> her kutudaki nokta sayısını verir — yani histogram. Matplotlib <code>plt.hist</code> tek satırda aynısını yapar:</p>
""" + code_block("""# plt.hist(x, bins, histtype='step')""", "plt_hist.py", readonly=True) + """
    <p>Matplotlib <code>np.histogram</code> kullanır. Karşılaştırma (notebook'ta <code>%timeit</code>):</p>
""" + code_block("""import time

def bench(fn, n=50):
    t0 = time.perf_counter()
    for _ in range(n):
        fn()
    return (time.perf_counter() - t0) / n * 1000

# 100 nokta
t_np = bench(lambda: np.histogram(x, bins))
t_custom = bench(lambda: np.add.at(np.zeros_like(bins), np.searchsorted(bins, x), 1))
print(f"100 nokta — np.histogram: {t_np:.3f} ms, özel: {t_custom:.3f} ms")

# 1M nokta
x_big = rng.normal(size=1_000_000)
t_np_big = bench(lambda: np.histogram(x_big, bins), n=5)
t_custom_big = bench(lambda: np.add.at(np.zeros_like(bins), np.searchsorted(bins, x_big), 1), n=5)
print(f"1M nokta — np.histogram: {t_np_big:.3f} ms, özel: {t_custom_big:.3f} ms")""", "binning_timing.py") + """
    <p>Küçük veride özel algoritma daha hızlı olabilir; büyük veride <code>np.histogram</code> daha esnek ve optimize edilmiştir. Algoritmik verimlilik basit değildir — bkz. <a href="08-sorting.html#big-o">2.8 Big-O Notasyonu</a>.</p>

    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>100 rastgele sayıdan 20 tanesini <code>np.random.choice</code> ile tekrarsız seçin.</p>
""" + code_block("""import numpy as np
X = np.random.randn(100, 2)
idx = np.random.choice(X.shape[0], 20, replace=False)
print("Seçilen:", len(idx), "  İlk 5 indeks:", idx[:5])""", "deneme_choice.py") + """
    </div>

    <div class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</div>
      <p><a href="08-sorting.html">2.8 Dizi Sıralama →</a></p>
    </div>
""" + FOOT

write("07-fancy-indexing.html", ch07)

# --- Chapter 08 ---
ch08 = head(
    "2.8 Dizi Sıralama",
    "08-sorting",
    "2.8 Dizi Sıralama",
    "https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html",
    "08 Sorting Arrays",
) + """
    <p>NumPy dizilerindeki değerleri sıralamayla ilgili algoritmalar. Bilgisayar biliminde insertion sort, selection sort, merge sort, quick sort, bubble sort… Hepsi benzer görevi yapar: liste veya dizideki değerleri sıralamak.</p>

    <p>Basit <strong>selection sort</strong> (seçmeli sıralama) listeden tekrar tekrar minimum değeri bulur ve yer değiştirir:</p>
""" + code_block("""import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x""", "selection_sort_fn.py") + code_block("""x = np.array([2, 1, 4, 3, 5])
selection_sort(x)""", "selection_sort_demo.py") + """
    <p>Selection sort basitliği için faydalıdır ama büyük diziler için çok yavaştır. $N$ değer için $N$ döngü, her biri $\sim N$ karşılaştırma — ortalama <strong>$\mathcal{O}[N^2]$</strong> (<a href="#big-o">Big-O Notasyonu</a>). Eleman sayısını iki katına çıkarırsanız süre yaklaşık dört kat artar.</p>

    <p>Selection sort bile favori algoritmam <strong>bogosort</strong>'tan çok daha iyidir:</p>
""" + code_block("""def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x""", "bogosort_fn.py") + code_block("""x = np.array([2, 1, 4, 3, 5])
bogosort(x)""", "bogosort_demo.py") + """
    <p>Bu algoritma saf şansa dayanır: diziyi rastgele karıştırıp sıralı olana kadar tekrarlar. Ortalama $\mathcal{O}[N \times N!]$ — gerçek hesaplamada asla kullanılmamalıdır.</p>

    <p>Neyse ki Python ve NumPy'da çok daha verimli yerleşik sıralama vardır.</p>

    <h2 id="numpy-sort">NumPy'da Hızlı Sıralama: np.sort ve np.argsort</h2>

    <p>Python'un <code>sort</code> ve <code>sorted</code> fonksiyonları listeler içindir; NumPy'nin <code>np.sort</code>'u uniform sayı dizileri için çok daha verimlidir. Varsayılan $\mathcal{O}[N\log N]$ quicksort; mergesort ve heapsort da mevcuttur.</p>
""" + code_block("""x = np.array([2, 1, 4, 3, 5])
np.sort(x)""", "np_sort.py") + """
    <p>Yerinde sıralama — dizi metodu <code>sort</code>:</p>
""" + code_block("""x.sort()
print(x)""", "sort_inplace.py") + """
    <p>İlgili fonksiyon <code>argsort</code> — sıralı <em>elemanların indekslerini</em> döndürür:</p>
""" + code_block("""x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)""", "argsort.py") + """
    <p>İlk eleman en küçüğün indeksi, ikinci ikinci en küçüğün… Fancy indexing ile sıralı dizi:</p>
""" + code_block("x[i]", "argsort_fancy.py") + """
    <p>Bu bölümün ilerleyen kısmında <code>argsort</code> uygulaması göreceksiniz.</p>

    <h3 id="axis-sort">Satır veya Sütun Boyunca Sıralama</h3>
""" + code_block("""rng = np.random.default_rng(seed=42)
X = rng.integers(0, 10, (4, 6))
print(X)""", "sort_X.py") + code_block("# X'in her sütununu sırala\nnp.sort(X, axis=0)", "sort_axis0.py") + code_block("# X'in her satırını sırala\nnp.sort(X, axis=1)", "sort_axis1.py") + """
    <p>Her satır veya sütun bağımsız dizi gibi ele alınır — satır/sütun değerleri arasındaki ilişki kaybolur!</p>

    <h2 id="partition">Kısmi Sıralama: Partitioning</h2>

    <p>Bazen tüm diziyi sıralamak değil, <em>k</em> en küçük değeri bulmak yeter. <code>np.partition</code> diziyi alır ve $K$ verir; sonuçta en küçük $K$ değer solda, geri kalan sağda (iç sıralama keyfi):</p>
""" + code_block("""x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)""", "partition.py") + """
    <p>Çok boyutlu dizide herhangi bir eksen boyunca:</p>
""" + code_block("np.partition(X, 2, axis=1)", "partition_axis.py") + """
    <p><code>np.argsort</code> gibi <code>np.argpartition</code> da partition indekslerini verir.</p>

    <h2 id="knn">Örnek: k-En Yakın Komşular</h2>

    <p><code>argsort</code>'u çok eksenli kullanarak her noktanın en yakın komşularını bulalım. 10 rastgele 2B nokta ($10 \times 2$):</p>
""" + code_block("X = rng.random((10, 2))", "knn_X.py") + """
    <p>Her nokta çifti arasındaki kare mesafe. İki nokta arası kare mesafe boyutlar boyunca kare farkların toplamı; <a href="05-broadcasting.html">broadcasting</a> ve <a href="04-aggregates.html">agregasyon</a> ile tek satırda:</p>
""" + code_block("dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)", "knn_dist.py") + """
    <p>Karmaşık görünüyorsa adım adım:</p>
""" + code_block("""differences = X[:, np.newaxis, :] - X[np.newaxis, :]
print("differences.shape:", differences.shape)""", "knn_step1.py") + code_block("""sq_differences = differences ** 2
print("sq_differences.shape:", sq_differences.shape)""", "knn_step2.py") + code_block("""dist_sq = sq_differences.sum(-1)
print("dist_sq.shape:", dist_sq.shape)""", "knn_step3.py") + """
    <p>Köşegen (her noktanın kendine mesafesi) sıfır olmalı:</p>
""" + code_block("dist_sq.diagonal()", "knn_diag.py") + """
    <p>Her satır boyunca <code>argsort</code> — sol sütunlar en yakın komşu indeksleri:</p>
""" + code_block("""nearest = np.argsort(dist_sq, axis=1)
print(nearest)""", "knn_nearest.py") + """
    <p>İlk sütun 0–9 sırası: her noktanın en yakın komşusu kendisi.</p>

    <p>Sadece en yakın $k$ komşu gerekiyorsa tam sıralama fazla — <code>np.argpartition</code>:</p>
""" + code_block("""K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)""", "knn_partition.py") + """
    <p>Her noktadan iki en yakın komşuya çizgi çizilebilir (Matplotlib). Bazı noktalardan iki satırdan fazla çizgi çıkabilir: A, B'nin en yakın komşusu olsa B, A'nın en yakın komşusu olmak zorunda değildir.</p>

    <p>Döngü yazmak cazip gelebilir ama vektörize sürüm çok daha verimlidir; girdi boyutundan bağımsız aynı kod 100 veya 1.000.000 noktada çalışır. Çok büyük aramalarda KD-Tree gibi $\mathcal{O}[N\log N]$ algoritmalar vardır — <a href="http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html" target="_blank" rel="noopener">Scikit-Learn KDTree</a>.</p>

    <h2 id="big-o">Ayrıntı: Big-O Notasyonu</h2>

    <p>Big-O notasyonu bir algoritmanın girdi büyüdükçe işlem sayısının nasıl ölçeklendiğini tanımlar. Teoride small-o, big-$\theta$, big-$\Omega$ ayrımları vardır; pratikte veri biliminde genelde daha gevşek yorum kullanılır: algoritmanın ölçeklenmesinin genel tanımı.</p>

    <p>$\mathcal{O}[N]$ algoritma $N=1000$ için 1 saniye sürüyorsa $N=5000$ için kabaca 5 saniye beklenir. $\mathcal{O}[N^2]$ algoritma $N=1000$ için 1 saniye ise $N=5000$ için yaklaşık 25 saniye.</p>

    <p>Big-O tek başına duvar saati süresini söylemez — yalnızca $N$ değişince ölçeklenmeyi. Küçük veride $\mathcal{O}[N^2]$ algoritma 0,01 s, $\mathcal{O}[N]$ algoritma 1 s sürebilir; $N$ 1000 kat artınca $\mathcal{O}[N]$ kazanır.</p>

    <p>Milyarlarca örnekte $\mathcal{O}[N]$ ile $\mathcal{O}[N^2]$ farkı kritiktir. Kitap boyunca algoritma karşılaştırmalarında bu notasyonu kullanacağız.</p>

    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p><code>np.argpartition</code> ile dizideki 3 en küçük elemanın indekslerini bulun.</p>
""" + code_block("""import numpy as np
x = np.array([7, 2, 9, 1, 5, 3])
i = np.argpartition(x, 3)[:3]
print("3 en küçük:", x[i], "  indeksler:", i)""", "deneme_argpartition.py") + """
    </div>

    <div class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</div>
      <p><a href="09-structured-arrays.html">2.9 Yapılandırılmış Diziler →</a></p>
    </div>
""" + FOOT

write("08-sorting.html", ch08)

# --- Chapter 09 ---
ch09 = head(
    "2.9 Yapılandırılmış Diziler",
    "09-structured-arrays",
    "2.9 Yapılandırılmış Veri: NumPy Structured Arrays",
    "https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html",
    "09 Structured Data: NumPy's Structured Arrays",
) + """
    <p>Verimiz çoğu zaman homojen sayı dizisi olarak temsil edilir; bazen bu yeterli değildir. Bu bölüm NumPy'nin <strong>structured arrays</strong> (yapılandırılmış diziler) ve <strong>record arrays</strong> (<code>recarray</code>) yapılarını anlatır — bileşik, heterojen veri için verimli depolama. Basit işlemler için kullanışlı olsalar da benzer senaryolar genelde Pandas <code>DataFrame</code>'e yönelir (<a href="../03-pandas/index.html">Bölüm 3 — Pandas</a>).</p>
""" + code_block("import numpy as np", "import_numpy.py") + """
    <p>Birkaç kişinin adı, yaşı, kilosu gibi kategorileri ayrı dizilerde tutmak mümkün:</p>
""" + code_block("""name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]""", "separate_arrays.py") + """
    <p>Bu biraz hantal — üç dizinin ilişkili olduğunu göstermez. Structured array tek yapıda tüm veriyi tutar:</p>
""" + code_block("x = np.zeros(4, dtype=int)", "zeros_simple.py") + """
    <p>Bileşik veri tipi ile structured array:</p>
""" + code_block("""data = np.zeros(4, dtype={'names': ('name', 'age', 'weight'),
                          'formats': ('U10', 'i4', 'f8')})
print(data.dtype)""", "structured_create.py") + """
    <p><code>'U10'</code> = en fazla 10 karakter Unicode string; <code>'i4'</code> = 32 bit tamsayı; <code>'f8'</code> = 64 bit float.</p>
""" + code_block("""data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)""", "structured_fill.py") + """
    <p>İndeks veya alan adıyla erişim:</p>
""" + code_block("data['name']          # tüm isimler", "struct_names.py") + code_block("data[0]               # ilk satır", "struct_row0.py") + code_block("data[-1]['name']      # son satırın adı", "struct_last_name.py") + """
    <p>Boolean maskeleme ile filtreleme:</p>
""" + code_block("data[data['age'] < 30]['name']  # 30 yaş altı isimler", "struct_filter.py") + """
    <p>Bunlardan karmaşık işlemler için muhtemelen Pandas düşünün — <code>DataFrame</code> NumPy dizileri üzerine kurulu, çok daha zengin manipülasyon sunar (<a href="../03-pandas/index.html">Bölüm 3</a>).</p>

    <h2 id="dtype-olusturma">Structured Array Oluşturmayı Keşfetmek</h2>

    <p>Structured array veri tipleri birkaç yolla belirtilebilir. Sözlük yöntemi:</p>
""" + code_block("""np.dtype({'names': ('name', 'age', 'weight'),
          'formats': ('U10', 'i4', 'f8')})""", "dtype_dict.py") + """
    <p>Sayısal tipler Python veya NumPy tipleriyle:</p>
""" + code_block("""np.dtype({'names': ('name', 'age', 'weight'),
          'formats': ((np.str_, 10), int, np.float32)})""", "dtype_python_types.py") + """
    <p>Tuple listesi:</p>
""" + code_block("np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])", "dtype_list.py") + """
    <p>Alan adları önemli değilse yalnızca tipler virgülle ayrılmış string:</p>
""" + code_block("np.dtype('S10,i4,f8')", "dtype_string.py") + """
    <p>Kısa format kodları: isteğe bağlı ilk karakter <code>&lt;</code> veya <code>&gt;</code> (little/big endian); sonra veri tipi karakteri; son olarak bayt cinsinden boyut.</p>

    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Karakter</th><th>Açıklama</th><th>Örnek</th></tr></thead>
        <tbody>
          <tr><td><code>'b'</code></td><td>Byte</td><td><code>np.dtype('b')</code></td></tr>
          <tr><td><code>'i'</code></td><td>İşaretli tamsayı</td><td><code>np.dtype('i4') == np.int32</code></td></tr>
          <tr><td><code>'u'</code></td><td>İşaretsiz tamsayı</td><td><code>np.dtype('u1') == np.uint8</code></td></tr>
          <tr><td><code>'f'</code></td><td>Kayan nokta</td><td><code>np.dtype('f8') == np.float64</code></td></tr>
          <tr><td><code>'c'</code></td><td>Karmaşık sayı</td><td><code>np.dtype('c16') == np.complex128</code></td></tr>
          <tr><td><code>'S'</code>, <code>'a'</code></td><td>String (byte)</td><td><code>np.dtype('S5')</code></td></tr>
          <tr><td><code>'U'</code></td><td>Unicode string</td><td><code>np.dtype('U') == np.str_</code></td></tr>
          <tr><td><code>'V'</code></td><td>Ham veri (void)</td><td><code>np.dtype('V') == np.void</code></td></tr>
        </tbody>
      </table>
    </div>

    <h2 id="gelismis-bilesik">Daha Gelişmiş Bileşik Tipler</h2>

    <p>Her eleman dizi veya matris içeren tip tanımlanabilir. $3 \times 3$ float matris alanı <code>mat</code>:</p>
""" + code_block("""tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])""", "nested_matrix.py") + """
    <p>Her eleman <code>id</code> ve $3 \times 3$ matris içerir. Neden çok boyutlu dizi veya sözlük değil? NumPy <code>dtype</code> doğrudan C yapı tanımına karşılık gelir — C/Fortran kütüphaneleriyle arayüzde güçlü köprü.</p>

    <h2 id="recarray">Record Arrays: Structured Array'in Bir Varyantı</h2>

    <p>NumPy <code>np.recarray</code> sınıfı structured array ile neredeyse aynıdır; ek özellik: alanlara sözlük anahtarı yerine <strong>nokta notasyonu</strong> ile erişim.</p>
""" + code_block("data['age']", "rec_age_bracket.py") + """
    <p>Record array olarak:</p>
""" + code_block("""data_rec = data.view(np.recarray)
data_rec.age""", "rec_age_dot.py") + """
    <p>Dezavantaj: record array'lerde alan erişiminde ek yük vardır — kitaptaki zamanlama (notebook <code>%timeit</code>):</p>
""" + code_block("""import time

def bench(fn, n=10000):
    t0 = time.perf_counter()
    for _ in range(n):
        fn()
    return (time.perf_counter() - t0) / n * 1e6

d = data  # structured array
dr = data.view(np.recarray)

print(f"data['age']:     {bench(lambda: d['age']):.2f} µs")
print(f"data_rec['age']: {bench(lambda: dr['age']):.2f} µs")
print(f"data_rec.age:    {bench(lambda: dr.age):.2f} µs")""", "recarray_timing.py") + """
    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Ders notu — recarray zamanlama</div>
      <p>Nokta notasyonu (<code>data_rec.age</code>) biraz daha yavaştır. Kolaylık mı performans mı — uygulamanıza bağlı. Günlük tablo verisinde Pandas DataFrame genelde daha iyi seçimdir.</p>
    </div>

    <h2 id="pandas-gecis">Pandas'a Geçiş</h2>

    <p>Bu bölüm kitabın bu kısmının sonunda bilinçli olarak yer alır — bir sonraki pakete, <strong>Pandas</strong>'a doğal geçiş sağlar. Structured array C/Fortran ikili formatlarına eşlemede işe yarar; günlük yapılandırılmış veri için Pandas çok daha iyi — <a href="../03-pandas/index.html">Bölüm 3</a>'te derinlemesine ele alınır. Bkz. ayrıca <a href="01-understanding-data-types.html">2.1 Veri Tipleri</a>'ndeki bileşik tip atfı.</p>

    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>İki kişilik structured array oluşturup <code>age</code> alanına göre filtreleyin.</p>
""" + code_block("""import numpy as np
d = np.array([('Ali', 20), ('Ayşe', 30)], dtype=[('name', 'U10'), ('age', 'i4')])
print(d[d['age'] >= 25])""", "deneme_structured.py") + """
    </div>
""" + FOOT

write("09-structured-arrays.html", ch09)

print("All 5 chapters written to", OUT)
