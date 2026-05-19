#!/usr/bin/env python3
"""Generate 14-image-features.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, next_link, try_it
from nb_html_utils import build_from_notebook, h1, h2, h3, orig_line, p, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.14-image-features.html"
EN_LABEL = "05.14 Image Features"

TR = {
    0: h1("5.14 Uygulama: Yüz Algılama Hattı"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Kitabın bu bölümü makine öğrenmesinin merkezi kavram ve "
                "algoritmalarının birçoğunu inceledi. Ancak bu kavramlardan "
                "gerçek dünya uygulamasına geçmek zor olabilir. Gerçek veri "
                "kümeleri gürültülü ve heterojendir; eksik öznitelikler olabilir, "
                "veri temiz <code>[n_samples, n_features]</code> matrisine "
                "dönüştürmek zor olabilir. Burada tartıştığımız yöntemleri "
                "uygulamadan önce veriden öznitelik çıkarmanız gerekir — "
                "tüm alanlara uyan tek bir formül yoktur; veri bilimci olarak "
                "kendi sezginiz ve uzmanlığınızı kullanırsınız."
            ),
            p(
                "Makine öğrenmesinin ilginç uygulamalarından biri görüntülerdir; "
                "piksel düzeyinde özniteliklerle sınıflandırma örneklerini "
                "görmüştük. Gerçek dünya verisi nadiren bu kadar düzenlidir; "
                "basit pikseller yeterli olmaz — bu da görüntü verisi için "
                "geniş bir <em>öznitelik çıkarma</em> literatürüne yol açmıştır "
                '(bkz. <a href="04-feature-engineering.html">5.4 Öznitelik Mühendisliği</a>).'
            ),
            p(
                "Bu bölümde bir öznitelik çıkarma tekniğine bakacağız: "
                '<a href="https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients" '
                'target="_blank" rel="noopener">yönelim gradyan histogramı (HOG)</a>. '
                "HOG, aydınlatma gibi karıştırıcı faktörlerden bağımsız geniş "
                "bilgi taşıyan görüntü özelliklerine duyarlı vektör temsiline "
                "dönüştürür. Bu özniteliklerle kitabın bu bölümünde gördüğümüz "
                "makine öğrenmesi algoritmaları ve kavramlarıyla basit bir yüz "
                "algılama hattı geliştireceğiz."
            ),
            p("Standart içe aktarmalarla başlayalım:"),
        ]
    ),
    3: "\n".join(
        [
            h2("HOG Öznitelikleri", "hog-oznitelik"),
            p(
                "HOG, görüntülerde yaya tanıma bağlamında geliştirilmiş "
                "doğrudan bir öznitelik çıkarma prosedürüdür. Adımlar:"
            ),
            ul(
                [
                    "İsteğe bağlı görüntü ön normalleştirme — aydınlatma değişimlerine karşı dayanıklı öznitelikler.",
                    "Yatay ve dikey parlaklık gradyanlarına duyarlı iki filtre ile evrişim — kenar, kontur ve doku.",
                    "Görüntüyü hücrelere bölüp her hücrede gradyan yönelim histogramı.",
                    "Komşu hücre bloğuyla karşılaştırarak hücre histogramlarını normalleştirme.",
                    "Her hücreden tek boyutlu öznitelik vektörü oluşturma.",
                ]
            ),
            p(
                "Hızlı bir HOG çıkarıcı Scikit-Image projesinde yerleşiktir; "
                "her hücredeki yönelim gradyanlarını görece hızlıca deneyip "
                "görselleştirebiliriz (aşağıdaki şekil):"
            ),
        ]
    ),
    5: "\n".join(
        [
            h2("HOG Uygulamada: Basit Yüz Dedektörü", "hog-yuz-dedektor"),
            p(
                "Bu HOG öznitelikleriyle herhangi bir Scikit-Learn tahmincisiyle "
                "basit yüz algılama algoritması kurulabilir; burada doğrusal destek "
                "vektör makinesi kullanacağız "
                '(<a href="07-support-vector-machines.html">5.7 SVM</a> hatırlatması). '
                "Adımlar:"
            ),
            ul(
                [
                    "Pozitif eğitim örnekleri: çeşitli yüz küçük resimleri.",
                    "Negatif eğitim örnekleri: yüz içermeyen küçük resimler.",
                    "Bu örneklerden HOG öznitelikleri çıkarın.",
                    "Doğrusal SVM eğitin.",
                    "Bilinmeyen görüntüde kayan pencereyle modeli değerlendirin.",
                    "Algılamalar örtüşürse birleştirin.",
                ]
            ),
            p("Adımları uygulayıp deneyelim."),
        ]
    ),
    6: "\n".join(
        [
            h3("1. Pozitif Eğitim Örnekleri", "pozitif-ornekler"),
            p(
                "Çeşitli yüzleri gösteren pozitif eğitim örnekleriyle başlayacağız. "
                "Kolay bir veri kümesi Labeled Faces in the Wild; Scikit-Learn ile "
                "indirilebilir:"
            ),
        ]
    ),
    8: p("Bu, eğitim için 13.000 yüz görüntüsü verir."),
    9: "\n".join(
        [
            h3("2. Negatif Eğitim Örnekleri", "negatif-ornekler"),
            p(
                "Sonra yüz <em>içermeyen</em>, benzer boyutlu küçük resimlere "
                "ihtiyacımız var. Girdi görüntü küpusundan çeşitli ölçeklerde "
                "küçük resimler çıkarılabilir. Burada Scikit-Image ile gelen "
                "görüntüleri ve Scikit-Learn <code>PatchExtractor</code>'ı kullanacağız:"
            ),
        ]
    ),
    13: p(
        "Artık yüz içermeyen 30.000 uygun görüntü yamasına sahibiz. "
        "Birkaçını görselleştirelim (aşağıdaki şekil):"
    ),
    15: p(
        "Umarız bunlar algoritmanın göreceği \"yüz olmayan\" uzayını "
        "yeterince kapsar."
    ),
    16: "\n".join(
        [
            h3("3. Kümeleri Birleştirip HOG Çıkarma", "hog-cikarma"),
            p(
                "Pozitif ve negatif örnekler hazır; birleştirip HOG özniteliklerini "
                "hesaplayabiliriz. Her görüntü için önemli hesaplama gerektiğinden "
                "bu adım biraz sürer:"
            ),
        ]
    ),
    19: p(
        "1.215 boyutta 43.000 eğitim örneğimiz kaldı; veriyi Scikit-Learn'e "
        "besleyebilecek biçimdeyiz!"
    ),
    20: "\n".join(
        [
            h3("4. Destek Vektör Makinesi Eğitimi", "svm-egitim"),
            p(
                "Burada öğrendiğimiz araçlarla küçük resim yamalarını "
                "sınıflandıran bir model oluşturacağız. Bu yüksek boyutlu "
                "ikili sınıflandırma için doğrusal SVM iyi seçimdir. "
                "Büyük örnek sayısında <code>SVC</code>'ye kıyasla genelde "
                "daha iyi ölçeklenen <code>LinearSVC</code> kullanacağız."
            ),
            p(
                "Önce hızlı bir taban çizgi için basit Gauss naive Bayes "
                "tahmincisi deneyelim:"
            ),
        ]
    ),
    22: p(
        "Eğitim verisinde basit naive Bayes bile %95'in üzerinde doğruluk "
        "veriyor. Destek vektör makinesini deneyelim; <code>C</code> "
        "parametresi üzerinde grid search yapalım:"
    ),
    25: p(
        "Bu bizi neredeyse %99 doğruluğa taşır. En iyi tahminciyi alıp "
        "tüm veri kümesinde yeniden eğitelim:"
    ),
    27: "\n".join(
        [
            h3("5. Yeni Görüntüde Yüz Bulma", "yeni-goruntu"),
            p(
                "Model hazır; yeni bir görüntü alıp modelin nasıl yaptığına "
                "bakalım. Basitlik için aşağıdaki şekildeki astronot "
                "görüntüsünün bir bölümünü kullanacağız; kayan pencere "
                "çalıştırıp her yamayı değerlendireceğiz:"
            ),
        ]
    ),
    29: p(
        "Sonra görüntü yamaları üzerinde yineleyen bir pencere oluşturup "
        "her yama için HOG özniteliklerini hesaplayalım:"
    ),
    31: p(
        "Son olarak HOG'lu yamaları modelle değerlendirip hangisinin yüz "
        "içerdiğini görelim:"
    ),
    33: p(
        "Yaklaşık 2.000 yamadan 48 algılama bulduk. Yamalar hakkındaki "
        "bilgiyle test görüntüsünde dikdörtgen olarak gösterelim (aşağıdaki şekil):"
    ),
    35: p(
        "Algılanan yamaların hepsi örtüşüyor ve görüntüdeki yüzü buldu! "
        "Birkaç satır Python için fena değil."
    ),
    36: "\n".join(
        [
            h2("Uyarılar ve İyileştirmeler", "uyarilar-iyilestirmeler"),
            p(
                "Önceki kod ve örneklere biraz daha inerseniz, üretime hazır "
                "yüz dedektörü iddiasında olmadan önce hâlâ işimiz olduğunu "
                "görürsünüz. Birkaç sorun ve iyileştirme:"
            ),
            p("<strong>Eğitim kümemiz, özellikle negatif öznitelikler için, pek eksiksiz değil</strong>"),
            p(
                "Temel sorun, eğitim kümesinde olmayan birçok yüz benzeri "
                "dokunun olması; mevcut model yanlış pozitiflere çok yatkın. "
                "Tam astronot görüntüsünde denerseniz model başka bölgelerde "
                "birçok yanlış algılama üretir. Negatif eğitim kümesine daha "
                "geniş görüntü seti eklemek iyileşme sağlayabilir. "
                "<em>Hard negative mining</em> de seçenektir: sınıflandırıcının "
                "görmediği yeni görüntülerde yanlış pozitif yamaları bulup "
                "negatif örnek olarak eğitime ekleyip yeniden eğitmek."
            ),
            p("<strong>Mevcut hat yalnızca tek ölçekte arıyor</strong>"),
            p(
                "Şu anki yazım yaklaşık 62×47 piksel olmayan yüzleri kaçırır. "
                "Çeşitli boyutlarda kayan pencere ve modele vermeden önce "
                "<code>skimage.transform.resize</code> ile yeniden boyutlandırma "
                "ile ele alınabilir; buradaki <code>sliding_window</code> "
                "yardımcısı bunun için tasarlanmıştır."
            ),
            p("<strong>Örtüşen algılama yamalarını birleştirmeliyiz</strong>"),
            p(
                "Üretim hattında aynı yüzün 30 algılamasını değil, örtüşen "
                "grupları tek algılamaya indirmek isteriz — mean shift kümeleme "
                "veya makine görüşünde yaygın <em>non-maximum suppression</em>."
            ),
            p("<strong>Hat akıcı hale getirilmeli</strong>"),
            p(
                "Önceki sorunlar giderildikten sonra eğitim görüntülerini alıp "
                "kayan pencere çıktısı üreten daha akıcı bir pipeline kurmak "
                "istenebilir — Python veri biliminde güçlü yön budur."
            ),
            p("<strong>Daha yeni gelişmeler: derin öğrenme</strong>"),
            p(
                "Son olarak, makine öğrenmesinde HOG ve benzeri prosedürel "
                "öznitelik çıkarma her zaman kullanılmaz; birçok modern nesne "
                "algılama hattı derin sinir ağı varyantlarını (<em>derin öğrenme</em>) "
                "kullanır: sinir ağları, kullanıcı sezgisine değil veriden optimal "
                "öznitelik stratejilerini öğrenen tahminciler olarak düşünülebilir."
            ),
            p(
                "Alan son yıllarda harika sonuçlar verse de derin öğrenme "
                "önceki bölümlerdeki modellerden kavramsal olarak çok farklı "
                "değildir; asıl ilerleme, çok daha büyük eğitim veri kütleleri "
                "üzerinde çok daha esnek modeller eğitmek için modern donanım "
                "kullanmaktır. Ölçek farklı olsa da amaç aynıdır: veriden model kurmak."
            ),
            p(
                "Daha ileri gitmek istiyorsanız "
                '<a href="15-learning-more.html">5.15 Kaynaklar</a> '
                "bölümündeki referans listesi iyi bir başlangıç noktasıdır!"
            ),
        ]
    ),
}

INSERTS = {
    2: addon(
        "Pyodide: PIL / scikit-image",
        "<code>skimage</code>, <code>PIL</code> ve <code>fetch_lfw_people</code> "
        "gibi örnekler tarayıcıda Pyodide ortamında sınırlı veya internet "
        "gerektirebilir. Bu bölümün tam demosu için yerel Jupyter "
        "<strong>.ipynb</strong> dosyasını kullanın; kod blokları referans "
        "olarak çalıştırılabilir.",
    ),
    4: try_it(
        "",
        "Basit HOG vektör boyutunu kontrol edin (scikit-image gerekir):",
        """# Pyodide'da skimage yoksa yerel notebook kullanın
