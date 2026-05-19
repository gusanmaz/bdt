#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_mpl_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_matplotlib_chapter import write_chapter

NB = "04.12-Three-Dimensional-Plotting.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>4.12 Matplotlib'da Üç Boyutlu Çizim</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html" target="_blank" rel="noopener">Three-Dimensional Plotting in Matplotlib</a></em></p>

    <p>Matplotlib başlangıçta yalnızca iki boyutlu çizim düşünülerek tasarlandı. 1.0 sürümü civarında bazı üç boyutlu çizim yardımcı programları Matplotlib'ın iki boyutlu görüntüsünün üzerine inşa edildi; sonuç, üç boyutlu veri görselleştirmesi için kullanışlı (biraz sınırlı olsa da) bir araç kümesidir. Üç boyutlu grafikler, ana Matplotlib kurulumuna dahil <code>mplot3d</code> araç takımını içe aktararak etkinleştirilir:</p>
""" + c(2, "import_mplot3d.py") + """
    <p>Bu alt modül içe aktarıldıktan sonra normal eksen oluşturma rutinlerinden herhangi birine <code>projection='3d'</code> anahtar sözcüğünü geçirerek üç boyutlu bir eksen oluşturulabilir (aşağıdaki şekil):</p>
""" + c(4, "import_mpl_np.py") + c(5, "axes_3d.py") + addon(
    "3B eksen ve etkileşim",
    "<p><code>projection='3d'</code> ile oluşturulan eksen <code>Axes3D</code> tipindedir; "
    "<code>plot3D</code>, <code>scatter3D</code>, <code>contour3D</code>, <code>plot_surface</code> gibi yöntemler yalnızca bu eksende vardır. "
    "Statik bir HTML sayfasında derinlik algısı sınırlıdır; Jupyter'de <code>%matplotlib notebook</code> ile grafiği sürükleyerek bakış açısını (<code>view_init</code> ile aynı işlev) keşfedebilirsiniz.</p>",
) + """
    <p>Üç boyutlu eksen etkinleştirildiğinde çeşitli üç boyutlu grafik türlerini çizebiliriz. Üç boyutlu çizim, notebook'ta statik yerine etkileşimli şekillerle görüntülemenin büyük fayda sağladığı işlevlerden biridir; etkileşimli şekiller için bu kodu çalıştırırken <code>%matplotlib inline</code> yerine <code>%matplotlib notebook</code> kullanabileceğinizi hatırlayın.</p>

    <h2 id="3d-points-lines">Üç Boyutlu Noktalar ve Çizgiler</h2>

    <p>En temel üç boyutlu grafik, (x, y, z) üçlülerinden oluşan kümelerden yaratılan bir çizgi veya saçılım grafiği koleksiyonudur. Daha önce ele alınan iki boyutlu grafiklere benzer şekilde bunlar <code>ax.plot3D</code> ve <code>ax.scatter3D</code> ile oluşturulabilir. Çağrı imzaları iki boyutlu karşılıklarına neredeyse özdeştir; çıktıyı kontrol etmek için <a href="01-simple-line-plots.html">4.1 Basit Çizgi Grafikleri</a> ve <a href="02-simple-scatter-plots.html">4.2 Basit Saçılım Grafikleri</a> bölümlerine bakabilirsiniz. Burada bir trigonometrik spiral ve çizgi civarında rastgele çizilmiş bazı noktaları çizeceğiz (aşağıdaki şekil):</p>
""" + c(8, "spiral_scatter3d.py") + """
    <p>Saçılım noktalarının sayfadaki derinlik hissini vermek için şeffaflıkları ayarlandığına dikkat edin. Üç boyutlu etki statik görüntüde bazen zor görülse de etkileşimli görünüm noktaların düzenine dair iyi bir sezgi sağlayabilir.</p>

    <h2 id="3d-contour">Üç Boyutlu Kontur Grafikleri</h2>

    <p><a href="04-density-and-contour-plots.html">4.4 Yoğunluk ve Kontur Grafikleri</a> bölümünde incelediğimiz kontur grafiklerine benzer şekilde <code>mplot3d</code>, aynı girdilerle üç boyutlu rölyef grafikleri oluşturma araçları içerir. <code>ax.contour</code> gibi <code>ax.contour3D</code> da tüm girdi verisinin iki boyutlu düzenli ızgaralar biçiminde olmasını ve <em>z</em> verisinin her noktada hesaplanmasını gerektirir. Burada üç boyutlu sinüzoidal bir fonksiyonun üç boyutlu kontur diyagramını göstereceğiz (aşağıdaki şekil):</p>
""" + c(11, "meshgrid_f.py") + c(12, "contour3d.py") + """
    <p>Bazen varsayılan bakış açısı optimal değildir; bu durumda yükseklik (elevation) ve azimut açılarını ayarlamak için <code>view_init</code> yöntemini kullanabiliriz. Aşağıdaki örnekte (aşağıdaki şekil) x-y düzleminin 60 derece üstünde (elevation 60) ve z ekseni etrafında saat yönünün tersine 35 derece döndürülmüş (azimuth 35) bir açı kullanacağız:</p>
