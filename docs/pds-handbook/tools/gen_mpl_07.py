#!/usr/bin/env python3
"""Generate 04-matplotlib/07-customizing-colorbars.html (TR body)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_mpl_helpers import addon, try_it, next_link
from nb_html_utils import build_from_notebook, orig_line, h1, h2, h3
from write_matplotlib_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html"

tr_md = {
    0: h1("Renk Çubukları Özelleştirme"),
    1: """    <p>Lejantlar ayrık noktaların ayrık etiketlerini gösterir.
    Nokta, çizgi veya bölgelerin rengine dayalı sürekli etiketler için etiketli bir renk çubuğu (colorbar) çok işe yarar.
    Matplotlib'de renk çubuğu, renklerin anlamına anahtar sağlayan ayrı bir eksen olarak çizilir.
    Kitap siyah-beyaz basıldığı için bu bölümün renkli şekilleri için
    <a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank" rel="noopener">çevrimiçi eki</a> vardır.
    Çizim için not defterini hazırlayıp kullanacağımız işlevleri içe aktararak başlayalım:</p>""",
    4: """    <p>Daha önce birkaç kez gördüğümüz gibi, en basit renk çubuğu <code>plt.colorbar</code> ile oluşturulur (aşağıdaki şekil):</p>""",
    6: """    <p>Şimdi bu renk çubuklarını özelleştirme ve çeşitli durumlarda etkili kullanma fikirlerine bakalım.</p>""",
    7: h2("Renk çubuklarını özelleştirme", "renk-cubugu-ozellestirme")
    + """    <p>Renk haritası (colormap), görselleştirmeyi oluşturan çizim işlevinin <code>cmap</code> bağımsız değişkeniyle belirtilir (aşağıdaki şekil):</p>""",
    9: """    <p>Kullanılabilir renk haritalarının adları <code>plt.cm</code> ad alanındadır; IPython sekme tamamlama ile yerleşik listeyi görebilirsiniz:</p>
    <div class="code-block" data-lang="text" data-filename="tab_tamamlama.txt" data-readonly="true">
      <pre><code>plt.cm.&lt;TAB&gt;</code></pre>
    </div>
    <p>Ancak renk haritası <em>seçebilmek</em> yalnızca ilk adımdır; asıl önemli olan olasılıklar arasında <em>nasıl karar vereceğinizdir</em>!
    Seçim ilk bakışta beklediğinizden çok daha incelikli olabilir.</p>""",
    10: h3("Renk haritası seçimi", "renk-haritasi-secimi")
    + """    <p>Görselleştirmede renk seçiminin tam bir işlenmesi bu kitabın kapsamı dışındadır; konuyla ilgili eğlenceli okuma için Nicholas Rougier, Michael Droettboom ve Philip Bourne'un
    <a href="http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833" target="_blank" rel="noopener">"Ten Simple Rules for Better Figures"</a> makalesine bakın.
    Matplotlib çevrimiçi belgelerinde de renk haritası seçimi üzerine
    <a href="https://matplotlib.org/stable/tutorials/colors/colormaps.html" target="_blank" rel="noopener">ayrıntılı bir tartışma</a> vardır.</p>
    <p>Genel olarak üç renk haritası kategorisini bilmelisiniz:</p>
    <ul>
      <li><em>Sıralı (sequential) haritalar</em>: Tek sürekli renk dizisi (ör. <code>binary</code>, <code>viridis</code>).</li>
      <li><em>Ayrışan (divergent) haritalar</em>: Ortalamadan pozitif/negatif sapmaları gösteren iki belirgin renk (ör. <code>RdBu</code>, <code>PuOr</code>).</li>
      <li><em>Nitel (qualitative) haritalar</em>: Belirli bir sıra olmadan karışık renkler (ör. <code>rainbow</code>, <code>jet</code>).</li>
    </ul>
    <p>Matplotlib 2.0 öncesi varsayılan olan <code>jet</code> nitel bir haritaya örnektir.
    Varsayılan olması talihsizdi; nitel haritalar nicel veriyi göstermek için genelde kötü seçimdir.
    Sorunlardan biri, ölçek arttıkça parlaklıkta düzgün bir ilerleme olmamasıdır.</p>
    <p><code>jet</code> renk çubuğunu siyah-beyaza çevirerek bunu görebiliriz (aşağıdaki şekil):</p>""",
    13: """    <p>Gri tonlamalı görüntüdeki parlak şeritlere dikkat edin.
    Tam renkte bile düzensiz parlaklık, gözün renk aralığının belirli bölümlerine çekilmesine ve veri setinin önemsiz kısımlarının vurgulanmasına yol açabilir.
    <code>viridis</code> (Matplotlib 2.0'dan beri varsayılan) gibi aralık boyunca eşit parlaklık değişimi için tasarlanmış bir harita daha iyidir; hem renk algısıyla uyumludur hem gri baskıya iyi aktarılır (aşağıdaki şekil):</p>""",
    15: """    <p>Ortalamadan pozitif/negatif sapmaları göstermek gibi durumlarda <code>RdBu</code> (*Kırmızı–Mavi*) gibi çift renkli çubuklar yardımcıdır. Ancak aşağıdaki şekilde görüldüğü gibi pozitif/negatif bilgi gri tonlamaya geçince kaybolabilir!</p>""",
    17: """    <p>Bu haritaların kullanımına devam ederken örnekler göreceğiz.</p>
    <p>Matplotlib'de çok sayıda renk haritası vardır; listelemek için IPython ile <code>plt.cm</code> alt modülünü keşfedebilirsiniz. Python'da daha ilkeli bir renk yaklaşımı için Seaborn kütüphanesine bakın
    (<a href="14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a>).</p>""",
    18: h3("Renk sınırları ve uzatmalar", "renk-sinirlari-uzatmalar")
    + """    <p>Matplotlib renk çubuğu özelleştirmesinde geniş olanak sunar.
    Renk çubuğu kendisi bir <code>Axes</code> örneğidir; gördüğümüz eksen ve işaret biçimlendirme yöntemleri geçerlidir.
    Örneğin renk sınırlarını daraltıp <code>extend</code> ile üst/alt sınır dışı değerleri üçgen okla gösterebiliriz.
    Gürültülü bir görüntü gösterirken işe yarayabilir (aşağıdaki şekil):</p>""",
    20: """    <p>Sol panelde varsayılan renk sınırları gürültülü piksellere uyum sağlar ve gürültü aralığı ilgilendiğimiz deseni tamamen bastırır.
    Sağ panelde sınırları elle ayarlayıp uzatmalar ekledik; sonuç veri için çok daha yararlı bir görselleştirmedir.</p>""",
    21: h3("Ayrık renk çubukları", "ayrik-renk-cubuklari")
    + """    <p>Renk haritaları varsayılan olarak süreklidir; bazen ayrık değerleri temsil etmek istersiniz.
    Bunun en kolay yolu uygun bir harita adıyla birlikte istenen bölme sayısını <code>plt.cm.get_cmap</code>'e vermektir (aşağıdaki şekil):</p>""",
    23: """    <p>Ayrık renk haritası diğerleri gibi kullanılabilir.</p>""",
    24: h2("Örnek: El yazısı rakamlar", "ornek-el-yazisi-rakamlar")
    + """    <p>Uygulama örneği: Scikit-Learn'deki rakamlar veri setinden el yazısı rakam görselleştirmesi; yaklaşık 2.000 adet $8 \\times 8$ küçük resim.</p>
    <p>Veri setini indirip birkaç örneği <code>plt.imshow</code> ile göstererek başlayalım (aşağıdaki şekil):</p>""",
    26: """    <p>Her rakam 64 pikselin tonuyla tanımlandığından, her rakam 64 boyutlu uzayda bir nokta düşünülebilir: her boyut bir pikselin parlaklığıdır.
    Bu kadar yüksek boyutlu veriyi görselleştirmek zordur; bir yaklaşım, ilişkileri koruyarak boyutu düşüren <em>boyut indirgeme</em> (ör. manifold öğrenme) kullanmaktır.
    Boyut indirgeme denetimsiz makine öğrenmesine örnektir;
    <a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.01-what-is-machine-learning.html" target="_blank" rel="noopener">Makine Öğrenmesi Nedir?</a> bölümünde ayrıntılandırılacaktır.</p>
    <p>Ayrıntıları erteleyerek rakam verisinin iki boyutlu bir manifold projeksiyonuna bakalım (ayrıntılar için
    <a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.10-manifold-learning.html" target="_blank" rel="noopener">Manifold Öğrenme</a>):</p>""",
    28: """    <p>Sonuçları ayrık renk haritamızla göstereceğiz; estetik için <code>ticks</code> ve <code>clim</code> ayarlayacağız (aşağıdaki şekil):</p>""",
    30: """    <p>Projeksiyon veri seti içindeki ilişkilere de ışık tutar: örneğin 2 ve 3 aralıkları neredeyse örtüşür; bazı 2 ve 3'lerin ayırt edilmesi zordur ve otomatik sınıflandırıcılar karıştırabilir.
    0 ve 1 gibi değerler daha uzaktır, karışma olasılığı daha düşüktür.</p>
    <p>Manifold öğrenme ve rakam sınıflandırmasına
    <a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.00-introduction.html" target="_blank" rel="noopener">Bölüm 5</a>'te döneceğiz.</p>""",
}

