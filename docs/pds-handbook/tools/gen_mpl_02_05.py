#!/usr/bin/env python3
"""Generate Matplotlib chapters 02–05 (TR HTML bodies)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from _gen_mpl_helpers import addon, code_block, next_link, try_it
from nb_html_utils import h1, h2, h3, load_notebook, orig_line

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent


def build_body(
    notebook: str,
    tr_md: dict[int, str],
    code_names: dict[int, str],
    readonly_cells: set[int] | None = None,
    inserts: dict[int, str] | None = None,
) -> str:
    cells = load_notebook(notebook)
    readonly_cells = readonly_cells or set()
    inserts = inserts or {}
    parts: list[str] = []
    for i, cell in enumerate(cells):
        if cell["cell_type"] == "markdown":
            if i in tr_md:
                parts.append(tr_md[i])
        else:
            src = "".join(cell["source"])
            parts.append(
                code_block(
                    src,
                    code_names.get(i, f"cell_{i:02d}.py"),
                    readonly=(i in readonly_cells),
                )
            )
        if i in inserts:
            parts.append(inserts[i])
    return "\n\n".join(parts)


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


def body_02() -> str:
    en = "https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html"
    tr_md = {
        0: h1("Basit Saçılım Grafikleri"),
        1: """    <p>Yaygın kullanılan bir grafik türü de basit saçılım grafiğidir; çizgi grafiğinin yakın akrabasıdır.
    Burada noktalar çizgi parçalarıyla birleştirilmez; her nokta nokta, daire veya başka bir şekille ayrı gösterilir.
    Önce not defterini çizim için hazırlayıp kullanacağımız paketleri içe aktaracağız:</p>""",
        3: h2("plt.plot ile saçılım grafikleri", "plt-plot-ile-sacilim")
        + """    <p>Önceki bölümde çizgi grafikleri için <code>plt.plot</code>/<code>ax.plot</code> kullanmıştık.
    Aynı işlev saçılım grafikleri de üretebilir (aşağıdaki şekle bakın):</p>""",
        5: """    <p>Fonksiyon çağrısındaki üçüncü argüman, çizimde kullanılan sembol türünü temsil eden bir karakterdir.
    Çizgi stilini <code>'-'</code> veya <code>'--'</code> ile belirttiğiniz gibi, işaretçi stilinin de kısa dize kodları vardır.
    Kullanılabilir sembollerin tam listesi <code>plt.plot</code> dokümantasyonunda veya Matplotlib'in
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html" target="_blank" rel="noopener">çevrimiçi dokümantasyonunda</a> görülebilir.
    Çoğu sezgiseldir; daha yaygın olanların bir kısmı burada gösterilmiştir (aşağıdaki şekle bakın):</p>""",
        7: """    <p>Daha fazla seçenek için bu karakter kodları, noktaları birleştiren çizgiyle birlikte kullanılabilir (aşağıdaki şekle bakın):</p>""",
        9: """    <p><code>plt.plot</code>'a verilen ek anahtar sözcük argümanları çizgi ve işaretçilerin geniş özellik aralığını belirler (aşağıdaki şekle bakın):</p>""",
        11: """    <p>Bu tür seçenekler <code>plt.plot</code>'u Matplotlib'de iki boyutlu grafikler için temel araç yapar.
    Kullanılabilir seçeneklerin tam açıklaması için
    <a href="https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.plot.html" target="_blank" rel="noopener"><code>plt.plot</code> dokümantasyonuna</a> bakın.</p>""",
        12: h2("plt.scatter ile saçılım grafikleri", "plt-scatter-ile-sacilim")
        + """    <p>Saçılım grafiği oluşturmanın ikinci, daha güçlü yolu <code>plt.scatter</code> işlevidir;
    <code>plt.plot</code>'a çok benzer kullanılır (aşağıdaki şekle bakın):</p>""",
        14: """    <p><code>plt.scatter</code>'ın <code>plt.plot</code>'tan temel farkı, her noktanın özelliklerinin
    (boyut, yüz rengi, kenar rengi vb.) ayrı ayrı kontrol edilebilmesi veya veriye eşlenebilmesidir.</p>
    <p>Çok renkli ve boyutlu rastgele bir saçılım grafiği oluşturalım.
    Üst üste binen sonuçları daha iyi görmek için <code>alpha</code> anahtar sözcüğüyle saydamlığı ayarlayacağız (aşağıdaki şekle bakın):</p>""",
        16: """    <p><code>color</code> argümanının otomatik olarak bir renk ölçeğine eşlendiğine dikkat edin
    (burada <code>colorbar</code> komutuyla gösterilir); <code>s</code> (size) argümanı piksel cinsindendir.
    Böylece renk ve nokta boyutu görselleştirmede bilgi taşıyabilir; çok boyutlu veriyi görselleştirmek için kullanılır.</p>
    <p>Örneğin Scikit-Learn'deki Iris veri setini kullanabiliriz: her örnek, taç yaprak ve çanak yaprak boyutları dikkatle ölçülmüş üç çiçek türünden biridir (aşağıdaki şekle bakın):</p>""",
        18: """    <p>Bu grafiğin tam renkli sürümü kitabın <a href="http://github.com/jakevdp/PythonDataScienceHandbook" target="_blank" rel="noopener">çevrimiçi sürümünde</a> mevcuttur.</p>
    <p>Bu saçılım grafiği verinin dört farklı boyutunu aynı anda keşfetmemizi sağladı:
    her noktanın (<em>x</em>, <em>y</em>) konumu çanak yaprak uzunluğu ve genişliğine karşılık gelir;
    nokta boyutu taç yaprak genişliğiyle, renk ise çiçek türüyle ilişkilidir.
    Bu tür çok renkli ve çok özellikli saçılım grafikleri hem keşif hem sunum için yararlıdır.</p>""",
        19: h2("plot ve scatter: verimlilik notu", "plot-vs-scatter-verimlilik")
        + """    <p><code>plt.plot</code> ve <code>plt.scatter</code>'daki farklı özellikler dışında neden birini diğerine tercih edersiniz?
    Küçük veri kümelerinde pek fark etmez; ancak birkaç bin noktadan büyük veri kümelerinde <code>plt.plot</code>,
    <code>plt.scatter</code>'dan belirgin şekilde daha verimli olabilir.
    Nedeni: <code>plt.scatter</code> her nokta için farklı boyut ve/veya renk çizebilir; oluşturucu her noktayı ayrı ayrı inşa etmek zorundadır.
    <code>plt.plot</code>'ta ise her noktanın işaretçileri aynıdır; görünüm yalnızca bir kez belirlenir.
    Büyük veri kümelerinde bu fark performansı büyük ölçüde etkileyebilir; bu yüzden büyük veri kümelerinde <code>plt.plot</code> tercih edilmelidir.</p>""",
    }
    code_names = {
        2: "scatter_setup.py",
        4: "scatter_plot_o.py",
        6: "marker_styles_demo.py",
        8: "scatter_line_marker.py",
        10: "scatter_styled_markers.py",
        13: "scatter_basic.py",
        15: "scatter_color_size.py",
        17: "iris_scatter.py",
    }
    inserts = {
        2: addon(
            "seaborn-whitegrid stili",
            "<p><code>seaborn-whitegrid</code> eksenlerde ızgara gösterir. Güncel Matplotlib sürümlerinde ad <code>seaborn-v0_8-whitegrid</code> olabilir; uyarı alırsanız <code>plt.style.available</code> ile mevcut stilleri listeleyin.</p>",
        ),
        15: addon(
            "alpha ve renk ölçeği",
            "<p><code>c=colors</code> sürekli bir renk haritasına eşlenir; kategorik veri için <code>c=iris.target</code> gibi tamsayı etiketler ve <code>cmap='viridis'</code> kullanın. <code>alpha</code> üst üste binen noktaların yoğunluğunu okumayı kolaylaştırır.</p>",
        ),
        17: try_it(
            "Renk ve boyutla saçılım deneyin",
            "Rastgele 50 nokta üretin; rengi ve boyutu ayrı değişkenlerle eşleyip colorbar ekleyin:",
            """import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
x = rng.normal(size=50)
y = rng.normal(size=50)
c = rng.random(50)
s = 500 * rng.random(50)

plt.scatter(x, y, c=c, s=s, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')""",
            "scatter_renk_boyut_deneme.py",
        ),
    }
    tr = dict(tr_md)
    title = tr.pop(0)
    return (
        title
        + "\n\n"
        + orig_line(en, "04.02 Simple Scatter Plots")
        + "\n"
        + build_body(
            "04.02-Simple-Scatter-Plots.ipynb",
            tr,
            code_names,
            readonly_cells={2},
            inserts=inserts,
        )
        + "\n"
        + next_link("03-errorbars.html", "4.3 Hata Çubukları")
    )