""" + c(14, "view_init.py") + """
    <p>Yine, bu tür döndürme Matplotlib'ın etkileşimli arka uçlarından biri kullanıldığında tıklayıp sürükleyerek etkileşimli yapılabilir.</p>

    <h2 id="wireframe-surface">Tel Kafes ve Yüzey Grafikleri</h2>

    <p>Izgara verisiyle çalışan iki diğer üç boyutlu grafik türü tel kafes (wireframe) ve yüzey (surface) grafikleridir. Bunlar bir değer ızgarasını belirtilen üç boyutlu yüzeye yansıtır ve ortaya çıkan üç boyutlu biçimlerin görselleştirilmesini kolaylaştırır. Tel kafes kullanan bir örnek (aşağıdaki şekil):</p>
""" + c(17, "wireframe.py") + """
    <p>Yüzey grafiği tel kafes grafiğine benzer; ancak tel kafesin her yüzü dolu bir çokgendir. Dolu çokgenlere renk haritası eklemek, görselleştirilen yüzeyin topolojisinin algılanmasına yardımcı olabilir (aşağıdaki şekil):</p>
""" + c(19, "surface.py") + """
    <p>Yüzey grafiği için değer ızgarası iki boyutlu olmalıdır; ancak dikdörtgensel olmak zorunda değildir. Kısmi polar ızgara oluşturup <code>surface3D</code> ile görselleştirdiğimiz fonksiyona bir dilim alabileceğimiz bir örnek (aşağıdaki şekil):</p>
""" + c(21, "polar_surface.py") + """
    <h2 id="triangulation">Yüzey Üçgenlemesi</h2>

    <p>Bazı uygulamalarda önceki rutinlerin gerektirdiği düzenli örneklenmiş ızgaralar fazla kısıtlayıcıdır. Bu durumlarda üçgenlemeye dayalı grafikler işe yarar. Kartezyen veya polar ızgaradan düzenli örnekleme yerine rastgele nokta kümesi varsa ne olur?</p>
""" + c(23, "random_polar_points.py") + """
    <p>Örneklediğimiz yüzeye dair fikir edinmek için noktaların saçılım grafiğini oluşturabiliriz (aşağıdaki şekil):</p>
""" + c(25, "scatter3d_points.py") + """
    <p>Bu nokta bulutu çok şey bırakıyor. Bu durumda yardımcı olacak fonksiyon <code>ax.plot_trisurf</code>'dur; komşu noktalar arasında oluşan üçgen kümesini bularak bir yüzey oluşturur (<code>x</code>, <code>y</code> ve <code>z</code> burada tek boyutlu dizilerdir); aşağıdaki şekil sonucu gösterir:</p>
""" + c(27, "plot_trisurf.py") + """
    <p>Sonuç ızgara ile çizildiğinde kadar temiz değil; ancak bu üçgenlemenin esnekliği gerçekten ilginç üç boyutlu grafiklere olanak tanır. Örneğin bir sonraki bölümde göreceğimiz gibi Matplotlib ile üç boyutlu bir Möbius şeridi çizmek mümkündür.</p>

    <h2 id="mobius">Örnek: Möbius Şeridi Görselleştirme</h2>

    <p>Möbius şeridi, yarım bükülerek halka haline getirilmiş bir kağıt şeridine benzer; sonuçta yalnızca tek yüzeyi olan bir nesne elde edilir! Burada Matplotlib'ın üç boyutlu araçlarıyla böyle bir nesneyi görselleştireceğiz. Möbius şeridini oluşturmanın anahtarı parametreleştirmesini düşünmektir: iki boyutlu bir şerit olduğu için iki içsel boyuta ihtiyacımız var. Halka boyunca $0$ ile $2\\pi$ arasında değişen $\\theta$ ve şerit genişliği boyunca –1 ile 1 arasında değişen $w$ diyelim:</p>
""" + c(30, "mobius_param.py") + """
    <p>Bu parametreleştirmeden gömülü şeridin (*x*, *y*, *z*) konumlarını belirlemeliyiz.</p>

    <p>Düşününce iki dönüşün gerçekleştiğini fark edebiliriz: biri döngünün merkezi etrafındaki konum ($\\theta$), diğeri şeridin ekseni etrafındaki bükülme ($\\phi$). Möbius şeridinde tam bir döngüde yarım bükülme olmalıdır: $\\Delta\\phi = \\Delta\\theta/2$:</p>
""" + c(32, "mobius_phi.py") + """
    <p>Şimdi trigonometri bilgimizi kullanarak üç boyutlu gömmele türetiriz. Her noktanın merkeze uzaklığı $r$'yi tanımlayıp gömülü $(x, y, z)$ koordinatlarını bulacağız:</p>
""" + c(34, "mobius_xyz.py") + """
    <p>Son olarak nesneyi çizmek için üçgenlemenin doğru olduğundan emin olmalıyız. Bunu en iyi, üçgenlemeyi <em>altta yatan parametreleştirme içinde</em> tanımlayıp Matplotlib'ın bu üçgenlemeyi Möbius şeridinin üç boyutlu uzayına yansıtmasına izin vererek yaparız (aşağıdaki şekil):</p>
""" + c(36, "mobius_trisurf.py") + """
    <p>Tüm bu teknikleri birleştirerek Matplotlib'da çok çeşitli üç boyutlu nesne ve desenler oluşturup görüntülemek mümkündür.</p>
""" + try_it(
    "Basit 3B yüzey",
    "Sinüs-tabanlı bir yüzeyi <code>plot_surface</code> ile çizin:",
    """import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
fig""",
    "deneme_3d_surface.py",
) + next_link("14-visualization-with-seaborn.html", "4.14 Seaborn ile Görselleştirme")

if __name__ == "__main__":
    path = write_chapter("12-three-dimensional-plotting", body)
    print("wrote", path)
