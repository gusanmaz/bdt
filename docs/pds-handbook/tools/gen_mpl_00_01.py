#!/usr/bin/env python3
"""Generate Matplotlib chapters 00 and 01 (TR HTML bodies)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from _gen_mpl_helpers import addon, code_block, next_link, try_it

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
SRC = TOOLS / "source" / "notebooks"


def count_cells(nb_name: str) -> int:
    nb = json.loads((SRC / nb_name).read_text(encoding="utf-8"))
    return len(nb["cells"])


def write_slug(slug: str, body: str) -> Path:
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "write_matplotlib_chapter.py"), slug],
        input=body,
        text=True,
        capture_output=True,
        cwd=TOOLS,
    )
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        proc.check_returncode()
    rel = proc.stdout.strip().split()[-1]
    return ROOT / rel


def body_00() -> str:
    return f"""<h1>Matplotlib ile Görselleştirme</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html" target="_blank" rel="noopener">04.00 Introduction to Matplotlib</a></em></p>

    <p>Şimdi Python'da görselleştirme için Matplotlib paketine ayrıntılı bakacağız. Matplotlib, NumPy dizileri üzerine kurulu, daha geniş SciPy yığınıyla uyumlu çalışacak şekilde tasarlanmış çok platformlu bir veri görselleştirme kütüphanesidir. John Hunter tarafından 2002'de, başlangıçta IPython'dan MATLAB tarzı etkileşimli çizim yapabilmek için <code>gnuplot</code> ile IPython komut satırından grafik üretmeye yarayan bir yama olarak düşünülmüştü. IPython'un yaratıcısı Fernando Perez o sırada doktorasını bitirmeye çalışıyordu ve John'a yamayı incelemek için aylarca vakti olmayacağını söyledi. John bunu kendi yoluna çıkmak için bir işaret saydı; Matplotlib paketi doğdu ve 0.1 sürümü 2003'te yayımlandı. Hubble Uzay Teleskobu'nun arkasındaki Space Telescope Science Institute tarafından tercih edilen çizim paketi olarak benimsenmesi erken bir ivme kazandırdı; kurum Matplotlib gelişimini mali olarak destekledi ve yeteneklerini büyük ölçüde genişletti.</p>

    <p>Matplotlib'in en önemli özelliklerinden biri birçok işletim sistemi ve grafik arka ucü (backend) ile sorunsuz çalabilmesidir. Matplotlib onlarca backend ve çıktı türünü destekler; yani hangi işletim sistemini kullandığınızdan veya hangi çıktı biçimini istediğinizden bağımsız olarak çalışacağına güvenebilirsiniz. Bu herkese-her şeye yaklaşım, Matplotlib'in büyük güçlerinden biridir; geniş bir kullanıcı tabanı, aktif geliştirici topluluğu ve bilimsel Python dünyasında güçlü araçlar ile yaygınlık getirmiştir.</p>

    <p>Son yıllarda Matplotlib'in arayüzü ve stili yaşını göstermeye başladı. R dilindeki <code>ggplot</code> ve <code>ggvis</code> ile D3js ve HTML5 canvas tabanlı web görselleştirme araçları, Matplotlib'i bazen hantal ve eski moda hissettirebilir. Yine de Matplotlib'i iyi test edilmiş, platformlar arası bir grafik motoru olarak görmezden gelemez. Güncel sürümlerde yeni genel çizim stilleri ayarlamak nispeten kolaydır (<a href="11-settings-and-stylesheets.html">Matplotlib Özelleştirme: Yapılandırma ve Stil Sayfaları</a>); Seaborn (<a href="14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a>), <a href="http://yhat.github.io/ggpy/" target="_blank" rel="noopener"><code>ggpy</code></a>, <a href="http://holoviews.org/" target="_blank" rel="noopener">HoloViews</a> ve hatta Pandas'ın kendisi gibi paketler, Matplotlib'in güçlü iç yapısı üzerine daha temiz API'ler kurar. Bu sarmalayıcılarla bile son grafik çıktısını ince ayar için Matplotlib sözdizimine dalmak sıkça yararlıdır. Topluluk zamanla doğrudan Matplotlib API'sinden uzaklaşsa da Matplotlib'in veri görselleştirme yığınının vazgeçilmez parçası olarak kalacağına inanıyorum.</p>

    <h2 id="genel-matplotlib-ipuclari">Genel Matplotlib İpuçları</h2>

    <p>Matplotlib ile görselleştirme ayrıntılarına girmeden önce paketi kullanırken işinize yarayacak birkaç noktayı bilmek iyi olur.</p>

    <h3 id="matplotlib-ice-aktarma">Matplotlib'i İçe Aktarma</h3>

    <p>NumPy için <code>np</code>, Pandas için <code>pd</code> kısaltmalarını kullandığımız gibi Matplotlib içe aktarmalarında da standart kısaltmalar vardır:</p>

