#!/usr/bin/env python3
"""Generate 04-matplotlib/09-text-and-annotation.html (TR body)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_mpl_helpers import addon, try_it, next_link
from nb_html_utils import build_from_notebook, orig_line, h1, h2
from write_matplotlib_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/04.09-text-and-annotation.html"

tr_md = {
    0: h1("Metin ve Açıklama"),
    1: """    <p>İyi bir görselleştirme okuyucuyu yönlendirerek figürün bir hikâye anlatmasını sağlar.
    Bazen hikâye tamamen görsel olabilir; bazen küçük metin ipuçları ve etiketler gerekir.
    En temel açıklamalar eksen etiketleri ve başlıklardır; seçenekler bununla sınırlı değildir.
    Veriye bakalım ve ilginç bilgiyi iletmek için nasıl görselleştirip açıklayabileceğimize bakalım.
    Çizim için not defterini hazırlayıp kullanacağımız işlevleri içe aktararak başlayalım:</p>""",
    3: h2("Örnek: Tatillerin ABD doğumlarına etkisi", "ornek-tatil-dogumlari")
    + """    <p>Daha önce
    <a href="../03-pandas/09-pivot-tables.html#ornek-dogum">Örnek: Doğum oranı verisi</a> bölümünde çalıştığımız veriye dönelim; takvim yılı boyunca ortalama doğumları çizmiştik.
    Aynı temizleme adımlarıyla başlayıp sonucu çizelim (aşağıdaki şekil):</p>""",
    7: """    <p>Bu tür veriyi görselleştirirken okuyucunun dikkatini çekmek için çizimin belirli özelliklerini elle açıklamak yararlıdır.
  Bu, <code>plt.text</code> / <code>ax.text</code> ile belirli <em>x</em>/<em>y</em> konumlarına metin yerleştirerek yapılır (aşağıdaki şekil):</p>""",
    9: """    <p><code>ax.text</code> bir <em>x</em> konumu, <em>y</em> konumu, bir dize ve isteğe bağlı olarak renk, boyut, stil, hizalama gibi metin özelliklerini alır.
    Burada <code>ha='right'</code> ve <code>ha='center'</code> kullandık; <code>ha</code> <em>horizontal alignment</em> (yatay hizalama) kısaltmasıdır.
    Seçenekler için <code>plt.text</code> ve <code>mpl.text.Text</code> docstring'lerine bakın.</p>""",
    10: h2("Dönüşümler ve metin konumu", "donusumler-metin")
    + """    <p>Önceki örnekte metni veri konumlarına sabitledik. Bazen metni veriden bağımsız olarak eksen veya figürün sabit bir konumuna sabitlemek iyidir.
    Matplotlib'de bu <em>transform</em> (dönüşüm) değiştirilerek yapılır.</p>
    <p>Matplotlib birkaç koordinat sistemi kullanır: $(x, y) = (1, 1)$ veri noktası eksen veya figürde belirli bir konuma, o da ekranda belirli bir piksele karşılık gelir.
    Matematiksel olarak bu sistemler arası dönüşüm görece basittir; Matplotlib bunu <code>matplotlib.transforms</code> alt modülünde yapar.</p>
    <p>Tipik kullanıcı dönüşüm ayrıntılarıyla nadiren uğraşır; metin yerleşiminde şu üç önceden tanımlı dönüşüm yararlıdır:</p>
    <ul>
      <li><code>ax.transData</code>: Veri koordinatlarıyla ilişkili dönüşüm</li>
      <li><code>ax.transAxes</code>: Eksen boyutlarının birimi cinsinden eksenle ilişkili dönüşüm</li>
      <li><code>fig.transFigure</code>: Figür boyutlarının birimi cinsinden figürle ilişkili dönüşüm</li>
    </ul>
    <p>Bu dönüşümleri kullanarak çeşitli konumlara metin çizen bir örneğe bakalım (aşağıdaki şekil):</p>""",
    12: """    <p>Matplotlib'in varsayılan metin hizalaması, her dizenin başındaki "." karakterinin belirtilen koordinata yaklaşık oturmasını sağlar.</p>
    <p><code>transData</code> x ve y eksen etiketleriyle ilişkili veri koordinatlarını verir.
    <code>transAxes</code> eksenin sol alt köşesinden (burada beyaz kutu) eksen boyutunun kesri olarak konum verir.
    <code>transFigure</code> benzerdir; konum figürün sol alt köşesinden (gri kutu) figür boyutunun kesri olarak verilir.</p>
    <p>Eksen sınırlarını değiştirirsek yalnızca <code>transData</code> koordinatlarının etkilendiğini, diğerlerinin sabit kaldığını görün (aşağıdaki şekil):</p>""",
    14: """    <p>Bu davranış eksen sınırlarını etkileşimli değiştirerek daha net görülebilir: kodu not defterinde çalıştırıyorsanız <code>%matplotlib inline</code> yerine <code>%matplotlib notebook</code> kullanıp menüyle etkileşime geçebilirsiniz.</p>""",
    15: h2("Oklar ve annotate", "oklar-annotate")
    + """    <p>İşaret çizgileri ve metinle birlikte yararlı bir başka açıklama basit oklardır.</p>
    <p><code>plt.arrow</code> vardır ancak önermem: oluşturduğu oklar SVG nesneleridir, en-boy oranı değişince hizalamak zorlaşır.
    Bunun yerine metin ve oku esnek tanımlayan <code>plt.annotate</code> önerilir.</p>
    <p>İşte <code>annotate</code>'in birkaç seçeneğiyle gösterimi (aşağıdaki şekil):</p>""",
    17: """    <p>Ok stili <code>arrowprops</code> sözlüğüyle kontrol edilir; çok sayıda seçenek vardır.
    Matplotlib çevrimiçi belgelerinde iyi belgelenmiştir; burada birkaç örnekle gösterelim.
    Önceki doğum grafiğinde olası seçeneklerin bir kısmını kullanalım (aşağıdaki şekil):</p>""",
    19: """    <p>Seçenek çeşitliliği <code>annotate</code>'i güçlü ve esnek kılar; neredeyse istediğiniz ok stilini oluşturabilirsiniz.
    Ne yazık ki bu özellikler çoğu zaman elle ince ayar gerektirir; yayın kalitesi grafiklerde zaman alıcı olabilir!
    Son olarak, yukarıdaki stil karışımı veri sunumu için en iyi uygulama değildir; mevcut seçeneklerin gösterimi içindir.</p>
    <p>Ok ve açıklama stilleri için Matplotlib
    <a href="https://matplotlib.org/stable/tutorials/text/annotations.html" target="_blank" rel="noopener">Annotations öğreticisi</a>nde daha fazla tartışma ve örnek vardır.</p>""",
}

