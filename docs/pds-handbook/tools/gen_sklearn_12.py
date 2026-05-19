#!/usr/bin/env python3
"""Generate 12-gaussian-mixtures.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, orig_line, p, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.12-gaussian-mixtures.html"
EN_LABEL = "05.12 Gaussian Mixtures"

TR = {
    0: h1("5.12 Derinlemesine: Gauss Karışımları"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Önceki bölümde incelediğimiz <em>k</em>-means kümeleme modeli basit "
                "ve anlaşılması nispeten kolaydır; ancak bu basitlik uygulamada pratik "
                "zorluklara yol açar. Özellikle <em>k</em>-means'in olasılıksal olmaması "
                "ve küme merkezine basit uzaklıkla üyelik ataması, birçok gerçek dünya "
                "durumunda zayıf performansa neden olur."
            ),
            p(
                "Bu bölümde Gauss karışım modellerine bakacağız; bunlar <em>k</em>-means "
                "fikirlerinin bir uzantısı olarak görülebilir, aynı zamanda basit "
                "kümelemenin ötesinde güçlü bir tahmin aracı da olabilir."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: h2("Gauss Karışımlarını Motive Etmek: k-Means'in Zayıflıkları", "kmeans-zayiflik"),
    4: p(
        "<em>k</em>-means'in bazı zayıflıklarına bakalım ve küme modelini nasıl "
        "iyileştirebileceğimizi düşünelim. Önceki bölümde gördüğümüz gibi, basit "
        "ve iyi ayrılmış veride <em>k</em>-means uygun kümeleme sonuçları bulur. "
        "Örneğin basit blob veride <em>k</em>-means algoritması kümeleri gözle "
        "yaptığımıza yakın etiketler (aşağıdaki şekil):"
    ),
    6: "\n".join(
        [
            p(
                "Sezgisel olarak bazı noktalar için küme atamasının diğerlerinden "
                "daha kesin olmasını bekleriz: ortadaki iki küme arasında hafif "
                "örtüşme var gibi görünüyor; aralarındaki noktaların küme "
                "atamasına tam güvenmeyebiliriz. Ne yazık ki <em>k</em>-means "
                "modelinin küme atamalarının olasılık veya belirsizliğini ölçen "
                "içsel bir ölçüsü yoktur (bootstrap ile tahmin edilebilir). "
                "Bunun için modeli genelleştirmeyi düşünmeliyiz."
            ),
            p(
                "<em>k</em>-means modelini, her kümenin merkezine bir daire (yüksek "
                "boyutlarda hiperküre) yerleştiren ve yarıçapını kümedeki en uzak "
                "noktayla tanımlayan bir model olarak düşünebiliriz. Bu yarıçap "
                "eğitim kümesinde sert bir kesim görevi görür: daire dışındaki "
                "noktalar küme üyesi sayılmaz. Bu küme modelini aşağıdaki fonksiyonla "
                "görselleştirebiliriz (aşağıdaki şekil):"
            ),
        ]
    ),
    9: p(
        "<em>k</em>-means için önemli bir gözlem: bu küme modelleri <em>dairesel "
        "olmak zorundadır</em> — <em>k</em>-means elips veya uzun kümeleri hesaba "
        "katamaz. Aynı veriyi dönüştürürsek küme atamaları karışır (aşağıdaki şekil):"
    ),
    11: "\n".join(
        [
            p(
                "Gözle bu dönüştürülmüş kümelerin dairesel olmadığını görürüz; "
                "dairesel kümeler kötü bir uyum olur. Yine de <em>k</em>-means "
                "buna uyum sağlayamaz ve veriyi dört dairesel kümeye zorlar; "
                "sonuçta daireler örtüşür — özellikle grafiğin sağ alt köşesine bakın."
            ),
            p(
                "Bu özel durumu PCA ile ön işlemeyle ele almayı düşünebiliriz "
                '(bkz. <a href="09-principal-component-analysis.html">5.9 PCA</a>); '
                "ancak pratikte böyle küresel bir işlemin bireysel grupları "
                "daireselleştireceğinin garantisi yoktur."
            ),
            p(
                "<em>k</em>-means'in bu iki dezavantajı — küme şeklinde esneklik "
                "eksikliği ve olasılıksal atama eksikliği — birçok veri kümesinde "
                "(özellikle düşük boyutlu) umut ettiğiniz kadar iyi performans "
                "vermeyebileceği anlamına gelir."
            ),
            p(
                "Belirsizliği, her noktanın yalnızca en yakın merkeze değil "
                "<em>tüm</em> küme merkezlerine uzaklıklarını karşılaştırarak "
                "ölçerek; küme sınırlarının daire yerine elips olmasına izin "
                "vererek genelleştirebilirsiniz. Bunlar Gauss karışım modellerinin "
                "iki temel bileşenidir."
            ),
        ]
    ),
    12: "\n".join(
        [
            h2("E–M'yi Genelleştirmek: Gauss Karışım Modelleri", "gmm-genelleme"),
            p(
                "Gauss karışım modeli (GMM), girdi veri kümesini en iyi modelleyen "
                "çok boyutlu Gauss olasılık dağılımları karışımını bulmaya çalışır. "
                "En basit durumda GMM, <em>k</em>-means ile aynı şekilde küme "
                "bulmak için kullanılabilir (aşağıdaki şekil):"
            ),
        ]
    ),
    14: p(
        "Ancak GMM kaputun altında olasılıksal bir model içerdiğinden, "
        "olasılıksal küme atamaları da bulunabilir — Scikit-Learn'de "
        "<code>predict_proba</code> yöntemiyle. Bu, herhangi bir noktanın "
        "verilen kümeye ait olasılığını ölçen <code>[n_samples, n_clusters]</code> "
        "boyutunda bir matris döndürür:"
    ),
    16: p(
        "Bu belirsizliği, örneğin her noktanın boyutunu tahmin kesinliğiyle "
        "orantılı yaparak görselleştirebiliriz; aşağıdaki şekilde kümeler "
        "arasındaki sınırdaki noktaların tam da bu atama belirsizliğini "
        "yansıttığını görürüz:"
    ),
    18: "\n".join(
        [
            p(
                "Kaputun altında Gauss karışım modeli <em>k</em>-means'e çok "
                "benzer: beklenti–maksimizasyon kullanır; nitel olarak şunları yapar:"
            ),
            ul(
                [
                    "Konum ve şekil için başlangıç tahminleri seçin.",
                    "Yakınsayana kadar tekrarlayın:",
                    "<em>E-adımı</em>: Her nokta için her kümedeki üyelik olasılığını kodlayan ağırlıkları bulun.",
                    "<em>M-adımı</em>: Her küme için konum, normalleştirme ve şekli <em>tüm</em> veri noktalarına, ağırlıkları kullanarak güncelleyin.",
                ]
            ),
            p(
                "Sonuçta her küme sert kenarlı bir küreyle değil, düzgün bir Gauss "
                "modeliyle ilişkilidir. <em>k</em>-means E–M'de olduğu gibi algoritma "
                "bazen küresel optimumu kaçırabilir; pratikte birden fazla rastgele "
                "başlangıç kullanılır."
            ),
            p(
                "GMM çıktısına dayanarak elipsler çizen ve küme konumlarını/şekillerini "
                "görselleştirmemize yardımcı olacak bir fonksiyon yazalım:"
            ),
        ]
    ),
    20: p(
        "Bununla birlikte dört bileşenli GMM'nin başlangıç verimize ne verdiğine "
        "bakalım (aşağıdaki şekil):"
    ),
    22: p(
        "Benzer şekilde GMM ile gerilmiş veri kümemize uyum sağlayabiliriz; "
        "tam kovaryansa izin verildiğinde model çok uzun, gerilmiş kümeleri "
        "bile uyabilir (aşağıdaki şekil):"
    ),
    24: p(
        "Bu, daha önce <em>k</em>-means ile karşılaşılan iki ana pratik sorunu "
        "GMM'nin nasıl giderdiğini netleştirir."
    ),
    25: h2("Kovaryans Tipini Seçmek", "kovaryans-tipi"),
    26: "\n".join(
        [
            p(
                "Önceki uyumlara bakarsanız <code>covariance_type</code> seçeneğinin "
                "her birinde farklı ayarlandığını görürsünüz. Bu hiperparametre, "
                "her kümenin şeklindeki serbestlik derecelerini kontrol eder; "
                "verilen problem için dikkatle ayarlanmalıdır."
            ),
            p(
                "Varsayılan <code>covariance_type=\"diag\"</code>, her boyutta küme "
                "boyutunun bağımsız ayarlanabileceği anlamına gelir; elips eksenlerle "
                "hizalı kalır. Biraz daha basit ve hızlı model "
                "<code>covariance_type=\"spherical\"</code>, tüm boyutların eşit "
                "olmasını zorlar; sonuç <em>k</em>-means'e benzer ama tam eşdeğil "
                "değildir. Daha karmaşık ve pahalı model (boyut arttıkça özellikle) "
                "<code>covariance_type=\"full\"</code>, her kümeyi keyfi yönelimli "
                "elips olarak modellemeye izin verir."
            ),
            p(
                "Tek bir küme için bu üç seçeneğin görsel temsilini aşağıdaki "
                "şekilde görebiliriz:"
            ),
        ]
    ),
    27: figure(
        "05.12-covariance-type.png",
        "GMM kovaryans tipleri: spherical, diag, full",
        "Kovaryans tipi seçenekleri (orijinal kitap ekinden).",
    ),
    29: "\n".join(
        [
            h2("Yoğunluk Tahmini Olarak Gauss Karışım Modelleri", "gmm-yogunluk"),
            p(
                "GMM sıklıkla kümeleme algoritması diye sınıflandırılsa da "
                "temelde bir <em>yoğunluk tahmini</em> algoritmasıdır. Yani GMM "
                "uyumu teknik olarak bir kümeleme modeli değil, verinin dağılımını "
                "tanımlayan üretken olasılıksal bir modeldir."
            ),
            p(
                "Örnek olarak Scikit-Learn'in <code>make_moons</code> fonksiyonundan "
                "üretilmiş veriyi düşünün "
                '(<a href="11-k-means.html">5.11 K-Means</a> bölümünde tanıtılmıştı; '
                "aşağıdaki şekil):"
            ),
        ]
    ),
    31: p(
        "Bunu kümeleme modeli olarak iki bileşenli GMM ile uydurmaya çalışırsak "
        "sonuç pek kullanışlı olmaz (aşağıdaki şekil):"
    ),
    33: p(
        "Ancak çok daha fazla bileşen kullanıp küme etiketlerini yok sayarsak, "
        "girdi verisine çok daha yakın bir uyum buluruz (aşağıdaki şekil):"
    ),
    35: p(
        "Burada 16 Gauss bileşenli karışım, ayrık kümeler bulmak için değil, "
        "girdi verisinin genel <em>dağılımını</em> modellemek içindir. Bu, "
        "girdi verimize benzer yeni rastgele veri üretmek için tarif veren "
        "üretken bir dağılım modelidir. Örneğin orijinal veriye uydurulmuş "
        "16 bileşenli GMM'den 400 yeni nokta çizebiliriz (aşağıdaki şekil):"
    ),
    36: p(
        "GMM, keyfi çok boyutlu veri dağılımını modellemek için esnek bir "
        "araçtır."
    ),
    38: "\n".join(
        [
            h3("Kaç Bileşen?", "kac-bilesen"),
            p(
                "GMM'nin üretken model olması, veri kümesi için optimal bileşen "
                "sayısını belirlemenin doğal bir yolunu verir. Üretken model "
                "doğası gereği veri kümesi için olasılık dağılımıdır; veriyi "
                "model altında değerlendirebiliriz, aşırı uyumu önlemek için "
                "çapraz doğrulama kullanırız."
            ),
            p(
                "Aşırı uyumu düzeltmek için "
                '<a href="https://en.wikipedia.org/wiki/Akaike_information_criterion" '
                'target="_blank" rel="noopener">AIC</a> veya '
                '<a href="https://en.wikipedia.org/wiki/Bayesian_information_criterion" '
                'target="_blank" rel="noopener">BIC</a> gibi analitik ölçütlerle '
                "model olabilirliklerini ayarlayabiliriz. Scikit-Learn "
                "<code>GaussianMixture</code> tahmincisi her ikisini de hesaplayan "
                "yerleşik yöntemler içerir."
            ),
            p(
                "Ay verisi için GMM bileşen sayısına karşı AIC ve BIC'ye bakalım "
                "(aşağıdaki şekil):"
            ),
        ]
    ),
    39: p(
        "Optimal küme sayısı AIC veya BIC'yi minimize eden değerdir. AIC, "
        "daha önce seçtiğimiz 16 bileşenin muhtemelen fazla olduğunu söyler: "
        "yaklaşık 8–12 bileşen daha iyi olurdu. Bu tür problemlerde BIC genelde "
        "daha sade model önerir."
    ),
    40: "\n".join(
        [
            p(
                "Önemli nokta: bileşen sayısı seçimi GMM'nin <em>yoğunluk "
                "tahmincisi</em> olarak ne kadar iyi çalıştığını ölçer; "
                "<em>kümeleme algoritması</em> olarak ne kadar iyi çalıştığını "
                "değil. GMM'yi öncelikle yoğunluk tahmincisi olarak düşünün; "
                "kümeleme için yalnızca basit veri kümelerinde kullanın."
            ),
            h2("Örnek: Yeni Veri Üretmek için GMM", "ornek-uretken"),
            p(
                "Girdi verisinin tanımladığı dağılımdan yeni örnekler oluşturmak "
                "için GMM'yi üretken model olarak kullandığımız basit bir örneği "
                "gördük. Şimdi bunu ilerletip standart digits küpusundan "
                "<em>yeni el yazısı rakamlar</em> üretelim."
            ),
            p("Başlangıç olarak Scikit-Learn veri araçlarıyla digits verisini yükleyelim:"),
        ]
    ),
    41: p(
        "Hatırlamak için ilk 50 tanesini çizelim (aşağıdaki şekil):"
    ),
    43: "\n".join(
        [
            p(
                "64 boyutta yaklaşık 1.800 rakamımız var; bunun üzerine GMM "
                "kurabiliriz. GMM bu kadar yüksek boyutta yakınsamakta zorlanabilir; "
                "veri üzerinde tersinir bir boyut indirgeme algoritmasıyla başlayacağız. "
                "Burada doğrudan PCA kullanıp yansıtılan veride %99 varyansı koruyacağız:"
            ),
        ]
    ),
    45: p(
        "Sonuç 41 boyuttur — neredeyse 1/3 azalma, neredeyse bilgi kaybı yok. "
        "Bu yansıtılmış veriyle kaç GMM bileşeni kullanmamız gerektiğine AIC "
        "ile bakalım (aşağıdaki şekil):"
    ),
    47: p(
        "Yaklaşık 140 bileşen AIC'yi minimize ediyor gibi görünüyor; bu modeli "
        "kullanacağız. Veriye hızlıca uydurup yakınsadığını doğrulayalım:"
    ),
    49: p(
        "Şimdi GMM'yi üretken model olarak kullanarak bu 41 boyutlu yansıtılmış "
        "uzayda 100 yeni nokta çekebiliriz:"
    ),
    51: p(
        "Son olarak PCA nesnesinin ters dönüşümüyle yeni rakamları oluşturabiliriz "
        "(aşağıdaki şekil):"
    ),
    53: p(
        "Sonuçların çoğu veri kümesindeki makul rakamlara benziyor! "
        "Burada yaptığımızı düşünün: el yazısı rakam örnekleminden yola çıkarak "
        "verinin dağılımını, karışım modeliyle girdi verisinde bireysel olarak "
        "görünmeyen ama genel özellikleri yakalayan yeni rakam örnekleri "
        "üretebilecek şekilde modelledik. Böyle bir üretken rakam modeli, "
        "sonraki bölümde göreceğimiz gibi Bayes üretken sınıflandırıcının "
        "bileşeni olarak çok faydalı olabilir."
    ),
}

INSERTS = {
    15: try_it(
        "",
        "GMM ile olasılıksal küme atamasını inceleyin:",
        """import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=200, centers=3, random_state=0)
