#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_mpl_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_matplotlib_chapter import write_chapter

NB = "04.14-Visualization-With-Seaborn.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>4.14 Seaborn ile Görselleştirme</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html" target="_blank" rel="noopener">Visualization with Seaborn</a></em></p>

    <p>Matplotlib on yıllardır Python'da bilimsel görselleştirmenin merkezinde olsa da en sadık kullanıcıları bile çoğu zaman yetersiz bıraktığını kabul eder. Matplotlib hakkında sık öne çıkan birkaç eleştiri vardır:</p>
    <ul>
      <li>Yaygın erken dönem eleştiri (artık güncelliğini yitirmiş): 2.0 sürümünden önce Matplotlib'ın renk ve stil varsayılanları zaman zaman zayıf ve eski moda görünüyordu.</li>
      <li>Matplotlib API'si nispeten düşük seviyededir. Gelişmiş istatistiksel görselleştirme mümkündür, ancak genelde <em>çok</em> fazla hazır kod gerektirir.</li>
      <li>Matplotlib, Pandas'tan on yıldan fazla önce vardı; bu nedenle Pandas <code>DataFrame</code> nesneleriyle kullanılmak üzere tasarlanmamıştır. <code>DataFrame</code>'den veri görselleştirmek için her <code>Series</code>'i ayıklayıp sık sık doğru biçime birleştirmeniz gerekir. <code>DataFrame</code> etiketlerini grafikte akıllıca kullanan bir çizim kütüphanesi daha hoş olurdu.</li>
    </ul>

    <p>Bu sorunlara bir yanıt <a href="http://seaborn.pydata.org/" target="_blank" rel="noopener">Seaborn</a>'dur. Seaborn, Matplotlib üzerinde grafik stili ve renk varsayılanları için mantıklı seçenekler sunan, yaygın istatistiksel grafik türleri için basit üst düzey fonksiyonlar tanımlayan ve Pandas'ın sağladığı işlevsellikle bütünleşen bir API sağlar.</p>

    <p>Adaletli olmak gerekirse Matplotlib ekibi de değişen ortama uyum sağladı: <a href="11-settings-and-stylesheets.html">4.11 Matplotlib Özelleştirme: Yapılandırma ve Stil Sayfaları</a> bölümünde ele alınan <code>plt.style</code> araçlarını ekledi ve Pandas verisini giderek daha sorunsuz işlemeye başlıyor. Ancak az önce sayılan nedenlerle Seaborn yararlı bir eklenti olmaya devam ediyor.</p>

    <p>Gelenek gereği Seaborn genelde <code>sns</code> olarak içe aktarılır. Aşağıdaki hücrede Matplotlib ile birlikte <strong>NumPy, Pandas ve Seaborn</strong> içe aktarılır; bu bölüm Pyodide'da Pandas + Matplotlib + Seaborn ön yüklemesi kullanır:</p>
""" + c(2, "import_sns.py") + addon(
    "Seaborn API katmanları",
    "<p>Seaborn'u üç katmanda düşünün:</p>"
    "<ul>"
    "<li><strong>Matplotlib katmanı:</strong> Her Seaborn grafiği altta Matplotlib <code>Axes</code> veya <code>Figure</code> oluşturur; "
    "<code>plt.xlabel</code>, <code>ax.set_title</code> gibi düşük seviye ayarlar hâlâ uygulanabilir.</li>"
    "<li><strong>Eksen düzeyi (axes-level):</strong> <code>sns.histplot</code>, <code>sns.scatterplot</code>, <code>sns.kdeplot</code>, "
    "<code>sns.violinplot</code> — mevcut veya yeni bir eksene çizer; <code>data=</code>, <code>x=</code>, <code>y=</code>, <code>hue=</code> ile sütun adlarına dayanır.</li>"
    "<li><strong>Şekil düzeyi (figure-level):</strong> <code>sns.relplot</code>, <code>sns.catplot</code>, <code>sns.pairplot</code>, "
    "<code>sns.jointplot</code>, <code>sns.lmplot</code>, <code>sns.displot</code> — çoğu alt grafik, lejant ve düzeni otomatik kurar; "
    "sonuç genelde <code>FacetGrid</code> veya <code>JointGrid</code> nesnesidir (<code>.map</code>, <code>.set_axis_labels</code> ile özelleştirilir).</li>"
    "</ul>"
    "<p>Kural: hızlı keşif için axes-level; kategorilere/alt grafiklere bölme için figure-level tercih edin.</p>",
) + """
    <h2 id="seaborn-grafikleri">Seaborn Grafiklerini Keşfetme</h2>

    <p>Seaborn'un ana fikri, istatistiksel veri keşfi için yararlı çeşitli grafik türlerini oluşturmaya yönelik üst düzey komutlar — hatta bazı istatistiksel model uydurmaları — sağlamasıdır.</p>

    <p>Seaborn'da kullanılabilir birkaç veri kümesine ve grafik türüne bakalım. Aşağıdakilerin <em>hepsi</em> ham Matplotlib komutlarıyla yapılabilir (Seaborn aslında altta bunu yapar); ancak Seaborn API'si çok daha uygundur.</p>

    <h3 id="histogram-kde">Histogramlar, KDE ve Yoğunluklar</h3>

    <p>İstatistiksel veri görselleştirmede çoğu zaman yalnızca histogram ve değişkenlerin birleşik dağılımlarını çizmek istersiniz. Matplotlib'da bunun nispeten doğrudan yapılabildiğini gördük (aşağıdaki şekil):</p>
