#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_mpl_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_matplotlib_chapter import write_chapter

NB = "04.11-Settings-and-Stylesheets.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>4.11 Matplotlib Özelleştirme: Yapılandırma ve Stil Sayfaları</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html" target="_blank" rel="noopener">Customizing Matplotlib: Configurations and Stylesheets</a></em></p>

    <p>Önceki bölümlerde ele alınan birçok konu grafik öğelerinin stilini tek tek ayarlamayı içerir; Matplotlib ayrıca bir grafiğin genel stilini toplu olarak ayarlama mekanizmaları da sunar. Bu bölümde Matplotlib'ın çalışma zamanı yapılandırma (<em>rc</em>) seçeneklerinden bazılarını inceleyecek ve güzel varsayılan yapılandırma kümeleri içeren <em>stil sayfaları</em> (<em>stylesheets</em>) özelliğine bakacağız.</p>

    <h2 id="elle-ozellestirme">Elle Grafik Özelleştirme</h2>

    <p>Kitabın bu kısmında tek tek grafik ayarlarını değiştirerek varsayılandan biraz daha hoş bir sonuca ulaşmanın mümkün olduğunu gördünüz. Bu özelleştirmeler her grafik için ayrı ayrı da yapılabilir. Örneğin aşağıdaki şekilde oldukça sade bir varsayılan histogram:</p>
""" + c(3, "import_mpl_np.py") + c(4, "default_hist.py") + """
    <p>Bunu elle ayarlayarak çok daha görsel açıdan hoş bir grafik elde edebiliriz (aşağıdaki şekil):</p>
""" + c(6, "custom_hist.py") + """
    <p>Bu daha iyi görünüyor; görünümü R dilindeki <code>ggplot</code> görselleştirme paketinden esinlenmiş olabilirsiniz. Ancak bu çok emek istedi! Her grafik oluşturduğumuzda tüm bu ince ayarları yapmak istemeyiz. Neyse ki bu varsayılanları bir kez ayarlayıp tüm grafikler için geçerli kılmanın bir yolu var.</p>

    <h2 id="rcparams">Varsayılanları Değiştirme: rcParams</h2>

    <p>Matplotlib her yüklendiğinde oluşturacağınız her grafik öğesinin varsayılan stillerini içeren bir çalışma zamanı yapılandırması tanımlar. Bu yapılandırma <code>plt.rc</code> kolaylık rutiniyle istediğiniz zaman ayarlanabilir. rc parametrelerini, varsayılan grafiğimizin önce yaptığımıza benzer görünmesini sağlayacak şekilde nasıl değiştirebileceğimizi görelim.</p>

    <p>Bu ayarlardan bazılarını değiştirmek için <code>plt.rc</code> kullanabiliriz:</p>
""" + c(9, "rc_params.py") + """
    <p>Bu ayarlar tanımlandıktan sonra bir grafik oluşturup ayarlarımızı görebiliriz (aşağıdaki şekil):</p>
""" + c(11, "hist_rc.py") + """
    <p>Bu rc parametreleriyle basit çizgi grafiklerinin nasıl göründüğüne bakalım (aşağıdaki şekil):</p>
""" + c(13, "lines_rc.py") + """
    <p>Ekranda (basılı değil) izlenen grafikler için bunu varsayılan stilden estetik açıdan çok daha hoş buluyorum. Estetik zevkimize katılmıyorsanız iyi haber: rc parametrelerini kendi zevkinize göre ayarlayabilirsiniz! İsteğe bağlı olarak bu ayarlar bir <em>.matplotlibrc</em> dosyasına kaydedilebilir; ayrıntılar için <a href="https://matplotlib.org/stable/tutorials/introductory/customizing.html" target="_blank" rel="noopener">Matplotlib dokümantasyonu</a>.</p>

    <h2 id="stylesheets">Stil Sayfaları</h2>

    <p>Genel grafik stillerini ayarlamanın daha yeni bir mekanizması Matplotlib'ın <code>style</code> modülü üzerindendir; bir dizi varsayılan stil sayfası ve kendi stillerinizi oluşturup paketleme olanağı içerir. Bu stil sayfaları daha önce bahsedilen <em>.matplotlibrc</em> dosyalarına benzer biçimlendirilir; ancak <em>.mplstyle</em> uzantısıyla adlandırılmalıdır.</p>

    <p>Kendi stilinizi oluşturmasanız bile aradığınızı yerleşik stil sayfalarında bulabilirsiniz. <code>plt.style.available</code> kullanılabilir stillerin listesini içerir — kısalık için burada yalnızca ilk beşini listeliyorum:</p>
