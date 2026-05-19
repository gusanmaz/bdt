#!/usr/bin/env python3
"""Generate 09-principal-component-analysis.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, orig_line, p
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html"
EN_LABEL = "05.09 Principal Component Analysis"

TR = {
    0: h1("5.9 Derinlemesine: Temel Bileşen Analizi"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Şimdiye kadar etiketli eğitim verisine dayalı denetimli tahmin "
                "edicilerini inceledik. Burada bilinen etiketlere başvurmadan "
                "verinin ilginç yönlerini vurgulayan denetimsiz tahmin edicilere "
                "bakmaya başlıyoruz."
            ),
            p(
                "Bu bölümde en yaygın kullanılan denetimsiz algoritmalardan biri olan "
                "temel bileşen analizini (PCA) ele alacağız. PCA temelde boyut "
                "indirgeme algoritmasıdır; görselleştirme, gürültü filtreleme ve "
                "öznitelik çıkarımı için de kullanılır."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: h2("Temel Bileşen Analizine Giriş", "pca-giris"),
    5: p(
        "Gözle <em>x</em> ve <em>y</em> değişkenleri arasında neredeyse doğrusal bir "
        "ilişki olduğu görülür. Bu "
        '<a href="06-linear-regression.html">5.6 Doğrusal Regresyon</a> verisini '
        "anımsatır; ancak burada <em>y</em> değerlerini <em>x</em> değerlerinden "
        "tahmin etmek yerine, <em>x</em> ve <em>y</em> arasındaki ilişkiyi öğrenmeye "
        "çalışıyoruz."
    ),
    7: p(
        "PCA bu ilişkiyi verideki <em>temel eksenler</em> listesini bularak niceler. "
        "Scikit-Learn <code>PCA</code> tahmin edicisiyle bunu hesaplayabiliriz:"
    ),
    10: p(
        "Bu sayıların anlamını, bileşenleri girdi verisi üzerinde vektör olarak "
        "görselleştirerek görelim (aşağıdaki şekil):"
    ),
    12: p(
        "Bu vektörler verinin temel eksenlerini temsil eder; uzunlukları o eksene "
        "yansıtıldığında varyansın ne kadar \"önemli\" olduğunu gösterir."
    ),
    13: figure("05.09-PCA-rotation.png", "PCA dönüşümü"),
    14: p(
        "Veri eksenlerinden temel eksenlere bu dönüşüm, öteleme, dönme ve ölçümlemeden "
        "oluşan bir <em>affine dönüşümdür</em>."
    ),
    15: h3("Boyut İndirgeme Olarak PCA", "pca-boyut-indirgeme"),
    17: p(
        "Dönüştürülmüş veri tek boyuta indirgendi. Etkiyi görmek için ters dönüşümü "
        "yapıp orijinal veriyle birlikte çizebiliriz (aşağıdaki şekil):"
    ),
    19: p(
        "Açık noktalar orijinal veri, koyu noktalar yansıtılmış sürümdür. En az "
        "önemli eksen(ler) boyunca bilgi atılır; atılan varyans oranı yaklaşık olarak "
        "atılan bilgi miktarını ölçer."
    ),
    20: h3("Görselleştirme için PCA: El Yazısı Rakamlar", "pca-rakamlar"),
    22: p(
        "Digits veri kümesi 8×8 piksel görüntülerden oluşur — 64 boyutludur. "
        "İlişkileri görmek için PCA ile iki boyuta indirebiliriz:"
    ),
    24: p(
        "İlk iki temel bileşeni çizerek veri hakkında bilgi ediniriz (aşağıdaki şekil). "
        "Bu bileşenler 64 boyutlu nokta bulutunun en büyük varyans yönlerine yansımasıdır."
    ),
    26: p(
        "Veri 64 boyutlu bir nokta bulutudur; bu yansıtmalar en büyük varyans "
        "yönleri boyunca yapılır — denetimsiz biçimde, etiketlere başvurmadan."
    ),
    27: "\n".join(
        [
            h3("Bileşenler Ne Anlama Gelir?", "bilesen-anlami"),
            p(
                "Biraz daha ileri gidip indirgenmiş boyutların <em>ne anlama geldiğini</em> "
                "sorabiliriz. Bu anlam, temel vektörlerin kombinasyonları cinsinden "
                "anlaşılabilir. Örneğin eğitim kümesindeki her görüntü 64 piksel değeriyle "
                "tanımlanır; buna $x$ vektörü diyelim:"
            ),
            """    <p>$$
