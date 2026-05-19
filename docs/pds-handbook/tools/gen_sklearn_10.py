#!/usr/bin/env python3
"""Generate 10-manifold-learning.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, h4, orig_line, p, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.10-manifold-learning.html"
EN_LABEL = "05.10 Manifold Learning"

TR = {
    0: h1("5.10 Derinlemesine: Manifold Öğrenme"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                'Önceki bölümde PCA\'nın boyut indirgeme için nasıl kullanıldığını gördük. '
                "PCA esnek ve hızlı olsa da veride <em>doğrusal olmayan</em> ilişkiler "
                "olduğunda iyi performans göstermez."
            ),
            p(
                "Bu eksikliği gidermek için <em>manifold öğrenme algoritmalarına</em> "
                "dönebiliriz — veri kümelerini yüksek boyutlu uzaylara gömülü düşük "
                "boyutlu manifoldlar olarak tanımlamaya çalışan denetimsiz tahmin ediciler."
            ),
            p(
                "Manifold düşünürken bir kağıt yaprağını hayal edin: üç boyutlu "
                "dünyamızda yaşayan iki boyutlu bir nesne. Kağıdı bükmek, kıvırmak "
                "veya buruşturmak onu hâlâ iki boyutlu bir manifold yapar; ancak "
                "üç boyutlu uzaya gömülüş artık doğrusal değildir."
            ),
            p(
                "Burada MDS, yerel doğrusal gömme (LLE) ve izometrik haritalama (Isomap) "
                "gibi yöntemleri inceleyeceğiz."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: h2('Manifold Öğrenme: "HELLO"', "manifold-hello"),
    5: p(
        'Kavramları netleştirmek için "HELLO" kelimesi şeklinde iki boyutlu veri '
        "üreten bir fonksiyonla başlayalım:"
    ),
    7: p(
        'Çıktı iki boyutludur ve "HELLO" şeklinde noktalardan oluşur. Bu biçim, '
        "algoritmaların ne yaptığını görsel olarak anlamamıza yardımcı olur."
    ),
    8: h2("Çok Boyutlu Ölçekleme (MDS)", "mds"),
    10: p(
        "Verinin <em>x</em> ve <em>y</em> değerleri en temel tanım olmayabilir; "
        "ölçekleme, döndürme veriyi değiştirse de \"HELLO\" yapısı kalır (aşağıdaki şekil)."
    ),
    12: p(
        "Burada temel olan noktalar arasındaki <em>uzaklıktır</em>. $N$ nokta için "
        "$(i,j)$ girişi $i$ ile $j$ arasındaki uzaklığı içeren $N \\times N$ bir "
        "uzaklık matrisi kurarız:"
    ),
    14: p(
        "$N$=1.000 nokta için 1000×1000 matris elde ederiz (aşağıdaki şekil). "
        "Döndürülmüş ve ötelenmiş veri için de aynı uzaklık matrisi oluşur."
    ),
    16: p(
        "Uzaklık matrisi dönme ve ötelemeye karşı değişmezdir; ancak görselleştirme "
        "sezgisel değildir — \"HELLO\" yapısı kaybolur. MDS tam olarak uzaklık "
        "matrisinden $D$ boyutlu koordinat temsilini kurtarmaya çalışır:"
    ),
    18: p(
        "MDS algoritması, yalnızca $N\\times N$ uzaklık matrisini kullanarak "
        "olası iki boyutlu koordinat gösterimlerinden birini kurtarır."
    ),
    19: h3("Manifold Öğrenme Olarak MDS", "mds-manifold"),
    21: p(
        "Uzaklık matrisleri herhangi bir boyuttaki veriden hesaplanabilir. "
        "Veriyi üç boyuta yansıtıp MDS ile iki boyutlu gömme isteyebiliriz "
        "(aşağıdaki şekil):"
    ),
    23: p(
        "Üç boyutlu veriyi girdi olarak verip MDS tahmin edicisi uzaklık matrisini "
        "hesaplayıp bu uzaklık matrisi için optimal iki boyutlu gömmeyi belirler "
        "(aşağıdaki şekil)."
    ),
    25: "\n".join(
        [
            p(
                "Bu, manifold öğrenme tahmin edicisinin hedefinin özüdür: yüksek boyutlu "
                "gömülü veri verildiğinde, veri içindeki belirli ilişkileri koruyan "
                "düşük boyutlu bir temsil aranır. MDS durumunda korunan nicelik her "
                "nokta çifti arasındaki uzaklıktır."
            ),
        ]
    ),
    26: h3("Doğrusal Olmayan Gömme: MDS'in Başarısız Olduğu Yer", "mds-dogrusal-olmayan"),
    28: p(
        "Veri üç boyutlu olsa da gömme daha karmaşıktır (aşağıdaki şekil). "
        "Veri \"S\" şeklinde bükülmüştür."
    ),
    30: p(
        "Temel ilişkiler hâlâ vardır; ancak veri doğrusal olmayan biçimde dönüştürülmüştür."
    ),
    32: p(
        "Basit MDS bu doğrusal olmayan gömülüşü \"açamaz\"; en iyi iki boyutlu "
        "<em>doğrusal</em> gömme orijinal $y$ eksenini atar (aşağıdaki şekil)."
    ),
    33: h2("Doğrusal Olmayan Manifoldlar: Yerel Doğrusal Gömme", "lle"),
    34: figure("05.10-LLE-vs-MDS.png", "LLE ve MDS bağlantıları"),
    35: p(
        "Solda MDS her nokta çifti arasındaki uzaklığı korumaya çalışır. Sağda "
        "<em>yerel doğrusal gömme</em> (LLE) yalnızca <em>komşu</em> noktalar "
        "arasındaki uzaklıkları korumaya çalışır. LLE, bu mantığı yansıtan bir "
        "maliyet fonksiyonunun küresel optimizasyonuyla veriyi açabilir "
        "(aşağıdaki şekil)."
    ),
    37: p(
        "Sonuç orijinal manifolda göre biraz bozuk kalsa da verideki temel "
        "ilişkileri yakalar!"
    ),
    38: h2("Manifold Yöntemleri Hakkında Düşünceler", "manifold-dusunceler"),
    39: "\n".join(
        [
            p(
                "Pratikte manifold teknikleri genelde yüksek boyutlu verinin basit "
                "nitel görselleştirmesinden öteye nadiren kullanılır."
            ),
            p("Manifold öğrenmenin PCA'ya kıyasla zorlukları:"),
            ul(
                [
                    "Eksik veri için iyi bir çerçeve yoktur; PCA'da yinelemeli yaklaşımlar vardır.",
                    "Gürültü manifoldu \"kısa devre\" edebilir; PCA gürültüyü filtreler.",
                    "Komşu sayısı seçimi kritiktir ve genelde optimal seçim için sağlam bir ölçüt yoktur.",
                    "Çıktı boyutu küresel olarak optimal belirlenmesi zordur.",
                    "Gömülü boyutların anlamı her zaman net değildir.",
                    "Hesaplama maliyeti genelde $O[N^2]$ veya $O[N^3]$ ölçeklenir.",
                ]
            ),
            p(
                "Manifold yöntemlerinin PCA'ya tek net üstünlüğü doğrusal olmayan "
                "ilişkileri korumasıdır; bu yüzden veriyi önce PCA ile keşfederim."
            ),
            p(
                "Scikit-Learn LLE ve Isomap dışında birçok manifold yöntemi sunar. "
                "Öneriler: oyuncak S-eğrisi için modified LLE; gerçek yüksek boyutlu "
                "veride Isomap; güçlü kümeleme için t-SNE (yavaş olabilir)."
            ),
        ]
    ),
    40: h2("Örnek: Yüzlerde Isomap", "ornek-isomap-yuzler"),
    42: p(
        "2.370 görüntü, her biri 2.914 piksel — görüntüler 2.914 boyutlu uzayda "
        "noktalar gibidir! Birkaç görüntüyü gösterelim (aşağıdaki şekil):"
    ),
    44: p(
        '<a href="09-principal-component-analysis.html">5.9 PCA</a> bölümünde '
        "sıkıştırma amacıyla bileşenleri kullanmıştık. Burada düşük boyutlu gömme "
        "ile görüntüler arası ilişkileri öğrenmek istiyoruz:"
    ),
    46: p(
        "Bu veri için %90 varyansı korumak yaklaşık 100 bileşen gerektirir — veri "
        "içsel olarak çok yüksek boyutludur. Bu durumda LLE ve Isomap yardımcı olabilir."
    ),
    48: p(
        "Çıktı, tüm girdi görüntülerinin iki boyutlu yansımasıdır. Küçük resimlerle "
        "görselleştirmek için bir fonksiyon tanımlayabiliriz:"
    ),
    50: p("Bu fonksiyonu çağırdığımızda sonuç aşağıdaki şekildedir:"),
    52: p(
        "İlk iki Isomap boyutu genel parlaklık ve yüz yönelimini betimler gibi görünür."
    ),
    53: h2("Örnek: Rakamlarda Yapıyı Görselleştirme", "ornek-mnist-manifold"),
    55: p(
        "MNIST veri kümesi 70.000 görüntü, her biri 784 piksel (28×28). "
        "İlk birkaç görüntüye bakalım (aşağıdaki şekil):"
    ),
    57: p(
        "El yazısı stillerinin çeşitliliğine dair fikir verir. Hız için verinin "
        "1/30'unu kullanarak manifold projeksiyonu hesaplayalım (aşağıdaki şekil):"
    ),
    59: p(
        "Tek bir rakamı (örneğin 1) vurgulayarak projeksiyonda biçim çeşitliliğini "
        "görebiliriz (aşağıdaki şekil):"
    ),
    61: p(
        "1 rakamının veri kümesindeki biçim çeşitliliğine dair fikir verir. "
        "Projeksiyon, sınıflandırma için doğrudan yararlı olmasa da veriyi anlamaya "
        "ve ön işleme fikirlerine yardımcı olabilir."
    ),
}

INSERTS = {
    2: addon(
        "MNIST ve ağ",
        "<p><code>fetch_openml</code> MNIST için ağ indirmesi gerektirir; Pyodide'da "
        "ilk çalıştırma uzun sürebilir. Isomap ve LLE büyük veride yavaştır — "
        "alt örnekleme kullanın.</p>",
    ),
    17: try_it(
        "Şimdi deneyin",
        "HELLO verisinde MDS:",
        """import numpy as np