""" + c(5, "matplotlib_hist.py") + """
    <p>Görsel çıktı olarak yalnızca histogram yerine, çekirdek yoğunluk tahmini (KDE) ile dağılımın pürüzsüz bir tahminini alabiliriz (<a href="04-density-and-contour-plots.html">4.4 Yoğunluk ve Kontur Grafikleri</a> bölümünde tanıtıldı); Seaborn bunu <code>sns.kdeplot</code> ile yapar (aşağıdaki şekil):</p>
""" + c(7, "kdeplot_1d.py") + """
    <p><code>kdeplot</code>'a <code>x</code> ve <code>y</code> sütunları geçirirsek bunun yerine birleşik yoğunluğun iki boyutlu görselleştirmesini elde ederiz (aşağıdaki şekil):</p>
""" + c(9, "kdeplot_2d.py") + """
    <p>Birleşik dağılımı ve kenar dağılımlarını birlikte görmek için bu bölümün ilerisinde daha ayrıntılı inceleyeceğimiz <code>sns.jointplot</code> kullanılabilir.</p>

    <h3 id="pair-plots">Çift Grafikler (Pair Plots)</h3>

    <p>Birleşik grafikleri daha büyük boyutlu veri kümelerine genellediğinizde <em>pair plot</em>'lara (çift grafiklere) ulaşırsınız. Çok boyutlu veride korelasyonları keşfetmek için — tüm değer çiftlerini birbirine karşı çizmek istediğinizde — çok yararlıdırlar.</p>

    <p>Bunu iyi bilinen Iris veri kümesiyle göstereceğiz; üç Iris türünün taç yaprak ve çanak yaprak ölçümlerini listeler:</p>
""" + c(12, "iris_load.py") + """
    <p>Örnekler arasındaki çok boyutlu ilişkileri görselleştirmek <code>sns.pairplot</code> çağırmak kadar kolaydır (aşağıdaki şekil):</p>
""" + c(14, "pairplot_iris.py") + """
    <h3 id="faceted-histograms">Yüzeyle ayrılmış histogramlar</h3>

    <p>Bazen veriyi alt kümelerin histogramlarıyla görmek en iyisidir (aşağıdaki şekil). Seaborn'un <code>FacetGrid</code>'i bunu basitleştirir. Çeşitli gösterge verilerine göre restoran personelinin aldığı bahşiş miktarına bakan bir veri kümesine bakacağız:<sup id="fnref1"><a href="#fn1">1</a></sup></p>

    <p><small id="fn1"><sup>1</sup> Bu bölümde kullanılan restoran personeli verisi çalışanları iki cinsiyete ayırır: kadın ve erkek. Biyolojik cinsiyet ikili değildir; ancak aşağıdaki tartışma ve görselleştirmeler bu veriyle sınırlıdır.</small></p>
""" + c(17, "tips_load.py") + c(18, "facetgrid_hist.py") + """
    <p>Yüzeyle ayrılmış grafik veri kümesine hızlı içgörüler verir: örneğin akşam yemeği saatinde erkek garsonlara ait verinin diğer kategorilere göre çok daha fazla olduğunu ve tipik bahşiş yüzdelerinin yaklaşık %10–20 aralığında olduğunu, her iki uçta aykırı değerler olduğunu görürüz.</p>

    <h3 id="categorical-plots">Kategorik Grafikler</h3>

    <p>Kategorik grafikler bu tür görselleştirme için de yararlı olabilir. Başka bir parametreyle tanımlanan kutular içinde bir parametrenin dağılımını görmenize olanak tanır (aşağıdaki şekil):</p>