x = [x_1, x_2, x_3 \\cdots x_{64}]
$$</p>""",
            p(
                "Bunu piksel temeli cinsinden düşünebiliriz: görüntüyü oluşturmak için "
                "vektörün her elemanını ilgili pikselle çarpıp sonuçları toplarız:"
            ),
            """    <p>$$
{\\rm image}(x) = x_1 \\cdot{\\rm (piksel~1)} + x_2 \\cdot{\\rm (piksel~2)} + x_3 \\cdot{\\rm (piksel~3)} \\cdots x_{64} \\cdot{\\rm (piksel~64)}
$$</p>""",
            p(
                "Boyutu indirmek için bu temel vektörlerin çoğunu sıfırlayabiliriz. "
                "Örneğin yalnızca ilk sekiz pikseli kullanırsak sekiz boyutlu bir "
                "projeksiyon elde ederiz (aşağıdaki şekil); ancak görüntünün bütününü "
                "yansıtmaz — piksellerin neredeyse %90'ını attık!"
            ),
        ]
    ),
    28: figure("05.09-digits-pixel-components.png", "Piksel temel bileşenleri"),
    29: p(
        "Üst sıra tek tek pikselleri, alt sıra bu piksellerin görüntü oluşturmadaki "
        "kümülatif katkısını gösterir. Yalnızca sekiz piksel temel bileşeniyle "
        "64 piksellik görüntünün yalnızca küçük bir kısmı oluşturulur."
    ),
    30: "\n".join(
        [
            p(
                "Piksel temsili tek temel seçeneği değildir. Her pikselden önceden "
                "tanımlı katkı içeren başka temel fonksiyonlar da kullanılabilir:"
            ),
            """    <p>$$
{\\rm image}(x) = {\\rm mean} + x_1 \\cdot{\\rm (temel~1)} + x_2 \\cdot{\\rm (temel~2)} + x_3 \\cdot{\\rm (temel~3)} \\cdots
$$</p>""",
            p(
                "PCA, yalnızca ilk birkaçının toplanmasının veri kümesinin büyük "
                "kısmını uygun biçimde yeniden oluşturmasına yetecek optimal temel "
                "fonksiyonları seçme süreci olarak düşünülebilir. Temel bileşenler, "
                "verinin düşük boyutlu temsilidir. Aşağıdaki şekil aynı rakamı ortalama "
                "artı ilk sekiz PCA temel fonksiyonuyla yeniden oluşturmayı gösterir."
            ),
        ]
    ),
    31: figure("05.09-digits-pca-components.png", "PCA temel bileşenleri"),
    32: p(
        "Piksel temeline göre PCA temeli, yalnızca ortalama artı sekiz bileşenle "
        "girdinin belirgin özelliklerini kurtarır!"
    ),
    33: h3("Bileşen Sayısını Seçmek", "bilesen-sayisi"),
    35: p(
        "Bu eğri, toplam 64 boyutlu varyansın ilk $N$ bileşende ne kadarının "
        "kaldığını gösterir. İlk 10 bileşen yaklaşık %75 varyans içerir; "
        "%100'e yakın için yaklaşık 50 bileşen gerekir."
    ),
    36: h2("Gürültü Filtreleme Olarak PCA", "pca-gurultu"),
    38: p(
        "Önce gürültüsüz birkaç örnek çizelim (aşağıdaki şekil), sonra rastgele "
        "gürültü ekleyip yeniden çizelim:"
    ),
    41: p(
        "Gürültülü veride PCA ile varyansın %50'sini koruyarak projeksiyon "
        "isteyelim:"
    ),
    43: p(
        "%50 varyans 64 öznitelikten 12 temel bileşene karşılık gelir. Ters "
        "dönüşümle filtrelenmiş rakamları elde ederiz (aşağıdaki şekil)."
    ),
    45: p(
        "Bu sinyal koruma/gürültü filtreleme özelliği PCA'yı güçlü bir öznitelik "
        "seçimi rutini yapar."
    ),
    46: h2("Örnek: Öz Yüzler (Eigenfaces)", "ornek-eigenfaces"),
    48: p(
        "Daha önce yüz tanımada PCA projeksiyonunu öznitelik seçici olarak "
        '<a href="07-support-vector-machines.html">5.7 SVM</a> ile kullandık. '
        "LFW veri kümesine tekrar bakalım:"
    ),
    50: p(
        "İlk 150 bileşenle ilişkili görüntüler <em>öz yüzler</em> (eigenfaces) "
        "olarak bilinir (aşağıdaki şekil):"
    ),
    52: p(
        "İlk birkaç öz yüz aydınlatma açısıyla, sonrakiler göz, burun, dudak gibi "
        "özellikleri seçer gibi görünür."
    ),
    54: p(
        "150 bileşen varyansın biraz üzerinde %90'ını açıklar. Girdi ile "
        "150 bileşenden yeniden oluşturulan görüntüleri karşılaştırabiliriz "
        "(aşağıdaki şekil):"
    ),
    57: p(
        "Üst sıra girdi, alt sıra ~3.000 öznitelikten yalnızca 150 ile yeniden "
        "oluşturma. Boyutluluğu yaklaşık 20 kat azaltırken bireyler gözle "
        "tanınabilir kalır — "
        '<a href="07-support-vector-machines.html">5.7 SVM</a> örneğindeki PCA '
        "seçiminin neden başarılı olduğu anlaşılır."
    ),
    58: "\n".join(
        [
            h2("Özet", "ozet"),
            p(
                "Bu bölümde PCA'yı boyut indirgeme, görselleştirme, gürültü filtreleme "
                "ve öznitelik seçimi için kullandık."
            ),
            p(
                "PCA'nın ana zayıflığı aykırı değerlere karşı hassasiyettir; "
                "Scikit-Learn <code>sklearn.decomposition</code> alt modülünde "
                "<code>SparsePCA</code> gibi varyantlar vardır."
            ),
            p("Sonraki bölümlerde PCA fikirlerini genişleten denetimsiz yöntemlere bakacağız."),
        ]
    ),
}

INSERTS = {
    2: addon(
        "Varyans oranı",
        "<p><code>explained_variance_ratio_</code> her bileşenin toplam varyansa "
        "katkısını verir. Yüksek boyutta ilk birkaç bileşene bakarak verinin "
        "içsel boyutunu kestirebilirsiniz.</p>",
    ),
    6: try_it(
        "Şimdi deneyin",
        "İki boyutlu veriye PCA uygulayın:",
        """import numpy as np
