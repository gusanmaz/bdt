#!/usr/bin/env python3
"""Generate 04-feature-engineering.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, next_link, try_it
from gen_sklearn_00_02 import code_block, cell_code, figure, img_from_md, load_nb, write_slug

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.04-feature-engineering.html"

TR = {
    0: f"""<h1>5.4 Öznitelik Mühendisliği</h1>

    <p><em>Orijinal: <a href="{EN}" target="_blank" rel="noopener">05.04 Feature Engineering</a></em></p>""",
    1: """    <p>Önceki bölümler makine öğrenmesinin temel fikirlerini özetledi; ancak tüm örnekler sayısal verinin düzenli <code>[n_samples, n_features]</code> biçiminde olduğunu varsaydı.
    Gerçek dünyada veri nadiren bu biçimde gelir.
    Makine öğrenmesini pratikte kullanmanın daha önemli adımlarından biri <em>öznitelik mühendisliği</em>dir: probleminiz hakkındaki bilgiyi, öznitelik matrisi oluşturmak için kullanabileceğiniz sayılara dönüştürmek.</p>
    <p>Bu bölümde öznitelik mühendisliğinin birkaç yaygın örneğini ele alacağız: kategorik veri, metin ve görüntüler için öznitelikler.
    Ayrıca model karmaşıklığını artırmak için türetilmiş öznitelikler ve eksik veri doldurma (imputation) tartışılacak.
    Bu sürece genelde <em>vektörizasyon</em> denir; keyfi veriyi düzgün vektörlere dönüştürmeyi içerir.</p>""",
    2: """    <h2 id="kategorik-oznitelikler">Kategorik Öznitelikler</h2>
    <p>Sayısal olmayan verinin yaygın türlerinden biri <em>kategorik</em> veridir.
    Örneğin konut fiyatları verisini inceliyorsunuz; \"fiyat\" ve \"oda sayısı\" gibi sayısal özniteliklerin yanında \"mahalle\" bilgisi de vardır.
    Veriniz kabaca şöyle görünebilir:</p>""",
    4: """    <p>Bu veriyi basit bir sayısal eşlemeyle kodlamak cazip gelebilir:</p>""",
    6: """    <p>Ancak bu Scikit-Learn'de genelde yararlı bir yaklaşım değildir. Paketin modelleri sayısal özniteliklerin cebirsel nicelikleri yansıttığını varsayar; böyle bir eşleme örneğin <em>Queen Anne &lt; Fremont &lt; Wallingford</em> veya <em>Wallingford − Queen Anne = Fremont</em> anlamına gelir ki bu pek anlamlı değildir.</p>
    <p>Bu durumda kanıtlanmış tekniklerden biri <em>one-hot encoding</em> (tek-sıcak kodlama)dir: kategorinin varlığını veya yokluğunu 1 veya 0 ile gösteren ek sütunlar oluşturur.
    Veriniz sözlük listesi biçimindeyken Scikit-Learn'ün <code>DictVectorizer</code> sınıfı bunu sizin için yapar:</p>""",
    8: """    <p><code>neighborhood</code> sütununun üç ayrı mahalle etiketini temsil eden üç sütuna genişletildiğine dikkat edin; her satır kendi mahalle sütununda 1 içerir.
    Kategorik öznitelikler bu şekilde kodlandıktan sonra normal şekilde Scikit-Learn modeli uydurabilirsiniz.</p>
    <p>Her sütunun anlamını görmek için öznitelik adlarına bakabilirsiniz:</p>""",
    10: """    <p>Bu yaklaşımın belirgin bir dezavantajı vardır: kategorinizin çok olası değeri varsa veri kümenizin boyutu <em>ciddi</em> artabilir.
    Ancak kodlanmış veri çoğunlukla sıfır içerdiğinden seyrek çıktı çok verimli bir çözüm olabilir:</p>""",
    12: """    <p>Scikit-Learn tahmin edicilerinin neredeyse tamamı uyum ve değerlendirme sırasında böyle seyrek girdileri kabul eder.
    <code>sklearn.preprocessing.OneHotEncoder</code> ve <code>sklearn.feature_extraction.FeatureHasher</code> bu tür kodlamayı destekleyen ek araçlardır.</p>""",
    13: """    <h2 id="metin-oznitelikleri">Metin Öznitelikleri</h2>
    <p>Öznitelik mühendisliğinde bir başka yaygın ihtiyaç metni temsil edici sayısal değerlere dönüştürmektir.
    Örneğin sosyal medya verisinin otomatik madenciliği büyük ölçüde metnin sayılara kodlanmasına dayanır.
    En basit kodlama yöntemlerinden biri <em>kelime sayımı</em>dır: her metin parçasındaki her kelimenin geçiş sayısını sayıp sonucu tabloya koyarsınız.</p>
    <p>Örneğin aşağıdaki üç cümleyi düşünün:</p>""",
    15: """    <p>Kelime sayımına dayalı vektörizasyon için \"problem\", \"of\", \"evil\" vb. kelimeleri temsil eden sütunlar oluşturabiliriz.
    Bu basit örnekte elle yapılabilir; tediumdan kaçınmak için Scikit-Learn'ün <code>CountVectorizer</code> sınıfını kullanırız:</p>""",
    17: """    <p>Sonuç her kelimenin kaç kez geçtiğini kaydeden seyrek bir matristir; etiketli sütunlarla <code>DataFrame</code>'e çevirirsek incelemek kolaylaşır:</p>""",
    19: """    <p>Basit ham kelime sayımının sorunları vardır: çok sık geçen kelimelere fazla ağırlık verebilir; bazı sınıflandırma algoritmaları için alt optimal olabilir.
    Bunu düzeltmek için <em>term frequency–inverse document frequency</em> (<em>TF–IDF</em>) kullanılır; kelime sayımlarını belgelerde ne sıklıkla göründüklerine göre ağırlıklandırır.
    Bu öznitelikleri hesaplama sözdizimi önceki örneğe benzer:</p>""",
    21: """    <p>TF–IDF'in sınıflandırma probleminde kullanımına <a href="05-naive-bayes.html">Derinlemesine: Naive Bayes Sınıflandırması</a> bölümünde örnek verilmiştir.</p>""",
    22: """    <h2 id="goruntu-oznitelikleri">Görüntü Öznitelikleri</h2>
    <p>Bir başka yaygın ihtiyaç görüntüleri makine öğrenmesi analizi için uygun biçimde kodlamaktır.
    En basit yaklaşım <a href="02-introducing-scikit-learn.html">Scikit-Learn'e Giriş</a> bölümündeki rakam verisinde kullandığımız gibidir: doğrudan piksel değerlerinin kendisi.
    Ancak uygulamaya göre bu optimal olmayabilir.</p>
    <p>Görüntüler için öznitelik çıkarma tekniklerinin kapsamlı özeti bu bölümün kapsamını aşar; ancak standart yaklaşımların birçoğu <a href="http://scikit-image.org" target="_blank" rel="noopener">Scikit-Image</a> projesinde mükemmel uygulamalara sahiptir.
    Scikit-Learn ve Scikit-Image birlikte kullanımına <a href="14-image-features.html">Görüntü Öznitelikleri</a> bölümüne bakın.</p>""",
    23: """    <h2 id="turetilmis-oznitelikler">Türetilmiş Öznitelikler</h2>
    <p>Bir başka yararlı öznitelik türü girdi özniteliklerinden matematiksel olarak türetilenlerdir.
    <a href="03-hyperparameters-and-model-validation.html">Hiperparametreler ve Model Doğrulama</a> bölümünde girdi verisinden <em>polinom öznitelikleri</em> oluşturduğumuz bir örnek gördük.
    Doğrusal regresyonu polinom regresyona dönüştürmek için modeli değiştirmeden girdiyi dönüştürdük!</p>
    <p>Örneğin bu veri düz bir çizgiyle iyi tanımlanamaz (Şekil 40-1):</p>""",
    25: """    <p><code>LinearRegression</code> ile yine de veriye doğru uydurup optimal sonucu alabiliriz (Şekil 40-2):</p>""",
    27: """    <p>Ancak $x$ ile $y$ arasındaki ilişkiyi tanımlamak için daha gelişmiş bir modele ihtiyacımız olduğu açıktır.</p>
    <p>Buna bir yaklaşım veriyi dönüştürüp modele daha fazla esneklik verecek ek öznitelik sütunları eklemektir.
    Örneğin polinom öznitelikleri şöyle ekleyebiliriz:</p>""",
    29: """    <p>Türetilmiş öznitelik matrisinde $x$, $x^2$ ve $x^3$'ü temsil eden sütunlar vardır.
    Bu genişletilmiş girdi üzerinde doğrusal regresyon veriye çok daha yakın bir uyum verir (Şekil 40-3):</p>""",
    31: """    <p>Modeli değiştirmeden girdileri dönüştürerek modeli iyileştirme fikri birçok güçlü makine öğrenmesi yönteminin temelidir.
    <em>temel fonksiyon regresyonu</em> bağlamında <a href="06-linear-regression.html">Derinlemesine: Doğrusal Regresyon</a> bölümünde daha derin ineceğiz.
    Daha genel olarak bu, <em>çekirdek yöntemleri</em> olarak bilinen güçlü tekniklere giden motivasyon yollarından biridir; <a href="07-support-vector-machines.html">Derinlemesine: Destek Vektör Makineleri</a> bölümünde keşfedeceğiz.</p>""",
    32: """    <h2 id="eksik-veri-doldurma">Eksik Verinin Doldurulması</h2>
    <p>Öznitelik mühendisliğinde bir başka yaygın ihtiyaç eksik verinin işlenmesidir.
    <code>DataFrame</code> nesnelerinde eksik veriyi <a href="../03-pandas/04-missing-values.html">Eksik Veri</a> bölümünde ele aldık; eksik değerler sıkça <code>NaN</code> ile işaretlenir.
    Örneğin veri kümemiz şöyle görünebilir:</p>""",
    34: """    <p>Tipik bir makine öğrenmesi modelini böyle veriye uygularken önce eksik değerleri uygun bir doldurma değeriyle değiştirmemiz gerekir.
    Buna eksik değerlerin <em>imputation</em> (doldurma) denir; stratejiler basit (sütunun ortalamasıyla değiştirme) ile gelişmiş (matris tamamlama veya sağlam model) arasında değişir.</p>
    <p>Gelişmiş yaklaşımlar genelde uygulamaya özgüdür; burada derinlemesine girmeyeceğiz.
    Ortalama, medyan veya en sık değerle temel doldurma için Scikit-Learn <code>SimpleImputer</code> sınıfını sağlar:</p>""",
    36: """    <p>Sonuç veride iki eksik değerin sütundaki kalan değerlerin ortalamasıyla değiştirildiğini görüyoruz.
    Bu doldurulmuş veri doğrudan örneğin <code>LinearRegression</code> tahmin edicisine verilebilir:</p>""",
    38: """    <h2 id="oznitelik-pipeline">Öznitelik Pipeline'ları</h2>
    <p>Önceki örneklerin herhangi birinde dönüşümleri elle yapmak, özellikle birden fazla adımı zincirlemek istediğinizde hızla yorucu olabilir.
    Örneğin şöyle bir işleme pipeline'ı isteyebiliriz:</p>
    <ol>
      <li>Eksik değerleri ortalama ile doldur.</li>
      <li>Öznitelikleri ikinci dereceye dönüştür.</li>
      <li>Doğrusal regresyon modeli uydur.</li>
    </ol>
    <p>Bu tür pipeline'ı kolaylaştırmak için Scikit-Learn <code>Pipeline</code> nesnesi sunar:</p>""",
    40: """    <p>Bu pipeline standart bir Scikit-Learn nesnesi gibi görünür ve davranır; belirtilen tüm adımları girdi verisine uygular:</p>""",
    42: """    <p>Modelin tüm adımları otomatik uygulanır.
    Basitlik için bu gösterimde modeli eğitildiği veriye uyguladık; bu yüzden sonucu mükemmel tahmin edebildi (ayrıntılı tartışma için <a href="03-hyperparameters-and-model-validation.html">Hiperparametreler ve Model Doğrulama</a> bölümüne bakın).</p>
    <p>Scikit-Learn pipeline örnekleri için naive Bayes sınıflandırması bölümüne, ayrıca <a href="06-linear-regression.html">Derinlemesine: Doğrusal Regresyon</a> ve <a href="07-support-vector-machines.html">Derinlemesine: Destek Vektör Makineleri</a> bölümlerine bakın.</p>""",
}

