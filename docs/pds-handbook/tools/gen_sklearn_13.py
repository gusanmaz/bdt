#!/usr/bin/env python3
"""Generate 13-kernel-density-estimation.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, orig_line, p
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.13-kernel-density-estimation.html"
EN_LABEL = "05.13 Kernel Density Estimation"

TR = {
    0: h1("5.13 Derinlemesine: Çekirdek Yoğunluk Tahmini"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Önceki bölümde Gauss karışım modellerini ele aldık; bunlar kümeleme "
                "tahmincisi ile yoğunluk tahmincisinin bir tür hibritidir. "
                "Yoğunluk tahmincisinin, $D$ boyutlu bir veri kümesini alıp verinin "
                "çekildiği $D$ boyutlu olasılık dağılımının tahminini üreten bir "
                "algoritma olduğunu hatırlayın. GMM algoritması yoğunluğu Gauss "
                "dağılımlarının ağırlıklı toplamı olarak temsil eder. "
                "<em>Çekirdek yoğunluk tahmini</em> (KDE), Gauss karışımı fikrini "
                "mantıksal uç noktaya taşır: <em>her nokta için bir</em> Gauss "
                "bileşeninden oluşan bir karışım kullanır; sonuçta esasen "
                "parametrik olmayan bir yoğunluk tahmincisi elde edilir. "
                "Bu bölümde KDE'nin motivasyonunu ve kullanımlarını inceleyeceğiz."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: "\n".join(
        [
            h2("KDE'yi Motive Etmek: Histogramlar", "kde-histogram"),
            p(
                "Daha önce belirtildiği gibi yoğunluk tahmincisi, veri kümesini "
                "üreten olasılık dağılımını modellemeye çalışan bir algoritmadır. "
                "Tek boyutlu veri için muhtemelen tanıdık basit bir yoğunluk "
                "tahmincisini biliyorsunuz: histogram. Histogram veriyi ayrık "
                "kutulara böler, her kutudaki nokta sayısını sayar ve sonucu "
                "sezgisel biçimde görselleştirir."
            ),
            p("Örneğin iki normal dağılımdan çekilmiş veri üretelim:"),
        ]
    ),
    5: p(
        "Daha önce gördüğümüz gibi standart sayım tabanlı histogram "
        "<code>plt.hist</code> ile oluşturulabilir. Histogramın <code>density</code> "
        "parametresini belirterek, kutu yükseklikleri sayıları değil olasılık "
        "yoğunluğunu yansıtan normalize bir histogram elde ederiz (aşağıdaki şekil):"
    ),
    7: p(
        "Eşit kutulama için bu normalleştirme yalnızca y eksenindeki ölçeği "
        "değiştirir; göreli yükseklikler sayım histogramıyla esasen aynı kalır. "
        "Normalleştirme, histogram altındaki toplam alanın 1 olması için seçilir; "
        "histogram fonksiyonunun çıktısıyla doğrulayabiliriz:"
    ),
    9: p(
        "Histogram yoğunluk tahmincisi olarak kullanıldığında sorunlardan biri, "
        "kutu boyutu ve konumu seçiminin niteliksel olarak farklı görünümlere yol "
        "açabilmesidir. Örneğin yalnızca 20 noktalık bu verinin farklı kutulama "
        "sürümlerine bakarsak, kutuların nasıl çizildiği tamamen farklı bir "
        "yorum ortaya çıkarabilir (aşağıdaki şekil):"
    ),
    12: p(
        "Solda histogram bunun iki modlu bir dağılım olduğunu net gösterir. "
        "Sağda uzun kuyruklu tek modlu bir dağılım görürüz. Önceki kodu görmeden "
        "bu iki histogramın aynı veriden yapıldığını tahmin etmek zordur. "
        "Histogramların verdiği sezgiye nasıl güvenebiliriz? Nasıl iyileştirebiliriz?"
    ),
    14: p(
        "Histogramı, veri kümesindeki her noktanın üzerine bir blok yığdığımız "
        "bir blok yığını olarak düşünebiliriz. Bunu doğrudan görelim (aşağıdaki şekil):"
    ),
    16: p(
        "İki kutulamadaki sorun, blok yığınının yüksekliğinin çoğu zaman "
        "yakındaki gerçek yoğunluğu değil, kutuların veri noktalarıyla "
        "hizalanmasındaki tesadüfleri yansıtmasından kaynaklanır. "
        "Noktalar ile blokları arasındaki bu hizasızlık burada görülen "
        "zayıf histogram sonuçlarının olası nedenidir. Peki blokları "
        "<em>kutularla</em> hizalamak yerine temsil ettikleri <em>noktalarla</em> "
        "hizalarsak? Bloklar hizalı olmaz; ancak x ekseni boyunca her konumdaki "
        "katkılarını toplayarak sonucu bulabiliriz. Deneyelim (aşağıdaki şekil):"
    ),
    18: "\n".join(
        [
            p(
                "Sonuç biraz dağınık görünür; ancak standart histogramdan verinin "
                "gerçek özelliklerinin çok daha sağlam bir yansımasıdır. Yine de "
                "kaba kenarlar estetik değildir ve verinin gerçek özelliklerini "
                "yansıtmaz. Yumuşatmak için her konumdaki blokları Gauss gibi "
                "düzgün bir fonksiyonla değiştirebiliriz. Her noktada standart "
                "normal eğri kullanalım (aşağıdaki şekil):"
            ),
            p(
                "Her girdi noktasının konumunda Gauss katkısıyla yumuşatılmış bu "
                "grafik, veri dağılımının şekline çok daha doğru bir fikir verir "
                "ve çok daha az varyansa sahiptir (örneklemedeki farklara daha az "
                "duyarlıdır)."
            ),
            p(
                "Son iki grafikte elde ettiğimiz şey, bir boyutta çekirdek yoğunluk "
                "tahminidir: her noktanın konumuna bir \"çekirdek\" — ilkinde kare "
                "veya \"tophat\", ikincide Gauss — yerleştirdik ve yoğunluk tahmini "
                "olarak toplamlarını kullandık. Bu sezgiyle KDE'yi daha ayrıntılı "
                "inceleyeceğiz."
            ),
        ]
    ),
    19: "\n".join(
        [
            h2("Uygulamada Çekirdek Yoğunluk Tahmini", "kde-uygulama"),
            p(
                "KDE'nin serbest parametreleri <em>çekirdek</em> (her noktaya "
                "yerleştirilen dağılımın şekli) ve <em>çekirdek bant genişliği</em> "
                "(her noktadaki çekirdeğin boyutu)dir. Scikit-Learn KDE altı çekirdek "
                "destekler "
                '(<a href="https://scikit-learn.org/stable/modules/density.html" '
                'target="_blank" rel="noopener">Density Estimation</a> bölümü). '
                "Python'da birkaç KDE uygulaması olsa da (SciPy, statsmodels), "
                "verimlilik ve esneklik için Scikit-Learn sürümünü tercih ediyorum. "
                "<code>sklearn.neighbors.KernelDensity</code> altı çekirdek ve "
                "birkaç düzine uzaklık metriğiyle çok boyutlu KDE yapar. "
                "Ağaç tabanlı algoritma kullanır; <code>atol</code>/<code>rtol</code> "
                "ile hız/doğruluk dengesi kurulabilir. Bant genişliği çapraz "
                "doğrulama araçlarıyla belirlenebilir."
            ),
            p(
                "Önceki grafiği Scikit-Learn <code>KernelDensity</code> ile "
                "çoğaltan basit bir örnekle başlayalım (aşağıdaki şekil):"
            ),
        ]
    ),
    21: p("Buradaki sonuç, eğri altındaki alan 1 olacak şekilde normalize edilmiştir."),
    22: "\n".join(
        [
            h2("Bant Genişliğini Çapraz Doğrulama ile Seçmek", "bant-genisligi"),
            p(
                "KDE'nin nihai tahmini bant genişliğine oldukça duyarlıdır; "
                "yoğunluk tahmininde önyargı–varyans dengesini kontrol eder. "
                "Çok dar bant yüksek varyans (aşırı uyum); çok geniş bant yüksek "
                "önyargı (yapının yıkanması). Makine öğrenmesinde hiperparametre "
                "ayarı genelde çapraz doğrulamayla yapılır. Scikit-Learn "
                "<code>KernelDensity</code> grid search ile kullanılabilir. "
                "Küçük veri kümesi için leave-one-out CV kullanacağız:"
            ),
        ]
    ),
    24: p(
        "Bant genişliğini maksimize eden seçimi bulabiliriz (varsayılan olarak "
        "log-olabilirlik):"
    ),
    26: p(
        "Optimal bant genişliği, daha önce bant genişliği 1.0 olan örnek "
        "grafige çok yakındır (<code>scipy.stats.norm</code> varsayılan genişliği)."
    ),
    27: "\n".join(
        [
            h2("Örnek: Tam Naive Olmayan Bayes", "ornek-kde-bayes"),
            p(
                "Bu örnek KDE ile Bayes üretken sınıflandırmaya bakar ve Scikit-Learn "
                "mimarisinde özel bir tahminci oluşturmayı gösterir."
            ),
            p(
                '<a href="05-naive-bayes.html">5.5 Naive Bayes Sınıflandırması</a> '
                "bölümünde naive Bayes sınıflandırmasını inceledik: her sınıf için "
                "basit bir üretken model kurup bu modellerle hızlı sınıflandırıcı "
                "oluşturduk. Gauss naive Bayes'te üretken model eksen hizalı basit "
                "Gauss'tur. KDE gibi yoğunluk tahmin algoritmasıyla \"naive\" "
                "unsuru kaldırıp her sınıf için daha sofistike üretken modelle "
                "aynı sınıflandırmayı yapabiliriz. Hâlâ Bayes sınıflandırmasıdır; "
                "ama artık naive değildir."
            ),
            p("Genel üretken sınıflandırma yaklaşımı şudur:"),
            p(
                "1. Eğitim verisini etikete göre bölün.<br>"
                "2. Her küme için KDE uydurarak verinin üretken modelini elde edin. "
                "Böylece her $(x, y)$ için olabilirlik $P(x~|~y)$ hesaplanabilir.<br>"
                "3. Eğitim kümesindeki sınıf örnek sayılarından <em>sınıf önsel</em> "
                "$P(y)$ hesaplayın.<br>"
                "4. Bilinmeyen $x$ için her sınıfın posterior olasılığı "
                "$P(y~|~x) \\propto P(x~|~y)P(y)$. Posterioru maksimize eden "
                "sınıf, noktaya atanan etikettir."
            ),
            p(
                "Algoritma basit ve sezgiseldir; zor kısım bunu grid search ve "
                "çapraz doğrulama mimarisinden yararlanmak için Scikit-Learn "
                "çerçevesine oturtmaktır. Algoritma kod bloğunda uygulanmıştır; "
                "kodu adım adım inceleyeceğiz:"
            ),
        ]
    ),
    29: h3("Özel Tahmincinin Anatomisi", "tahminci-anatomi"),
    30: "\n".join(
        [
            p("Kodu adım adım inceleyelim; temel özellikler:"),
            p(
                "Scikit-Learn'deki her tahminci bir sınıftır; <code>BaseEstimator</code> "
                "ve uygun mixin'den türetmek en uygunudur. <code>BaseEstimator</code> "
                "çapraz doğrulama için klonlama mantığını içerir; <code>ClassifierMixin</code> "
                "varsayılan <code>score</code> yöntemini tanımlar. Docstring IPython "
                'yardımına yakalanır (bkz. <a href="../01-ipython/01-help-and-documentation.html">'
                "1.1 Yardım ve Dokümantasyon</a>)."
            ),
        ]
    ),
    31: p(
        "Sırada sınıf başlatma yöntemi gelir. Scikit-Learn'de <code>__init__</code> "
        "içinde, geçirilen değerleri <code>self</code>'e atamaktan başka işlem "
        "<em>olmaması</em> önemlidir — <code>BaseEstimator</code> klonlama mantığı "
        "bunu gerektirir. <code>*args</code> / <code>**kwargs</code> kaçınılmalıdır."
    ),
    32: p(
        "Ardından eğitim verisini işlediğimiz <code>fit</code> yöntemi gelir: "
        "eğitim verisindeki benzersiz sınıflar bulunur, her sınıf için "
        "<code>KernelDensity</code> eğitilir, sınıf önselleri örnek sayılarından "
        "hesaplanır. <code>fit</code> her zaman <code>self</code> döndürmelidir. "
        "Kalıcı sonuçlar sondaki alt çizgiyle saklanır (ör. <code>self.logpriors_</code>)."
    ),
    33: p(
        "Son olarak yeni veride etiket tahmini: olasılıksal sınıflandırıcı "
        "olduğu için önce <code>predict_proba</code> uygulanır; <code>[i,j]</code> "
        "girişi örnek <code>i</code>'nin sınıf <code>j</code> üyesi olma posterior "
        "olasılığıdır. <code>predict</code> en büyük olasılıklı sınıfı döndürür."
    ),
    34: p(
        "Özel tahmincimizi daha önce gördüğümüz el yazısı rakam sınıflandırmasında "
        "deneyelim. Rakamları yükleyip <code>GridSearchCV</code> ile aday bant "
        "genişliklerinin çapraz doğrulama skorunu hesaplayacağız "
        '(bkz. <a href="03-hyperparameters-and-model-validation.html">5.3 Hiperparametreler</a>):'
    ),
    36: p(
        "Bant genişliğine karşı çapraz doğrulama skorunu çizebiliriz (aşağıdaki şekil):"
    ),
    38: p(
        "KDE sınıflandırıcımız %96'nın üzerinde çapraz doğrulama doğruluğuna "
        "ulaşır; naive Bayes sınıflandırıcısı yaklaşık %80 civarındadır:"
    ),
    40: "\n".join(
        [
            p(
                "Böyle üretken sınıflandırıcının bir faydası, sonuçların "
                "yorumlanabilirliğidir: her bilinmeyen örnek için yalnızca "
                "olasılıksal sınıflandırma değil, karşılaştırdığımız nokta "
                "dağılımının <em>tam modeli</em> elde edilir! SVM ve rastgele "
                "orman gibi algoritmaların gizlediği nedenlere sezgisel bir "
                "pencere sunar."
            ),
            p("Daha ileri gitmek isteyenler için iyileştirme fikirleri:"),
            p(
                "• Her sınıfta bant genişliğinin bağımsız değişmesine izin verilebilir.<br>"
                "• Bant genişlikleri yalnızca tahmin skoruna göre değil, her sınıftaki "
                "üretken model olabilirliğine göre optimize edilebilir.<br>"
                "• KDE yerine Gauss karışım modelleri kullanan benzer Bayes "
                "sınıflandırıcısı kurmak iyi bir alıştırmadır."
            ),
        ]
    ),
}

INSERTS = {
    19: addon(
        "KDE çekirdekleri",
        "Scikit-Learn KDE altı çekirdek ve birkaç düzine uzaklık metriğini "
        "destekler. Büyük veride <code>atol</code>/<code>rtol</code> ile "
        "hız/doğruluk dengesi ayarlanır.",
    ),
    22: try_it(
        "",
        "Basit 1B KDE ile histogram karşılaştırması:",
        """import numpy as np