from sklearn.decomposition import PCA
rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
pca = PCA(n_components=2)
pca.fit(X)
print("Bileşenler:\\n", pca.components_)
print("Açıklanan varyans:", pca.explained_variance_ratio_)""",
        "deneme_pca_2d.py",
    ),
    23: try_it(
        "Şimdi deneyin",
        "Digits verisini 2D'ye indirin:",
        """from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
digits = load_digits()
proj = PCA(2).fit_transform(digits.data)
print("Projeksiyon şekli:", proj.shape)""",
        "deneme_pca_digits.py",
    ),
}

CODE_NAMES = {
    2: "imports_pca.py",
    4: "pca_sample_data.py",
    6: "pca_fit.py",
    8: "pca_components_print.py",
    9: "pca_variance_print.py",
    11: "draw_vector.py",
    16: "pca_n_components_1.py",
    18: "pca_inverse_transform.py",
    21: "load_digits_pca.py",
    23: "pca_2d_digits.py",
    25: "pca_scatter_digits.py",
    34: "pca_full_fit_digits.py",
    37: "plot_digits_fn.py",
    39: "add_noise_digits.py",
    40: "plot_noisy_digits.py",
    42: "pca_denoise_fit.py",
    44: "pca_denoise_inverse.py",
    47: "fetch_lfw_pca.py",
    49: "pca_eigenfaces.py",
    51: "plot_eigenfaces.py",
    53: "pca_variance_cumsum.py",
    55: "pca_reconstruct_faces.py",
    56: "plot_reconstructed_faces.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.09-Principal-Component-Analysis.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link("10-manifold-learning.html", "5.10 Manifold Öğrenme")
    path = write_chapter("09-principal-component-analysis", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
