#!/usr/bin/env python3
"""Generate Scikit-Learn chapters 00–02 (TR HTML bodies)."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from _gen_sklearn_helpers import addon, code_block, figure, next_link, try_it

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
SRC = TOOLS / "source" / "notebooks"


def count_cells(nb_name: str) -> int:
    nb = json.loads((SRC / nb_name).read_text(encoding="utf-8"))
    return len(nb["cells"])


def write_slug(slug: str, body: str) -> Path:
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "write_sklearn_chapter.py"), slug],
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


def load_nb(name: str) -> dict:
    return json.loads((SRC / name).read_text(encoding="utf-8"))


def cell_code(cell: dict) -> str:
    return "".join(cell["source"])


def img_from_md(md: str) -> str | None:
    m = re.match(r"!\[\]\(images/([^)]+)\)", md.strip())
    if not m:
        return None
    return m.group(1)


def linkify(html: str) -> str:
    reps = [
        ("05.15-Learning-More.ipynb", "15-learning-more.html"),
        ("05.05-Naive-Bayes.ipynb", "05-naive-bayes.html"),
        ("05.07-Support-Vector-Machines.ipynb", "07-support-vector-machines.html"),
        ("05.08-Random-Forests.ipynb", "08-random-forests.html"),
        ("05.06-Linear-Regression.ipynb", "06-linear-regression.html"),
        ("05.11-K-Means.ipynb", "11-k-means.html"),
        ("05.12-Gaussian-Mixtures.ipynb", "12-gaussian-mixtures.html"),
        ("05.09-Principal-Component-Analysis.ipynb", "09-principal-component-analysis.html"),
        ("05.10-Manifold-Learning.ipynb", "10-manifold-learning.html"),
        ("05.03-Hyperparameters-and-Model-Validation.ipynb", "03-hyperparameters-and-model-validation.html"),
        ("04.14-Visualization-With-Seaborn.ipynb", "../04-matplotlib/14-visualization-with-seaborn.html"),
        ("03.00-Introduction-to-Pandas.ipynb", "../03-pandas/00-introduction.html"),
    ]
    for old, new in reps:
        html = html.replace(old, new)
    html = re.sub(
        r'\[([^\]]+)\]\(05\.(\d+)-([^)]+)\.ipynb\)',
        lambda m: f'<a href="{m.group(2).zfill(2)}-{m.group(3).lower().replace("_", "-")}.html">{m.group(1)}</a>',
        html,
    )
    return html


CODE_NAMES_02: dict[int, str] = {
    5: "seaborn_iris_load.py",
    9: "iris_pairplot.py",
    11: "X_iris.py",
    12: "y_iris.py",
    20: "linear_reg_data.py",
    23: "import_linear_regression.py",
    26: "linear_model_instance.py",
    29: "X_reshape.py",
    31: "model_fit.py",
    33: "model_coef.py",
    34: "model_intercept.py",
    37: "xfit_linspace.py",
    39: "predict_yfit.py",
    41: "plot_linear_fit.py",
    44: "iris_train_test_split.py",
    46: "iris_gaussian_nb.py",
    48: "iris_accuracy.py",
    51: "iris_pca.py",
    53: "iris_pca_plot.py",
    56: "iris_gmm.py",
    58: "iris_gmm_plot.py",
    63: "digits_load.py",
    65: "digits_grid_plot.py",
    67: "digits_X.py",
    68: "digits_y.py",
    71: "digits_isomap.py",
    73: "digits_isomap_scatter.py",
    76: "digits_train_test.py",
    77: "digits_gaussian_nb.py",
    79: "digits_accuracy.py",
    81: "digits_confusion_matrix.py",
    83: "digits_misclassified_plot.py",
}


def render_nb(
    nb_name: str,
    md_html: dict[int, str],
    code_names: dict[int, str] | None = None,
    skip_md: set[int] | None = None,
) -> str:
    """Emit HTML for every cell; markdown from md_html, code from notebook."""
    nb = load_nb(nb_name)
    code_names = code_names or {}
    skip_md = skip_md or set()
    parts: list[str] = []
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            src = cell_code(cell)
            fn = code_names.get(i, f"cell_{i:02d}.py")
            ro = src.lstrip().startswith("%")
            parts.append(code_block(src, fn, readonly=ro))
        else:
            if i in skip_md:
                continue
            raw = cell_code(cell)
            if i in md_html:
                parts.append(md_html[i])
            elif img := img_from_md(raw):
                alt = img.replace(".png", "").replace("-", " ")
                parts.append(figure(img, alt))
            else:
                raise ValueError(f"{nb_name} cell {i}: missing Turkish markdown")
    return "\n".join(parts)


def body_00() -> str:
    en_url = "https://jakevdp.github.io/PythonDataScienceHandbook/05.00-machine-learning.html"
    return f"""<h1>Makine Öğrenmesi</h1>

    <p><em>Orijinal: <a href="{en_url}" target="_blank" rel="noopener">05.00 Machine Learning</a></em></p>

    <p>Kitabın bu son bölümü, özellikle Python'un <a href="http://scikit-learn.org" target="_blank" rel="noopener">Scikit-Learn</a> paketi üzerinden çok geniş bir konu olan makine öğrenmesine giriş niteliğindedir.
    Makine öğrenmesini, bir programın bir veri kümesindeki belirli örüntüleri algılamasına ve böylece veriden \"öğrenerek\" çıkarımlar yapmasına olanak tanıyan bir algoritma sınıfı olarak düşünebilirsiniz.
    Burada makine öğrenmesi alanının kapsamlı bir girişi yapılmamaktadır; bu büyük bir konudur ve burada aldığımızdan daha teknik bir yaklaşım gerektirir.
    Scikit-Learn paketinin kullanımına yönelik kapsamlı bir el kitabı da değildir (bunun için <a href="15-learning-more.html">Daha Fazla Makine Öğrenmesi Kaynağı</a> bölümündeki kaynaklara bakabilirsiniz).
    Bunun yerine hedefler şunlardır:</p>

    <ul>
      <li>Makine öğrenmesinin temel sözlüğünü ve kavramlarını tanıtmak</li>
      <li>Scikit-Learn API'sini tanıtmak ve kullanımına birkaç örnek göstermek</li>
      <li>Birkaç önemli klasik makine öğrenmesi yaklaşımının ayrıntılarına inmek; nasıl çalıştıklarına ve ne zaman/nerede uygulanabilir olduklarına dair sezgi geliştirmek</li>
    </ul>

    <p>Bu bölümdeki malzemenin önemli kısmı, yıllar içinde PyCon, SciPy, PyData ve diğer konferanslarda verdiğim Scikit-Learn öğreticilerinden ve atölyelerinden derlenmiştir.
    Aşağıdaki sayfalardaki netlik büyük olasılıkla bu malzeme üzerinde değerli geri bildirim veren çok sayıda atölye katılımcısı ve yardımcı eğitmene borçluyum!</p>

{addon("Bölüm 5 ve önkoşullar", """<p>Bu bölüm <a href="../02-numpy/00-introduction.html">NumPy</a>, <a href="../03-pandas/00-introduction.html">Pandas</a> ve <a href="../04-matplotlib/00-introduction.html">Matplotlib</a> bölümlerindeki araçları varsayar. Kod örnekleri bu sayfada Pyodide ile çalıştırılabilir; Scikit-Learn gerektiren bölümlerde paket önceden yüklenir.</p>""")}