{code_block("""import matplotlib as mpl
import matplotlib.pyplot as plt""", "matplotlib_import.py")}

    <p>Kitabın bu bölümünde en çok <code>plt</code> arayüzünü kullanacağız.</p>

{addon("plt ve pyplot", """<p><code>import matplotlib.pyplot as plt</code> pratikte <code>matplotlib.pyplot</code> modülünün takma adıdır; çoğu örnek <code>plt.plot</code>, <code>plt.xlabel</code> gibi <em>pyplot</em> (MATLAB tarzı) arayüzünü kullanır. Daha ayrıntılı kontrol için <code>fig, ax = plt.subplots()</code> ile nesne yönelimli <code>ax.plot</code> yoluna geçilir — ikisi de aynı Matplotlib motorunu çalıştırır.</p>""")}

    <h3 id="stil-ayarlama">Stil Ayarlama</h3>

    <p>Şekillerimiz için uygun estetik stilleri seçmek üzere <code>plt.style</code> yönergesini kullanacağız. Burada klasik Matplotlib görünümünü sağlayan <code>classic</code> stilini ayarlıyoruz:</p>

{code_block("plt.style.use('classic')", "matplotlib_classic_style.py")}

{addon("classic stili", """<p><code>plt.style.use('classic')</code> kitaptaki örneklerin orijinal görünümüne yakın kalır. Yeni projelerde <code>seaborn-v0_8</code> veya <code>ggplot</code> gibi stiller de yaygındır. Stil sayfalarının tam listesi için <a href="11-settings-and-stylesheets.html">4.11 Ayarlar ve Stil Sayfaları</a> bölümüne bakın.</p>""")}

    <p>Bu bölüm boyunca gerektiğinde stili değiştireceğiz.</p>

    <h3 id="goster-yoksa-gosterme">Göster ya da Gösterme? Grafiklerinizi Nasıl Görüntülersiniz</h3>

    <p>Göremediğiniz bir görselleştirme pek işe yaramaz; Matplotlib grafiklerini nasıl gördüğünüz bağlama bağlıdır. Matplotlib'i betikten, IPython terminalinden veya Jupyter not defterinden kullanmak kabaca üç ayrı senaryodur.</p>

    <h4 id="betikten-cizim">Betikten Çizim</h4>

    <p>Matplotlib'i bir betikten kullanıyorsanız <code>plt.show</code> işinize yarar. <code>plt.show</code> bir olay döngüsü başlatır, etkin tüm <code>Figure</code> nesnelerini bulur ve şekillerinizi gösteren etkileşimli pencereler açar.</p>

    <p>Örneğin <em>myplot.py</em> adlı bir dosyanız olabilir:</p>

{code_block("""# file: myplot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()""", "myplot.py")}

    <p>Bu betiği komut satırından çalıştırdığınızda şeklinizin göründüğü bir pencere açılır:</p>

