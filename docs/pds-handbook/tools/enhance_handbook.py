#!/usr/bin/env python3
"""Post-process split handbook pages: expand toward full PDS fidelity + ders notları."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# slug -> HTML block inserted before </main> (before footer content in source files)
INSERTIONS: dict[str, str] = {
    "chapters/01-ipython/01-help-and-documentation.html": '''
    <h3>Jupyter'de joker eşleme (<code>*Warning?</code>)</h3>
    <p>IPython'da <code>*</code> ile joker arama yapılır — kitaptaki örnek:</p>
    <div class="code-block" data-lang="text" data-readonly="true">
      <pre><code>In [10]: *Warning?
BytesWarning    DeprecationWarning    RuntimeWarning    ...</code></pre>
    </div>
    <div class="code-block" data-lang="text" data-readonly="true">
      <pre><code>In [10]: str.*find*?
str.find    str.rfind</code></pre>
    </div>
    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Ders notu</div>
      <p>Bilmiyorsanız ezberlemeyin — <code>?</code>, <code>??</code> ve Tab tamamlama veri biliminde en çok kullanılan üç araçtır. Kitabın bu bölümünü mutlaka okuyun.</p>
    </div>
''',
    "chapters/02-numpy/04-aggregates.html": '''
    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>3×4 rastgele matriste her satırın ortalamasını <code>axis=1</code> ile hesaplayın.</p>
      <div class="code-block" data-lang="python" data-filename="deneme_axis_mean.py">
        <pre><code>import numpy as np
M = np.random.random((3, 4))
print(M)
print("Satır ortalamaları:", M.mean(axis=1))</code></pre>
      </div>
    </div>
    <h3>Tam agregasyon tablosu (kitap)</h3>
    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Fonksiyon</th><th>NaN-güvenli</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>np.prod</code></td><td><code>np.nanprod</code></td><td>Çarpım</td></tr>
          <tr><td><code>np.var</code></td><td><code>np.nanvar</code></td><td>Varyans</td></tr>
          <tr><td><code>np.argmax</code></td><td><code>np.nanargmax</code></td><td>Maximum indeksi</td></tr>
          <tr><td><code>np.any</code></td><td>—</td><td>Herhangi biri True mu?</td></tr>
          <tr><td><code>np.all</code></td><td>—</td><td>Hepsi True mu?</td></tr>
        </tbody>
      </table>
    </div>
''',
    "chapters/02-numpy/06-boolean-masks.html": '''
    <h3>and / or vs &amp; / | (kitap uyarısı)</h3>
    <p>Python'un <code>and</code> / <code>or</code> operatörleri tek bir Boolean değer bekler; NumPy dizilerinde “belirsiz truth value” hatası verir. Dizi mantığı için bit düzeyinde <code>&amp;</code>, <code>|</code>, <code>~</code> kullanın.</p>
    <div class="code-block" data-lang="python" data-filename="and_vs_ampersand.py">
      <pre><code>import numpy as np
x = np.arange(10)
print((x &gt; 4) &amp; (x &lt; 8))  # doğru

# x &gt; 4 and x &lt; 8  # ValueError!</code></pre>
    </div>
    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>1–100 arası dizide 3'e ve 5'e tam bölünen sayıları maske ile seçin.</p>
      <div class="code-block" data-lang="python" data-filename="deneme_bolunebilir.py">
        <pre><code>import numpy as np
x = np.arange(1, 101)
mask = (x % 3 == 0) &amp; (x % 5 == 0)
print(x[mask])</code></pre>
      </div>
    </div>
''',
    "chapters/02-numpy/08-sorting.html": '''
    <h3>Selection sort ve bogosort (kitap)</h3>
    <p>Kitap, NumPy'nin hızlı sıralamasına karşılık eğitim amaçlı yavaş algoritmaları gösterir:</p>
    <div class="code-block" data-lang="python" data-filename="selection_sort.py">
      <pre><code>import numpy as np

def selection_sort(x):
    x = x.copy()
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        x[i], x[swap] = x[swap], x[i]
    return x

print(selection_sort(np.array([2, 1, 4, 3, 5])))</code></pre>
    </div>
    <div class="alert alert-tip handbook-addon">
      <div class="alert-title">💡 Big-O (kitap)</div>
      <p>Selection sort ortalama <code>O(N²)</code> — veri büyüdükçe kare oranında yavaşlar. NumPy <code>np.sort</code> ise <code>O(N log N)</code> quicksort kullanır; büyük dizilerde fark çarpıcıdır.</p>
    </div>
    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p><code>np.argpartition</code> ile dizideki 3 en küçük elemanın indekslerini bulun.</p>
      <div class="code-block" data-lang="python" data-filename="deneme_argpartition.py">
        <pre><code>import numpy as np
x = np.array([7, 2, 9, 1, 5, 3])
i = np.argpartition(x, 3)[:3]
print("3 en küçük:", x[i], "  indeksler:", i)</code></pre>
      </div>
    </div>
''',
    "chapters/02-numpy/09-structured-arrays.html": '''
    <h3>dtype tanımlama yolları (kitap)</h3>
    <div class="code-block" data-lang="python" data-filename="dtype_varyant.py">
      <pre><code>import numpy as np

print(np.dtype({'names': ('name', 'age'), 'formats': ('U10', 'i4')}))
print(np.dtype([('name', 'S10'), ('age', 'i4')]))
print(np.dtype('U10,i4,f8'))</code></pre>
    </div>
    <h3>İç içe alan: matris tipi</h3>
    <div class="code-block" data-lang="python" data-filename="dtype_matris.py">
      <pre><code>import numpy as np
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
print(X['mat'][0])</code></pre>
    </div>
    <div class="try-it-box">
      <div class="try-it-title">🧪 Şimdi deneyin</div>
      <p>İki kişilik structured array oluşturup <code>age</code> alanına göre filtreleyin.</p>
      <div class="code-block" data-lang="python" data-filename="deneme_structured.py">
        <pre><code>import numpy as np
d = np.array([('Ali', 20), ('Ayşe', 30)], dtype=[('name', 'U10'), ('age', 'i4')])
print(d[d['age'] &gt;= 25])</code></pre>
      </div>
    </div>
''',
}


def main():
    for rel, block in INSERTIONS.items():
        path = ROOT / rel
        if not path.exists():
            print(f"SKIP {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        marker = "  </main>"
        if block.strip() in text:
            print(f"already enhanced {rel}")
            continue
        if marker not in text:
            print(f"WARN no marker {rel}")
            continue
        text = text.replace(marker, block + "\n" + marker, 1)
        path.write_text(text, encoding="utf-8")
        print(f"enhanced {rel}")


if __name__ == "__main__":
    main()