""" + c(20, "catplot_box.py") + """
    <h3 id="joint-distributions">Birleşik Dağılımlar</h3>

    <p>Daha önce gördüğümüz pair plot'a benzer şekilde farklı veri kümeleri arasındaki birleşik dağılımı ve ilişkili kenar dağılımlarını göstermek için <code>sns.jointplot</code> kullanılabilir (aşağıdaki şekil):</p>
""" + c(22, "jointplot_hex.py") + """
    <p>Birleşik grafik otomatik çekirdek yoğunluk tahmini ve regresyon da yapabilir (aşağıdaki şekil):</p>
""" + c(24, "jointplot_reg.py") + """
    <h3 id="bar-plots">Çubuk Grafikleri</h3>

    <p>Zaman serileri <code>sns.factorplot</code> ile çizilebilir. Aşağıdaki örnekte <a href="../03-pandas/08-aggregation-and-grouping.html">3.8 Agregasyon ve Gruplama</a> bölümünde ilk gördüğümüz Gezegenler veri kümesini kullanacağız; sonuç aşağıdaki şekildedir:</p>
""" + c(26, "planets_load.py") + c(27, "catplot_count_year.py") + """
    <p>Bu gezegenlerin keşif <em>yöntemine</em> bakarak daha fazla bilgi edinebiliriz (aşağıdaki şekil):</p>