def body_03() -> str:
    en = "https://jakevdp.github.io/PythonDataScienceHandbook/04.03-errorbars.html"
    tr_md = {
        0: h1("Hata Çubukları"),
        1: """    <p>Her bilimsel ölçümde belirsizliklerin doğru hesaba katılması, çoğu zaman sayının kendisinin doğru raporlanması kadar — hatta daha da — önemlidir.
    Örneğin bazı astrofizik gözlemlerle Evren'in yerel genişleme hızı olan Hubble Sabiti'ni tahmin ettiğimi düşünün.
    Güncel literatür ~70 (km/s)/Mpc öneriyor; yöntemimle 74 (km/s)/Mpc ölçtüm. Değerler tutarlı mı? Verilen bilgiyle tek doğru cevap: bilemeyiz.</p>
    <p>Bu bilgiye belirsizlikleri ekleyelim: literatür 70 ± 2,5 (km/s)/Mpc, yöntemim 74 ± 5 (km/s)/Mpc ölçtü.
    Şimdi tutarlılık nicel olarak sorulabilir.</p>
    <p>Veri ve sonuçların görselleştirilmesinde bu hataların etkili gösterilmesi, grafiğin çok daha eksiksiz bilgi aktarmasını sağlar.</p>""",
        2: h2("Temel hata çubukları", "temel-hata-cubuklari")
        + """    <p>Belirsizlikleri görselleştirmenin standart yollarından biri hata çubuğudur.
    Temel bir hata çubuğu tek bir Matplotlib fonksiyon çağrısıyla oluşturulabilir (aşağıdaki şekle bakın):</p>""",
        5: """    <p>Burada <code>fmt</code>, çizgi ve noktaların görünümünü kontrol eden bir biçim kodudur;
    önceki bölümde ve bu bölümün başında özetlenen <code>plt.plot</code> kısaltma sözdizimiyle aynıdır.</p>
    <p>Temel seçeneklere ek olarak <code>errorbar</code> çıktıyı ince ayarlamak için birçok seçenek sunar.
    Özellikle kalabalık grafiklerde hata çubuklarını noktalardan daha açık renkte yapmayı yararlı bulurum (aşağıdaki şekle bakın):</p>""",
        7: """    <p>Bu seçeneklere ek olarak yatay hata çubukları, tek taraflı hata çubukları ve birçok varyant belirtilebilir.
    Kullanılabilir seçenekler için <code>plt.errorbar</code> docstring'ine bakın.</p>""",
        8: h2("Sürekli hatalar", "surekli-hatalar")
        + """    <p>Bazı durumlarda sürekli nicelikler üzerinde hata çubukları göstermek istenir.
    Matplotlib bu tür uygulama için hazır bir kolaylık rutini sunmasa da,
    <code>plt.plot</code> ve <code>plt.fill_between</code> gibi yapı taşlarını birleştirmek nispeten kolaydır.</p>
    <p>Burada Scikit-Learn API'siyle basit bir <em>Gaussian süreç regresyonu</em> yapacağız.
    Bu, sürekli belirsizlik ölçüsüyle veriye çok esnek parametrik olmayan bir fonksiyon uydurma yöntemidir.
    Gaussian süreç regresyonunun ayrıntılarına girmeyeceğiz; bunun yerine bu tür sürekli hata ölçümünü nasıl görselleştirebileceğimize odaklanacağız:</p>""",
        10: """    <p>Artık verimize sürekli uydurmayı örnekleyen <code>xfit</code>, <code>yfit</code> ve <code>dyfit</code> değişkenlerimiz var.
    Bunları önceki bölümdeki gibi <code>plt.errorbar</code>'a verebilirdik; ancak 1.000 noktaya 1.000 hata çubuğu çizmek istemeyiz.
    Bunun yerine sürekli hatayı görselleştirmek için açık renkle <code>plt.fill_between</code> kullanabiliriz (aşağıdaki şekle bakın):</p>""",
        12: """    <p><code>fill_between</code> çağrı imzasına bakın: bir <em>x</em> değeri, alt <em>y</em> sınırı, üst <em>y</em> sınırı verilir; bu bölgeler arası doldurulur.</p>
    <p>Ortaya çıkan şekil, Gaussian süreç regresyon algoritmasının ne yaptığına sezgisel bir bakış verir:
    ölçülmüş veri noktasına yakın bölgelerde model güçlü kısıtlanır; model belirsizlikleri küçüktür.
    Uzak bölgelerde model zayıf kısıtlanır; belirsizlikler artar.</p>
    <p><code>plt.fill_between</code> (ve yakından ilişkili <code>plt.fill</code>) seçenekleri için fonksiyon docstring'ine veya Matplotlib dokümantasyonuna bakın.</p>
    <p>Son olarak bu biraz düşük seviyeli geliyorsa,
    <a href="14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a> bölümüne bakın;
    Seaborn bu tür sürekli hata çubuklarını görselleştirmek için daha akıcı bir API sunar.</p>""",
    }
    code_names = {
        3: "errorbars_setup.py",
        4: "errorbar_basic.py",
        6: "errorbar_styled.py",
        9: "gaussian_process_fit.py",
        11: "fill_between_errors.py",
    }
    inserts = {
        3: addon(
            "fmt biçim kodları",
            "<p><code>fmt='.k'</code> siyah nokta demektir; <code>'o'</code> daire, <code>'-'</code> çizgi. Hata çubuğu uçları (<code>capsize</code>) ve renk (<code>ecolor</code>) ayrı ayarlanır.</p>",
        ),
        8: addon(
            "Gaussian süreç regresyonu",
            "<p><code>GaussianProcessRegressor</code> Scikit-Learn'den gelir; veri noktalarına yakın bölgelerde dar, uzakta geniş belirsizlik bandı üretir. Bu bölümde amaç algoritmayı öğrenmek değil, <code>fill_between</code> ile sürekli güven aralığını göstermektir.</p>",
        ),
        6: try_it(
            "Yatay hata çubukları",
            "Aynı veri için <code>xerr</code> ekleyerek yatay belirsizlik gösterin:",
            """import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.sin(x)
dy = 0.15
dx = 0.3

plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', capsize=3)
plt.title('Yatay ve dikey hata çubukları')""",
            "errorbar_xy_deneme.py",
        ),
    }
    tr = dict(tr_md)
    title = tr.pop(0)
    return (
        title
        + "\n\n"
        + orig_line(en, "04.03 Errorbars")
        + "\n"
        + build_body(
            "04.03-Errorbars.ipynb",
            tr,
            code_names,
            readonly_cells={3},
            inserts=inserts,
        )
        + "\n"
        + next_link("04-density-and-contour-plots.html", "4.4 Yoğunluk ve Kontur Grafikleri")
    )


