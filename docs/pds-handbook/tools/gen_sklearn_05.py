#!/usr/bin/env python3
"""Generate 05-naive-bayes.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from gen_sklearn_00_02 import code_block, cell_code, img_from_md, load_nb, write_slug

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.05-naive-bayes.html"
FIG = "https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb#Gaussian-Naive-Bayes"

TR = {
    0: f"""<h1>5.5 Derinlemesine: Naive Bayes Sınıflandırması</h1>

    <p><em>Orijinal: <a href="{EN}" target="_blank" rel="noopener">05.05 Naive Bayes</a></em></p>""",
    1: """    <p>Önceki dört bölüm makine öğrenmesi kavramlarına genel bir bakış verdi.
    Bu ve sonraki bölümlerde önce denetimli öğrenme için dört algoritmaya, ardından denetimsiz öğrenme için dört algoritmaya daha yakından bakacağız.
    Denetimli yöntemlerimizden ilki olan naive Bayes sınıflandırmasıyla başlıyoruz.</p>
    <p>Naive Bayes modelleri çok hızlı ve basit sınıflandırma algoritmaları grubudur; çok yüksek boyutlu veri kümeleri için sıkça uygundur.
    Çok hızlı olmaları ve ayarlanabilir parametreleri az olduğu için sınıflandırma problemlerinde hızlı bir temel çizgi (baseline) olarak yararlıdırlar.
    Bu bölüm naive Bayes sınıflandırıcılarının sezgisel açıklamasını ve birkaç veri kümesindeki örneklerini sunar.</p>""",
    2: """    <h2 id="bayes-siniflandirma">Bayes Sınıflandırması</h2>
    <p>Naive Bayes sınıflandırıcıları Bayes sınıflandırma yöntemleri üzerine kuruludur.
    Bunlar Bayes teoremini kullanır; bu teorem koşullu olasılıklar arasındaki ilişkiyi tanımlar.
    Bayes sınıflandırmasında gözlemlenen öznitelikler verildiğinde bir etiket $L$'nin olasılığı $P(L~|~{\\rm features})$ ile ilgileniyoruz.
    Bayes teoremi bunu daha doğrudan hesaplayabileceğimiz niceliklerle ifade etmemizi sağlar:</p>
    <p>$$P(L~|~{\\rm features}) = \\frac{P({\\rm features}~|~L)P(L)}{P({\\rm features})}$$</p>
    <p>İki etiket $L_1$ ve $L_2$ arasında karar vermek istiyorsak, her etiket için posterior olasılıkların oranını hesaplayabiliriz:</p>
    <p>$$\\frac{P(L_1~|~{\\rm features})}{P(L_2~|~{\\rm features})} = \\frac{P({\\rm features}~|~L_1)}{P({\\rm features}~|~L_2)}\\frac{P(L_1)}{P(L_2)}$$</p>
    <p>Her etiket için $P({\\rm features}~|~L_i)$ hesaplayabileceğimiz bir modele ihtiyacımız var.
    Böyle bir modele <em>üretici model</em> denir; veriyi üreten varsayımsal rastgele süreci tanımlar.
    Her etiket için üretici modeli tanımlamak bu Bayes sınıflandırıcısının eğitiminin ana parçasıdır.
    Bu eğitim adımının genel hali çok zordur; ancak model biçimine dair basitleştirici varsayımlarla kolaylaştırabiliriz.</p>
    <p>\"Naive\" Bayes'teki \"naive\" buradan gelir: her etiket için üretici model hakkında çok naif varsayımlar yaparsak, her sınıf için üretici modelin kaba bir yaklaşımını bulup Bayes sınıflandırmasına devam edebiliriz.
    Farklı naive Bayes türleri veri hakkında farklı naif varsayımlara dayanır; aşağıda birkaçını inceleyeceğiz.</p>
    <p>Standart içe aktarmalarla başlayalım:</p>""",
    4: """    <h2 id="gauss-naive-bayes">Gauss Naive Bayes</h2>
    <p>Anlaşılması belki de en kolay naive Bayes sınıflandırıcısı Gauss naive Bayes'tir.
    Bu sınıflandırıcıda varsayım, <em>her etiketten gelen verinin basit bir Gauss dağılımından çekilmesidir</em>.
    Aşağıdaki veriyi düşünün (Şekil 41-1):</p>""",
    6: """    <p>En basit Gauss modeli, verinin boyutlar arası kovaryans olmadan Gauss dağılımıyla tanımlandığını varsayar.
    Bu model her etiket içindeki noktaların ortalama ve standart sapmasını hesaplayarak uydurulabilir; böyle bir dağılımı tanımlamak için gereken tek şey budur.
    Bu naif Gauss varsayımının sonucu aşağıdaki şekilde gösterilir:</p>""",
    7: figure("05.05-gaussian-NB.png", "Gauss naive Bayes üretici modeli", f'Kaynak: <a href="{FIG}" target="_blank" rel="noopener">Ek — Şekil kodu</a>'),
    8: """    <p>Buradaki elipsler her etiket için Gauss üretici modelini temsil eder; elips merkezine doğru olasılık daha yüksektir.
    Her sınıf için üretici model yerindeyken herhangi bir veri noktası için $P({\\rm features}~|~L_1)$ olabilirliğini hızlıca hesaplayabilir; böylece posterior oranı hesaplayıp verilen nokta için en olası etiketi belirleriz.</p>
    <p>Bu prosedür Scikit-Learn'ün <code>sklearn.naive_bayes.GaussianNB</code> tahmin edicisinde uygulanmıştır:</p>""",
    10: """    <p>Yeni veri üretip etiket tahmin edelim:</p>""",
    12: """    <p>Bu yeni veriyi çizerek karar sınırının nerede olduğuna bakalım (aşağıdaki şekil):</p>""",
    14: """    <p>Sınıflandırmalarda hafif eğri bir sınır görüyoruz — genelde Gauss naive Bayes modelinin ürettiği sınır ikinci dereceden olur.</p>
    <p>Bu Bayes biçiminin güzel yanı, <code>predict_proba</code> yöntemiyle olasılıksal sınıflandırmaya doğal olarak izin vermesidir:</p>""",
    16: """    <p>Sütunlar sırasıyla birinci ve ikinci etiketin posterior olasılıklarını verir.
    Sınıflandırmada belirsizlik tahminleri arıyorsanız bu tür Bayes yaklaşımları iyi bir başlangıç noktası olabilir.</p>
    <p>Elbette nihai sınıflandırma yalnızca ona yol açan model varsayımları kadar iyi olacaktır; bu yüzden Gauss naive Bayes sık sık çok iyi sonuç vermez.
    Yine de birçok durumda — özellikle öznitelik sayısı büyüdükçe — bu varsayım Gauss naive Bayes'in güvenilir bir yöntem olmasını engelleyecek kadar zararlı değildir.</p>""",
    17: """    <h2 id="multinomial-naive-bayes">Multinomial Naive Bayes</h2>
    <p>Az önce anlatılan Gauss varsayımı her etiket için üretici dağılımı tanımlamanın tek basit varsayımı değildir.
    Başka yararlı bir örnek multinomial naive Bayes'tir; özniteliklerin basit bir multinomial dağılımdan üretildiği varsayılır.
    Multinomial dağılım bir dizi kategori arasında gözlemlenen sayımların olasılığını tanımlar; bu yüzden multinomial naive Bayes sayımları veya sayım oranlarını temsil eden öznitelikler için en uygundur.</p>
    <p>Fikir öncekiyle aynıdır; yalnızca veri dağılımını en iyi Gauss ile değil en iyi multinomial dağılımla modellemek farkı vardır.</p>""",
    18: """    <h3 id="metin-siniflandirma">Örnek: Metin Sınıflandırması</h3>
    <p>Multinomial naive Bayes'in sık kullanıldığı yer metin sınıflandırmasıdır; öznitelikler sınıflandırılacak belgelerdeki kelime sayımları veya frekanslarıyla ilgilidir.
    Metinden bu özniteliklerin çıkarımını <a href="04-feature-engineering.html">Öznitelik Mühendisliği</a> bölümünde tartıştık; burada Scikit-Learn üzerinden 20 Newsgroups külliyatının seyrek kelime sayımı özniteliklerini kullanarak kısa belgeleri kategorilere sınıflandırmayı göstereceğiz.</p>
    <p>Veriyi indirip hedef adlarına bakalım:</p>""",
    20: """    <p>Basitlik için yalnızca birkaç kategori seçip eğitim ve test kümelerini indireceğiz:</p>""",
    22: """    <p>Veriden temsil bir giriş:</p>""",
    24: """    <p>Bu veriyi makine öğrenmesinde kullanmak için her dizenin içeriğini sayılar vektörüne dönüştürmemiz gerekir.
    Bunun için TF–IDF vektörizörünü (<a href="04-feature-engineering.html">Öznitelik Mühendisliği</a> bölümünde tanıtıldı) kullanıp multinomial naive Bayes sınıflandırıcısına bağlayan bir pipeline oluşturacağız:</p>""",
    26: """    <p>Bu pipeline ile modeli eğitim verisine uygulayıp test verisi için etiket tahmin edebiliriz:</p>""",
    28: """    <p>Test verisi için etiketleri tahmin ettikten sonra tahmin edicinin performansını öğrenmek için değerlendirebiliriz.
    Örneğin test verisinde gerçek ve tahmin edilen etiketler arasındaki karmaşıklık matrisine bakalım (aşağıdaki şekil):</p>""",
    30: """    <p>Görülüyor ki bu çok basit sınıflandırıcı bile uzay tartışmalarını bilgisayar tartışmalarından ayırabilir; ancak din ve Hristiyanlık tartışmaları arasında karışır.
    Bu belki de beklenebilir!</p>
    <p>İlginç olan, <code>predict</code> yöntemiyle <em>herhangi</em> bir dize için kategoriyi belirleyebilmemizdir.
    Tek bir dize için tahmin döndüren bir yardımcı fonksiyon:</p>""",
    32: """    <p>Deneyelim:</p>""",
    36: """    <p>Bunun dizedeki her kelimenin (ağırlıklı) frekansı için basit bir olasılık modelinden fazlası olmadığını unutmayın; yine de sonuç çarpıcıdır.
    Çok naif bir algoritma bile dikkatle kullanıldığında ve yüksek boyutlu büyük veri kümesi üzerinde eğitildiğinde şaşırtıcı derecede etkili olabilir.</p>""",
    37: """    <h2 id="ne-zaman-naive-bayes">Naive Bayes Ne Zaman Kullanılır?</h2>
    <p>Naive Bayes sınıflandırıcıları veri hakkında bu kadar katı varsayımlar yaptığından genelde daha karmaşık modeller kadar iyi performans göstermez.
    Yine de birkaç avantajları vardır:</p>
    <ul>
      <li>Eğitim ve tahmin için hızlıdır.</li>
      <li>Doğrudan olasılıksal tahmin sağlar.</li>
      <li>Genelde kolay yorumlanır.</li>
      <li>Az (hatta hiç) ayarlanabilir parametreleri vardır.</li>
    </ul>
    <p>Bu avantajlar naive Bayes sınıflandırıcısının sıkça iyi bir başlangıç temel çizgisi olması anlamına gelir.
    Uygun performans gösterirse tebrikler: probleminiz için çok hızlı, çok yorumlanabilir bir sınıflandırıcınız var.
    İyi değilse, ne kadar iyi olmaları gerektiğine dair temel bilgiyle daha gelişmiş modellere geçebilirsiniz.</p>
    <p>Naive Bayes sınıflandırıcıları özellikle şu durumlarda iyi performans gösterir:</p>
    <ul>
      <li>Naif varsayımlar gerçekten veriye uyduğunda (pratikte çok nadirdir)</li>
      <li>Kategoriler iyi ayrıldığında, model karmaşıklığı daha az önemli olduğunda</li>
      <li>Çok yüksek boyutlu veride, model karmaşıklığı daha az önemli olduğunda</li>
    </ul>
    <p>Son iki nokta farklı görünür ama aslında ilişkilidir: veri kümesinin boyutu arttıkça iki noktanın birbirine yakın bulunması çok daha az olasıdır (genel olarak yakın olmak için <em>her boyutta</em> yakın olmaları gerekir).
    Bu yüzden yüksek boyutlarda kümeler ortalama olarak daha ayrık olma eğilimindedir; yeni boyutlar gerçekten bilgi eklediyse varsayılır.
    Bu nedenle burada tartışılan basit sınıflandırıcılar, boyut arttıkça daha karmaşık sınıflandırıcılar kadar veya onlardan daha iyi çalışabilir: yeterli veriniz olduğunda basit bir model bile çok güçlü olabilir.</p>""",
}