from sklearn.neighbors import KernelDensity
rng = np.random.default_rng(0)
x = np.concatenate([rng.normal(0, 1, 500), rng.normal(4, 1, 500)])
X = x[:, None]
kde = KernelDensity(bandwidth=0.8).fit(X)
log_dens = kde.score_samples(np.linspace(-3, 8, 100)[:, None])
print("max log-density:", log_dens.max().round(2))""",
        "deneme_kde_1d.py",
    ),
    34: try_it(
        "",
        "Digits verisinde KDE sınıflandırıcı bant genişliği denemesi (kısa):",
        """from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KernelDensity
import numpy as np
digits = load_digits()
# Basit tek-sınıf KDE skoru örneği
kde = KernelDensity(bandwidth=1.0).fit(digits.data[digits.target == 0])
print("digit-0 log-lik sample:", kde.score_samples(digits.data[:3]).round(2))""",
        "deneme_kde_digits.py",
    ),
}

CODE_NAMES = {
    2: "imports_kde.py",
    4: "make_data_kde.py",
    6: "hist_density.py",
    8: "hist_area_check.py",
    10: "make_data_20.py",
    11: "hist_bin_compare.py",
    13: "block_histogram.py",
    15: "stacked_blocks.py",
    17: "gauss_kernel_sum.py",
    20: "sklearn_kde_fit.py",
    23: "kde_gridsearch.py",
    25: "kde_best_params.py",
    28: "kde_classifier.py",
    35: "kde_digits_grid.py",
    37: "kde_cv_plot.py",
    39: "kde_vs_gnb.py",
}

if __name__ == "__main__":
    body = build_from_notebook(
        "05.13-Kernel-Density-Estimation.ipynb", TR, CODE_NAMES, INSERTS
    )
    body += "\n\n" + next_link("14-image-features.html", "5.14 Görüntü Öznitelikleri")
    path = write_chapter("13-kernel-density-estimation", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