""" + c(16, "style_available.py") + """
    <p>Bir stil sayfasına geçmenin standart yolu <code>style.use</code> çağırmaktır:</p>

    <div class="code-block" data-lang="python" data-filename="style_use.py">
      <pre><code>plt.style.use('stylename')</code></pre>
    </div>

    <p>Ancak bunun Python oturumunun geri kalanı için stili değiştireceğini unutmayın! Geçici olarak stil ayarlamak için stil bağlam yöneticisini kullanabilirsiniz:</p>

    <div class="code-block" data-lang="python" data-filename="style_context.py">
      <pre><code>with plt.style.context('stylename'):
    make_a_plot()</code></pre>
    </div>

    <p>Bu stilleri göstermek için iki temel grafik türü üreten bir fonksiyon tanımlayalım:</p>
""" + c(19, "hist_and_lines.py") + """
    <p>Bunu çeşitli yerleşik stillerle grafiklerin nasıl göründüğünü keşfetmek için kullanacağız.</p>

    <h3 id="default-style">Varsayılan Stil</h3>

    <p>Matplotlib'ın <code>default</code> stili 2.0 sürümünde güncellendi; önce buna bakalım (aşağıdaki şekil):</p>
""" + c(22, "style_default.py") + """
    <h3 id="fivethirtyeight-style">FiveThirtyEight Stili</h3>

    <p><code>fivethirtyeight</code> stili popüler <a href="https://fivethirtyeight.com" target="_blank" rel="noopener">FiveThirtyEight web sitesindeki</a> grafikleri taklit eder. Aşağıdaki şekilde görüldüğü gibi kalın renkler, kalın çizgiler ve şeffaf eksenlerle belirgindir:</p>
""" + c(24, "style_fivethirtyeight.py") + """
    <h3 id="ggplot-style">ggplot Stili</h3>

    <p>R dilindeki <code>ggplot</code> paketi veri bilimciler arasında popüler bir görselleştirme aracıdır. Matplotlib'ın <code>ggplot</code> stili o paketin varsayılan stillerini taklit eder (aşağıdaki şekil):</p>
""" + c(26, "style_ggplot.py") + """
    <h3 id="bmh-style">Bayesian Methods for Hackers Stili</h3>

    <p>Cameron Davidson-Pilon tarafından yazılan <a href="http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/" target="_blank" rel="noopener"><em>Probabilistic Programming and Bayesian Methods for Hackers</em></a> adlı kısa çevrimiçi kitap, Matplotlib ile oluşturulmuş şekiller içerir ve kitap boyunca tutarlı ve görsel açıdan hoş bir stil için güzel bir rc parametre seti kullanır. Bu stil <code>bmh</code> stil sayfasında yeniden üretilmiştir (aşağıdaki şekil):</p>
""" + c(28, "style_bmh.py") + """
    <h3 id="dark-background">Koyu Arka Plan Stili</h3>

    <p>Sunumlarda kullanılan şekiller için açık yerine koyu arka plan sık işe yarar. <code>dark_background</code> stili bunu sağlar (aşağıdaki şekil):</p>
""" + c(30, "style_dark.py") + """
    <h3 id="grayscale-style">Gri Ton Stili</h3>

    <p>Bazen renkli şekil kabul etmeyen bir basılı yayın için grafik hazırlıyor olabilirsiniz. Bu durumda <code>grayscale</code> stili (aşağıdaki şekil) yararlı olabilir:</p>
""" + c(32, "style_grayscale.py") + """
    <h3 id="seaborn-style">Seaborn Stili</h3>

    <p>Matplotlib, Seaborn kütüphanesinden esinlenen birkaç stil sayfasına da sahiptir (<a href="14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a> bölümünde daha ayrıntılı). Bu ayarları çok beğeniyorum ve kendi veri keşiflerimde varsayılan olarak kullanıyorum (aşağıdaki şekil):</p>
""" + c(34, "style_seaborn.py") + """
    <p>Yerleşik seçenekleri keşfetmek için biraz zaman ayırın ve size hitap eden birini bulun! Kitap boyunca grafik oluştururken genelde bu stil kurallarından bir veya birkaçını kullanacağım.</p>
""" + addon(
    "rcParams vs stil sayfası",
    "<p><code>plt.rc(...)</code> oturum boyunca kalıcı varsayılanları değiştirir; "
    "<code>plt.style.use(...)</code> veya <code>with plt.style.context(...)</code> önceden paketlenmiş rc ayar kümesini yükler. "
    "Keşif aşamasında stil sayfası, yayın öncesi ince ayar için tek tek rc değişiklikleri pratik bir kombinasyondur.</p>",
) + try_it(
    "Stil karşılaştırması",
    "Aynı rastgele veriyi iki farklı stil sayfasıyla çizin:",
    """import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
x = rng.normal(size=100)

for style in ['default', 'seaborn-v0_8-whitegrid']:
    with plt.style.context(style):
        plt.figure()
        plt.hist(x, bins=20)
        plt.title(style)
plt.show()""",
    "deneme_stil_karsilastirma.py",
) + next_link("12-three-dimensional-plotting.html", "4.12 Üç Boyutlu Çizim")

if __name__ == "__main__":
    path = write_chapter("11-settings-and-stylesheets", body)
    print("wrote", path)
