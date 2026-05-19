#!/usr/bin/env python3
"""Generate 08-random-forests.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, orig_line, p, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.08-random-forests.html"
EN_LABEL = "05.08 Random Forests"

TR = {
    0: h1("5.8 Derinlemesine: Karar Ağaçları ve Rastgele Ormanlar"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                'Daha önce basit bir üretici sınıflandırıcıyı (naive Bayes; bkz. '
                '<a href="05-naive-bayes.html">5.5 Naive Bayes</a>) ve güçlü bir '
                'ayırt edici sınıflandırıcıyı (destek vektör makineleri; bkz. '
                '<a href="07-support-vector-machines.html">5.7 SVM</a>) derinlemesine '
                "inceledik. Burada <em>rastgele ormanlar</em> adlı güçlü parametrik "
                "olmayan bir algoritmaya bakacağız."
            ),
            p(
                "Rastgele ormanlar, daha basit tahmin edicilerin sonuçlarını birleştiren "
                "<em>topluluk</em> (ensemble) yöntemine bir örnektir. Şaşırtıcı biçimde "
                "böyle yöntemlerde bütün, parçaların toplamından büyük olabilir: çok sayıda "
                "tahmin edicinin çoğunluk oyu, tek tek oylayanların herhangi birinden daha "
                "iyi doğruluk verebilir!"
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: h2("Rastgele Ormanları Motive Etmek: Karar Ağaçları", "karar-agaclari-motivasyon"),
    4: p(
        "Rastgele ormanlar, karar ağaçları üzerine kurulu topluluk öğrenicileridir; "
        "bu yüzden karar ağaçlarıyla başlayacağız. Karar ağaçları nesneleri "
        "sınıflandırmak veya etiketlemek için son derece sezgisel yöntemlerdir: "
        "sınıflandırmaya yönelik bir dizi soru sorarsınız. Örneğin yürüyüşte "
        "gördüğünüz hayvanları sınıflandırmak için aşağıdaki şekildeki gibi bir ağaç "
        "kurabilirsiniz."
    ),
    5: figure("05.08-decision-tree.png", "Örnek karar ağacı"),
    6: p(
        "İkili bölme çok verimlidir: iyi kurulmuş bir ağaçta her soru seçenek sayısını "
        "kabaca yarıya indirir. Zorluk, her adımda hangi soruların sorulacağına "
        "karar vermektir. Makine öğrenmesinde sorular genelde veride eksen hizalı "
        "bölümler biçimindedir."
    ),
    7: h3("Karar Ağacı Oluşturma", "karar-agaci-olusturma"),
    9: p(
        "Bu iki boyutlu veri üzerinde basit bir karar ağacı, veriyi eksenlerden "
        "birinde bir eşik değerine göre yinelemeli böler ve her bölgede çoğunluk "
        "oyuyla etiket atar (aşağıdaki şekil, ilk dört seviye)."
    ),
    10: figure("05.08-decision-tree-levels.png", "Karar ağacının ilk dört seviyesi"),
    11: p(
        "İlk bölmeden sonra üst daldeki her nokta değişmeden kalır; bu dalı daha "
        "fazla bölmeye gerek yoktur. Tek renkten oluşmayan her düğümde bölge "
        "yine iki öznitelikten biri boyunca bölünür."
    ),
    12: p(
        "Bu uydurma Scikit-Learn'de <code>DecisionTreeClassifier</code> ile yapılır:"
    ),
    14: p("Sınıflandırıcı çıktısını görselleştirmek için bir yardımcı fonksiyon yazalım:"),
    16: p(
        "Karar ağacı sınıflandırmasının nasıl göründüğüne bakalım (aşağıdaki şekil):"
    ),
    18: p(
        "Not defterini canlı çalıştırıyorsanız, çevrimiçi "
        '<a href="https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb#Helper-Code" '
        'target="_blank" rel="noopener">ek bölümdeki</a> yardımcı betikle karar ağacı '
        "oluşturma sürecini etkileşimli gösterebilirsiniz:"
    ),
    20: p(
        "Derinlik arttıkça çok garip şekilli sınıflandırma bölgeleri oluşur; bu, "
        "gerçek dağılımdan çok örnekleme veya gürültüye bağlıdır — ağaç aşırı "
        "uyum yapmaktadır."
    ),
    21: h3("Karar Ağaçları ve Aşırı Uyum", "karar-agaci-asiri-uyum"),
    22: figure("05.08-decision-tree-overfitting.png", "Karar ağacı aşırı uyumu"),
    23: p(
        "Bazı yerlerde iki ağaç tutarlı, bazı yerlerde çok farklı sonuç verir. "
        "Tutarsızlıklar genelde sınıflandırmanın belirsiz olduğu yerlerde olur; "
        "iki ağacın bilgisini birleştirirsek daha iyi sonuç elde edebiliriz!"
    ),
    24: p(
        "Not defterini canlı çalıştırıyorsanız, verinin rastgele alt kümesiyle "
        "eğitilmiş ağaçları etkileşimli gösterebilirsiniz:"
    ),
    26: p(
        "İki ağaçtan bilgi kullanmak sonucu iyileştirirse, birçok ağaçtan bilgi "
        "kullanmanın sonucu daha da iyileştireceğini bekleyebiliriz."
    ),
    27: h2("Tahmin Edici Toplulukları: Rastgele Ormanlar", "rastgele-ormanlar"),
    29: p(
        "Birden fazla aşırı uyumlu tahmin edicinin birleştirilmesi <em>bagging</em> "
        "topluluk yönteminin temelidir. Paralel tahmin edicilerin ortalaması/alınması "
        "aşırı uyumu azaltır. Rastgeleleştirilmiş karar ağaçları topluluğuna "
        "<em>rastgele orman</em> denir. Aşağıdaki şekilde "
        "<code>BaggingClassifier</code> ile manuel bagging gösterilir:"
    ),
    31: p(
        "Burada her tahmin edici eğitim noktalarının rastgele %80'iyle eğitildi. "
        "Pratikte bölümlerin nasıl seçildiğine stokastisite enjekte etmek daha "
        "etkilidir. Scikit-Learn'de <code>RandomForestClassifier</code> bunu "
        "otomatik yapar (aşağıdaki şekil):"
    ),
    32: h2("Rastgele Orman Regresyonu", "rastgele-orman-regresyonu"),
    34: p(
        "Rastgele ormanlar regresyonda da kullanılır (<code>RandomForestRegressor</code>). "
        "Aşağıdaki veri hızlı ve yavaş salınımın birleşiminden üretilmiştir:"
    ),
    36: p(
        "Gerçek model düzgün gri eğri, rastgele orman modeli kırmızı pürüzlü eğridir. "
        "Parametrik olmayan model çok periyotlu veriyi çok periyotlu model belirtmeden "
        "uyabilmektedir!"
    ),
    37: h2("Örnek: Rakamları Rastgele Ormanla Sınıflandırma", "ornek-rakamlar"),
    39: p(
        "Scikit-Learn'in digits veri kümesini kullanacağız. İlk birkaç noktayı "
        "görselleştirelim (aşağıdaki şekil):"
    ),
    41: p("Rakamları rastgele ormanla şöyle sınıflandırabiliriz:"),
    43: p("Sınıflandırma raporuna bakalım:"),
    45: p("Karışıklık matrisini de çizelim (aşağıdaki şekil):"),
    47: p(
        "Basit, ayarsız bir rastgele orman digits verisinde oldukça doğru "
        "sınıflandırma sağlar."
    ),
    48: "\n".join(
        [
            h2("Özet", "ozet"),
            p(
                "Bu bölüm topluluk tahmin edicilerine ve özellikle rastgele ormanlara "
                "kısa bir giriş sundu."
            ),
            p("Rastgele ormanların birkaç avantajı:"),
            ul(
                [
                    "Karar ağaçlarının basitliği sayesinde eğitim ve tahmin çok hızlıdır; paralelleştirilebilir.",
                    "Çoklu ağaçlar olasılıksal sınıflandırma sağlar (<code>predict_proba</code>).",
                    "Parametrik olmayan model esnektir ve yetersiz uyumda iyi performans gösterebilir.",
                ]
            ),
            p(
                "Ana dezavantaj: sonuçlar kolay yorumlanamaz; sınıflandırma modelinin "
                "<em>anlamı</em> hakkında sonuç çıkarmak istiyorsanız rastgele ormanlar "
                "en iyi seçenek olmayabilir."
            ),
        ]
    ),
}

INSERTS = {
    2: addon(
        "helpers_05_08",
        "<p><code>helpers_05_08</code> modülü yalnızca orijinal kitabın ek deposunda "
        "bulunur; Pyodide'da etkileşimli ağaç görselleştirmesi çalışmayabilir. "
        "Statik karar ağacı örnekleri bu sayfada çalışır.</p>",
    ),
    17: try_it(
        "Şimdi deneyin",
        "İki blob üzerinde karar ağacı:",
        """from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier
