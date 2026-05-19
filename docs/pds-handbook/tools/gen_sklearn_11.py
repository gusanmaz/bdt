#!/usr/bin/env python3
"""Generate 11-k-means.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, h4, orig_line, p, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html"
EN_LABEL = "05.11 K-Means"

TR = {
    0: h1("5.11 Derinlemesine: K-Means Kümeleme"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Önceki bölümlerde boyut indirgeme için denetimsiz makine öğrenmesi "
                "modellerini inceledik. Şimdi denetimsiz makine öğrenmesinin bir başka "
                "sınıfına geçeceğiz: kümeleme algoritmaları. Kümeleme algoritmaları, "
                "verinin özelliklerinden yola çıkarak nokta gruplarının en uygun "
                "bölünmesini veya ayrık etiketlemesini öğrenmeye çalışır."
            ),
            p(
                "Scikit-Learn ve başka yerlerde birçok kümeleme algoritması vardır; "
                "ancak anlaşılması belki de en kolay olanı <em>k-means kümeleme</em> "
                "algoritmasıdır; <code>sklearn.cluster.KMeans</code> içinde uygulanmıştır."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: h2("k-Means'e Giriş", "k-means-giris"),
    4: "\n".join(
        [
            p(
                "<em>k</em>-means algoritması, etiketsiz çok boyutlu bir veri kümesinde "
                "önceden belirlenmiş sayıda küme arar. Bunu, optimal kümelemenin basit "
                "bir tanımına dayanarak yapar:"
            ),
            ul(
                [
                    "<em>Küme merkezi</em>, kümeye ait tüm noktaların aritmetik ortalamasıdır.",
                    "Her nokta kendi küme merkezine, diğer küme merkezlerine olduğundan daha yakındır.",
                ]
            ),
            p(
                "Bu iki varsayım <em>k</em>-means modelinin temelidir. Algoritmanın bu "
                "çözüme tam olarak <em>nasıl</em> ulaştığını yakında inceleyeceğiz; "
                "şimdilik basit bir veri kümesine bakıp <em>k</em>-means sonucunu görelim."
            ),
            p(
                "Önce dört ayrı blob içeren iki boyutlu bir veri kümesi üretelim. "
                "Bunun denetimsiz bir algoritma olduğunu vurgulamak için etiketleri "
                "görselleştirmeden çıkaracağız (aşağıdaki şekil):"
            ),
        ]
    ),
    6: p(
        "Gözle dört kümeyi seçmek nispeten kolaydır. "
        "<em>k</em>-means algoritması bunu otomatik yapar; Scikit-Learn'de tipik "
        "tahminci API'si kullanılır:"
    ),
    8: p(
        "Sonuçları, veriyi bu etiketlere göre renklendirerek görselleştirelim "
        "(aşağıdaki şekil). <em>k</em>-means tahmincisinin belirlediği küme "
        "merkezlerini de çizeceğiz:"
    ),
    10: p(
        "İyi haber şu: <em>k</em>-means algoritması (en azından bu basit durumda) "
        "noktaları kümelerine, gözle atayabileceğimiz şekle oldukça benzer atar. "
        "Ancak algoritmanın bu kümeleri bu kadar hızlı nasıl bulduğunu merak "
        "edebilirsiniz: küme atamalarının olası kombinasyon sayısı veri noktası "
        "sayısında üsteldir — tüm arama çok, çok maliyetli olurdu. Neyse ki böyle "
        "kapsamlı bir arama gerekmez: bunun yerine <em>k</em>-means'te tipik yaklaşım, "
        "<em>beklenti–maksimizasyon</em> (E–M) adı verilen sezgisel yinelemeli bir "
        "yöntemdir."
    ),
    11: h2("Beklenti–Maksimizasyon", "beklenti-maksimizasyon"),
    12: "\n".join(
        [
            p(
                "Beklenti–maksimizasyon (E–M), veri biliminde çeşitli bağlamlarda "
                "karşımıza çıkan güçlü bir algoritmadır. <em>k</em>-means, algoritmanın "
                "özellikle basit ve anlaşılır bir uygulamasıdır; burada kısaca adımlarını "
                "göreceğiz. Kısaca E–M yaklaşımı şu prosedürden oluşur:"
            ),
            ul(
                [
                    "Bazı küme merkezlerini tahmin edin.",
                    "Yakınsayana kadar tekrarlayın:",
                    "<em>E-adımı</em>: Noktaları en yakın küme merkezine atayın.",
                    "<em>M-adımı</em>: Küme merkezlerini atanan noktaların ortalaması yapın.",
                ]
            ),
            p(
                "Burada <em>E-adımı</em> veya <em>beklenti adımı</em>, her noktanın "
                "hangi kümeye ait olduğu beklentimizi güncellediğimiz için böyle adlandırılır. "
                "<em>M-adımı</em> veya <em>maksimizasyon adımı</em>, küme merkezlerinin "
                "konumunu tanımlayan bir uygunluk fonksiyonunu maksimize ettiğimiz için "
                "böyle adlandırılır — burada bu maksimizasyon, her kümedeki verinin "
                "basit ortalaması alınarak yapılır."
            ),
            p(
                "Bu algoritma hakkındaki literatür geniştir; tipik koşullar altında E- "
                "ve M-adımının her tekrarı küme özelliklerinin daha iyi bir tahminini "
                "verir. Algoritmayı aşağıdaki şekilde görselleştirebiliriz. "
                "Buradaki başlangıç için kümeler yalnızca üç yinelemede yakınsar. "
                "(Etkileşimli sürüm için çevrimiçi "
                '<a href="https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb#Interactive-K-Means" '
                'target="_blank" rel="noopener">ek</a> koduna bakın.)'
            ),
        ]
    ),
    13: figure(
        "05.11-expectation-maximization.png",
        "k-means beklenti–maksimizasyon adımları",
        "E–M ile k-means yinelemesi (orijinal kitap ekinden).",
    ),
    14: p(
        "<em>k</em>-means algoritması birkaç satır kodla yazılabilecek kadar "
        "basittir. Aşağıdaki çok temel bir uygulamadır (aşağıdaki şekil):"
    ),
    16: p(
        "İyi test edilmiş uygulamalar kaputun altında biraz daha fazlasını yapar; "
        "ancak önceki fonksiyon E–M yaklaşımının özünü verir."
    ),
    17: p(
        "Beklenti–maksimizasyon algoritmasını kullanırken dikkat edilmesi gereken "
        "birkaç uyarı vardır:"
    ),
    18: "\n".join(
        [
            h4("Küresel en iyi sonuç garanti edilmez", "global-optimum"),
            p(
                "Öncelikle, E–M prosedürü her adımda sonucu iyileştirmeyi garanti etse de, "
                "küresel en iyi çözüme ulaşacağına dair güvence yoktur. Örneğin basit "
                "prosedürümüzde farklı bir rastgele tohum kullanırsak, başlangıç tahminleri "
                "kötü sonuçlara yol açabilir (aşağıdaki şekil):"
            ),
        ]
    ),
    20: p(
        "E–M prosedürü her adımda sonucu iyileştirmeyi garanti etse de, "
        "<em>küresel</em> en iyi çözüme ulaşacağına dair güvence yoktur. "
        "Bu yüzden algoritmanın birden fazla başlangıç tahminiyle çalıştırılması "
        "yaygındır; Scikit-Learn bunu varsayılan olarak yapar "
        "(<code>n_init</code> parametresi, varsayılan 10)."
    ),
    21: "\n".join(
        [
            h4("Küme sayısı önceden seçilmelidir", "kume-sayisi"),
            p(
                "<em>k</em>-means'in bir başka yaygın zorluğu, kaç küme beklediğinizi "
                "söylemeniz gerekmesidir: küme sayısını veriden öğrenemez. Örneğin "
                "algoritmaya altı küme tanımlamasını istersek, en iyi altı kümeyi "
                "mutlu bir şekilde bulur (aşağıdaki şekil):"
            ),
        ]
    ),
    23: "\n".join(
        [
            p(
                "Sonucun anlamlı olup olmadığı kesin yanıtlanması zor bir sorudur; "
                "burada daha fazla ele almayacağımız sezgisel bir yaklaşım "
                '<a href="https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html" '
                'target="_blank" rel="noopener">silhouette analizi</a> adını alır.'
            ),
            p(
                "Alternatif olarak, küme sayısına göre uygunluğu daha iyi ölçen daha "
                "karmaşık bir kümeleme algoritması (ör. Gauss karışımları; bkz. "
                '<a href="12-gaussian-mixtures.html">5.12 Gauss Karışımları</a>) '
                "veya uygun küme sayısını seçebilen bir algoritma "
                "(DBSCAN, mean-shift, affinity propagation — "
                "<code>sklearn.cluster</code> alt modülünde) kullanılabilir."
            ),
        ]
    ),
    24: "\n".join(
        [
            h4("k-means doğrusal küme sınırlarıyla sınırlıdır", "dogrusal-sinir"),
            p(
                "<em>k</em>-means'in temel model varsayımları (noktalar kendi küme "
                "merkezlerine diğerlerinden daha yakındır), kümelerin karmaşık "
                "geometrileri olduğunda algoritmanın sık sık etkisiz kalmasına yol "
                "açar. Özellikle <em>k</em>-means kümeleri arasındaki sınırlar "
                "her zaman doğrusaldır; daha karmaşık sınırlarda başarısız olur. "
                "Aşağıdaki veriyi ve tipik <em>k</em>-means yaklaşımının bulduğu "
                "küme etiketlerini düşünün (aşağıdaki şekil):"
            ),
        ]
    ),
    27: "\n".join(
        [
            p(
                "Bu durum "
                '<a href="07-support-vector-machines.html">5.7 Destek Vektör Makineleri</a> '
                "bölümündeki tartışmayı anımsatır: veriyi doğrusal ayrımın mümkün "
                "olduğu daha yüksek boyuta çevirmek için çekirdek dönüşümü kullanmıştık. "
                "Aynı numarayı <em>k</em>-means'in doğrusal olmayan sınırlar keşfetmesine "
                "izin vermek için kullanabiliriz."
            ),
            p(
                "Bu çekirdekli <em>k</em>-means'in bir sürümü Scikit-Learn'de "
                "<code>SpectralClustering</code> tahmincisi içinde uygulanmıştır. "
                "En yakın komşu grafiğini kullanarak verinin daha yüksek boyutlu "
                "temsilini hesaplar, ardından <em>k</em>-means ile etiketler atar "
                "(aşağıdaki şekil):"
            ),
        ]
    ),
    29: p(
        "Bu çekirdek dönüşümü yaklaşımıyla, çekirdekli <em>k</em>-means kümeler "
        "arasındaki daha karmaşık doğrusal olmayan sınırları bulabilir."
    ),
    30: "\n".join(
        [
            h4("k-means çok sayıda örnekte yavaş olabilir", "buyuk-ornek"),
            p(
                "<em>k</em>-means'in her yinelemesi veri kümesindeki her noktaya "
                "erişmek zorunda olduğundan, örnek sayısı arttıkça algoritma "
                "görece yavaşlayabilir. Her yinelemede tüm veriyi kullanma "
                "gereksinimi gevşetilebilir mi diye düşünebilirsiniz; örneğin "
                "her adımda küme merkezlerini güncellemek için verinin bir alt "
                "kümesini kullanmak. Bu, mini-batch <em>k</em>-means algoritmalarının "
                "fikridir; bunlardan biri <code>sklearn.cluster.MiniBatchKMeans</code> "
                "içinde uygulanmıştır. Arayüz standart <code>KMeans</code> ile "
                "aynıdır; tartışmaya devam ederken bir örneğini göreceğiz."
            ),
        ]
    ),
    31: "\n".join(
        [
            h2("Örnekler", "ornekler"),
            p(
                "Algoritmanın bu sınırlamalarına dikkat ederek <em>k</em>-means'i "
                "çeşitli durumlarda kullanabiliriz. Şimdi birkaç örneğe bakalım."
            ),
        ]
    ),
    32: "\n".join(
        [
            h3("Örnek 1: Rakamlarda k-Means", "ornek-rakamlar"),
            p(
                "Başlangıç olarak "
                '<a href="08-random-forests.html">5.8 Rastgele Ormanlar</a> ve '
                '<a href="09-principal-component-analysis.html">5.9 Temel Bileşen Analizi</a> '
                "bölümlerinde gördüğümüz basit rakam verisine <em>k</em>-means "
                "uygulayalım. Orijinal etiket bilgisini <em>kullanmadan</em> benzer "
                "rakamları tanımlamaya çalışacağız; bu, <em>a priori</em> etiket "
                "bilginiz olmayan yeni bir veri kümesinden anlam çıkarmanın ilk "
                "adımına benzer olabilir."
            ),
            p(
                "Veri kümesini yükleyip kümeleri bulacağız. Digits veri kümesi "
                "1.797 örnek ve 64 öznitelikten oluşur; her öznitelik 8×8 "
                "görüntüdeki bir pikselin parlaklığıdır:"
            ),
        ]
    ),
    34: p("Kümeleme daha önce yaptığımız gibi yapılabilir:"),
    36: p(
        "Sonuç 64 boyutta 10 kümedir. Küme merkezlerinin kendileri 64 boyutlu "
        "noktalardır ve küme içindeki \"tipik\" rakamı temsil eder. "
        "Bu küme merkezlerinin nasıl göründüğüne bakalım (aşağıdaki şekil):"
    ),
    38: p(
        "<em>k</em>-means etiketler hakkında hiçbir şey bilmediği için 0–9 "
        "etiketleri permüte olabilir. Her öğrenilen küme etiketini kümelerde "
        "bulunan gerçek etiketlerle eşleştirerek düzeltebiliriz:"
    ),
    40: p(
        "Denetimsiz kümelemenin veride benzer rakamları bulmada ne kadar "
        "başarılı olduğunu kontrol edebiliriz:"
    ),
    42: p(
        "Basit bir <em>k</em>-means algoritmasıyla girdi rakamlarının %80'i "
        "için doğru gruplamayı bulduk! Bunun karışıklık matrisine bakalım "
        "(aşağıdaki şekil):"
    ),
    44: "\n".join(
        [
            p(
                "Daha önce görselleştirdiğimiz küme merkezlerinden beklenebileceği gibi "
                "asıl karışıklık sekizler ve birler arasındadır. Yine de <em>k</em>-means "
                "ile, bilinen etiketlere referans olmadan esasen bir rakam sınıflandırıcısı "
                "kurabileceğimizi gösterir!"
            ),
            p(
                "Eğlence için biraz daha ileri gidelim. "
                '<a href="10-manifold-learning.html">5.10 Manifold Öğrenme</a> '
                "bölümünde bahsedilen t-dağıtımlı stokastik komşu gömme (t-SNE) "
                "algoritmasını, <em>k</em>-means öncesinde veriyi ön işlemek için "
                "kullanabiliriz. t-SNE, kümeler içindeki noktaları koruma konusunda "
                "özellikle başarılı doğrusal olmayan bir gömme algoritmasıdır. "
                "Nasıl yaptığına bakalım:"
            ),
        ]
    ),
    46: p(
        "Bu, etiketleri <em>kullanmadan</em> %94 sınıflandırma doğruluğu. "
        "Denetimsiz öğrenmenin dikkatli kullanıldığında gücü budur: veri kümesinden "
        "elle veya gözle çıkarması zor bilgileri çıkarabilir."
    ),
    47: "\n".join(
        [
            h3("Örnek 2: Renk Sıkıştırma için k-Means", "ornek-renk"),
            p(
                "Kümelemenin ilginç uygulamalarından biri görüntülerde renk "
                "sıkıştırmasıdır (bu örnek Scikit-Learn'in "
                '<a href="https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html" '
                'target="_blank" rel="noopener">"Color Quantization Using K-Means"</a> '
                "örneğinden uyarlanmıştır). Örneğin milyonlarca rengi olan bir "
                "görüntünüz olduğunu düşünün. Çoğu görüntüde renklerin büyük "
                "kısmı kullanılmaz; birçok piksel benzer veya özdeş renklere sahiptir."
            ),
            p(
                "Aşağıdaki şekilde Scikit-Learn <code>datasets</code> modülünden "
                "bir görüntü düşünün (bunun çalışması için <code>PIL</code> "
                "Python paketinin kurulu olması gerekir):"
            ),
        ]
    ),
    49: p(
        "Görüntü kendisi <code>(yükseklik, genişlik, RGB)</code> boyutunda üç "
        "boyutlu bir dizide saklanır; kırmızı/mavi/yeşil katkılar 0–255 arası "
        "tamsayıdır:"
    ),
    51: p(
        "Bu pikselleri üç boyutlu renk uzayında bir nokta bulutu olarak "
        "görebiliriz. Veriyi <code>[n_samples, n_features]</code> biçimine "
        "getirip renkleri 0–1 arasına ölçekleriz:"
    ),
    53: p(
        "Bu pikselleri renk uzayında görselleştirebiliriz; verimlilik için "
        "10.000 piksellik bir alt küme kullanıyoruz (aşağıdaki şekil):"
    ),
    56: p(
        "Şimdi piksel uzayında <em>k</em>-means kümelemesiyle 16 milyon rengi "
        "16 renge indirelim. Çok büyük bir veri kümesiyle uğraştığımız için "
        "standart <em>k</em>-means'ten çok daha hızlı sonuç veren mini-batch "
        "<em>k</em>-means kullanacağız (aşağıdaki şekil):"
    ),
    58: p(
        "Sonuç, her piksele en yakın küme merkezinin renginin atandığı "
        "orijinal piksellerin yeniden renklendirilmesidir. Bu yeni renkleri "
        "piksel uzayı yerine görüntü uzayında çizersek etkiyi görürüz "
        "(aşağıdaki şekil):"
    ),
    60: p(
        "Sağ panelde kesinlikle ayrıntı kaybı var; ancak genel görüntü hâlâ "
        "kolayca tanınır. Ham veriyi saklamak için gereken bayt açısından sağdaki "
        "görüntü yaklaşık 1 milyonluk bir sıkıştırma faktörü sağlar! Bu tür "
        "yaklaşım JPEG gibi özel görüntü sıkıştırma şemalarının kalitesine "
        "ulaşmaz; ancak <em>k</em>-means gibi denetimsiz yöntemlerle kutu "
        "dışında düşünmenin gücünü gösterir."
    ),
}

INSERTS = {
    2: addon(
        "Pyodide",
        "Bu bölümdeki <code>load_sample_image</code> örneği <code>PIL</code> "
        "gerektirir; tarayıcıda Pyodide ortamında PIL sınırlı olabilir. "
        "Tam renk sıkıştırma demosu için yerel Jupyter notebook kullanın.",
    ),
    10: try_it(
        "",
        "Sentetik blob verisinde k-means deneyin:",
        """import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=200, centers=3, random_state=0)