def body_04() -> str:
    en = "https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html"
    tr_md = {
        0: h1("Yoğunluk ve Kontur Grafikleri"),
        1: """    <p>Bazen üç boyutlu veriyi kontur veya renk kodlu bölgelerle iki boyutta göstermek yararlıdır.
    Matplotlib'te bunun birkaç aracı vardır: <code>plt.contour</code>, <code>plt.contourf</code> ve <code>plt.imshow</code>.
    Burada bunları bir $z = f(x, y)$ fonksiyonu üzerinde göstereceğiz.</p>""",
        3: h2("Üç boyutlu bir fonksiyonu görselleştirme", "uc-boyutlu-fonksiyon"),
        4: """    <p>İlk örneğimiz $z = f(x, y)$ fonksiyonu için kontur grafiği gösterir; fonksiyon şöyle seçilmiştir:</p>""",
        6: """    <p>Kontur grafiği <code>plt.contour</code> ile oluşturulur. Üç argüman alır: <em>x</em> değerleri ızgarası, <em>y</em> değerleri ızgarası ve <em>z</em> değerleri ızgarası.</p>""",
        8: """    <p>Şimdi yalnızca çizgili standart kontur grafiğine bakalım (aşağıdaki şekle bakın):</p>""",
        10: """    <p>Tek renk kullanıldığında negatif değerler kesikli, pozitif değerler düz çizgiyle gösterilir.
    Alternatif olarak <code>cmap</code> argümanıyla çizgiler renklendirilebilir.
    Burada veri aralığında 20 eşit aralıklı çizgi istiyoruz (aşağıdaki şekle bakın):</p>""",
        12: """    <p><code>RdGy</code> (<em>Red–Gray</em>, kırmızı–gri) renk haritasını seçtik; sıfır etrafında pozitif ve negatif sapma olan
    <em>ıraksak</em> (divergent) veri için iyi bir seçimdir.
    Matplotlib'te birçok renk haritası vardır; IPython'da <code>plt.cm</code> modülünde sekme tamamlama ile kolayca gezinebilirsiniz:</p>
    <div class="code-block" data-lang="text" data-readonly="true" data-filename="colormap_tab.txt">
      <pre><code>plt.cm.&lt;TAB&gt;</code></pre>
    </div>
    <p>Grafiğimiz daha iyi görünüyor; çizgiler arası boşluklar dikkat dağıtıcı olabilir.
    Bunu <code>plt.contourf</code> ile dolu kontur grafiğine geçerek değiştirebiliriz; sözdizimi büyük ölçüde <code>plt.contour</code> ile aynıdır.</p>
    <p>Ek olarak renk bilgisi için etiketli ek bir eksen oluşturan <code>plt.colorbar</code> komutunu ekleyeceğiz (aşağıdaki şekle bakın):</p>""",
        14: """    <p>Renk çubuğu siyah bölgelerin «tepe», kırmızı bölgelerin «vadi» olduğunu netleştirir.</p>
    <p>Bu grafikte renk adımları ayrık olduğu için lekeli görünebilir; her zaman istenen bu değildir.
    Çok yüksek kontur sayısı ayarlanabilir ama verimsiz olur: Matplotlib her seviye için yeni bir çokgen çizer.
    Daha pürüzsüz gösterim için <code>plt.imshow</code> ve <code>interpolation</code> argümanı kullanılabilir (aşağıdaki şekle bakın):</p>""",
        16: """    <p><code>plt.imshow</code> ile birkaç olası tuzak vardır:</p>
    <ul>
      <li><em>x</em> ve <em>y</em> ızgarası kabul etmez; görüntünün grafikteki kapsamını [<em>xmin</em>, <em>xmax</em>, <em>ymin</em>, <em>ymax</em>] ile elle belirtmeniz gerekir.</li>
      <li>Varsayılan olarak köken sol üsttedir; çoğu kontur grafiğindeki gibi sol alt değildir. Izgara verisi gösterirken değiştirilmelidir.</li>
      <li>Girdi verisine göre eksen en-boy oranını otomatik ayarlar; <code>aspect</code> ile değiştirilebilir.</li>
    </ul>""",
        17: """    <p>Son olarak kontur ve görüntü grafiklerini birleştirmek bazen yararlıdır.
    Örneğin kısmen saydam arka plan görüntüsü (<code>alpha</code> ile) ve üzerine <code>plt.clabel</code> ile etiketlenmiş konturlar kullanalım (aşağıdaki şekle bakın):</p>""",
        19: """    <p><code>plt.contour</code>, <code>plt.contourf</code> ve <code>plt.imshow</code> birleşimi,
    bu tür üç boyutlu veriyi iki boyutlu grafikte göstermek için neredeyse sınırsız olanak sunar.
    Bu işlevlerdeki seçenekler için docstring'lerine bakın.
    Bu tür verinin üç boyutlu görselleştirmesiyle ilgileniyorsanız
    <a href="12-three-dimensional-plotting.html">Matplotlib'te Üç Boyutlu Çizim</a> bölümüne bakın.</p>""",
    }
    code_names = {
        2: "contour_setup.py",
        5: "contour_function_f.py",
        7: "meshgrid_xyz.py",
        9: "contour_black.py",
        11: "contour_colormap.py",
        13: "contourf_colorbar.py",
        15: "imshow_interpolation.py",
        18: "contour_imshow_combo.py",
    }
    inserts = {
        2: addon(
            "seaborn-white stili",
            "<p><code>seaborn-white</code> arka planı beyaz tutar; kontur ve <code>imshow</code> örneklerinde renk haritası daha net okunur. Güncel sürümlerde <code>seaborn-v0_8-white</code> gerekebilir.</p>",
        ),
        7: addon(
            "meshgrid ve extent",
            "<p><code>np.meshgrid</code> iki boyutlu ızgara oluşturur; <code>plt.imshow</code> kullanırken <code>extent=[xmin, xmax, ymin, ymax]</code> ve <code>origin='lower'</code> ile eksenleri kontur grafikleriyle hizalayın.</p>",
        ),
        13: try_it(
            "Kontur + renk çubuğu",
            "Aynı <code>f(x,y)</code> fonksiyonu için <code>contourf</code> ve farklı bir <code>cmap</code> (ör. <code>'viridis'</code>) deneyin:",
            """import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 25, cmap='viridis')
plt.colorbar(label='z')
plt.title('Dolu kontur — viridis')""",
            "contourf_deneme.py",
        ),
    }
    tr = dict(tr_md)
    title = tr.pop(0)
    return (
        title
        + "\n\n"
        + orig_line(en, "04.04 Density and Contour Plots")
        + "\n"
        + build_body(
            "04.04-Density-and-Contour-Plots.ipynb",
            tr,
            code_names,
            readonly_cells={2},
            inserts=inserts,
        )
        + "\n"
        + next_link("05-histograms-and-binnings.html", "4.5 Histogramlar ve Binleme")
    )


