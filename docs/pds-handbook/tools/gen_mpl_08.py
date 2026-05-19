#!/usr/bin/env python3
"""Generate 04-matplotlib/08-multiple-subplots.html (TR body)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_mpl_helpers import addon, try_it, next_link
from nb_html_utils import build_from_notebook, orig_line, h1, h2
from write_matplotlib_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html"

tr_md = {
    0: h1("Çoklu Alt Grafikler"),
    1: """    <p>Bazen verinin farklı görünümlerini yan yana karşılaştırmak yararlıdır.
    Matplotlib bunu tek bir figür içinde birden fazla alt grafik (subplot) düzenleyerek sağlar.</p>""",
    3: h2("plt.axes: Elle alt grafikler", "plt-axes-el")
    + """    <p>Eksen oluşturmanın en temel yolu <code>plt.axes</code> kullanmaktır.
    Varsayılan olarak bu, tüm figürü kaplayan standart bir eksen oluşturur; farklı bir konum ve boyut için <code>plt.axes</code>'e bir dizi verilebilir (aşağıdaki şekil):</p>""",
    5: """    <p>Nesne yönelimli arayüzdeki karşılığı <code>fig.add_axes</code>'tir.
    İki dikey istiflenmiş eksen oluşturmak için bunu kullanalım (aşağıdaki şekil):</p>""",
    7: """    <p>Artık iki eksenimiz var (üstteki işaret etiketleri yok); üst panelin altı (konum 0.5) alt panelin üstüyle (0.1 + 0.4) örtüşüyor.</p>""",
    8: h2("plt.subplot: Basit alt grafik ızgaraları", "plt-subplot-izgara")
    + """    <p>Hizalı sütun veya satır alt grafikler yaygındır; Matplotlib bunları kolaylaştıran birkaç yardımcı rutin sunar.
    En düşük seviye <code>plt.subplot</code>'tur; ızgarada tek bir alt grafik oluşturur.
    Komut üç tamsayı alır — satır sayısı, sütun sayısı ve bu şemada (sol üstten sağ alta) oluşturulacak grafiğin indeksi (aşağıdaki şekil):</p>""",
    10: """    <p>Alt grafikler arasındaki boşluğu ayarlamak için <code>plt.subplots_adjust</code> kullanılabilir.
    Aşağıdaki kod nesne yönelimli eşdeğeri <code>fig.add_subplot</code>'u kullanır (aşağıdaki şekil):</p>""",
    12: """    <p>Burada <code>plt.subplots_adjust</code>'in <code>hspace</code> ve <code>wspace</code> bağımsız değişkenlerini kullandık; bunlar alt grafik boyutunun birimleri cinsinden dikey ve yatay boşluğu belirtir (burada boşluk alt grafik genişlik ve yüksekliğinin %40'ı).</p>""",
    13: h2("plt.subplots: Tüm ızgarayı tek seferde", "plt-subplots-tek")
    + """    <p>Büyük bir alt grafik ızgarası oluştururken ve iç panellerde eksen etiketlerini gizlemek istediğinizde yukarıdaki yöntem çabuk yorucu olur.
    Bu iş için <code>plt.subplots</code> daha kolaydır (sonundaki <code>s</code>'e dikkat). Tek alt grafik yerine tek satırda tam bir ızgara oluşturur ve NumPy dizisi olarak döndürür.
    Bağımsız değişkenler satır ve sütun sayısıdır; isteğe bağlı <code>sharex</code> ve <code>sharey</code> eksenler arası ölçek ilişkisini belirler.</p>
    <p>Aynı satırdaki tüm eksenler y ölçeğini, aynı sütundakiler x ölçeğini paylaşan $2 \\times 3$ bir ızgara oluşturalım (aşağıdaki şekil):</p>""",
    15: """    <p><code>sharex</code> ve <code>sharey</code> ile ızgaranın iç etiketleri otomatik kaldırıldı; daha temiz bir çizim elde edildi.
    Dönen eksen dizisi, standart dizi indeksleme ile istenen ekseni seçmeyi kolaylaştırır (aşağıdaki şekil):</p>""",
    17: """    <p><code>plt.subplot</code>'a kıyasla <code>plt.subplots</code> Python'un sıfırdan başlayan indekslemesiyle daha tutarlıdır; <code>plt.subplot</code> MATLAB tarzı birden başlayan indeks kullanır.</p>""",
    18: h2("plt.GridSpec: Daha karmaşık düzenler", "plt-gridspec")
    + """    <p>Birden fazla satır ve sütunu kapsayan alt grafiklere geçmek için en iyi araç <code>plt.GridSpec</code>'tir.
    <code>plt.GridSpec</code> kendi başına çizim oluşturmaz; <code>plt.subplot</code> tarafından tanınan bir arayüzdür.
    Örneğin belirli genişlik ve yükseklik aralıklı iki satır üç sütunlu bir <code>GridSpec</code> şöyle görünür:</p>""",
    21: """    <p>Bundan sonra alt grafik konum ve boyutlarını tanıdık Python dilimleme sözdizimiyle belirtebiliriz (aşağıdaki şekil):</p>""",
    23: """    <p>Bu esnek hizalama geniş kullanım alanına sahiptir; en çok aşağıdaki şekildeki gibi çok eksenli histogram düzenleri için kullanırım:</p>""",
    25: """    <p>Kenarlarıyla birlikte bu tür dağılım çizimi yeterince yaygındır; Seaborn paketinde kendi çizim API'si vardır — ayrıntılar için
    <a href="14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a> bölümüne bakın.</p>""",
}

inserts = {
    9: try_it(
        "Alt grafik ızgarası",
        "2×2 ızgara oluşturup her hücreye metin yazın.",
        """fig, axes = plt.subplots(2, 2)
for ax in axes.flat:
    ax.text(0.5, 0.5, 'panel', ha='center', fontsize=14)""",
        "deneme_subplots_2x2.py",
    ),
    14: addon(
        "sharex ve sharey",
        "<p>Paylaşılan eksenler ölçeği eşitler; karşılaştırma grafiklerinde çok kullanışlıdır. İç etiketler gizlenir; dış kenarlarda etiket bırakın.</p>",
    ),
    24: try_it(
        "GridSpec dilimleme",
        "Üst satırın tamamını tek panel, alt sol iki sütunu bir panel yapın.",
        """grid = plt.GridSpec(2, 3)
plt.subplot(grid[0, :])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])""",
        "deneme_gridspec.py",
    ),
}

code_names = {
    2: "matplotlib_inline.py",
    4: "axes_manual.py",
    6: "add_axes_stacked.py",
    9: "subplot_loop.py",
    11: "subplots_adjust.py",
    14: "subplots_share.py",
    16: "subplots_index.py",
    19: "gridspec_empty.py",
    20: "gridspec_create.py",
    22: "gridspec_slice.py",
    24: "marginal_histogram.py",
}

body = (
    orig_line(EN, "04.08 Multiple Subplots")
    + "\n"
    + build_from_notebook(
        "04.08-Multiple-Subplots.ipynb",
        tr_md,
        code_names=code_names,
        inserts=inserts,
    )
    + "\n"
    + next_link("09-text-and-annotation.html", "4.9 Metin ve Açıklama")
)

if __name__ == "__main__":
    path = write_chapter("08-multiple-subplots", body)
    print("wrote", path)