labels = KMeans(n_clusters=3, random_state=0).fit_predict(X)
print(np.bincount(labels))""",
        "deneme_kmeans_blob.py",
    ),
    38: try_it(
        "",
        "Digits verisinde k-means küme sayısını değiştirin:",
        """from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
digits = load_digits()
km = KMeans(n_clusters=10, random_state=0, n_init=10)
clusters = km.fit_predict(digits.data)
print("Küme boyutları:", [sum(clusters == i) for i in range(10)])""",
        "deneme_kmeans_digits.py",
    ),
}

CODE_NAMES = {
    2: "imports_kmeans.py",
    5: "make_blobs.py",
    7: "kmeans_fit.py",
    9: "kmeans_scatter.py",
    15: "find_clusters_em.py",
    19: "em_bad_seed.py",
    22: "kmeans_six_clusters.py",
    25: "make_moons.py",
    26: "kmeans_moons_fail.py",
    28: "spectral_clustering.py",
    33: "load_digits.py",
    35: "kmeans_digits.py",
    37: "cluster_centers_plot.py",
    39: "match_cluster_labels.py",
    41: "cluster_accuracy.py",
    43: "confusion_matrix_digits.py",
    45: "tsne_kmeans_digits.py",
    48: "load_sample_image.py",
    50: "china_shape.py",
    52: "reshape_color_data.py",
    54: "plot_pixels_fn.py",
    55: "plot_color_space.py",
    57: "minibatch_kmeans_colors.py",
    59: "recolored_image.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.11-K-Means.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link("12-gaussian-mixtures.html", "5.12 Gauss Karışımları")
    path = write_chapter("11-k-means", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