try:
    from skimage import data, color, feature
    image = color.rgb2gray(data.chelsea())
    hog_vec, _ = feature.hog(image, pixels_per_cell=(16, 16), visualize=True)
    print("HOG boyutu:", hog_vec.shape)
except ImportError:
    print("skimage bu ortamda yok — yerel Jupyter önerilir")""",
        "deneme_hog_boyut.py",
    ),
    19: addon(
        "Eğitim süresi",
        "43.000 yamada HOG çıkarma dakikalar sürebilir. Pyodide'da daha küçük "
        "alt küme ile deneyin; tam pipeline yerel ortamda çalıştırılmalıdır.",
    ),
}

CODE_NAMES = {
    2: "imports_hog.py",
    4: "hog_chelsea.py",
    7: "fetch_lfw_people.py",
    10: "camera_shape.py",
    11: "negative_patches.py",
    12: "extract_patches_fn.py",
    14: "negative_patches_plot.py",
    17: "hog_features_train.py",
    18: "X_train_shape.py",
    21: "gnb_baseline_faces.py",
    23: "linearsvc_grid_faces.py",
    24: "linearsvc_best_c.py",
    26: "linearsvc_final_fit.py",
    28: "test_astronaut_crop.py",
    30: "sliding_window_fn.py",
    32: "predict_patches.py",
    34: "draw_detections.py",
}

if __name__ == "__main__":
    body = build_from_notebook("05.14-Image-Features.ipynb", TR, CODE_NAMES, INSERTS)
    body += "\n\n" + next_link("15-learning-more.html", "5.15 Daha Fazla Kaynak")
    path = write_chapter("14-image-features", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