gmm = GaussianMixture(n_components=3, random_state=0).fit(X)
print(gmm.predict_proba(X[:3]).round(3))""",
        "deneme_gmm_proba.py",
    ),
    38: addon(
        "AIC / BIC",
        "Bileşen sayısı seçimi küme kalitesinden çok yoğunluk uyumunu ölçer. "
        "Kümeleme için silhouette; yoğunluk için AIC/BIC daha uygundur.",
    ),
}

CODE_NAMES = {
    2: "imports_gmm.py",
    4: "make_blobs_gmm.py",
    5: "kmeans_labels_plot.py",
    7: "plot_kmeans_fn.py",
    8: "kmeans_circles.py",
    10: "kmeans_stretched.py",
    13: "gmm_fit_predict.py",
    15: "gmm_predict_proba.py",
    17: "gmm_uncertainty_size.py",
    19: "draw_ellipse_fn.py",
    21: "plot_gmm_four.py",
    23: "gmm_stretched_full.py",
    28: "make_moons_gmm.py",
    30: "gmm2_moons_fail.py",
    32: "gmm16_density.py",
    34: "gmm16_sample.py",
    37: "gmm_aic_bic.py",
    40: "load_digits_gmm.py",
    42: "plot_digits_fn.py",
    44: "pca_digits_gmm.py",
    46: "gmm_aic_digits.py",
    48: "gmm140_fit.py",
    50: "gmm_sample_latent.py",
    52: "gmm_new_digits.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.12-Gaussian-Mixtures.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link(
        "13-kernel-density-estimation.html", "5.13 Çekirdek Yoğunluk Tahmini"
    )
    path = write_chapter("12-gaussian-mixtures", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