CODE_NAMES = {
    3: "housing_dict_data.py",
    5: "neighborhood_map_bad.py",
    7: "dict_vectorizer.py",
    9: "feature_names_out.py",
    11: "dict_vectorizer_sparse.py",
    14: "text_sample_phrases.py",
    16: "count_vectorizer.py",
    18: "count_vectorizer_df.py",
    20: "tfidf_vectorizer.py",
    24: "derived_features_plot1.py",
    26: "linear_on_nonlinear.py",
    28: "polynomial_features.py",
    30: "poly_fit_plot.py",
    33: "missing_data_array.py",
    35: "simple_imputer.py",
    37: "impute_then_regress.py",
    39: "make_pipeline_impute.py",
    41: "pipeline_fit.py",
}

INSERTS = {
    12: addon("One-hot ve seyreklik", "<p>Kategorik sütun sayısı çok büyükse (ör. posta kodu) <code>FeatureHasher</code> veya hedef kodlama gibi alternatiflere bakın. Seyrek matrisler bellek açısından verimlidir.</p>"),
    21: try_it("", "Basit TF–IDF vektörizasyonu deneyin:", """from sklearn.feature_extraction.text import TfidfVectorizer
docs = ['problem of evil', 'evil queen', 'problem of heart']
vec = TfidfVectorizer()
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))""", "deneme_tfidf.py"),
}

if __name__ == "__main__":
    nb = load_nb("05.04-Feature-Engineering.ipynb")
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
    body = "\n".join(parts) + "\n" + next_link("05-naive-bayes.html", "5.5 Naive Bayes Sınıflandırması")
    path = write_slug("04-feature-engineering", body)
    print("wrote", path)