def body_05() -> str:
    en = "https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html"
    tr_md = {
        0: h1("Histogramlar ve Binleme"),
        1: """    <p>Basit bir histogram veri setini anlamanın iyi bir ilk adımı olabilir.
    Daha önce Matplotlib'in histogram işlevinin önizlemesini görmüştük
    (<a href="../02-numpy/06-boolean-masks.html">Karşılaştırma, Maskeler ve Boolean Mantık</a> bölümünde tartışıldı);
    standart içe aktarmalardan sonra tek satırda temel histogram oluşturur (aşağıdaki şekle bakın):</p>""",
        4: """    <p><code>hist</code> hem hesaplamayı hem görüntüyü ayarlamak için birçok seçenek sunar;
    daha özelleştirilmiş bir histogram örneği aşağıdaki şekilde:</p>""",
        6: """    <p><code>plt.hist</code> docstring'inde başka özelleştirme seçenekleri vardır.
    Birkaç dağılımın histogramlarını karşılaştırırken <code>histtype='stepfilled'</code> ile bir miktar saydamlık (<code>alpha</code>) yararlı bulurum (aşağıdaki şekle bakın):</p>""",
        8: """    <p>Histogramı hesaplamak ama göstermemek istiyorsanız (yani verilen kutudaki nokta sayısını saymak),
    <code>np.histogram</code> kullanılabilir:</p>""",
        10: h2("İki boyutlu histogramlar ve binleme", "iki-boyutlu-histogramlar"),
        12: h3("plt.hist2d: İki boyutlu histogram", "plt-hist2d")
        + """    <p>İki boyutlu histogram çizmenin doğrudan yolu Matplotlib'in <code>plt.hist2d</code> işlevidir (aşağıdaki şekle bakın):</p>""",
        14: """    <p><code>plt.hist</code> gibi <code>plt.hist2d</code>'nin de grafik ve binlemeyi ince ayarlayan seçenekleri vardır; docstring'te güzel özetlenmiştir.
    <code>plt.hist</code>'in <code>np.histogram</code> karşılığı olduğu gibi <code>plt.hist2d</code>'nin karşılığı <code>np.histogram2d</code>'dir:</p>""",
        16: """    <p>İki boyuttan fazla boyutta binlemenin genellemesi için <code>np.histogramdd</code> işlevine bakın.</p>""",
        17: h3("plt.hexbin: Altıgen binleme", "plt-hexbin")
        + """    <p>İki boyutlu histogram eksenler boyunca karelerden oluşan bir döşeme oluşturur.
    Bu tür döşeme için doğal bir başka şekil düzenli altıgendir.
    Matplotlib bu amaçla <code>plt.hexbin</code> sunar; iki boyutlu veriyi altıgen ızgarada gruplar (aşağıdaki şekle bakın):</p>""",
        19: """    <p><code>plt.hexbin</code>'in ek seçenekleri vardır: her nokta için ağırlık belirtme, her kutudaki çıktıyı herhangi bir NumPy toplamına (ağırlık ortalaması, ağırlık standart sapması vb.) çevirme.</p>""",
        20: h3("Çekirdek yoğunluk tahmini", "cekirdek-yogunluk-tahmini")
        + """    <p>Çok boyutlu yoğunlukları tahmin etmenin ve göstermenin bir başka yaygın yolu <em>çekirdek yoğunluk tahmini</em> (KDE)'dir.
    Bu konu kitapta ayrıntılı ele alınır; şimdilik KDE'nin uzaydaki noktaları «yayarak» sonucu toplayıp pürüzsüz bir fonksiyon elde etme yolu olarak düşünülebilir.
    <code>scipy.stats</code> paketinde çok hızlı ve basit bir KDE uygulaması vardır.
    KDE kullanımına kısa bir örnek (aşağıdaki şekle bakın):</p>""",
        22: """    <p>KDE'nin ayrıntı ile pürüzsüzlük arasında kaydıran bir yumuşatma uzunluğu vardır (yaygın önyargı–varyans ödünleşiminin bir örneği).
    Uygun yumuşatma uzunluğu seçimi geniş bir literatüre sahiptir; <code>gaussian_kde</code> girdi verisi için neredeyse optimal bir uzunluk bulmaya çalışır.</p>
    <p>SciPy ekosisteminde farklı güçlü ve zayıf yönleri olan başka KDE uygulamaları da vardır; örneğin <code>sklearn.neighbors.KernelDensity</code> ve <code>statsmodels.nonparametric.KDEMultivariate</code>.</p>
    <p>KDE tabanlı görselleştirmelerde Matplotlib genelde fazla ayrıntılı olabilir.
    <a href="14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a> bölümünde tartışılan Seaborn kütüphanesi KDE tabanlı görselleştirmeler için çok daha kompakt bir API sunar.</p>""",
    }
    code_names = {
        2: "histogram_setup.py",
        3: "hist_basic.py",
        5: "hist_custom.py",
        7: "hist_multiple.py",
        9: "np_histogram.py",
        11: "bivariate_normal_sample.py",
        13: "hist2d_plot.py",
        15: "np_histogram2d.py",
        18: "hexbin_plot.py",
        21: "kde_plot.py",
    }
    inserts = {
        2: addon(
            "density=True",
            "<p><code>density=True</code> histogramı olasılık yoğunluğuna normalize eder (alan 1); ham sayım için varsayılan <code>density=False</code> kullanın. <code>bins</code> kutuların sayısını veya sınır listesini belirler.</p>",
        ),
        5: addon(
            "histtype seçenekleri",
            "<p><code>histtype='stepfilled'</code> dolu adım histogram; <code>'step'</code> yalnızca kenar çizgisi. Üst üste binen dağılımlarda <code>alpha</code> karşılaştırmayı kolaylaştırır.</p>",
        ),
        7: try_it(
            "Üç dağılımı üst üste çizin",
            "Üç farklı normal dağılımdan 500'er örnek alıp aynı eksende yarı saydam histogram çizin:",
            """import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
kwargs = dict(histtype='stepfilled', alpha=0.4, density=True, bins=30)
for mu, sigma in [(0, 1), (-2, 0.8), (2, 1.5)]:
    data = rng.normal(mu, sigma, 500)
    plt.hist(data, **kwargs, label=f'μ={mu}, σ={sigma}')
plt.legend()
plt.title('Üç normal dağılım')""",
            "hist_coklu_deneme.py",
        ),
    }
    tr = dict(tr_md)
    title = tr.pop(0)
    return (
        title
        + "\n\n"
        + orig_line(en, "04.05 Histograms and Binnings")
        + "\n"
        + build_body(
            "04.05-Histograms-and-Binnings.ipynb",
            tr,
            code_names,
            readonly_cells={2},
            inserts=inserts,
        )
        + "\n"
        + next_link("06-customizing-legends.html", "4.6 Lejant Özelleştirme")
    )


def verify_counts() -> None:
    expected = {
        "04.02-Simple-Scatter-Plots.ipynb": 20,
        "04.03-Errorbars.ipynb": 13,
        "04.04-Density-and-Contour-Plots.ipynb": 20,
        "04.05-Histograms-and-Binnings.ipynb": 23,
    }
    for nb, n in expected.items():
        assert len(load_notebook(nb)) == n, nb


def main() -> None:
    verify_counts()
    chapters = [
        ("02-simple-scatter-plots", body_02()),
        ("03-errorbars", body_03()),
        ("04-density-and-contour-plots", body_04()),
        ("05-histograms-and-binnings", body_05()),
    ]
    for slug, body in chapters:
        path = write_slug(slug, body)
        print("wrote", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