from sklearn.manifold import MDS
# make_hello fonksiyonu notebook'ta tanımlı; basit 2D örnek:
rng = np.random.RandomState(42)
X = rng.randn(50, 2)
emb = MDS(n_components=2, random_state=0).fit_transform(X)
print("Gömme şekli:", emb.shape)""",
        "deneme_mds.py",
    ),
    36: try_it(
        "Şimdi deneyin",
        "S-eğrisi verisinde LLE (sentetik veri gerektirir):",
        """from sklearn.manifold import LocallyLinearEmbedding
from sklearn.datasets import make_s_curve
X, _ = make_s_curve(200, random_state=0)
emb = LocallyLinearEmbedding(n_components=2, n_neighbors=15).fit_transform(X)
print("LLE gömme şekli:", emb.shape)""",
        "deneme_lle.py",
    ),
}

CODE_NAMES = {
    2: "imports_manifold.py",
    4: "make_hello.py",
    6: "hello_plot.py",
    9: "rotate_hello.py",
    11: "pairwise_distances.py",
    13: "distance_matrix_plot.py",
    15: "distance_matrix_rotated.py",
    17: "mds_hello.py",
    20: "random_projection.py",
    22: "hello_3d_plot.py",
    24: "mds_3d.py",
    27: "make_hello_s_curve.py",
    29: "s_curve_3d.py",
    31: "mds_s_curve.py",
    36: "lle_s_curve.py",
    41: "fetch_lfw_isomap.py",
    43: "plot_lfw_faces.py",
    45: "pca_lfw_variance.py",
    47: "isomap_faces.py",
    49: "plot_component_faces.py",
    51: "isomap_face_grid.py",
    54: "fetch_openml_mnist.py",
    56: "mnist_reshape.py",
    58: "isomap_mnist_subset.py",
    60: "isomap_digit_one.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.10-Manifold-Learning.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link("11-k-means.html", "5.11 K-Means Kümeleme")
    path = write_chapter("10-manifold-learning", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