inserts = {
    4: addon(
        "births.csv verisi",
        "<p><code>data/births.csv</code> dosyası handbook deposunda veya yorum satırındaki <code>curl</code> ile indirilebilir. Pyodide ortamında dosya yolu çalışma dizinine bağlıdır.</p>",
    ),
    8: try_it(
        "Türkçe tatil etiketi",
        "Grafiğe kendi dilinizde bir etiket ekleyin.",
        """ax.text('2012-5-1', 4000, 'İşçi Bayramı', ha='center', size=10, color='gray')""",
        "deneme_text_tr.py",
    ),
    11: try_it(
        "transAxes ile başlık",
        "Eksenin üst ortasına figürden bağımsız bir not ekleyin.",
        "ax.text(0.5, 1.02, 'Üst not', transform=ax.transAxes, ha='center', va='bottom')",
        "deneme_trans_axes.py",
    ),
}

code_names = {
    2: "imports_text.py",
    4: "download_births.py",
    5: "births_clean.py",
    6: "births_plot.py",
    8: "births_text_labels.py",
    11: "transforms_demo.py",
    13: "transforms_limits.py",
    16: "annotate_demo.py",
    18: "births_annotate.py",
}

body = (
    orig_line(EN, "04.09 Text and Annotation")
    + "\n"
    + build_from_notebook(
        "04.09-Text-and-Annotation.ipynb",
        tr_md,
        code_names=code_names,
        inserts=inserts,
    )
    + "\n"
    + next_link("10-customizing-ticks.html", "4.10 Eksen İşaretleri Özelleştirme")
)

if __name__ == "__main__":
    path = write_chapter("09-text-and-annotation", body)
    print("wrote", path)
