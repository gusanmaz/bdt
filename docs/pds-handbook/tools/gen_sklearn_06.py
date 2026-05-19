#!/usr/bin/env python3
"""Generate 06-linear-regression.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from gen_sklearn_00_02 import code_block, cell_code, img_from_md, load_nb, write_slug

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html"
FIG = "https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb"

TR = {
    0: f"""<h1>5.6 Derinlemesine: Doğrusal Regresyon</h1>

    <p><em>Orijinal: <a href="{EN}" target="_blank" rel="noopener">05.06 Linear Regression</a></em></p>""",
    1: """    <p><a href="05-naive-bayes.html">Derinlemesine: Naive Bayes Sınıflandırması</a> bölümünde tartışıldığı gibi naive Bayes sınıflandırma görevleri için iyi bir başlangıç noktasıysa, doğrusal regresyon modelleri regresyon görevleri için iyi bir başlangıç noktasıdır.
    Bu modeller hızlı uydurulabildiği ve yorumlanması kolay olduğu için popülerdir.
    En basit doğrusal regresyon modeline (iki boyutlu veriye düz çizgi uydurma) zaten aşinasınız; ancak bu modeller daha karmaşık veri davranışını modellemek için genişletilebilir.</p>
    <p>Bu bölümde bu iyi bilinen problemin matematiğine kısa bir bakıştan başlayıp doğrusal modellerin daha karmaşık örüntüleri nasıl hesaba katacak şekilde genellenebileceğini göreceğiz.</p>
    <p>Standart içe aktarmalarla başlayalım:</p>""",
    3: """    <h2 id="basit-dogrusal-regresyon">Basit Doğrusal Regresyon</h2>
    <p>En tanıdık doğrusal regresyonla, veriye düz çizgi uydurmayla başlayacağız.
    Düz çizgi uyumu şu biçimde bir modeldir: $$y = ax + b$$
    Burada $a$ genelde <em>eğim</em>, $b$ genelde <em>kesişim</em> (intercept) olarak bilinir.</p>
    <p>Eğimi 2, kesişimi −5 olan bir doğru etrafında dağılmış aşağıdaki veriyi düşünün (aşağıdaki şekil):</p>""",
    5: """    <p>Scikit-Learn'ün <code>LinearRegression</code> tahmin edicisiyle bu veriye uyum yapıp en iyi uyum doğrusunu oluşturabiliriz (aşağıdaki şekil):</p>""",
    7: """    <p>Verinin eğim ve kesişimi modelin uyum parametrelerinde saklanır; Scikit-Learn'de bunlar her zaman sondaki alt çizgiyle işaretlenir.
    İlgili parametreler <code>coef_</code> ve <code>intercept_</code>:</p>""",
    9: """    <p>Sonuçların veriyi üretmek için kullanılan değerlere (eğim 2, kesişim −1) çok yakın olduğunu görüyoruz; umarız beklediğimiz gibidir.</p>""",
    10: """    <p><code>LinearRegression</code> tahmin edicisi bundan çok daha yeteneklidir — basit düz çizgi uyumlarına ek olarak çok boyutlu doğrusal modelleri de işleyebilir:
    $$y = a_0 + a_1 x_1 + a_2 x_2 + \\cdots$$
    Birden fazla $x$ değeri vardır.
    Geometrik olarak bu, üç boyutta düzleme veya daha yüksek boyutlarda hiperdüzleme nokta uydurmaya benzer.</p>
    <p>Çok boyutlu regresyonlar görselleştirmeyi zorlaştırır; ancak NumPy'nin matris çarpım operatörüyle örnek veri oluşturarak böyle bir uydurmayı görebiliriz:</p>""",
    12: """    <p>Burada $y$ verisi üç rastgele $x$ değerinin doğrusal birleşiminden oluşturulmuş; doğrusal regresyon veriyi oluşturmak için kullanılan katsayıları geri kazanmıştır.</p>
    <p>Bu şekilde tek bir <code>LinearRegression</code> tahmin edicisiyle verimize doğru, düzlem veya hiperdüzlem uydurabiliriz.
    Bu yaklaşım değişkenler arasında yalnızca doğrusal ilişkilere sınırlı gibi görünse de bunu da gevşetebiliriz.</p>""",
    13: """    <h2 id="temel-fonksiyon-regresyonu">Temel Fonksiyon Regresyonu</h2>
    <p>Doğrusal regresyonu değişkenler arasındaki doğrusal olmayan ilişkilere uyarlamak için kullanabileceğiniz bir numara, veriyi <em>temel fonksiyonlara</em> (basis functions) göre dönüştürmektir.
    <a href="03-hyperparameters-and-model-validation.html">Hiperparametreler ve Model Doğrulama</a> ve <a href="04-feature-engineering.html">Öznitelik Mühendisliği</a> bölümlerinde kullanılan <code>PolynomialRegression</code> pipeline'ında bunun bir sürümünü görmüştük.
    Fikir, çok boyutlu doğrusal modelimizi almak:
    $$y = a_0 + a_1 x_1 + a_2 x_2 + a_3 x_3 + \\cdots$$
    ve tek boyutlu girdimiz $x$'ten $x_1, x_2, x_3$ vb. oluşturmaktır; yani $x_n = f_n(x)$, burada $f_n()$ verimizi dönüştüren bir fonksiyondur.</p>
    <p>Örneğin $f_n(x) = x^n$ ise model polinom regresyona dönüşür:
    $$y = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \\cdots$$
    Bu hâlâ <em>doğrusal bir modeldir</em> — doğrusallık katsayıların $a_n$ birbirleriyle çarpılmaması veya bölünmemesi anlamına gelir.
    Etkili olarak tek boyutlu $x$ değerlerimizi daha yüksek boyuta yansıttık; böylece doğrusal uyum $x$ ile $y$ arasındaki daha karmaşık ilişkileri yakalayabilir.</p>""",
    14: """    <h3 id="polinom-temel">Polinom Temel Fonksiyonları</h3>
    <p>Bu polinom projeksiyonu yeterince yararlıdır ki Scikit-Learn'e <code>PolynomialFeatures</code> dönüştürücüsüyle gömülüdür:</p>""",
    16: """    <p>Dönüştürücü tek boyutlu dizimizi her sütunda üssü alınmış değeri içeren üç boyutlu bir diziye çevirmiştir.
    Bu yeni, daha yüksek boyutlu temsil doğrusal regresyona takılabilir.</p>
    <p><a href="04-feature-engineering.html">Öznitelik Mühendisliği</a> bölümünde gördüğümüz gibi bunu yapmanın en temiz yolu pipeline kullanmaktır.
    Bu şekilde 7. derece polinom modeli oluşturalım:</p>""",
    18: """    <p>Bu dönüşümle doğrusal model $x$ ile $y$ arasındaki çok daha karmaşık ilişkileri uydurabilir.
    Örneğin gürültülü bir sinüs dalgası (aşağıdaki şekil):</p>""",
    20: """    <p>Yedinci derece polinom temel fonksiyonları kullanan doğrusal modelimiz bu doğrusal olmayan veriye mükemmel bir uyum sağlayabilir!</p>""",
    21: """    <h3 id="gauss-temel">Gauss Temel Fonksiyonları</h3>
    <p>Elbette başka temel fonksiyonlar da mümkündür.
    Yararlı bir örüntü, polinom tabanlarının toplamı değil Gauss tabanlarının toplamını uyduran bir modeldir.
    Sonuç kabaca aşağıdaki şekildeki gibi görünebilir:</p>""",
    22: figure("05.06-gaussian-basis.png", "Gauss temel fonksiyonları", f'Kaynak: <a href="{FIG}" target="_blank" rel="noopener">Ek — Şekil kodu</a>'),
    23: """    <p>Grafikteki gölgeli bölgeler ölçeklenmiş temel fonksiyonlardır; toplandığında veriden geçen düzgün eğriyi oluştururlar.
    Bu Gauss temel fonksiyonları Scikit-Learn'e gömülü değildir; ancak bunları oluşturan özel bir dönüştürücü yazabiliriz (Scikit-Learn dönüştürücüleri Python sınıfları olarak uygulanır; kaynak kodunu okumak nasıl oluşturulacağını görmek için iyi bir yoldur):</p>""",
    25: """    <p>Bu örneği yalnızca polinom temel fonksiyonlarında sihir olmadığını netleştirmek için ekledim: verinizin üretim sürecine dair sezginiz bir temelin diğerinden daha uygun olduğunu düşündürüyorsa onu kullanabilirsiniz.</p>""",
    26: """    <h2 id="duzenlilestirme">Düzenlileştirme</h2>
    <p>Doğrusal regresyona temel fonksiyonları eklemek modeli çok daha esnek yapar; ancak çok hızlı aşırı uyuma yol açabilir (<a href="03-hyperparameters-and-model-validation.html">Hiperparametreler ve Model Doğrulama</a> bölümüne bakın).
    Örneğin çok sayıda Gauss temel fonksiyonu kullanırsak aşağıdaki şekilde olur:</p>""",
    28: """    <p>Veri 30 boyutlu temele yansıtıldığında model fazla esnektir ve veriyle kısıtlandığı noktalar arasında aşırı değerlere gider.
    Bunun nedenini Gauss temellerinin katsayılarını konumlarına göre çizersek görebiliriz (aşağıdaki şekil):</p>""",
    30: """    <p>Bu şeklin alt paneli her konumdaki temel fonksiyonun genliğini gösterir.
    Temel fonksiyonlar örtüştüğünde tipik aşırı uyum davranışı budur: bitişik temellerin katsayıları şişer ve birbirini iptal eder.
    Bu davranışın sorunlu olduğunu biliyoruz; model parametrelerinin büyük değerlerini cezalandırarak bu sıçramaları açıkça sınırlamak güzel olurdu.
    Böyle bir ceza <em>düzenlileştirme</em> (regularization) olarak bilinir; birkaç biçimi vardır.</p>""",
    31: """    <h3 id="ridge">Ridge Regresyon ($L_2$ Düzenlileştirme)</h3>
    <p>Belki en yaygın düzenlileştirme biçimi <em>ridge regresyon</em> veya $L_2$ <em>düzenlileştirme</em> (bazen <em>Tikhonov düzenlileştirme</em>) olarak bilinir.
    Model katsayıları $\\theta_n$'nin kareler toplamını (2-norm) cezalandırır. Bu durumda uyum cezası:
    $$P = \\alpha\\sum_{n=1}^N \\theta_n^2$$
    $\\alpha$ cezanın gücünü kontrol eden serbest parametredir.
    Bu tür cezalı model Scikit-Learn'de <code>Ridge</code> tahmin edicisiyle gömülüdür (aşağıdaki şekil):</p>""",
    33: """    <p>$\\alpha$ parametresi esasen ortaya çıkan modelin karmaşıklığını kontrol eden bir düğmedir.
    $\\alpha \\to 0$ limitinde standart doğrusal regresyon sonucunu elde ederiz; $\\alpha \\to \\infty$ limitinde tüm model yanıtları baskılanır.
    Ridge regresyonun bir avantajı çok verimli hesaplanabilmesidir — neredeyse orijinal doğrusal regresyon maliyetinden fazla değildir.</p>""",
    34: """    <h3 id="lasso">Lasso Regresyon ($L_1$ Düzenlileştirme)</h3>
    <p>Bir başka yaygın düzenlileştirme <em>lasso regresyon</em> veya <em>L1 düzenlileştirme</em>dir; regresyon katsayılarının mutlak değerler toplamını (1-norm) cezalandırır:
    $$P = \\alpha\\sum_{n=1}^N |\\theta_n|$$
    Kavramsal olarak ridge'e çok benzer olsa da sonuçlar şaşırtıcı biçimde farklı olabilir. Örneğin yapısı nedeniyle lasso regresyon mümkün olduğunda <em>seyrek modelleri</em> tercih eder: birçok model katsayısını tam olarak sıfıra ayarlar.</p>
    <p>Önceki örneği L1-normalize katsayılarla tekrarlarsak bunu görebiliriz (aşağıdaki şekil):</p>""",
    36: """    <p>Lasso regresyon cezasıyla katsayıların çoğu tam olarak sıfırdır; işlevsel davranış mevcut temel fonksiyonların küçük bir alt kümesiyle modellenir.
    Ridge düzenlileştirmede olduğu gibi $\\alpha$ parametresi cezanın gücünü ayarlar ve örneğin çapraz doğrulama ile belirlenmelidir (<a href="03-hyperparameters-and-model-validation.html">Hiperparametreler ve Model Doğrulama</a> bölümüne bakın).</p>""",
    37: """    <h2 id="bisiklet-ornegi">Örnek: Bisiklet Trafiği Tahmini</h2>""",
    38: """    <p>Örnek olarak Seattle Fremont Köprüsü'nden geçen bisiklet yolculuk sayısını hava durumu, mevsim ve diğer faktörlere göre tahmin edip edemeyeceğimize bakalım.
    Bu veriyi <a href="../03-pandas/11-working-with-time-series.html">Zaman Serileri</a> bölümünde görmüştük; burada bisiklet verisini başka bir veri kümesiyle birleştirip hava durumu ve mevsimsel faktörlerin — sıcaklık, yağış ve gün ışığı süresi — bisiklet trafiğini ne ölçüde etkilediğini anlamaya çalışacağız.
    Neyse ki NOAA günlük <a href="http://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND" target="_blank" rel="noopener">hava istasyonu verisini</a> yayınlar — istasyon USW00024233 — ve Pandas ile iki kaynağı kolayca birleştirebiliriz.
    Hava ve diğer bilgileri bisiklet sayılarıyla ilişkilendirmek için basit doğrusal regresyon yapacağız; böylece bu parametrelerden birindeki değişimin belirli bir gündeki yolcu sayısını nasıl etkilediğini tahmin edebiliriz.</p>
    <p>Özellikle bu, Scikit-Learn araçlarının istatistiksel modelleme çerçevesinde kullanılabileceği bir örnektir; model parametrelerinin yorumlanabilir anlamları olduğu varsayılır.
    Daha önce tartışıldığı gibi bu makine öğrenmesi içinde standart bir yaklaşım değildir; ancak bazı modeller için böyle yorum mümkündür.</p>
    <p>İki veri kümesini tarihe göre indeksleyerek yükleyerek başlayalım:</p>""",
    41: """    <p>Basitlik için COVID-19 salgınının Seattle'daki ulaşım alışkanlıklarını önemli ölçüde etkilediği 2020 sonrası etkilerden kaçınmak için 2020 öncesi veriye bakalım:</p>""",
    43: """    <p>Ardından günlük toplam bisiklet trafiğini hesaplayıp kendi <code>DataFrame</code>'ine koyalım:</p>""",
    45: """    <p>Daha önce kullanım örüntülerinin günden güne değiştiğini görmüştük. Veriye haftanın gününü gösteren ikili sütunlar ekleyelim:</p>""",
    47: """    <p>Benzer şekilde tatillerde sürücülerin farklı davrandığını bekleyebiliriz; bunun için de bir gösterge ekleyelim:</p>""",
    49: """    <p>Gün ışığı süresinin kaç kişinin bisiklete bindiğini etkileyebileceğinden şüphelenebiliriz. Standart astronomik hesapla bu bilgiyi ekleyelim (aşağıdaki şekil):</p>""",
    51: """    <p>Ortalama sıcaklık ve toplam yağışı da ekleyebiliriz.
    Yağış inch cinsine ek olarak günün kuru olup olmadığını (sıfır yağış) gösteren bir bayrak ekleyelim:</p>""",
    53: """    <p>Son olarak 1. günden artan ve kaç yıl geçtiğini ölçen bir sayaç ekleyelim.
    Bu, gözlemlenen yıllık günlük geçiş artış veya azalışını ölçmemizi sağlar:</p>""",
    55: """    <p>Verimiz hazır; bir göz atalım:</p>""",
    57: """    <p>Bu hazır olduktan sonra kullanılacak sütunları seçip verimize doğrusal regresyon uydurabiliriz.
    <code>fit_intercept=False</code> ayarlayacağız çünkü günlük bayraklar esasen kendi gün özel kesişimleri gibi çalışır:</p>""",
    59: """    <p>Son olarak toplam ve tahmin edilen bisiklet trafiğini görsel olarak karşılaştırabiliriz (aşağıdaki şekil):</p>""",
    61: """    <p>Veri ile model tahminlerinin tam örtüşmemesinden bazı önemli öznitelikleri kaçırdığımız açıktır.
    Ya özniteliklerimiz eksiktir (insanlar yalnızca bunlara göre değil daha fazlasına göre karar verir) ya da hesaba katmadığımız doğrusal olmayan ilişkiler vardır (örneğin hem yüksek hem düşük sıcaklıkta daha az binme).
    Yine de kaba yaklaşımımız içgörü vermeye yeter; doğrusal modelin katsayılarına bakarak her özniteliğin günlük bisiklet sayısına ne kadar katkıda bulunduğunu tahmin edebiliriz:</p>""",
    63: """    <p>Bu sayıları belirsizlik ölçüsü olmadan yorumlamak zordur.
    Bootstrap yeniden örnekleme ile bu belirsizlikleri hızlıca hesaplayabiliriz:</p>""",
    65: """    <p>Bu hatalar tahmin edildikten sonra sonuçlara tekrar bakalım:</p>""",
    67: """    <p>Buradaki <code>effect</code> sütunu kabaca söz konusu öznitelikteki değişimin yolcu sayısını nasıl etkilediğini gösterir.
    Örneğin haftanın günü açık bir ayrım gösterir: hafta sonlarında hafta içine göre binlerce daha az yolcu vardır.
    Ek her gün ışığı saati başına 409 ± 26 kişinin bisikleti seçtiğini, bir Fahrenheit derece artışının 179 ± 7 kişiyi teşvik ettiğini, kuru günün ortalama 2.111 ± 101 ek yolcu, her inch yağmurun 2.790 ± 186 yolcuyu başka ulaşım moduna yönlendirdiğini görüyoruz.
    Tüm bu etkiler hesaba katıldığında yılda 324 ± 22 yeni günlük yolcu artışı görüyoruz.</p>
    <p>Basit modelimiz neredeyse kesinlikle ilgili bilgileri kaçırıyor. Örneğin daha önce belirtildiği gibi doğrusal olmayan etkiler (yağış <em>ve</em> soğuk sıcaklık etkileri) ve her değişken içindeki doğrusal olmayan eğilimler (çok soğuk ve çok sıcakta binme isteksizliği) basit doğrusal modelde hesaba katılamaz.
    Ayrıca daha ince ayrıntılı bilgiyi attık (yağmurlu sabah ile yağmurlu öğleden sonra farkı) ve günler arası korelasyonları yok saydık (yağmurlu salının çarşamba sayısına etkisi veya yağmurlu günlerden sonra beklenmedik güneşli gün).
    Bunların hepsi ilginç olası etkilerdir; artık keşfetmek için araçlara sahipsiniz!</p>""",
}

