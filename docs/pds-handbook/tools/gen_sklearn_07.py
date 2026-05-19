#!/usr/bin/env python3
"""Generate 07-support-vector-machines.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, orig_line, p, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.07-support-vector-machines.html"
EN_LABEL = "05.07 Support Vector Machines"

TR = {
    0: h1("5.7 Derinlemesine: Destek Vektör Makineleri"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Destek vektör makineleri (SVM), hem sınıflandırma hem regresyon için "
                "özellikle güçlü ve esnek bir denetimli algoritma sınıfıdır. Bu bölümde "
                "SVM'lerin sezgisini ve sınıflandırma problemlerinde kullanımını "
                "inceleyeceğiz."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: h2("Destek Vektör Makinelerini Motive Etmek", "svm-motivasyon"),
    4: p(
        'Bayes sınıflandırması tartışmamızın bir parçası olarak (bkz. '
        '<a href="05-naive-bayes.html">5.5 Naive Bayes</a>), her sınıfın dağılımını '
        "tanımlayan basit bir model türünü ve yeni noktalar için olasılıksal etiket "
        "belirlemeyi gördük. Bu <em>üretici sınıflandırma</em> örneğiydi; burada "
        "<em>ayırt edici sınıflandırmayı</em> ele alacağız: her sınıfı modellemek "
        "yerine, sınıfları birbirinden ayıran bir doğru veya eğri (iki boyutta) ya da "
        "çok boyutta bir manifold buluruz."
    )
    + p(
        "Örnek olarak, iki sınıf noktasının iyi ayrıldığı basit bir sınıflandırma "
        "görevini düşünün (aşağıdaki şekil):"
    ),
    6: p(
        "Doğrusal ayırt edici bir sınıflandırıcı, iki veri kümesini ayıran düz bir "
        "çizgi çizmeye ve böylece bir sınıflandırma modeli oluşturmaya çalışır. "
        "Burada gösterilen gibi iki boyutlu veri için bunu elle yapabiliriz. Ancak "
        "hemen bir sorun görürüz: iki sınıfı mükemmel ayıran birden fazla olası "
        "ayırıcı doğru vardır!"
    ),
    8: p(
        'Bunlar örnekleri mükemmel ayıran üç <em>çok farklı</em> ayırıcıdır. '
        "Hangisini seçerseniz, yeni bir veri noktası (örneğin grafikte \"X\" ile "
        "işaretlenen) farklı etiket alır! Görünüşte \"sınıflar arasına çizgi çekme\" "
        "sezgimiz yeterli değil; biraz daha derin düşünmemiz gerekir."
    ),
    9: h2("Destek Vektör Makineleri: Marjı Maksimize Etmek", "marj-maksimize"),
    11: p(
        "Bu marjı maksimize eden doğru, optimal model olarak seçilecektir."
    ),
    12: h3("Destek Vektör Makinesi Uydurma", "svm-uyum"),
    14: p(
        "Bu veriye gerçek bir uydurmanın sonucuna bakalım: Scikit-Learn'in destek "
        "vektör sınıflandırıcısını (<code>SVC</code>) kullanarak bu veride bir SVM "
        "modeli eğiteceğiz. Şimdilik doğrusal çekirdek ve <code>C</code> parametresini "
        "çok büyük bir değere ayarlayacağız (anlamlarını kısa süre içinde "
        "tartışacağız):"
    ),
    17: p(
        "Bu, iki nokta kümesi arasındaki marjı maksimize eden ayırıcı doğrudur. "
        "Birkaç eğitim noktasının marja tam dokunduğunu — aşağıdaki şekilde "
        "daire içine alındığını — fark edin. Bu noktalar uydurmanın kritik "
        "öğeleridir; <em>destek vektörleri</em> olarak bilinir ve algoritmaya adını "
        "verir. Scikit-Learn'de kimlikleri sınıflandırıcının "
        "<code>support_vectors_</code> özniteliğinde saklanır:"
    ),
    19: p(
        "Bu sınıflandırıcının başarısının anahtarı, uydurma için yalnızca destek "
        "vektörlerinin konumlarının önemli olmasıdır; marjdan uzakta ve doğru "
        "tarafta kalan noktalar uydurmayı değiştirmez. Teknik olarak bunun nedeni, "
        "bu noktaların modele uydurulurken kullanılan kayıp fonksiyonuna katkı "
        "vermemesidir."
    )
    + p(
        "Örneğin veri kümesinin ilk 60 ve ilk 120 noktasından öğrenilen modeli "
        "çizersek bunu görebiliriz (aşağıdaki şekil):"
    ),
    21: p(
        "Sol panelde 60 eğitim noktası için model ve destek vektörlerini görürüz. "
        "Sağ panelde eğitim noktası sayısını ikiye katladık, ancak model değişmedi: "
        "soldaki üç destek vektörü sağdakilerle aynıdır. Uzak noktaların tam "
        "davranışına duyarsızlık, SVM modelinin güçlü yönlerinden biridir."
    ),
    22: p(
        "Bu not defterini canlı çalıştırıyorsanız, IPython etkileşimli araçlarıyla "
        "SVM modelinin bu özelliğini etkileşimli inceleyebilirsiniz:"
    ),
    24: h3("Doğrusal Sınırların Ötesinde: Çekirdek SVM", "cekirdek-svm"),
    26: p(
        "SVM'nin çok güçlü olabildiği yer, <em>çekirdeklerle</em> birleştirildiğinde "
        "ortaya çıkar. Çekirdekleri daha önce "
        '<a href="06-linear-regression.html">5.6 Doğrusal Regresyon</a> bölümündeki '
        "temel fonksiyon regresyonlarında gördük. Veriyi polinom ve Gauss temel "
        "fonksiyonlarıyla tanımlanan daha yüksek boyutlu bir uzaya yansıttık ve "
        "böylece doğrusal bir sınıflandırıcıyla doğrusal olmayan ilişkileri "
        "uyabildik."
    )
    + p(
        "SVM modellerinde aynı fikrin bir sürümünü kullanabiliriz. Çekirdeklere "
        "olan ihtiyacı motive etmek için doğrusal olarak ayrılamayan veriye bakalım "
        "(aşağıdaki şekil):"
    ),
    28: p(
        "Hiçbir doğrusal ayırım bu veriyi <em>asla</em> ayıramayacaktır. Ancak "
        '<a href="06-linear-regression.html">5.6 Doğrusal Regresyon</a> bölümündeki '
        "temel fonksiyon regresyonlarından ders çıkarabiliriz: veriyi doğrusal bir "
        "ayırıcının yeterli olacağı daha yüksek bir boyuta nasıl yansıtabiliriz? "
        "Örneğin orta kümeye merkezlenmiş bir <em>radyal temel fonksiyonu</em> (RBF) "
        "hesaplayabiliriz:"
    ),
    30: p(
        "Bu ek veri boyutunu üç boyutlu bir çizimle görselleştirebiliriz "
        "(aşağıdaki şekil). Bu ek boyutla veri, örneğin <em>r</em>=0.7 düzleminde "
        "bir ayırıcı çizerek önemsiz biçimde doğrusal ayrılabilir hale gelir."
    ),
    32: p(
        "Daha önce tanımladığımız fonksiyonla uydurmayı görselleştirip destek "
        "vektörlerini belirleyelim (aşağıdaki şekil):"
    ),
    34: p(
        "Bu çekirdekli destek vektör makinesiyle uygun doğrusal olmayan karar "
        "sınırını öğreniriz. Bu çekirdek dönüşüm stratejisi, özellikle çekirdek "
        "hilekullanımının uygulanabildiği modellerde, hızlı doğrusal yöntemleri "
        "hızlı doğrusal olmayan yöntemlere dönüştürmek için sık kullanılır."
    ),
    35: h3("SVM Ayarı: Marjı Yumuşatmak", "marj-yumusatma"),
    37: p(
        "Tartışmamız şimdiye kadar mükemmel karar sınırının olduğu çok temiz "
        "veri kümelerine odaklandı. Verinizde bir miktar örtüşme varsa ne olur? "
        "Bu durumu ele almak için SVM uygulamasında marjı \"yumuşatan\" bir düzeltme "
        "faktörü vardır: daha iyi bir uyum için bazı noktaların marja girmesine "
        "izin verir. Marjın sertliği genelde <code>C</code> olarak bilinen bir "
        "ayar parametresiyle kontrol edilir."
    ),
    39: p(
        "Optimal <code>C</code> değeri veri kümenize bağlıdır; çapraz doğrulama veya "
        'benzeri bir yöntemle ayarlanmalıdır (bkz. '
        '<a href="03-hyperparameters-and-model-validation.html">5.3 Hiperparametreler '
        "ve Model Doğrulama</a>)."
    ),
    40: h2("Örnek: Yüz Tanıma", "ornek-yuz-tanima"),
    42: p(
        "Destek vektör makinelerinin uygulaması olarak yüz tanıma problemini "
        "inceleyelim. Çeşitli kamuya mal olmuş kişilerin fotoğraflarından oluşan "
        "Labeled Faces in the Wild veri kümesini kullanacağız. Veri kümesi için "
        "bir getirici Scikit-Learn'e yerleştirilmiştir:"
    ),
    44: p(
        "Birkaç yüzü çizerek neyle çalıştığımıza bakalım (aşağıdaki şekil). Her "
        "görüntü 62×47, yaklaşık 3.000 piksel içerir. Her piksel değerini öznitelik "
        "olarak kullanabiliriz; ancak genelde daha anlamlı öznitelikler çıkaran bir "
        "ön işlemci daha etkilidir. Burada destek vektör makinesi sınıflandırıcısına "
        "beslemek için 150 temel bileşen çıkarmak üzere "
        '<a href="09-principal-component-analysis.html">5.9 PCA</a> kullanacağız. '
        "Bunu ön işlemci ve sınıflandırıcıyı tek bir boru hattında paketleyerek "
        "yapabiliriz:"
    ),
    46: p(
        "Sınıflandırıcı çıktısını test etmek için veriyi eğitim ve test kümelerine "
        "ayıracağız:"
    ),
    48: p(
        "Son olarak ızgara arama çapraz doğrulamasıyla parametre kombinasyonlarını "
        "keşfedebiliriz. Burada <code>C</code> (marj sertliği) ve <code>gamma</code> "
        "(RBF çekirdek boyutu) ayarlayıp en iyi modeli belirleyeceğiz:"
    ),
    50: p(
        "Optimal değerler ızgaranın ortasına yakınsa iyi; kenarlardaysa gerçek "
        "optimumu bulmak için ızgarayı genişletmek isteyebilirsiniz. Bu çapraz "
        "doğrulanmış modelle henüz görülmemiş test verisinin etiketlerini "
        "tahmin edebiliriz:"
    ),
    52: p(
        "Küçük örneklemde birkaç test görüntüsünü tahminleriyle birlikte "
        "görelim (aşağıdaki şekil):"
    ),
    54: p(
        "Bu küçük örneklemde optimal tahmin edici yalnızca tek bir yüzü yanlış "
        "etiketledi. Sınıflandırma raporuyla etiket bazında performansa bakabiliriz:"
    ),
    56: p(
        "Sınıflar arası karışıklık matrisini de gösterebiliriz (aşağıdaki şekil). "
        "Bu, hangi etiketlerin birbiriyle karıştırılmaya eğilimli olduğuna dair "
        "fikir verir."
    ),
    58: p(
        "Gerçek dünya yüz tanımada fotoğraflar düzgün ızgaralara önceden kırpılmamış "
        "olur; tek fark öznitelik seçimidir: yüzleri bulmak ve piksellemeden "
        "bağımsız öznitelikler çıkarmak için daha gelişmiş algoritmalar gerekir. "
        'Bu tür uygulamalar için <a href="http://opencv.org" target="_blank" '
        'rel="noopener">OpenCV</a> iyi bir seçenektir.'
    ),
    59: "\n".join(
        [
            h2("Özet", "ozet"),
            p("Bu, destek vektör makinelerinin arkasındaki ilkelerin kısa sezgisel bir girişiydi."),
            p("Bu modeller güçlü bir sınıflandırma yöntemidir; birkaç nedenden dolayı:"),
            ul(
                [
                    "Görece az sayıda destek vektörüne bağlı olmaları, kompakt olmalarını ve çok az bellek kullanmalarını sağlar.",
                    "Model eğitildikten sonra tahmin aşaması çok hızlıdır.",
                    "Yalnızca marja yakın noktalardan etkilenmeleri sayesinde yüksek boyutlu veride — örnekten fazla boyutta bile — iyi çalışırlar.",
                    "Çekirdek yöntemleriyle entegrasyonları onları çok yönlü kılar.",
                ]
            ),
            p("Ancak SVM'lerin dezavantajları vardır:"),
            ul(
                [
                    "Örnek sayısı $N$ ile ölçekleme en kötü $\\mathcal{O}[N^3]$, verimli uygulamalarda $\\mathcal{O}[N^2]$ olabilir.",
                    "Sonuçlar <code>C</code> parametresinin uygun seçimine güçlü bağımlıdır; çapraz doğrulama maliyetli olabilir.",
                    "Sonuçların doğrudan olasılıksal yorumu yoktur (<code>SVC</code> <code>probability</code> parametresiyle tahmin edilebilir).",
                ]
            ),
            p(
                "Genelde SVM'lere, daha basit ve hızlı yöntemler yetersiz kaldığında "
                "geçerim. Yine de verinizde eğitim ve çapraz doğrulama için CPU "
                "döngüsü ayırabiliyorsanız, yöntem mükemmel sonuçlar verebilir."
            ),
        ]
    ),
}

INSERTS = {
    2: addon(
        "Pyodide ve LFW",
        "<p>Yüz tanıma örneği <code>fetch_lfw_people</code> ile veri indirir; tarayıcıda "
        "ilk çalıştırma yavaş olabilir. <code>ipywidgets</code> etkileşimli hücreleri "
        "Pyodide'da çalışmayabilir — yerel Jupyter'de deneyin.</p>",
    ),
    13: try_it(
        "Şimdi deneyin",
        "İki blob üzerinde doğrusal SVM uydurun:",
        """from sklearn.datasets import make_blobs