X, y = make_blobs(n_samples=100, centers=2, random_state=0)
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X, y)
print("Doğruluk:", clf.score(X, y))""",
        "deneme_decision_tree.py",
    ),
    30: try_it(
        "Şimdi deneyin",
        "Digits verisinde rastgele orman:",
        """from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, random_state=0)
rf = RandomForestClassifier(n_estimators=100, random_state=0)
rf.fit(X_train, y_train)
print("Test doğruluğu:", rf.score(X_test, y_test))""",
        "deneme_random_forest_digits.py",
    ),
}

CODE_NAMES = {
    2: "imports_rf.py",
    8: "make_blobs_tree.py",
    13: "decision_tree_classifier.py",
    15: "visualize_classifier.py",
    17: "visualize_tree.py",
    19: "helpers_tree_depth.py",
    25: "helpers_tree_subset.py",
    28: "bagging_classifier.py",
    30: "random_forest_classifier.py",
    33: "regression_data.py",
    35: "random_forest_regressor.py",
    38: "load_digits_rf.py",
    40: "plot_digits_rf.py",
    42: "rf_train_test.py",
    44: "classification_report_rf.py",
    46: "confusion_matrix_rf.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.08-Random-Forests.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link("09-principal-component-analysis.html", "5.9 Temel Bileşen Analizi")
    path = write_chapter("08-random-forests", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