inserts = {
    5: addon(
        "get_cmap ve seaborn-white",
        "<p>Matplotlib 3.7+ için <code>matplotlib.colormaps['Blues']</code> veya <code>plt.colormaps['Blues']</code> tercih edilir; kod orijinal <code>get_cmap</code> ile bırakılmıştır. <code>seaborn-white</code> güncel sürümlerde farklı adla gelebilir.</p>",
    ),
    12: try_it(
        "Renk haritası karşılaştırın",
        "<code>view_colormap('plasma')</code> ve <code>view_colormap('jet')</code> yan yana düşünün; gri tonlamada hangisi daha düzgün?",
        "view_colormap('plasma')",
        "deneme_plasma.py",
    ),
    22: try_it(
        "Ayrık renk çubuğu",
        "6 bölümlü bir Blues haritası ve <code>extend='both'</code> deneyin.",
        """plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar(extend='both')
plt.clim(-1, 1)""",
        "deneme_discrete_cbar.py",
    ),
}

code_names = {
    2: "import_plt_style.py",
    3: "matplotlib_inline.py",
    5: "colorbar_basic.py",
    8: "imshow_blues.py",
    11: "grayscale_cmap.py",
    12: "view_jet.py",
    14: "view_viridis.py",
    16: "view_rdbu.py",
    19: "color_limits_extend.py",
    22: "discrete_colorbar.py",
    25: "digits_imshow.py",
    27: "digits_isomap.py",
    29: "digits_scatter_cbar.py",
}

body = (
    orig_line(EN, "04.07 Customizing Colorbars")
    + "\n"
    + build_from_notebook(
        "04.07-Customizing-Colorbars.ipynb",
        tr_md,
        code_names=code_names,
        inserts=inserts,
    )
    + "\n"
    + next_link("08-multiple-subplots.html", "4.8 Çoklu Alt Grafikler")
)

if __name__ == "__main__":
    path = write_chapter("07-customizing-colorbars", body)
    print("wrote", path)