from sklearn.svm import SVC
X, y = make_blobs(n_samples=50, centers=2, random_state=0)
clf = SVC(kernel='linear', C=1e5)
clf.fit(X, y)
print("Destek vektör sayısı:", clf.support_vectors_.shape[0])""",
        "deneme_svc_linear.py",
    ),
    31: try_it(
        "Şimdi deneyin",
        "Halka verisinde RBF çekirdekli SVM:",
        """from sklearn.datasets import make_circles
from sklearn.svm import SVC
X, y = make_circles(100, factor=0.1, noise=0.1)
clf = SVC(kernel='rbf', C=1e6)
clf.fit(X, y)
print("Doğruluk:", clf.score(X, y))""",
        "deneme_svc_rbf.py",
    ),
}

CODE_NAMES = {
    2: "imports_svm.py",
    5: "make_blobs_svm.py",
    7: "linear_separators.py",
    10: "margin_plot.py",
    13: "svc_fit.py",
    15: "plot_svc_decision_function.py",
    16: "svc_scatter.py",
    18: "support_vectors_.py",
    20: "plot_svm_subsets.py",
    23: "interact_svm.py",
    25: "make_circles.py",
    27: "rbf_projection.py",
    29: "rbf_3d_plot.py",
    31: "svc_rbf.py",
    33: "plot_svc_rbf.py",
    36: "soft_margin_data.py",
    38: "soft_margin_C.py",
    41: "fetch_lfw_people.py",
    43: "plot_faces.py",
    45: "pca_svc_pipeline.py",
    47: "train_test_split_faces.py",
    49: "gridsearch_svc.py",
    51: "predict_faces.py",
    53: "plot_test_predictions.py",
    55: "classification_report_faces.py",
    57: "confusion_matrix_faces.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.07-Support-Vector-Machines.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link("08-random-forests.html", "5.8 Rastgele Ormanlar")
    path = write_chapter("07-support-vector-machines", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