CODE_NAMES = {
    3: "imports_nb.py",
    5: "make_blobs_nb.py",
    9: "gaussian_nb_fit.py",
    11: "nb_predict_new.py",
    13: "nb_decision_boundary.py",
    15: "nb_predict_proba.py",
    19: "fetch_20newsgroups.py",
    21: "newsgroups_subset.py",
    23: "newsgroups_sample.py",
    25: "tfidf_multinomial_pipeline.py",
    27: "newsgroups_fit_predict.py",
    29: "newsgroups_confusion.py",
    31: "predict_category_fn.py",
    33: "predict_iss.py",
    34: "predict_god.py",
    35: "predict_screen.py",
}

INSERTS = {
    16: addon("predict_proba", "<p><code>predict_proba</code> her sınıf için olasılık vektörü döndürür; en yüksek olasılıklı sınıf <code>predict</code> ile aynıdır. Eşik veya \"bilmiyorum\" kararı için olasılıkları kullanabilirsiniz.</p>"),
    30: try_it("", "Gauss naive Bayes ile make_blobs verisinde sınıflandırma deneyin:", """from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
X, y = make_blobs(n_samples=100, centers=2, random_state=0)
clf = GaussianNB().fit(X, y)
print("Doğruluk (eğitim):", clf.score(X, y))""", "deneme_gaussian_nb.py"),
}

if __name__ == "__main__":
    nb = load_nb("05.05-Naive-Bayes.ipynb")
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
    body = "\n".join(parts) + "\n" + next_link("06-linear-regression.html", "5.6 Doğrusal Regresyon")
    path = write_slug("05-naive-bayes", body)
    print("wrote", path)