{try_it(
    "Scikit-Learn sürümünü kontrol edin",
    "Aşağıdaki kodu çalıştırarak ortamınızda scikit-learn kurulu mu bakın (Bölüm 5.2'den itibaren yoğun kullanılacak):",
    """try:
    import sklearn
    print("scikit-learn", sklearn.__version__)
except ImportError:
    print("scikit-learn yüklü değil")""",
    "check_sklearn.py",
)}

{next_link("01-what-is-machine-learning.html", "5.1 Makine Öğrenmesi Nedir?")}
"""


def md_01() -> dict[int, str]:
    en = "https://jakevdp.github.io/PythonDataScienceHandbook/05.01-what-is-machine-learning.html"
    return {
        0: f"""<h1>Makine Öğrenmesi Nedir?</h1>

    <p><em>Orijinal: <a href="{en}" target="_blank" rel="noopener">05.01 What Is Machine Learning?</a></em></p>
""",
        1: """    <p>Birkaç makine öğrenmesi yönteminin ayrıntılarına geçmeden önce makine öğrenmesinin ne olduğuna — ve ne olmadığına — bakalım.
    Makine öğrenmesi sıkça yapay zekanın alt alanı olarak sınıflandırılır; ancak bu sınıflandırma yanıltıcı olabilir.
    Makine öğrenmesi araştırması kesinlikle bu bağlamdan doğmuştur; fakat veri biliminde makine öğrenmesi yöntemlerinin uygulanmasında, makine öğrenmesini <em>veriden model oluşturmanın</em> bir aracı olarak düşünmek daha yararlıdır.</p>

    <p>Bu bağlamda \"öğrenme\", bu modellere gözlemlenen veriye uyarlanabilen <em>ayarlanabilir parametreler</em> verdiğimizde devreye girer; böylece program veriden \"öğreniyor\" sayılabilir.
    Modeller daha önce görülen veriye uydurulduktan sonra, yeni gözlemlenen verinin yönlerini tahmin etmek ve anlamak için kullanılabilir.
    Bu tür matematiksel, modele dayalı \"öğrenmenin\" insan beyninin sergilediği \"öğrenmeye\" ne ölçüde benzediği konusundaki daha felsefi tartışmayı okuyucuya bırakıyorum.</p>

    <p>Makine öğrenmesinde problem bağlamını anlamak, bu araçları etkili kullanmak için gereklidir; bu yüzden burada ele alacağımız yaklaşım türlerinin geniş bir sınıflandırmasıyla başlayacağız.</p>
""",
        2: """    <h2 id="makine-ogrenmesi-kategorileri">Makine Öğrenmesi Kategorileri</h2>

    <p>Makine öğrenmesi iki ana türe ayrılabilir: <em>denetimli öğrenme</em> ve <em>denetimsiz öğrenme</em>.</p>

    <p><em>Denetimli öğrenme</em>, verinin ölçülen öznitelikleri ile veriyle ilişkili etiketler arasındaki ilişkiyi bir şekilde modellemeyi içerir; model belirlendikten sonra yeni, bilinmeyen verilere etiket uygulamak için kullanılabilir.
    Bu bazen <em>sınıflandırma</em> ve <em>regresyon</em> görevlerine ayrılır: sınıflandırmada etiketler ayrık kategorilerdir; regresyonda süreklidir.
    Sonraki bölümde her iki denetimli öğrenme türüne de örnekler göreceksiniz.</p>

    <p><em>Denetimsiz öğrenme</em>, herhangi bir etikete başvurmadan bir veri kümesinin özniteliklerini modellemeyi içerir.
    Bu modeller <em>kümeleme</em> ve <em>boyut indirgeme</em> gibi görevleri kapsar.
    Kümeleme algoritmaları verinin belirgin gruplarını tanımlar; boyut indirgeme algoritmaları verinin daha özlü temsillerini arar.
    Denetimsiz öğrenmenin her iki türüne de örnekler göreceksiniz.</p>

    <p>Buna ek olarak, denetimli ile denetimsiz arasında kalan <em>yarı denetimli öğrenme</em> yöntemleri vardır; yalnızca eksik etiketler mevcut olduğunda sıkça yararlıdır.</p>
""",
        3: """    <h2 id="nitel-ornekler">Makine Öğrenmesi Uygulamalarına Nitel Örnekler</h2>

    <p>Bu fikirleri somutlaştırmak için bir makine öğrenmesi görevinin birkaç çok basit örneğine bakalım.
    Bu örnekler, kitabın bu bölümünde inceleyeceğimiz makine öğrenmesi görev türlerine sezgisel, nicel olmayan bir genel bakış vermek içindir.
    Sonraki bölümlerde belirli modellere ve kullanımlarına daha derin ineceğiz.
    Daha teknik yönlerin önizlemesi için aşağıdaki şekilleri üreten Python kaynağını çevrimiçi <a href="https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb" target="_blank" rel="noopener">ek bölümde</a> bulabilirsiniz.</p>
""",
        4: """    <h3 id="siniflandirma">Sınıflandırma: Ayrık Etiketleri Tahmin Etmek</h3>

    <p>Önce etiketli noktalar verildiğinde bunları kullanarak etiketsiz noktaları sınıflandırmak istediğimiz basit bir sınıflandırma görevine bakalım.</p>

    <p>Aşağıdaki şekilde gösterilen veriye sahip olduğumuzu düşünün:</p>