CODE_NAMES = {
    2: "imports_linreg.py",
    4: "simple_linreg_data.py",
    6: "linear_regression_fit.py",
    8: "model_coef_intercept.py",
    11: "multidim_linreg.py",
    15: "polynomial_features_demo.py",
    17: "poly_pipeline_7.py",
    19: "sine_noise_fit.py",
    24: "gaussian_features_class.py",
    27: "gaussian_overfit.py",
    29: "basis_plot_fn.py",
    32: "ridge_regression.py",
    35: "lasso_regression.py",
    39: "bike_counts_url.py",
    40: "load_bike_weather.py",
    42: "filter_pre2020.py",
    44: "daily_bike_total.py",
    46: "day_of_week_dummies.py",
    48: "holiday_flag.py",
    50: "hours_of_daylight.py",
    52: "weather_features.py",
    54: "annual_counter.py",
    56: "daily_head.py",
    58: "linear_model_bike.py",
    60: "bike_predict_plot.py",
    62: "model_coef_series.py",
    64: "bootstrap_errors.py",
    66: "effect_with_errors.py",
}

INSERTS = {
    9: addon("coef_ ve intercept_", "<p><code>model.coef_</code> çok boyutlu regresyonda vektör, <code>intercept_</code> skalerdir. Tek öznitelikte <code>coef_[0]</code> eğimdir.</p>"),
    33: try_it("", "Ridge ile polinom regresyonda aşırı uyumu azaltmayı deneyin:", """import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
rng = np.random.RandomState(0)
x = rng.rand(30)
y = np.sin(2 * np.pi * x) + 0.1 * rng.randn(30)
X = x[:, np.newaxis]
model = make_pipeline(PolynomialFeatures(10), Ridge(alpha=1e-3))
model.fit(X, y)
print("R^2:", model.score(X, y))""", "deneme_ridge_poly.py"),
    61: addon("fetch_openml / ağ", "Bisiklet verisi örnekte URL'den okunur; Pyodide'da ağ erişimi sınırlı olabilir. Tam örnek için yerel Jupyter notebook kullanın."),
}

if __name__ == "__main__":
    nb = load_nb("05.06-Linear-Regression.ipynb")
    parts = []
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            src = cell_code(cell)
            ro = src.lstrip().startswith("%")
            parts.append(code_block(src, CODE_NAMES.get(i, f"cell_{i:02d}.py"), readonly=ro))
        elif i in TR:
            parts.append(TR[i])
        else:
            raw = cell_code(cell)
            if img := img_from_md(raw):
                parts.append(figure(img, img.replace(".png", "")))
            else:
                raise ValueError(f"missing TR cell {i}")
        if i in INSERTS:
            parts.append(INSERTS[i])
    body = "\n".join(parts) + "\n" + next_link("07-support-vector-machines.html", "5.7 Destek Vektör Makineleri")
    path = write_slug("06-linear-regression", body)
    print("wrote", path)