{code_block("$ python myplot.py", "terminal_myplot.sh", lang="text", readonly=True)}

    <p><code>plt.show</code> sisteminizin etkileşimli grafik arka ucüyla konuştuğu için kurulumdan kuruluma davranış değişebilir; Matplotlib bu ayrıntıları mümkün olduğunca gizlemeye çalışır.</p>

    <p>Dikkat: <code>plt.show</code> bir Python oturumunda <em>yalnızca bir kez</em> kullanılmalıdır; çoğu zaman betiğin en sonunda görülür. Birden fazla <code>show</code> çağrısı arka uca bağlı öngörülemeyen davranışlara yol açabilir.</p>

    <h4 id="ipython-kabugundan-cizim">IPython Kabuğundan Çizim</h4>

    <p>Matplotlib, IPython kabuğu içinde de sorunsuz çalışır (<a href="../01-ipython/00-introduction.html">IPython: Normal Python'un Ötesinde</a>). Matplotlib modunu etkinleştirmek için <code>ipython</code> başlattıktan sonra <code>%matplotlib</code> sihirli komutunu kullanabilirsiniz:</p>

{code_block("""In [1]: %matplotlib
Using matplotlib backend: TkAgg

In [2]: import matplotlib.pyplot as plt""", "ipython_matplotlib_magic.txt", lang="text", readonly=True)}

    <p>Bu noktadan sonra her <code>plt</code> çizim komutu bir şekil penceresi açar; grafik güncellemek için ek komutlar çalıştırılabilir. Zaten çizilmiş çizgilerin özelliklerini değiştirmek gibi bazı işlemler otomatik yeniden çizilmez; zorlamak için <code>plt.draw</code> kullanın. IPython Matplotlib modunda <code>plt.show</code> gerekli değildir.</p>

    <h4 id="jupyter-not-defterinden-cizim">Jupyter Not Defterinden Çizim</h4>

    <p>Jupyter not defteri, anlatı, kod, grafik ve HTML öğelerini tek çalıştırılabilir belgede birleştiren tarayıcı tabanlı bir araçtır (<a href="../01-ipython/00-introduction.html">IPython: Normal Python'un Ötesinde</a>).</p>

    <p>Not defteri içinde etkileşimli çizim <code>%matplotlib</code> ile yapılır; IPython kabuğuna benzer. Grafikleri doğrudan not defterine gömmek için iki seçenek vardır:</p>

    <ul>
      <li><code>%matplotlib inline</code> — grafiklerin <em>statik</em> gömülü görüntüleri.</li>
      <li><code>%matplotlib notebook</code> — not defteri içinde <em>etkileşimli</em> grafikler.</li>
    </ul>

    <p>Bu kitapta çoğunlukla statik gömülü şekiller kullanacağız:</p>

{code_block("%matplotlib inline", "jupyter_inline_magic.py", readonly=True)}

{code_block("""import numpy as np
x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');""", "jupyter_basic_plot.py")}

{addon("Web sayfası ve Pyodide", """<p>Bu el kitabının HTML sayfalarında kod Pyodide ile tarayıcıda çalıştırılabilir; ancak <strong>Matplotlib şekilleri her ortamda güvenilir biçimde görüntülenmeyebilir</strong> (özellikle <code>%matplotlib inline</code> ve dosyaya kaydetme örnekleri). Grafik çıktısını görmek ve kaydetmek için orijinal <a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank" rel="noopener">Jupyter <code>.ipynb</code></a> dosyalarını yerel Jupyter Lab/Notebook'ta açmanızı öneririz.</p>""")}

    <h3 id="sekilleri-dosyaya-kaydetme">Şekilleri Dosyaya Kaydetme</h3>

    <p>Matplotlib'in güzel bir özelliği şekilleri birçok biçimde kaydedebilmesidir. <code>savefig</code> komutuyla örneğin önceki şekli PNG olarak kaydedebiliriz:</p>

{code_block("fig.savefig('my_figure.png')", "savefig_png.py")}

    <p>Çalışma dizininde <em>my_figure.png</em> oluşur:</p>

{code_block("!ls -lh my_figure.png", "shell_ls_figure.sh", lang="text", readonly=True)}

    <p>İçeriği doğrulamak için IPython <code>Image</code> nesnesi kullanılabilir:</p>

{code_block("""from IPython.display import Image
Image('my_figure.png')""", "display_saved_figure.py")}

    <p><code>savefig</code> içinde dosya biçimi, dosya adının uzantısından çıkarılır. Kurulu arka uçlara bağlı olarak birçok biçim desteklenir. Desteklenen türlerin listesi:</p>

{code_block("fig.canvas.get_supported_filetypes()", "supported_filetypes.py")}

    <p>Şekli kaydederken daha önce bahsedilen <code>plt.show</code> veya benzeri komutlar gerekli değildir.</p>

    <h3 id="iki-arayuz-teklik-fiyatina">Tek Paraya İki Arayüz</h3>

    <p>Matplotlib'in kafa karıştırıcı olabilen özelliği çift arayüzdür: kullanışlı MATLAB tarzı durum tabanlı arayüz ve daha güçlü nesne yönelimli arayüz. Kısaca farkları özetleyelim.</p>

    <h4 id="matlab-tarzi-arayuz">MATLAB Tarzı Arayüz</h4>

    <p>Matplotlib başlangıçta MATLAB kullanıcıları için bir Python alternatifi olarak düşünüldü; sözdiziminin önemli kısmı bunu yansıtır. MATLAB tarzı araçlar <code>pyplot</code> (<code>plt</code>) arayüzündedir:</p>

{code_block("""plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));""", "matlab_style_subplots.py")}

    <p>Bu arayüz <em>durum tabanlıdır</em>: «şu anki» şekil ve eksenleri izler; tüm <code>plt</code> komutları bunlara uygulanır. <code>plt.gcf</code> (get current figure) ve <code>plt.gca</code> (get current axes) ile referans alınabilir.</p>

    <p>Basit grafiklerde hızlı ve pratiktir; ancak ikinci panel oluşturulduktan sonra birinciye bir şey eklemek gibi durumlarda MATLAB tarzı arayüz hantal kalabilir. Daha iyi bir yol vardır.</p>

    <h4 id="nesne-yonelimli-arayuz">Nesne Yönelimli Arayüz</h4>

    <p>Daha karmaşık durumlar ve şekil üzerinde daha fazla kontrol için nesne yönelimli arayüz kullanılır. «Aktif» şekil/eksen yerine çizim işlevleri açık <code>Figure</code> ve <code>Axes</code> nesnelerinin <em>yöntemleridir</em>:</p>

{code_block("""# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)

# Call plot() method on the appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x));""", "oo_style_subplots.py")}

    <p>Daha karmaşık grafiklerde nesne yönelimli yaklaşım zorunlu hale gelebilir. Sonraki bölümlerde uygun olanı kullanacağız; çoğu zaman fark <code>plt.plot</code> ile <code>ax.plot</code> arasındaki kadar küçüktür.</p>

{try_it(
    "Matplotlib'i içe aktarın ve sürümü kontrol edin",
    "Aşağıdaki kodu çalıştırın; ardından basit bir çizgi çizmeyi deneyin (Jupyter'de grafik görünür, tarayıcıda Pyodide ile görünmeyebilir):",
    """import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print("Matplotlib sürümü:", matplotlib.__version__)
plt.style.use('classic')
x = np.linspace(0, 10, 50)
plt.plot(x, np.sin(x))
plt.title("Hızlı deneme")""",
    "matplotlib_hizli_deneme.py",
)}

{next_link("01-simple-line-plots.html", "4.1 Basit Çizgi Grafikleri")}
"""


def body_01() -> str:
    return f"""<h1>Basit Çizgi Grafikleri</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html" target="_blank" rel="noopener">04.01 Simple Line Plots</a></em></p>

    <p>Belki de en basit grafik türü tek bir fonksiyonun $y = f(x)$ görselleştirmesidir. Burada böyle basit bir grafiğe ilk bakışı atacağız. Sonraki bölümlerde olduğu gibi önce not defterini çizim için hazırlayıp paketleri içe aktaracağız:</p>

{code_block("""%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np""", "line_plots_setup.py", readonly=True)}

{addon("seaborn-whitegrid stili", """<p><code>seaborn-whitegrid</code> eksenlerde ızgara gösterir; çizgi grafiklerini okumayı kolaylaştırır. Güncel Matplotlib sürümlerinde ad <code>seaborn-v0_8-whitegrid</code> olabilir; uyarı alırsanız <code>plt.style.available</code> ile mevcut stilleri listeleyin.</p>""")}

    <p>Tüm Matplotlib grafiklerinde bir <em>figure</em> ve <em>axes</em> oluşturarak başlarız. En basit haliyle:</p>

{code_block("""fig = plt.figure()
ax = plt.axes()""", "figure_and_axes.py")}

    <p>Matplotlib'de <em>figure</em> (<code>plt.Figure</code> örneği), eksenleri, grafikleri, metni ve etiketleri içeren tek bir kaptır. <em>axes</em> (<code>plt.Axes</code> örneği) yukarıda gördüğünüz sınırlayıcı kutu, işaretler, ızgara ve etiketlerdir; sonunda çizim öğeleri buraya yerleşir. Kitapta <code>fig</code> genelde şekil örneği, <code>ax</code> tek veya birden fazla eksen örneği için kullanılır.</p>

    <p>Eksen oluşturduktan sonra <code>ax.plot</code> ile veri çizeriz. Basit bir sinüs eğrisi:</p>

{code_block("""fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));""", "sinus_plot_oo.py")}

    <p>Son satırdaki noktalı virgül kasıtlıdır: çıktıda grafiğin metin temsilini bastırır.</p>

    <p>Alternatif olarak PyLab arayüzünü kullanıp şekil ve eksenin arka planda oluşturulmasına izin verebilirsiniz (<a href="00-introduction.html#iki-arayuz-teklik-fiyatina">Tek Paraya İki Arayüz</a>); sonuç aynıdır:</p>

{code_block("plt.plot(x, np.sin(x));", "sinus_plot_plt.py")}

    <p>Tek bir şekilde birden fazla çizgi için <code>plot</code> fonksiyonunu birden fazla kez çağırın:</p>

{code_block("""plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));""", "sin_and_cos.py")}

    <p>Matplotlib'de basit fonksiyon çizmek bu kadar! Şimdi eksen ve çizgi görünümünü nasıl kontrol edeceğimize geçiyoruz.</p>

    <h2 id="cizgi-renk-ve-stil">Grafiği Ayarlama: Çizgi Renkleri ve Stilleri</h2>

    <p>İlk ayar genelde çizgi rengi ve stilidir. <code>plt.plot</code> bunları belirten ek argümanlar alır. Renk için <code>color</code> anahtar sözcüğü kullanılır:</p>

{code_block("""plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # hex code (RRGGBB, 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # HTML color names supported""", "line_colors.py")}

    <p>Renk belirtilmezse Matplotlib birden fazla çizgi için varsayılan renkleri döngüsel uygular.</p>

    <p>Çizgi stili <code>linestyle</code> ile ayarlanır:</p>

{code_block("""plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted""", "line_styles.py")}

    <p><code>linestyle</code> ve <code>color</code> kodlarını tek bir konumsal argümanda birleştirebilirsiniz:</p>

{code_block("""plt.plot(x, x + 0, '-g')   # solid green
plt.plot(x, x + 1, '--c')  # dashed cyan
plt.plot(x, x + 2, '-.k')  # dashdot black
plt.plot(x, x + 3, ':r');  # dotted red""", "line_style_color_short.py")}

    <p>Bu tek karakterli renk kodları RGB ve CMYK kısaltmalarını yansıtır.</p>

    <p>Görünümü ince ayar için <code>plt.plot</code> docstring'inde başka anahtar sözcükler vardır (<a href="../01-ipython/01-help-and-documentation.html">IPython'da Yardım ve Dokümantasyon</a>).</p>

    <h2 id="eksen-sinirlari">Grafiği Ayarlama: Eksen Sınırları</h2>

    <p>Matplotlib varsayılan eksen sınırlarını iyi seçer; bazen daha ince kontrol istersiniz. En temel yol <code>plt.xlim</code> ve <code>plt.ylim</code>:</p>

{code_block("""plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);""", "axis_limits.py")}

    <p>Bir ekseni ters göstermek için argüman sırasını ters çevirin:</p>

{code_block("""plt.plot(x, np.sin(x))

plt.xlim(10, 0)
plt.ylim(1.2, -1.2);""", "reversed_axis_limits.py")}

    <p><code>plt.axis</code> (<em>axes</em> ile <em>e</em> ve <em>axis</em> ile <em>i</em> karışmasın) daha niteliksel sınır ayarı sağlar; örneğin içeriğe sıkı sınır:</p>

{code_block("""plt.plot(x, np.sin(x))
plt.axis('tight');""", "axis_tight.py")}

    <p>Veya <code>x</code>'te bir birimin <code>y</code>'deki bir birime görsel olarak eşit olması:</p>

{code_block("""plt.plot(x, np.sin(x))
plt.axis('equal');""", "axis_equal.py")}

    <p>Diğer seçenekler: <code>'on'</code>, <code>'off'</code>, <code>'square'</code>, <code>'image'</code> ve daha fazlası — <code>plt.axis</code> docstring'ine bakın.</p>

    <h2 id="grafik-etiketleme">Grafikleri Etiketleme</h2>

    <p>Bu bölümün sonunda kısaca başlık, eksen etiketleri ve basit lejantlara bakıyoruz:</p>

{code_block("""plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");""", "plot_labels.py")}

    <p>Konum, boyut ve stil docstring'teki isteğe bağlı argümanlarla ayarlanır.</p>

    <p>Tek eksende birden fazla çizgi varken her çizgi için <code>plot</code> içinde <code>label</code> verip <code>plt.legend</code> kullanmak pratiktir:</p>

{code_block("""plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend();""", "plot_legend.py")}

    <p><code>plt.legend</code> çizgi stili ve rengi etiketle eşleştirir. Gelişmiş lejant seçenekleri <a href="06-customizing-legends.html">4.6 Lejant Özelleştirme</a> bölümünde.</p>

    <h2 id="matplotlib-tuzaklari">Matplotlib Tuzakları</h2>

    <p>Çoğu <code>plt</code> işlevi <code>ax</code> yöntemine karşılık gelir (<code>plt.plot</code> → <code>ax.plot</code>); sınır, etiket ve başlık komutları biraz farklıdır:</p>

    <ul>
      <li><code>plt.xlabel</code> → <code>ax.set_xlabel</code></li>
      <li><code>plt.ylabel</code> → <code>ax.set_ylabel</code></li>
      <li><code>plt.xlim</code> → <code>ax.set_xlim</code></li>
      <li><code>plt.ylim</code> → <code>ax.set_ylim</code></li>
      <li><code>plt.title</code> → <code>ax.set_title</code></li>
    </ul>

    <p>Nesne yönelimli arayüzde bunları tek tek çağırmak yerine <code>ax.set</code> ile toplu ayar yapılabilir:</p>

{code_block("""ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot');""", "ax_set_properties.py")}

{addon("plt.plot ile ax.plot", """<p>Aynı veriyi hem <code>plt.plot(x, y)</code> hem <code>ax.plot(x, y)</code> ile çizebilirsiniz; ikinci yol hangi eksene çizildiğini açıkça belirler. Karmaşık düzenlerde <code>fig, ax = plt.subplots()</code> tercih edin.</p>""")}

{try_it(
    "İki fonksiyonu aynı grafikte çizin",
    "Sinüs ve kosinüsü farklı renk/stille çizin; eksen etiketleri ve lejant ekleyin:",
    """import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')
x = np.linspace(0, 10, 200)
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), '--b', label='cos(x)')
plt.xlabel('x')
plt.ylabel('değer')
plt.title('Sinüs ve kosinüs')
plt.legend()
plt.axis('equal')""",
    "iki_cizgi_deneme.py",
)}

{next_link("02-simple-scatter-plots.html", "4.2 Basit Saçılım Grafikleri")}
"""


def verify_counts() -> None:
    n0 = count_cells("04.00-Introduction-To-Matplotlib.ipynb")
    n1 = count_cells("04.01-Simple-Line-Plots.ipynb")
    # Expected: all markdown headings + all code cells represented in HTML
    assert n0 == 32, n0
    assert n1 == 37, n1
    print(f"Source notebooks: 00={n0} cells, 01={n1} cells")


def main() -> None:
    verify_counts()
    p0 = write_slug("00-introduction", body_00())
    p1 = write_slug("01-simple-line-plots", body_01())
    print("wrote", p0.relative_to(ROOT))
    print("wrote", p1.relative_to(ROOT))
    print("Verified cell counts: 00-introduction=32, 01-simple-line-plots=37")


if __name__ == "__main__":
    main()