""",
        6: """    <p>Bu veri iki boyutludur: her nokta için düzlemdeki (x,y) konumlarıyla temsil edilen iki <em>öznitelik</em> vardır.
    Ayrıca her nokta için iki <em>sınıf etiketinden</em> biri vardır; burada noktaların renkleriyle gösterilir.
    Bu öznitelikler ve etiketlerden, yeni bir noktanın \"mavi\" mi \"kırmızı\" mı etiketleneceğine karar verecek bir model oluşturmak isteriz.</p>

    <p>Böyle bir sınıflandırma görevi için birçok model mümkündür; çok basit biriyle başlayacağız. İki grubun düzlemde aralarına çizilen düz bir doğruyla ayrılabileceğini, doğrunun her iki tarafındaki noktaların aynı gruba düştüğünü varsayacağız.
    Burada <em>model</em>, \"düz bir doğru sınıfları ayırır\" ifadesinin nicel bir sürümüdür; <em>model parametreleri</em> ise bu doğrunun verimiz için konum ve yönelimini tanımlayan sayılardır.
    Bu parametrelerin en uygun değerleri veriden öğrenilir (makine öğrenmesindeki \"öğrenme\" budur); buna genelde <em>modeli eğitmek</em> denir.</p>

    <p>Aşağıdaki şekil, eğitilmiş modelin bu veri için nasıl göründüğünü gösterir:</p>
""",
        8: """    <p>Model eğitildikten sonra yeni, etiketlenmemiş veriye genellenebilir.
    Başka bir deyişle, yeni bir veri kümesi alıp bu doğruyu çizebilir ve modele göre yeni noktalara etiket atayabiliriz (aşağıdaki şekil).
    Bu aşamaya genelde <em>tahmin</em> denir.</p>
""",
        10: """    <p>Bu, makine öğrenmesinde \"sınıflandırma\" görevinin temel fikridir; verinin ayrık sınıf etiketleri olduğunu belirtir.
    İlk bakışta bu önemsiz görünebilir: veriye bakıp böyle bir ayırıcı doğru çizmek kolaydır.
    Makine öğrenmesi yaklaşımının yararı ise çok daha büyük ve çok daha fazla boyutlu veri kümelerine genellenebilmesidir.</p>

    <p>Örneğin bu, e-posta için otomatik spam tespitine benzer. Burada şu öznitelik ve etiketleri kullanabiliriz:</p>

    <ul>
      <li><em>öznitelik 1</em>, <em>öznitelik 2</em>, … → önemli kelime veya ifadelerin normalize sayıları (\"Viagra\", \"Extended warranty\" vb.)</li>
      <li><em>etiket</em> → \"spam\" veya \"spam değil\"</li>
    </ul>

    <p>Eğitim kümesi için etiketler küçük bir temsil örneğinin tek tek incelenmesiyle belirlenebilir; kalan e-postalar için etiket modelle belirlenir.
    Yeterince iyi oluşturulmuş özniteliklere (genelde binlerce veya milyonlarca kelime/ifade) sahip uygun eğitilmiş bir sınıflandırma algoritması çok etkili olabilir.
    Metin tabanlı böyle bir sınıflandırma örneğini <a href="05-naive-bayes.html">Derinlemesine: Naive Bayes Sınıflandırması</a> bölümünde göreceğiz.</p>

    <p>Daha ayrıntılı ele alacağımız önemli sınıflandırma algoritmaları arasında Gauss naive Bayes (<a href="05-naive-bayes.html">Derinlemesine: Naive Bayes</a>), destek vektör makineleri (<a href="07-support-vector-machines.html">Derinlemesine: SVM</a>) ve rastgele orman sınıflandırması (<a href="08-random-forests.html">Derinlemesine: Karar Ağaçları ve Rastgele Ormanlar</a>) vardır.</p>
""",
        11: """    <h3 id="regresyon">Regresyon: Sürekli Etiketleri Tahmin Etmek</h3>

    <p>Sınıflandırma algoritmasının ayrık etiketlerinin aksine, etiketlerin sürekli nicelikler olduğu basit bir regresyon görevine bakalım.</p>

    <p>Aşağıdaki şekildeki veriyi düşünün; her noktanın sürekli bir etiketi vardır:</p>
""",
        13: """    <p>Sınıflandırma örneğinde olduğu gibi iki boyutlu verimiz var: her veri noktasını tanımlayan iki öznitelik.
    Her noktanın rengi o nokta için sürekli etiketi temsil eder.</p>

    <p>Bu tür veri için birçok regresyon modeli kullanılabilir; burada noktaları tahmin etmek için basit doğrusal regresyon kullanacağız.
    Bu basit model, etiketi üçüncü bir uzamsal boyut olarak ele alırsak veriye bir düzlem sığdırabileceğimizi varsayar.
    Bu, iki koordinatlı veriye doğru sığdırma probleminin daha üst düzey bir genellemesidir.</p>

    <p>Bu kurulumu aşağıdaki şekilde görselleştirebiliriz:</p>
""",
        15: """    <p><em>öznitelik 1–öznitelik 2</em> düzleminin iki boyutlu çizimdekiyle aynı olduğuna dikkat edin; burada etiketleri hem renkle hem üç boyutlu eksen konumuyla temsil ettik.
    Bu bakış açısından, bu üç boyutlu veriye bir düzlem sığdırmak herhangi bir girdi parametre seti için beklenen etiketi tahmin etmemize olanak tanır gibi görünür.
    İki boyutlu izdüşüme döndüğümüzde böyle bir düzlem sığdırdığımızda aşağıdaki sonucu elde ederiz:</p>
""",
        17: """    <p>Bu uyum düzlemi yeni noktalar için etiket tahmin etmemiz için gerekeni verir.
    Görsel olarak sonuçlar aşağıdaki şekildedir:</p>
""",
        19: """    <p>Sınıflandırma örneğinde olduğu gibi, az sayıda boyutta bu görev önemsiz görünebilir.
    Ancak bu yöntemlerin gücü, çok sayıda özniteliği olan veriye doğrudan uygulanıp değerlendirilebilmesidir.</p>

    <p>Örneğin bu, teleskopla gözlemlenen galaksilere uzaklık hesaplamaya benzer:</p>

    <ul>
      <li><em>öznitelik 1</em>, <em>öznitelik 2</em>, … → her galaksinin bir veya birkaç dalga boyundaki parlaklığı</li>
      <li><em>etiket</em> → galaksinin uzaklığı veya kırmızıya kayması</li>
    </ul>

    <p>Küçük bir galaksi alt kümesinin uzaklıkları bağımsız (genelde daha pahalı/karmaşık) gözlemlerle belirlenebilir.
    Kalan galaksilerin uzaklıkları uygun bir regresyon modeliyle tahmin edilebilir; tüm küme için pahalı gözlemi tekrarlamaya gerek kalmaz.
    Astronomi çevrelerinde buna \"fotometrik kırmızıya kayma\" problemi denir.</p>

    <p>Ele alacağımız önemli regresyon algoritmaları arasında doğrusal regresyon (<a href="06-linear-regression.html">Derinlemesine: Doğrusal Regresyon</a>), destek vektör makineleri (<a href="07-support-vector-machines.html">Derinlemesine: SVM</a>) ve rastgele orman regresyonu (<a href="08-random-forests.html">Derinlemesine: Karar Ağaçları ve Rastgele Ormanlar</a>) vardır.</p>
""",
        20: """    <h3 id="kumeleme">Kümeleme: Etiketsiz Veride Etiket Çıkarsama</h3>

    <p>Az önce gördüğümüz sınıflandırma ve regresyon örnekleri, yeni veri için etiket tahmin edecek model oluşturmaya çalışan <em>denetimli</em> öğrenme algoritmalarıdır.
    Denetimsiz öğrenme, bilinen etiketlere başvurmadan veriyi tanımlayan modelleri içerir.</p>

    <p>Denetimsiz öğrenmenin yaygın bir durumu \"kümeleme\"dir; veri otomatik olarak belirli sayıda ayrık gruba atanır.
    Örneğin aşağıdaki şekildeki gibi iki boyutlu verimiz olabilir:</p>
""",
        22: """    <p>Gözle her noktanın belirgin bir grubun parçası olduğu açıktır.
    Bu girdiyle bir kümeleme modeli, verinin iç yapısını kullanarak hangi noktaların ilişkili olduğunu belirler.
    Çok hızlı ve sezgisel <em>k</em>-ortalama algoritmasıyla (<a href="11-k-means.html">Derinlemesine: K-Means Kümeleme</a>) aşağıdaki kümeleri buluruz:</p>
""",
        24: """    <p><em>k</em>-ortalama, <em>k</em> küme merkezinden oluşan bir model sığdırır; en uygun merkezler, her noktanın atandığı merkeze uzaklığını minimize edenler varsayılır.
    İki boyutta bu yine basit görünebilir; veri büyüdükçe ve karmaşıklaştıkça kümeleme algoritmaları veri kümesinden yararlı bilgi çıkarmaya devam eder.</p>

    <p><em>k</em>-ortalama algoritmasını <a href="11-k-means.html">Derinlemesine: K-Means Kümeleme</a> bölümünde daha derin ele alacağız.
    Diğer önemli kümeleme algoritmaları arasında Gauss karışım modelleri (<a href="12-gaussian-mixtures.html">Derinlemesine: Gauss Karışımları</a>) ve spektral kümeleme (<a href="http://scikit-learn.org/stable/modules/clustering.html" target="_blank" rel="noopener">Scikit-Learn kümeleme dokümantasyonu</a>) vardır.</p>
""",
        25: """    <h3 id="boyut-indirgeme">Boyut İndirgeme: Etiketsiz Verinin Yapısını Çıkarsama</h3>

    <p>Boyut indirgeme, etiketlerin veya diğer bilgilerin veri kümesinin yapısından çıkarıldığı denetimsiz bir algoritma örneğidir.
    Önceki örneklerden biraz daha soyuttur; genelde veri kümesinin ilgili niteliklerini koruyan düşük boyutlu bir temsil çıkarmayı hedefler.
    Farklı boyut indirgeme yöntemleri bu nitelikleri farklı ölçer (<a href="10-manifold-learning.html">Derinlemesine: Manifold Öğrenme</a>).</p>

    <p>Örnek olarak aşağıdaki veriyi düşünün:</p>
""",
        27: """    <p>Görsel olarak bu veride yapı vardır: iki boyutlu uzayda spiral biçiminde düzenlenmiş tek boyutlu bir çizgiden çekilmiştir.
    Bir bakıma veri aslında \"içsel\" olarak yalnızca tek boyutludur; bu tek boyutlu veri iki boyutlu uzaya gömülmüştür.
    Uygun bir boyut indirgeme modeli bu doğrusal olmayan gömülü yapıya duyarlı olur ve daha düşük boyutlu temsili algılayabilir.</p>

    <p>Aşağıdaki şekil tam bunu yapan bir manifold öğrenme algoritması olan Isomap'ın sonuçlarını gösterir.</p>
""",
        29: """    <p>Renklerin (çıkarılan tek boyutlu gizli değişkeni temsil eden) spiral boyunca düzgün değiştiğine dikkat edin; algoritmanın gözle gördüğümüz yapıyı algıladığını gösterir.
    Önceki örneklerde olduğu gibi, boyut indirgeme algoritmalarının gücü daha yüksek boyutlarda belirginleşir.
    Örneğin 100 veya 1000 özniteliği olan bir veri kümesindeki önemli ilişkileri görselleştirmek isteyebiliriz.
    1000 boyutlu veriyi görselleştirmek zordur; veriyi 2 veya 3 boyuta indirgeyerek yönetilebilir kılabiliriz.</p>

    <p>Ele alacağımız önemli boyut indirgeme algoritmaları arasında temel bileşen analizi (<a href="09-principal-component-analysis.html">Derinlemesine: PCA</a>) ve Isomap ile yerel doğrusal gömme dahil çeşitli manifold öğrenme algoritmaları (<a href="10-manifold-learning.html">Derinlemesine: Manifold Öğrenme</a>) vardır.</p>
""",
        30: """    <h2 id="ozet-01">Özet</h2>

    <p>Burada temel makine öğrenmesi yaklaşım türlerinin birkaç basit örneğini gördük.
    Kuşkusuz göz ardı ettiğimiz önemli pratik ayrıntılar vardır; ancak bu bölüm, makine öğrenmesi yaklaşımlarının hangi problem türlerini çözebileceğine dair temel bir fikir vermek için tasarlandı.</p>

    <p>Kısaca şunları gördük:</p>

    <ul>
      <li><em>Denetimli öğrenme</em>: Etiketli eğitim verisine dayanarak etiket tahmin eden modeller
        <ul>
          <li><em>Sınıflandırma</em>: Etiketleri iki veya daha fazla ayrık kategori olarak tahmin eden modeller</li>
          <li><em>Regresyon</em>: Sürekli etiket tahmin eden modeller</li>
        </ul>
      </li>
      <li><em>Denetimsiz öğrenme</em>: Etiketsiz veride yapı tanımlayan modeller
        <ul>
          <li><em>Kümeleme</em>: Veride belirgin grupları tespit eden modeller</li>
          <li><em>Boyut indirgeme</em>: Yüksek boyutlu veride daha düşük boyutlu yapıyı bulan modeller</li>
        </ul>
      </li>
    </ul>

    <p>Sonraki bölümlerde bu kategoriler içinde çok daha derine inecek ve bu kavramların nerede yararlı olduğuna dair daha ilginç örnekler göreceğiz.</p>

    <p>Önceki tartışmadaki tüm şekiller gerçek makine öğrenmesi hesaplarına dayanır; arkalarındaki kod <a href="https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb" target="_blank" rel="noopener">Ek: Şekil Kodu</a> bölümünde bulunur.</p>
""",
    }


def body_01() -> str:
    md = md_01()
    imgs = {
        5: ("05.01-classification-1.png", "Sınıflandırma verisi — etiketli iki boyutlu noktalar"),
        7: ("05.01-classification-2.png", "Eğitilmiş sınıflandırma modeli — ayırıcı doğru"),
        9: ("05.01-classification-3.png", "Yeni veriye tahmin — sınıflandırma"),
        12: ("05.01-regression-1.png", "Regresyon verisi — sürekli etiketli noktalar"),
        14: ("05.01-regression-2.png", "Regresyon — üç boyutlu düzlem uyumu"),
        16: ("05.01-regression-3.png", "Regresyon — iki boyutlu izdüşümde düzlem"),
        18: ("05.01-regression-4.png", "Regresyon — yeni noktalara tahmin"),
        21: ("05.01-clustering-1.png", "Kümeleme — etiketsiz iki boyutlu veri"),
        23: ("05.01-clustering-2.png", "K-means kümeleme sonucu"),
        26: ("05.01-dimesionality-1.png", "Boyut indirgeme — spiral gömülü veri"),
        28: ("05.01-dimesionality-2.png", "Isomap ile boyut indirgeme sonucu"),
    }
    for i, (img, alt) in imgs.items():
        md[i] = figure(img, alt)

    core = render_nb("05.01-What-Is-Machine-Learning.ipynb", md)
    return core + "\n" + addon(
        "Denetimli ve denetimsiz",
        """<p><strong>Denetimli</strong> öğrenmede modelinize hem <code>X</code> (öznitelikler) hem <code>y</code> (etiket) verirsiniz; <strong>denetimsiz</strong> öğrenmede yalnızca <code>X</code> vardır. Bölüm 5.2'de her ikisi için de Scikit-Learn'de aynı <code>fit</code> / <code>predict</code> / <code>transform</code> kalıbını göreceksiniz.</p>""",
    ) + "\n" + try_it(
        "İki küme üretin",
        "Aşağıda rastgele 2D noktalar üretin; gerçek kümeleme algoritmalarını Bölüm 5.11'de göreceksiniz:",
        """import numpy as np
rng = np.random.RandomState(0)
A = rng.randn(20, 2) + [2, 2]
B = rng.randn(20, 2) + [-2, -2]
X = np.vstack([A, B])
print("X.shape =", X.shape)""",
        "two_clusters_X.py",
    ) + "\n" + next_link("02-introducing-scikit-learn.html", "5.2 Scikit-Learn'e Giriş")


def md_02() -> dict[int, str]:
    en = "https://jakevdp.github.io/PythonDataScienceHandbook/05.02-introducing-scikit-learn.html"
    return {
        0: f"""<h1>Scikit-Learn'e Giriş</h1>

    <p><em>Orijinal: <a href="{en}" target="_blank" rel="noopener">05.02 Introducing Scikit-Learn</a></em></p>
""",
        1: """    <p>Bir dizi makine öğrenmesi algoritmasının sağlam uygulamalarını sunan birkaç Python kütüphanesi vardır.
    En bilinenlerinden biri, yaygın algoritmaların çoğunun verimli sürümlerini sağlayan <a href="http://scikit-learn.org" target="_blank" rel="noopener">Scikit-Learn</a>'dir.
    Scikit-Learn temiz, tutarlı ve akıcı bir API ile çok yararlı ve eksiksiz çevrimiçi dokümantasyonla öne çıkar.
    Bu tutarlılığın yararı, bir model türü için Scikit-Learn'ün temel kullanımını ve sözdizimini anladığınızda yeni bir modele veya algoritmaya geçmenin kolay olmasıdır.</p>

    <p>Bu bölüm Scikit-Learn API'sine genel bir bakış sunar. Bu API öğelerinin sağlam anlayışı, sonraki bölümlerdeki makine öğrenmesi algoritmalarının ve yaklaşımlarının daha uygulamalı tartışmasının temelini oluşturur.</p>

    <p>Scikit-Learn'de veri temsilinden başlayacak, Estimator API'sine inecek ve son olarak el yazısı rakam görüntüleri kümesini keşfetmek için bu araçları kullanan daha ilginç bir örneğe geçeceğiz.</p>
""",
        2: """    <h2 id="veri-temsili">Scikit-Learn'de Veri Temsili</h2>
""",
        3: """    <p>Makine öğrenmesi veriden model oluşturmaktır; bu yüzden verinin nasıl temsil edilebileceğini tartışarak başlayacağız.
    Scikit-Learn içinde veriyi düşünmenin en iyi yolu <em>tablolar</em> üzerinden yapılır.</p>
""",
        4: """    <p>Temel bir tablo, satırların veri kümesindeki tek tek öğeleri, sütunların ise bu öğelerle ilişkili nicelikleri temsil ettiği iki boyutlu bir veri ızgarasıdır.
    Örneğin 1936'da Ronald Fisher tarafından ünlü biçimde analiz edilen <a href="https://en.wikipedia.org/wiki/Iris_flower_data_set" target="_blank" rel="noopener">Iris veri kümesini</a> düşünün.
    Bu veri kümesini <a href="http://seaborn.pydata.org/" target="_blank" rel="noopener">Seaborn</a> kütüphanesiyle Pandas <code>DataFrame</code> olarak indirip ilk birkaç satıra bakabiliriz:</p>
""",
        6: """    <p>Burada her satır tek bir gözlemlenen çiçeği ifade eder; satır sayısı veri kümesindeki toplam çiçek sayısıdır.
    Genelde matrisin satırlarına <em>örnek</em> (<code>samples</code>), satır sayısına <code>n_samples</code> deriz.</p>

    <p>Benzer şekilde her sütun, her örneği tanımlayan belirli bir nicel bilgi parçasıdır.
    Genelde sütunlara <em>öznitelik</em> (<code>features</code>), sütun sayısına <code>n_features</code> deriz.</p>
""",
        7: """    <h3 id="ozellik-matrisi">Öznitelik Matrisi</h3>

    <p>Tablo düzeni, bilginin iki boyutlu sayısal dizi veya matris olarak düşünülebileceğini gösterir; buna <em>öznitelik matrisi</em> (<code>features matrix</code>) deriz.
    Gelenek gereği bu matris çoğu zaman <code>X</code> adlı değişkende tutulur.
    Öznitelik matrisi iki boyutlu, <code>[n_samples, n_features]</code> şeklinde varsayılır ve çoğunlukla NumPy dizisi veya Pandas <code>DataFrame</code> içinde bulunur; bazı Scikit-Learn modelleri SciPy seyrek matrislerini de kabul eder.</p>

    <p>Örnekler (satırlar) her zaman veri kümesinde tanımlanan tek tek nesnelere karşılık gelir: bir çiçek, kişi, belge, görüntü, ses dosyası, video, astronomik cisim veya nicel ölçümlerle tanımlayabileceğiniz başka herhangi bir şey.</p>

    <p>Öznitelikler (sütunlar) her örneği nicel olarak tanımlayan farklı gözlemlerdir. Öznitelikler çoğu zaman gerçek sayılıdır; bazı durumlarda Boolean veya ayrık değerli olabilir.</p>
""",
        8: """    <h3 id="hedef-dizisi">Hedef Dizisi</h3>

    <p>Öznitelik matrisi <code>X</code>'e ek olarak genelde <em>etiket</em> veya <em>hedef</em> dizisiyle çalışırız; gelenek gereği bunu <code>y</code> adlandırırız.
    Hedef dizisi genelde <code>n_samples</code> uzunluğunda tek boyutludur ve çoğunlukla NumPy dizisi veya Pandas <code>Series</code> içinde bulunur.
    Hedef dizisi sürekli sayısal değerler veya ayrık sınıflar/etiketler içerebilir.
    Bazı Scikit-Learn tahmin edicileri <code>[n_samples, n_targets]</code> biçiminde çoklu hedefi desteklese de, çoğunlukla tek boyutlu hedef dizisiyle çalışacağız.</p>

    <p>Yaygın bir karışıklık, hedef dizisinin diğer öznitelik sütunlarından nasıl farklılaştığıdır. Hedef dizisinin ayırt edici özelliği, genelde özniteliklerden <em>tahmin etmek istediğimiz</em> nicelik olmasıdır; istatistikte bağımlı değişkendir.
    Önceki veride örneğin diğer ölçümlere dayanarak çiçek türünü tahmin edecek bir model kurmak isteyebiliriz; bu durumda <code>species</code> sütunu hedef dizisi sayılır.</p>

    <p>Bu hedef dizisiyle Seaborn'u (<a href="../04-matplotlib/14-visualization-with-seaborn.html">Seaborn ile Görselleştirme</a> bölümünde tartışıldı) kullanarak veriyi görselleştirebiliriz:</p>
""",
        10: """    <p>Scikit-Learn için öznitelik matrisi ve hedef dizisini <code>DataFrame</code>'den çıkaracağız; bunu <a href="../03-pandas/00-introduction.html">Bölüm 3</a>'teki Pandas <code>DataFrame</code> işlemleriyle yapabiliriz:</p>
""",
        13: """    <p>Özetle, öznitelik ve hedef değerlerinin beklenen düzeni aşağıdaki şekilde görselleştirilir.</p>
""",
        14: figure(
            "05.02-samples-features.png",
            "Scikit-Learn öznitelik matrisi X ve hedef dizisi y düzeni",
            "Kaynak: <a href=\"https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb#Features-and-Labels-Grid\" target=\"_blank\" rel=\"noopener\">Ek — Şekil kodu</a>",
        ),
        15: """    <p>Veri bu biçimde olduktan sonra Scikit-Learn'ün Estimator API'sine geçebiliriz.</p>
""",
        16: """    <h2 id="estimator-api">Estimator API</h2>
""",
        17: """    <p>Scikit-Learn API'si <a href="http://arxiv.org/abs/1309.0238" target="_blank" rel="noopener">Scikit-Learn API makalesinde</a> özetlenen şu ilkelere göre tasarlanmıştır:</p>

    <ul>
      <li><em>Tutarlılık</em>: Tüm nesneler sınırlı bir yöntem kümesinden türetilen ortak bir arayüzü paylaşır; dokümantasyon tutarlıdır.</li>
      <li><em>Denetlenebilirlik</em>: Belirtilen tüm parametre değerleri genel nitelikler olarak açıktır.</li>
      <li><em>Sınırlı nesne hiyerarşisi</em>: Yalnızca algoritmalar Python sınıflarıyla temsil edilir; veri kümeleri standart biçimlerde (NumPy, Pandas, SciPy seyrek) temsil edilir; parametre adları standart Python dizeleridir.</li>
      <li><em>Birleşim</em>: Birçok görev daha temel algoritmaların dizileri olarak ifade edilebilir; Scikit-Learn bunu mümkün olduğunca kullanır.</li>
      <li><em>Mantıklı varsayılanlar</em>: Kullanıcı parametresi gerektiğinde kütüphane uygun bir varsayılan tanımlar.</li>
    </ul>

    <p>Pratikte bu ilkeler, temel ilkeler anlaşıldıktan sonra Scikit-Learn'ü çok kullanışlı kılar.
    Scikit-Learn'deki her makine öğrenmesi algoritması, geniş uygulama yelpazesi için tutarlı bir arayüz sunan Estimator API ile uygulanır.</p>
""",
        18: """    <h3 id="api-temelleri">API'nin Temelleri</h3>

    <p>En yaygın olarak Scikit-Learn Estimator API kullanım adımları şöyledir:</p>

    <ol>
      <li>Scikit-Learn'den uygun tahmin edici sınıfını içe aktararak bir model sınıfı seçin.</li>
      <li>Bu sınıfı istenen değerlerle örnekleyerek model hiperparametrelerini seçin.</li>
      <li>Veriyi bu bölümün başında anlatıldığı gibi öznitelik matrisi ve hedef vektörüne düzenleyin.</li>
      <li>Model örneğinin <code>fit</code> yöntemini çağırarak modeli veriye uydurun.</li>
      <li>Modeli yeni veriye uygulayın:
        <ul>
          <li>Denetimli öğrenmede genelde <code>predict</code> ile bilinmeyen veri için etiket tahmin edilir.</li>
          <li>Denetimsiz öğrenmede genelde <code>transform</code> veya <code>predict</code> ile veri dönüştürülür veya özellikleri çıkarılır.</li>
        </ul>
      </li>
    </ol>

    <p>Şimdi denetimli ve denetimsiz öğrenme yöntemlerinin birkaç basit uygulama örneğine geçeceğiz.</p>
""",
        19: """    <h3 id="denetimli-dogrusal-regresyon">Denetimli Öğrenme Örneği: Basit Doğrusal Regresyon</h3>

    <p>Bu sürecin örneği olarak basit doğrusal regresyona — yani $(x, y)$ verisine doğru sığdırma durumuna — bakalım.
    Regresyon örneğimiz için aşağıdaki basit veriyi kullanacağız:</p>
""",
        21: """    <p>Veri hazır olduktan sonra daha önce özetlenen tarifi kullanabiliriz. Süreci adım adım izleyelim:</p>
""",
        22: """    <h4 id="adim-1-model-sinifi">1. Model sınıfını seçin</h4>

    <p>Scikit-Learn'de her model sınıfı bir Python sınıfıyla temsil edilir.
    Örneğin basit bir <code>LinearRegression</code> modeli hesaplamak için doğrusal regresyon sınıfını içe aktarabiliriz:</p>
""",
        24: """    <p>Daha genel doğrusal regresyon modelleri de vardır; ayrıntılar için <a href="http://scikit-learn.org/stable/modules/linear_model.html" target="_blank" rel="noopener"><code>sklearn.linear_model</code> modül dokümantasyonuna</a> bakın.</p>
""",
        25: """    <h4 id="adim-2-hiperparametreler">2. Model hiperparametrelerini seçin</h4>

    <p>Önemli bir nokta: <em>model sınıfı, model örneğiyle aynı şey değildir</em>.</p>

    <p>Model sınıfına karar verdikten sonra hâlâ seçeneklerimiz vardır. Kullandığımız modele göre şu sorulardan bir veya birkaçına yanıt vermemiz gerekebilir:</p>

    <ul>
      <li>Ofseti (<em>y</em>-kesişini) sığdırmak istiyor muyuz?</li>
      <li>Model normalize edilsin mi?</li>
      <li>Öznitelikleri ön işleyerek model esnekliği artsın mı?</li>
      <li>Ne düzeyde düzenlileştirme (regularization) kullanılsın?</li>
      <li>Kaç model bileşeni kullanılsın?</li>
    </ul>

    <p>Bunlar model sınıfı seçildikten <em>sonra</em> verilmesi gereken önemli seçimlerdir.
    Bu seçimler genelde <em>hiperparametre</em> olarak adlandırılır; model veriye uydurulmadan önce ayarlanır.
    Scikit-Learn'de hiperparametreler model örneği oluşturulurken verilir.
    Hiperparametreleri nicel seçmeyi <a href="03-hyperparameters-and-model-validation.html">Hiperparametreler ve Model Doğrulama</a> bölümünde ele alacağız.</p>

    <p>Doğrusal regresyon örneğinde <code>fit_intercept</code> hiperparametresiyle kesişimi sığdırmak istediğimizi belirterek <code>LinearRegression</code> örneği oluşturabiliriz:</p>
""",
        27: """    <p>Model örneklendiğinde yalnızca hiperparametre değerlerinin saklandığını unutmayın.
    Özellikle model henüz hiçbir veriye uygulanmamıştır: Scikit-Learn API, <em>model seçimi</em> ile <em>modelin veriye uygulanması</em> arasındaki ayrımı çok net yapar.</p>
""",
        28: """    <h4 id="adim-3-x-y">3. Veriyi öznitelik matrisi ve hedef vektörüne düzenleyin</h4>

    <p>Daha önce Scikit-Learn veri temsilini inceledik; iki boyutlu öznitelik matrisi ve tek boyutlu hedef dizisi gerekir.
    Burada hedef <code>y</code> zaten doğru biçimdedir (<code>n_samples</code> uzunluğunda dizi); <code>x</code> verisini <code>[n_samples, n_features]</code> boyutuna getirmemiz gerekir.
    Bu durumda tek boyutlu diziyi yeniden şekillendirmek yeterlidir:</p>
""",
        30: """    <h4 id="adim-4-fit">4. Modeli veriye uydurun</h4>

    <p>Şimdi modeli veriye uygulama zamanı. Bunu modelin <code>fit</code> yöntemiyle yaparız:</p>
""",
        32: """    <p>Bu <code>fit</code> komutu modele bağlı bir dizi iç hesaplama tetikler; sonuçlar kullanıcının inceleyebileceği, sondaki alt çizgiyle biten model özniteliklerinde saklanır.
    Scikit-Learn'de gelenek gereği <code>fit</code> sırasında öğrenilen tüm model parametreleri sondaki alt çizgiyle biter; bu doğrusal modelde örneğin:</p>
""",
        35: """    <p>Bu iki parametre veriye basit doğrusal uyumun eğim ve kesişimini temsil eder.
    Sonuçları veri tanımıyla karşılaştırırsak, veriyi üretmek için kullanılan değerlere (eğim 2, kesişim –1) yakın olduklarını görürüz.</p>

    <p>İç model parametrelerindeki belirsizlik sıkça sorulur.
    Genel olarak Scikit-Learn, iç parametrelerden doğrudan çıkarım araçları sunmaz: parametre yorumu daha çok <em>istatistiksel modelleme</em> sorusudur; makine öğrenmesi modelin <em>ne tahmin ettiğine</em> odaklanır.
    Uyum parametrelerinin anlamına inmek isterseniz <a href="http://statsmodels.sourceforge.net/" target="_blank" rel="noopener"><code>statsmodels</code></a> gibi başka araçlar vardır.</p>
""",
        36: """    <h4 id="adim-5-predict">5. Bilinmeyen veri için etiket tahmin edin</h4>

    <p>Model eğitildikten sonra denetimli makine öğrenmesinin ana görevi, eğitim kümesinin parçası olmayan yeni veri hakkında ne söylediğine göre değerlendirmektir.
    Scikit-Learn'de bunu <code>predict</code> yöntemiyle yaparız.
    Bu örnekte \"yeni veri\" bir <em>x</em> değerleri ızgarasıdır; modelin hangi <em>y</em> değerlerini tahmin ettiğini sorarız:</p>
""",
        38: """    <p>Daha önce olduğu gibi bu <em>x</em> değerlerini <code>[n_samples, n_features]</code> öznitelik matrisine dönüştürmemiz, ardından modele vermemiz gerekir:</p>
""",
        40: """    <p>Son olarak ham veriyi ve model uyumunu çizerek sonuçları görselleştirelim:</p>
""",
        42: """    <p>Genelde modelin etkinliği, sonuçların bilinen bir tem çizgisiyle karşılaştırılmasıyla değerlendirilir; bunu sonraki örnekte göreceğiz.</p>
""",
        43: """    <h3 id="iris-siniflandirma">Denetimli Öğrenme Örneği: Iris Sınıflandırması</h3>

    <p>Daha önce tartıştığımız Iris veri kümesiyle sürecin başka bir örneğine bakalım.
    Sorumuz: Iris verisinin bir bölümüyle eğitilen model, kalan etiketleri ne kadar iyi tahmin eder?</p>

    <p>Bu görev için her sınıfın eksen hizalı bir Gauss dağılımından çekildiğini varsayan <em>Gauss naive Bayes</em> üretici modelini kullanacağız (ayrıntılar: <a href="05-naive-bayes.html">Derinlemesine: Naive Bayes</a>).
    Hızlı olduğu ve seçilecek hiperparametre olmadığı için Gauss naive Bayes sıkça temel sınıflandırma modeli olarak kullanılır.</p>

    <p>Modeli görmediği veride değerlendirmek istiyoruz; veriyi <em>eğitim</em> ve <em>test</em> kümelerine ayırırız.
    Elle yapılabilir; <code>train_test_split</code> yardımcı işlevi daha uygundur:</p>
""",
        45: """    <p>Veri düzenlendikten sonra etiketleri tahmin etmek için tarifimizi uygularız:</p>
""",
        47: """    <p>Son olarak tahmin edilen etiketlerin gerçek değerlerle eşleşme oranını görmek için <code>accuracy_score</code> yardımcısını kullanırız:</p>
""",
        49: """    <p>%97'nin üzerinde doğrulukla, bu çok basit sınıflandırma algoritmasının bile bu veri kümesi için etkili olduğunu görüyoruz!</p>
""",
        50: """    <h3 id="iris-boyut-indirgeme">Denetimsiz Öğrenme Örneği: Iris Boyut İndirgeme</h3>

    <p>Denetimsiz öğrenme örneği olarak Iris verisinin boyutunu indirerek görselleştirmeyi kolaylaştıralım.
    Iris verisi dört boyutludur: her örnek için dört öznitelik kaydedilmiştir.</p>

    <p>Boyut indirgeme görevi, verinin temel özniteliklerini koruyan uygun daha düşük boyutlu bir temsil olup olmadığını belirlemeye odaklanır.
    Sıkça görselleştirme yardımcısı olarak kullanılır: dört boyutta çizmek, iki veya üç boyutta çizmekten çok daha zordur!</p>

    <p>Burada hızlı doğrusal boyut indirgeme tekniği <em>temel bileşen analizi</em> (PCA; <a href="09-principal-component-analysis.html">Derinlemesine: PCA</a>) kullanacağız.
    Modele iki bileşen — yani verinin iki boyutlu temsili — döndürmesini isteyeceğiz.</p>

    <p>Daha önce özetlenen adım dizisini izleyerek:</p>
""",
        52: """    <p>Şimdi sonuçları çizelim. Hızlı bir yol, sonuçları orijinal Iris <code>DataFrame</code>'ine ekleyip Seaborn <code>lmplot</code> ile göstermektir:</p>
""",
        54: """    <p>İki boyutlu temsilde türler oldukça iyi ayrılmış; PCA algoritması tür etiketlerini bilmiyordu!
    Bu, veri kümesinde nispeten basit bir sınıflandırmanın etkili olacağını — daha önce gördüğümüz gibi — düşündürür.</p>
""",
        55: """    <h3 id="iris-kumeleme">Denetimsiz Öğrenme Örneği: Iris Kümeleme</h3>

    <p>Şimdi Iris verisine kümeleme uygulayalım.
    Kümeleme algoritması herhangi bir etikete başvurmadan verinin belirgin gruplarını bulmaya çalışır.
    Burada <a href="12-gaussian-mixtures.html">Derinlemesine: Gauss Karışımları</a> bölümünde ayrıntılı ele alınan <em>Gauss karışım modeli</em> (GMM) kullanacağız.
    GMM veriyi Gauss \"lekeleri\" koleksiyonu olarak modellemeye çalışır.</p>

    <p>Gauss karışım modelini şöyle uydurabiliriz:</p>
""",
        57: """    <p>Yine küme etiketini Iris <code>DataFrame</code>'ine ekleyip Seaborn ile çizeceğiz:</p>
""",
        59: """    <p>Veriyi küme numarasına göre ayırınca GMM algoritmasının alt etiketleri ne kadar iyi kurtardığını görürüz: <em>setosa</em> türü küme 0 içinde mükemmel ayrılmış; <em>versicolor</em> ile <em>virginica</em> arasında küçük bir karışma var.
    Yani uzman olmadan bile çiçek ölçümleri, farklı tür gruplarının varlığını basit bir kümeleme algoritmasıyla <em>otomatik</em> tanımlamaya yeterince ayırt edicidir!
    Bu tür algoritma, alandaki uzmanlara örnekler arasındaki ilişkilere ipucu verebilir.</p>
""",
        60: """    <h2 id="el-yazisi-rakamlar">Uygulama: El Yazısı Rakamları</h2>
""",
        61: """    <p>Bu ilkeleri daha ilginç bir problemde göstermek için optik karakter tanımanın bir parçasına bakalım: el yazısı rakamların tanınması.
    Gerçek dünyada bu hem görüntüde karakterleri bulmayı hem tanımayı içerir. Burada kısayol kullanıp Scikit-Learn'ün kütüphaneye gömülü önceden biçimlendirilmiş rakam kümesini kullanacağız.</p>
""",
        62: """    <h3 id="rakamlari-yukleme">Rakam Verisini Yükleme ve Görselleştirme</h3>

    <p>Scikit-Learn'ün veri erişim arayüzüyle bu veriye bakabiliriz:</p>
""",
        64: """    <p>Görüntü verisi üç boyutlu bir dizidir: 1.797 örnek, her biri 8×8 piksel ızgara.
    İlk yüz tanesini görselleştirelim:</p>
""",
        66: """    <p>Scikit-Learn ile çalışmak için iki boyutlu <code>[n_samples, n_features]</code> temsil gerekir.
    Her pikseli bir öznitelik sayarak piksel dizilerini düzleştirerek uzunluk 64 piksel değeri dizisi elde ederiz.
    Ayrıca her rakam için önceden belirlenmiş etiketi veren hedef dizisi gerekir; ikisi de <code>data</code> ve <code>target</code> özniteliklerinde bulunur:</p>
""",
        69: """    <p>1.797 örnek ve 64 öznitelik görüyoruz.</p>
""",
        70: """    <h3 id="rakam-boyut-indirgeme">Denetimsiz Öğrenme Örneği: Boyut İndirgeme</h3>

    <p>64 boyutlu parametre uzayında noktalarımızı görselleştirmek isteriz; bu kadar yüksek boyutta etkili görselleştirme zordur.
    Bunun yerine boyutu denetimsiz bir yöntemle indireceğiz.
    Burada <a href="10-manifold-learning.html">Derinlemesine: Manifold Öğrenme</a> bölümündeki Isomap manifold öğrenme algoritmasını kullanıp veriyi iki boyuta dönüştüreceğiz:</p>
""",
        72: """    <p>Yansıtılan veri artık iki boyutlu. Yapıdan bir şey öğrenip öğrenemeyeceğimizi görmek için çizelim:</p>
""",
        74: """    <p>Bu çizim, 64 boyutlu uzayda çeşitli rakamların ne kadar ayrıldığına dair iyi bir sezgi verir.
    Örneğin sıfır ve bir parametre uzayında çok az örtüşür; sezgisel olarak mantıklıdır: sıfır görüntü ortasında boştur, bir genelde ortada mürekkep vardır.
    Öte yandan birler ile dörtler arasında sürekli bir spektrum vardır: bazıları \"şapkalı\" bir çizer; bu da dörtlere benzetir.</p>

    <p>Genel olarak kenarlarda bir miktar karışma olsa da farklı gruplar parametre uzayında oldukça yerelleşmiş görünür; bu da tam yüksek boyutlu veri kümesinde bile basit bir denetimli sınıflandırmanın uygun performans gösterebileceğini düşündürür.
    Deneyelim.</p>
""",
        75: """    <h3 id="rakam-siniflandirma">Rakamlarda Sınıflandırma</h3>

    <p>Rakam verisine bir sınıflandırma algoritması uygulayalım.
    Iris'te yaptığımız gibi veriyi eğitim ve test kümelerine ayırıp Gauss naive Bayes modeli uyduracağız:</p>
""",
        78: """    <p>Modelin tahminleri elimizde; doğruluğu test kümesinin gerçek değerleriyle karşılaştırarak ölçeriz:</p>
""",
        80: """    <p>Bu çok basit modelle bile rakam sınıflandırmasında yaklaşık %83 doğruluk buluyoruz!
    Ancak tek bir sayı nerede hata yaptığımızı söylemez. Bunun güzel bir yolu <em>karmaşıklık matrisi</em>dir; Scikit-Learn ile hesaplayıp Seaborn ile çizebiliriz:</p>
""",
        82: """    <p>Bu, yanlış etiketlenen noktaların nerede yoğunlaştığını gösterir: örneğin burada birçok iki, bir veya sekiz olarak yanlış sınıflandırılmış.</p>

    <p>Modelin özelliklerine dair sezgi için girdileri tahmin edilen etiketlerle yeniden çizebiliriz.
    Doğru etiketler yeşil, yanlışlar kırmızı olacak:</p>
""",
        84: """    <p>Veri alt kümesini incelemek, algoritmanın nerede optimal olmayabileceğine dair ipucu verir.
    %83 sınıflandırma başarısının ötesine geçmek için destek vektör makineleri (<a href="07-support-vector-machines.html">Derinlemesine: SVM</a>), rastgele ormanlar (<a href="08-random-forests.html">Derinlemesine: Karar Ağaçları ve Rastgele Ormanlar</a>) veya başka bir sınıflandırma yaklaşımına geçebiliriz.</p>
""",
        85: """    <h2 id="ozet-02">Özet</h2>
""",
        86: """    <p>Bu bölümde Scikit-Learn veri temsilinin ve Estimator API'sinin temel özelliklerini ele aldık.
    Kullanılan tahmin edici türünden bağımsız olarak aynı içe aktar/örnekle/uydur/tahmin et kalıbı geçerlidir.
    Estimator API hakkında bu bilgiyle Scikit-Learn dokümantasyonunu keşfedebilir ve çeşitli modelleri verinizde denemeye başlayabilirsiniz.</p>

    <p>Sonraki bölümde makine öğrenmesinde belki en önemli konuya geçeceğiz: modelinizi nasıl seçip doğrulayacağınız.</p>
""",
    }


def body_02() -> str:
    md = md_02()
    core = render_nb("05.02-Introducing-Scikit-Learn.ipynb", md, CODE_NAMES_02)

    extras = (
        addon(
            "fit / predict / transform",
            """<p>Scikit-Learn tahmin edicilerinde ortak kalıp: <code>model.fit(X, y)</code> (denetimli) veya <code>model.fit(X)</code> (denetimsiz);
            <code>model.predict(X)</code> sınıflandırma/regresyon tahmini;
            <code>model.transform(X)</code> boyut indirgeme ve ön işleme için dönüşüm.
            Bu sayfa <strong>Pyodide ile scikit-learn önceden yüklenir</strong> (<code>data-preload-sklearn</code>); ilk çalıştırmada paket indirme süresi olabilir.</p>""",
        )
        + "\n"
        + addon(
            "X ve y şekilleri",
            """<p><code>X</code> her zaman <code>(n_samples, n_features)</code>, <code>y</code> tek boyutlu <code>(n_samples,)</code> olmalıdır.
            Tek öznitelikli regresyonda <code>x[:, np.newaxis]</code> ile sütun vektörüne çevirmeyi unutmayın.</p>""",
        )
        + "\n"
        + try_it(
            "Iris X ve y oluşturun",
            "Seaborn Iris veri kümesinden öznitelik matrisi ve hedef dizisi çıkarın:",
            """import seaborn as sns
iris = sns.load_dataset('iris')
X = iris.drop('species', axis=1)
y = iris['species']
print(X.shape, y.shape)""",
            "iris_X_y.py",
        )
        + "\n"
        + try_it(
            "Basit doğrusal regresyon",
            "Rastgele 1D veriye <code>LinearRegression</code> uydurup eğimi yazdırın:",
            """import numpy as np
from sklearn.linear_model import LinearRegression
rng = np.random.RandomState(0)
x = rng.rand(20)
y = 2 * x + 1 + 0.1 * rng.randn(20)
X = x[:, np.newaxis]
m = LinearRegression().fit(X, y)
print("coef_:", m.coef_, "intercept_:", m.intercept_)""",
            "quick_linear_regression.py",
        )
        + "\n"
        + next_link("03-hyperparameters-and-model-validation.html", "5.3 Hiperparametreler ve Model Doğrulama")
    )
    return core + "\n" + extras


def main() -> None:
    specs = [
        ("00-introduction", body_00, "05.00-Machine-Learning.ipynb"),
        ("01-what-is-machine-learning", body_01, "05.01-What-Is-Machine-Learning.ipynb"),
        ("02-introducing-scikit-learn", body_02, "05.02-Introducing-Scikit-Learn.ipynb"),
    ]
    for slug, fn, nb in specs:
        path = write_slug(slug, fn())
        n = count_cells(nb)
        print(f"wrote {path.relative_to(ROOT)} ({n} notebook cells)")


if __name__ == "__main__":
    main()