""" + c(29, "catplot_count_method.py") + """
    <p>Seaborn ile çizim hakkında daha fazla bilgi için <a href="http://seaborn.pydata.org/" target="_blank" rel="noopener">Seaborn dokümantasyonuna</a> ve özellikle <a href="https://seaborn.pydata.org/examples/index.html" target="_blank" rel="noopener">örnek galerisine</a> bakın.</p>

    <h2 id="marathon-ornegi">Örnek: Maraton Bitiş Sürelerini Keşfetme</h2>

    <p>Burada Seaborn'u bir maratonun bitiş sonuçlarını görselleştirmeye ve anlamaya yardımcı olmak için kullanacağız. Veriyi web kaynaklarından kazıdım, birleştirdim ve tanımlayıcı bilgileri kaldırdım; GitHub'a koydum, oradan indirilebilir (Python ile web kazıma ilgileniyorsanız O'Reilly'den Ryan Mitchell'in <a href="http://shop.oreilly.com/product/0636920034391.do" target="_blank" rel="noopener"><em>Web Scraping with Python</em></a> kitabını öneririm). Veriyi indirip Pandas'a yükleyerek başlayacağız:<sup id="fnref2"><a href="#fn2">2</a></sup></p>

    <p><small id="fn2"><sup>2</sup> Bu bölümde kullanılan maraton verisi koşucuları iki cinsiyete ayırır: erkek ve kadın. Cinsiyet bir spektrum olsa da aşağıdaki tartışma ve görselleştirmeler veriye bağlı oldukları için bu ikili ayrımı kullanır.</small></p>
""" + c(32, "download_marathon.py") + addon(
    "Maraton veri dosyası",
    "<p><code>data/marathon-data.csv</code> dosyası orijinal notebook ortamında olmalıdır. "
    "Tarayıcıdaki Pyodide ortamında dosya yoksa indirme hücresini okuyun veya veriyi yerel Jupyter'de indirin; "
    "mantığı anlamak için kodu salt okunur incelemek de yeterlidir.</p>",
) + c(33, "read_marathon.py") + """
    <p>Pandas'ın zaman sütunlarını Python dizileri (<code>object</code> tipi) olarak yüklediğine dikkat edin; bunu <code>DataFrame</code>'in <code>dtypes</code> özniteliğine bakarak görebiliriz:</p>
""" + c(35, "dtypes_before.py") + """
    <p>Zamanlar için bir dönüştürücü sağlayarak bunu düzeltelim:</p>
""" + c(37, "convert_time.py") + c(38, "dtypes_after.py") + """
    <p>Bu, zaman verisini işlemeyi kolaylaştırır. Seaborn çizim yardımcılarımız için ardından süreleri saniye cinsinden veren sütunlar ekleyelim:</p>
""" + c(40, "split_final_sec.py") + """
    <p>Verinin nasıl göründüğüne dair fikir edinmek için veri üzerinde bir <code>jointplot</code> çizebiliriz; aşağıdaki şekil sonucu gösterir:</p>
""" + c(42, "jointplot_marathon.py") + """
    <p>Kesikli çizgi, birinin maratonu tamamen sabit tempoda koşsaydı süresinin nerede olacağını gösterir. Dağılımın bunun üstünde olması (beklediğiniz gibi) çoğu insanın maraton boyunca yavaşladığını gösterir. Rekabet koşmuşsanız ikinci yarıda hızlananların — yani yarışı \"negatif bölmüş\" olanların — sözlükte adının geçtiğini bilirsiniz.</p>

    <p>Veride başka bir sütun oluşturalım: bölünme oranı (<code>split_frac</code>), her koşucunun yarışı ne ölçüde negatif veya pozitif böldüğünü ölçer:</p>
""" + c(44, "split_frac.py") + """
    <p>Bu bölünme farkı sıfırın altındaysa kişi yarışı o oranda negatif bölmüştür. Bu bölünme oranının dağılım grafiğini çizelim (aşağıdaki şekil):</p>
""" + c(46, "displot_split_frac.py") + c(47, "count_negative_split.py") + """
    <p>Yaklaşık 40.000 katılımcıdan yalnızca 250 kişi maratonunu negatif bölmüştür.</p>

    <p>Bu bölünme oranı ile diğer değişkenler arasında korelasyon olup olmadığına bakalım. Bunu tüm bu korelasyonların grafiklerini çizen bir <code>PairGrid</code> ile yapacağız (aşağıdaki şekil):</p>
""" + c(49, "pairgrid_marathon.py") + """
    <p>Bölünme oranı yaşla özellikle korelasyon göstermiyor gibi görünüyor; ancak bitiş süresiyle korelasyon gösteriyor: daha hızlı koşucular maraton sürelerini daha dengeli bölmeye eğilimli. Cinsiyete göre ayrılmış bölünme oranı histogramlarına yakınlaşalım (aşağıdaki şekil):</p>
""" + c(51, "kdeplot_gender.py") + """
    <p>İlginç olan, erkekler arasında neredeyse eşit bölmeye yakın koşan çok daha fazla kişi var! Erkekler ve kadınlar arasında neredeyse çift modlu bir dağılım görünüyor. Dağılımları yaş fonksiyonu olarak inceleyerek neler olup bittiğini anlamaya çalışalım.</p>

    <p>Dağılımları karşılaştırmanın güzel bir yolu <em>keman grafiği</em> (violin plot) kullanmaktır (aşağıdaki şekil):</p>
""" + c(53, "violinplot_gender.py") + """
    <p>Biraz daha derine inelim ve bu keman grafiklerini yaşa göre karşılaştıralım (aşağıdaki şekil). Her kişinin on yıllık yaş aralığında olduğunu belirten yeni bir sütun oluşturarak başlayacağız:</p>
""" + c(55, "age_dec.py") + c(56, "violinplot_age_dec.py") + """
    <p>Erkek ve kadın dağılımlarının nerede farklılaştığını görebiliriz: 20'li–50'li yaşlardaki erkeklerin bölünme dağılımları, aynı yaş grubundaki (veya herhangi bir yaştaki) kadınlara kıyasla düşük bölünmeye doğru belirgin bir aşırı yoğunluk gösteriyor.</p>

    <p>Ayrıca şaşırtıcı biçimde 80 yaşındaki kadınlar bölünme sürelerinde <em>herkesi</em> geride bırakıyor gibi görünüyor; ancak bu muhtemelen az sayıda etkisidir, çünkü bu aralıkta yalnızca bir avuç koşucu var:</p>
""" + c(58, "count_age_80.py") + """
    <p>Negatif bölen erkeklere dönelim: bunlar kim? Bölünme oranı hızlı bitişle korelasyon gösteriyor mu? Bunu çok kolay çizebiliriz. <code>regplot</code> kullanacağız; veriye otomatik doğrusal regresyon modeli uydurur (aşağıdaki şekil):</p>
""" + c(60, "lmplot_marathon.py") + """
    <p>Görünüşe göre hem erkekler hem kadınlar arasında hızlı bölenler, yaklaşık 15.000 saniye (yaklaşık 4 saat) içinde bitiren daha hızlı koşuculardır. Bundan yavaş olanların ikinci yarıyı hızlı koşma olasılığı çok daha düşüktür.</p>
""" + try_it(
    "Seaborn + Pandas",
    "Küçük bir DataFrame ile <code>sns.scatterplot</code> deneyin — sütun adlarını doğrudan kullanın:",
    """import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [1, 4, 2, 3], 'grup': ['A', 'A', 'B', 'B']})
sns.scatterplot(data=df, x='x', y='y', hue='grup')
plt.title('Seaborn scatterplot')
plt.show()""",
    "deneme_sns_scatter.py",
) + next_link("15-further-resources.html", "4.15 Daha Fazla Matplotlib Kaynağı")

if __name__ == "__main__":
    path = write_chapter("14-visualization-with-seaborn", body)
    print("wrote", path)
