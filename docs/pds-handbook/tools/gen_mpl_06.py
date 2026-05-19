#!/usr/bin/env python3
"""Generate 04-matplotlib/06-customizing-legends.html (TR body)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_mpl_helpers import addon, try_it, next_link
from nb_html_utils import build_from_notebook, orig_line, h1, h2
from write_matplotlib_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html"

tr_md = {
    0: h1("Lejant Özelleştirme"),
    1: """    <p>Lejantlar bir görselleştirmeye anlam katar; çeşitli çizim öğelerine etiket atar.
    Basit bir lejant oluşturmayı daha önce gördük; burada Matplotlib'de lejantın konumunu ve görünümünü özelleştirmeye bakacağız.</p>
    <p>En basit lejant <code>plt.legend</code> komutuyla oluşturulur; bu komut etiketlenmiş tüm çizim öğeleri için otomatik lejant üretir (aşağıdaki şekle bakın):</p>""",
    5: """    <p>Böyle bir lejantı birçok yönden özelleştirebiliriz.
    Örneğin konumu belirtebilir ve çerçeveyi açabiliriz (aşağıdaki şekle bakın):</p>""",
    7: """    <p>Lejanttaki sütun sayısını <code>ncol</code> ile belirleyebiliriz (aşağıdaki şekil):</p>""",
    9: """    <p>Yuvarlatılmış kutu (<code>fancybox</code>), gölge, çerçeve saydamlığı (<code>framealpha</code>) veya metin etrafındaki dolgu (<code>borderpad</code>) gibi seçenekler de vardır (aşağıdaki şekil):</p>""",
    11: """    <p>Kullanılabilir lejant seçenekleri için <code>plt.legend</code> docstring'ine bakın.</p>""",
    12: h2("Lejant için öğe seçimi", "lejant-oge-secimi")
    + """    <p>Varsayılan olarak lejant, çizimdeki tüm etiketli öğeleri içerir.
    İstenen bu değilse, <code>plot</code> komutlarının döndürdüğü nesnelerle hangi öğe ve etiketlerin görüneceğini ince ayar yapabiliriz.
    <code>plt.plot</code> birden fazla çizgiyi aynı anda oluşturabilir ve oluşan <code>Line2D</code> örneklerinin listesini döndürür.
    Bunlardan herhangi birini <code>plt.legend</code>'a vermek, hangilerinin gösterileceğini ve hangi etiketlerin kullanılacağını belirtir (aşağıdaki şekil):</p>""",
    14: """    <p>Pratikte genelde ilk yöntem daha net: lejantta göstermek istediğiniz öğelere doğrudan <code>label</code> verin (aşağıdaki şekil):</p>""",
    16: """    <p>Lejant, <code>label</code> özniteliği ayarlanmamış tüm öğeleri yok sayar.</p>""",
    17: h2("Nokta boyutu için lejant", "nokta-boyutu-lejant")
    + """    <p>Bazen varsayılan lejant veri görselleştirmesi için yeterli olmaz.
    Örneğin nokta boyutunu kullanarak verinin belirli özelliklerini işaretliyorsanız, bunu yansıtan bir lejant isteyebilirsiniz.
    Burada Kaliforniya şehirlerinin nüfusunu nokta boyutuyla gösteriyoruz.
    Nokta boyutlarının ölçeğini gösteren bir lejant oluşturmak için etiketli ama veri içermeyen çizimler kullanacağız (aşağıdaki şekil):</p>""",
    20: """    <p>Lejant her zaman çizimdeki bir nesneye referans verir; belirli bir şekli göstermek istiyorsanız onu çizmeniz gerekir.
    Burada istediğimiz nesneler (gri daireler) çizimde olmadığı için boş listeler çizerek sahte öğeler oluşturuyoruz.
    Lejant yalnızca <code>label</code> belirtilmiş öğeleri listeler.</p>
    <p>Boş listeler çizerek lejantın alacağı etiketli nesneler yaratılır; lejant böylece yararlı bilgi verir.
    Bu strateji daha gelişmiş görselleştirmeler için kullanışlı olabilir.</p>""",
    21: h2("Birden fazla lejant", "birden-fazla-lejant")
    + """    <p>Bazen aynı eksene birden fazla lejant eklemek istersiniz.
    Maalesef Matplotlib bunu kolay yapmaz: standart <code>legend</code> arayüzüyle yalnızca tek bir lejant oluşturulabilir.
    İkinci bir <code>plt.legend</code> veya <code>ax.legend</code> çağrısı birincisinin üzerine yazar.
    Bunu, sıfırdan yeni bir lejant sanatçısı (<code>Artist</code>, Matplotlib'in görsel öğe taban sınıfı) oluşturup düşük seviyeli <code>ax.add_artist</code> ile ikinci sanatçıyı elle ekleyerek aşabiliriz (aşağıdaki şekil):</p>""",
    23: """    <p>Bu, her Matplotlib çizimini oluşturan düşük seviyeli sanatçı nesnelerine kısa bir bakıştır.
    <code>ax.legend</code> kaynak koduna bakarsanız (Jupyter'de <code>ax.legend??</code> ile yapabilirsiniz) işlevin uygun bir <code>Legend</code> sanatçısı oluşturup <code>legend_</code> özniteliğine kaydettiğini ve çizim çizilirken figüre eklendiğini görürsünüz.</p>""",
}

inserts = {
    4: addon(
        "seaborn stil adları",
        "<p><code>seaborn-whitegrid</code> eski Matplotlib sürümlerinde yaygındı; güncel sürümlerde <code>plt.style.use('ggplot')</code> veya <code>seaborn-v0_8-whitegrid</code> gerekebilir. Kod hücresi orijinal kitapla aynı bırakılmıştır.</p>",
    ),
    8: try_it(
        "Lejant konumunu değiştirin",
        "<code>loc</code> için <code>'best'</code>, <code>'outside upper right'</code> veya <code>bbox_to_anchor</code> deneyin.",
        "ax.legend(loc='best', frameon=True, title='Fonksiyonlar')\nfig",
        "deneme_legend_loc.py",
    ),
    19: try_it(
        "Boş liste lejantı",
        "Farklı boyutlarda sahte noktalarla özel bir lejant oluşturun.",
        """for s, lab in [(20, 'küçük'), (80, 'büyük')]:
    plt.scatter([], [], s=s, c='gray', alpha=0.5, label=lab)
plt.legend(scatterpoints=1, title='Boyut')""",
        "deneme_scatter_legend.py",
    ),
}

code_names = {
    2: "import_plt_style.py",
    3: "matplotlib_inline.py",
    4: "legend_basic.py",
    6: "legend_loc_frame.py",
    8: "legend_ncol.py",
    10: "legend_fancy.py",
    13: "legend_lines_list.py",
    15: "legend_labels.py",
    18: "download_cities.py",
    19: "cities_scatter_legend.py",
    22: "multiple_legends.py",
}

body = (
    orig_line(EN, "04.06 Customizing Legends")
    + "\n"
    + build_from_notebook(
        "04.06-Customizing-Legends.ipynb",
        tr_md,
        code_names=code_names,
        inserts=inserts,
    )
    + "\n"
    + next_link("07-customizing-colorbars.html", "4.7 Renk Çubukları Özelleştirme")
)

if __name__ == "__main__":
    path = write_chapter("06-customizing-legends", body)
    print("wrote", path)
