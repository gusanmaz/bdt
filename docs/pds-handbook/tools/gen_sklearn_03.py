#!/usr/bin/env python3
"""Generate 03-hyperparameters-and-model-validation.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _gen_sklearn_helpers import addon, figure, next_link, try_it
from gen_sklearn_00_02 import write_slug

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.03-hyperparameters-and-model-validation.html"

FIG = "https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb"

TR = {
    0: """<h1>5.3 Hiperparametreler ve Model Doğrulama</h1>

    <p><em>Orijinal: <a href="{en}" target="_blank" rel="noopener">05.03 Hyperparameters and Model Validation</a></em></p>""".format(en=EN),
    1: """    <p>Önceki bölümde denetimli bir makine öğrenmesi modelini uygulamanın temel tarifini gördük:</p>
    <ol>
      <li>Bir model sınıfı seçin.</li>
      <li>Model hiperparametrelerini seçin.</li>
      <li>Modeli eğitim verisine uydurun.</li>
      <li>Modeli yeni veri için etiket tahmin etmekte kullanın.</li>
    </ol>
    <p>Bu sürecin ilk iki parçası — model seçimi ve hiperparametre seçimi — bu araçları etkili kullanmanın belki de en önemli kısmıdır.
    Bilinçli seçimler yapabilmek için modelimizin ve hiperparametrelerimizin veriye iyi uyup uymadığını <em>doğrulayacak</em> bir yola ihtiyacımız vardır.
    Kulağa basit gelse de bunu etkili yapmak için kaçınılması gereken tuzaklar vardır.</p>""",
    2: """    <h2 id="model-dogrulama-dusunce">Model Doğrulamayı Düşünmek</h2>
    <p>İlke olarak model doğrulama çok basittir: bir model ve hiperparametrelerini seçtikten sonra, eğitim verisinin bir kısmına uygulayıp tahminleri bilinen değerlerle karşılaştırarak ne kadar etkili olduğunu tahmin edebiliriz.</p>
    <p>Bu bölüm önce model doğrulamada naif bir yaklaşımı ve neden başarısız olduğunu gösterecek; ardından daha sağlam model değerlendirmesi için tutma kümeleri ve çapraz doğrulamayı inceleyecektir.</p>""",
    3: """    <h3 id="yanlis-dogrulama">Model Doğrulamanın Yanlış Yolu</h3>
    <p>Önceki bölümde gördüğümüz Iris veri kümesiyle naif doğrulama yaklaşımıyla başlayalım. Veriyi yükleyerek başlıyoruz:</p>""",
    5: """    <p>Ardından bir model ve hiperparametre seçeriz. Burada <code>n_neighbors=1</code> ile <em>k</em>-en yakın komşu sınıflandırıcısı kullanacağız.
    Bu, \"bilinmeyen bir noktanın etiketi, en yakın eğitim noktasının etiketiyle aynıdır\" diyen çok basit ve sezgisel bir modeldir:</p>""",
    7: """    <p>Sonra modeli eğitir ve etiketlerini zaten bildiğimiz veri için etiket tahmin ederiz:</p>""",
    9: """    <p>Son olarak doğru etiketlenmiş noktaların oranını hesaplarız:</p>""",
    11: """    <p>1,0 doğruluk skoru görüyoruz; bu modelimizin noktaların %100'ünü doğru etiketlediğini gösterir!
    Ama bu gerçekten beklenen doğruluğu ölçüyor mu? %100 doğru olmasını bekleyeceğimiz bir modele mi rastladık?</p>
    <p>Tahmin edebileceğiniz gibi cevap hayır.
    Bu yaklaşım temel bir kusur içerir: <em>modeli aynı veri üzerinde hem eğitir hem değerlendirir</em>.
    Ayrıca bu en yakın komşu modeli, eğitim verisini saklayan <em>örnek tabanlı</em> bir tahmin edicidir; yeni veriyi saklanan noktalarla karşılaştırarak etiketler: yapay durumlar dışında her seferinde %100 doğruluk alır!</p>""",
    12: """    <h3 id="tutma-kumesi">Model Doğrulamanın Doğru Yolu: Tutma Kümeleri</h3>
    <p>Ne yapılabilir? Model performansına daha iyi bir fikir, <em>tutma kümesi</em> (holdout set) kullanarak elde edilir: model eğitiminden verinin bir alt kümesini geri tutarız, sonra bu tutma kümesiyle performansı kontrol ederiz.
    Bu bölme Scikit-Learn'deki <code>train_test_split</code> yardımcısıyla yapılabilir:</p>""",
    14: """    <p>Burada daha makul bir sonuç görüyoruz: bir-en yakın komşu sınıflandırıcısı bu tutma kümesinde yaklaşık %90 doğru.
    Tutma kümesi bilinmeyen veriye benzer; model onu daha önce \"görmemiştir\".</p>""",
    15: """    <h3 id="capraz-dogrulama">Çapraz Doğrulama ile Model Doğrulama</h3>
    <p>Tutma kümesi kullanmanın bir dezavantajı, verinin bir kısmını model eğitimine kaybetmemizdir.
    Önceki durumda veri kümesinin yarısı modele katkıda bulunmuyor! Bu optimal değildir; özellikle başlangıç eğitim verisi küçükse.</p>
    <p>Bunu ele almanın bir yolu <em>çapraz doğrulama</em>dır: verinin her alt kümesinin hem eğitim hem doğrulama kümesi olarak kullanıldığı bir dizi uyum yapılır.
    Görsel olarak aşağıdaki şekle benzer:</p>
""" + figure("05.03-2-fold-CV.png", "İki katlı çapraz doğrulama", f'Kaynak: <a href="{FIG}#2-Fold-Cross-Validation" target="_blank" rel="noopener">Ek — Şekil kodu</a>') + """
    <p>Burada iki doğrulama denemesi yapıyoruz; verinin her yarısını sırayla tutma kümesi olarak kullanıyoruz.
    Daha önce bölünmüş veriyle şöyle uygulayabiliriz:</p>""",
    17: """    <p>Çıkan iki doğruluk skorudur; bunları birleştirerek (örneğin ortalamasını alarak) genel model performansının daha iyi bir ölçüsünü elde edebiliriz.
    Bu çapraz doğrulama biçimi <em>iki katlı çapraz doğrulama</em>dır — veriyi iki kümeye bölüp her birini sırayla doğrulama kümesi olarak kullandığımız.</p>
    <p>Bu fikri daha fazla deneme ve daha fazla katla genişletebiliriz; örneğin aşağıdaki şekil beş katlı çapraz doğrulamayı gösterir.</p>
""" + figure("05.03-5-fold-CV.png", "Beş katlı çapraz doğrulama", f'Kaynak: <a href="{FIG}#5-Fold-Cross-Validation" target="_blank" rel="noopener">Ek — Şekil kodu</a>') + """
    <p>Veriyi beş gruba bölüp her birini sırayla diğer dörtte beşlik veri üzerinde uydurulan modeli değerlendirmek için kullanırız.
    Elle yapmak yorucu olurdu; Scikit-Learn'ün <code>cross_val_score</code> yardımcı rutiniyle özlü yapabiliriz:</p>""",
    19: """    <p>Doğrulamayı farklı alt kümelerde tekrarlamak algoritmanın performansı hakkında daha iyi bir fikir verir.</p>
    <p>Scikit-Learn belirli durumlarda yararlı birçok çapraz doğrulama şeması uygular; bunlar <code>model_selection</code> modülündeki yineleyicilerle sağlanır.
    Örneğin kat sayısını veri noktası sayısına eşitlemek isteyebiliriz: her denemede tüm noktalar hariç bir tanesiyle eğitim.
    Bu tür çapraz doğrulamaya <em>leave-one-out</em> (birini bırak) çapraz doğrulama denir:</p>""",
    21: """    <p>150 örneğimiz olduğundan leave-one-out çapraz doğrulama 150 deneme skoru verir; her skor başarılı (1,0) veya başarısız (0,0) tahmini gösterir.
    Bunların ortalaması hata oranı tahmini verir:</p>""",
    23: """    <p>Diğer çapraz doğrulama şemaları benzer kullanılabilir.
    Scikit-Learn'de nelerin mevcut olduğu için IPython'da <code>sklearn.model_selection</code> alt modülünü keşfedin veya Scikit-Learn <a href="http://scikit-learn.org/stable/modules/cross_validation.html" target="_blank" rel="noopener">çapraz doğrulama dokümantasyonuna</a> bakın.</p>""",
    24: """    <h2 id="en-iyi-model">En İyi Modeli Seçmek</h2>
    <p>Doğrulama ve çapraz doğrulamanın temellerini gördükten sonra model seçimi ve hiperparametre seçimine biraz daha derin ineceğiz.
    Bu konular makine öğrenmesi pratiğinin en önemli yönlerinden bazılarıdır; ancak giriş öğreticilerinde sıkça yüzeysel geçilir.</p>
    <p>Önemli soru: <em>tahmin edicimiz yetersiz performans gösteriyorsa nasıl ilerlemeliyiz?</em> Olası cevaplar:</p>
    <ul>
      <li>Daha karmaşık/esnek bir model kullanın.</li>
      <li>Daha az karmaşık/daha az esnek bir model kullanın.</li>
      <li>Daha fazla eğitim örneği toplayın.</li>
      <li>Her örneğe öznitelik eklemek için daha fazla veri toplayın.</li>
    </ul>
    <p>Bu sorunun cevabı sıkça sezgisine aykırıdır.
    Bazen daha karmaşık model daha kötü sonuç verir; daha fazla eğitim örneği eklemek sonucu iyileştirmeyebilir!
    Modelinizi ne adımlarla iyileştireceğinizi belirleme yeteneği başarılı makine öğrenmesi uygulayıcılarını başarısız olanlardan ayırır.</p>""",
    25: """    <h3 id="bias-variance">Önyargı–Varyans Ödünleşimi</h3>
    <p>Temelde \"en iyi modeli\" bulmak <em>önyargı</em> (bias) ile <em>varyans</em> arasındaki ödünleşimde uygun bir nokta bulmaktır.
    Aşağıdaki şekil aynı veri kümesine iki regresyon uyumunu sunar.</p>
""" + figure("05.03-bias-variance.png", "Önyargı–varyans ödünleşimi", f'Kaynak: <a href="{FIG}#Bias-Variance-Tradeoff" target="_blank" rel="noopener">Ek — Şekil kodu</a>') + """
    <p>Hiçbir model veriye iyi uyum değil; ancak farklı şekillerde başarısız olurlar.</p>
    <p>Soldaki model veride düz çizgi uyumu arar. Düz çizgi bu veriyi doğru ayıramayacağından model veri kümesini iyi tanımlayamaz.
    Böyle bir modele veriyi <em>yetersiz uyum</em> (underfit) yapar denir: tüm öznitelikleri uygun biçimde hesaba katacak esneklik yoktur; modele yüksek önyargı denir.</p>
    <p>Sağdaki model yüksek dereceli polinom uydurmayı dener. Uyum ince ayrıntıları neredeyse mükemmel yakalar; ancak biçim veriyi üreten sürecin özelliklerinden çok gürültü özelliklerini yansıtıyor gibi görünür.
    Böyle bir modele veriyi <em>aşırı uyum</em> (overfit) yapar denir: o kadar esnektir ki rastgele hataları da hesaba katar. Modele yüksek varyans denir.</p>""",
    26: """    <p>Başka bir açıdan, bu iki modeli yeni veri için <em>y</em> değerlerini tahmin etmekte kullanırsak ne olur?
    Aşağıdaki şekildeki grafiklerde kırmızı/açık noktalar eğitim kümesinden çıkarılan veriyi gösterir.</p>
""" + figure("05.03-bias-variance-2.png", "Önyargı–varyans metrikleri", f'Kaynak: <a href="{FIG}#Bias-Variance-Tradeoff-Metrics" target="_blank" rel="noopener">Ek — Şekil kodu</a>') + """
    <p>Skor burada $R^2$ skoru veya <a href="https://en.wikipedia.org/wiki/Coefficient_of_determination" target="_blank" rel="noopener">belirleme katsayısı</a>dır; modelin hedef değerlerin basit ortalamasına göre performansını ölçer. $R^2=1$ mükemmel eşleşme, $R^2=0$ model ortalamadan iyi değil, negatif değerler daha kötü modeller demektir.
    İki modelin skorlarından daha genel bir gözlem çıkarabiliriz:</p>
    <ul>
      <li>Yüksek önyargılı modellerde doğrulama kümesi performansı eğitim kümesi performansına benzer.</li>
      <li>Yüksek varyanslı modellerde doğrulama performansı eğitim performansından çok daha kötüdür.</li>
    </ul>""",
    27: """    <p>Model karmaşıklığını ayarlama yeteneğimiz varsa, eğitim ve doğrulama skorlarının aşağıdaki şekildeki gibi davranmasını bekleriz:</p>
""" + figure("05.03-validation-curve.png", "Doğrulama eğrisi", f'Kaynak: <a href="{FIG}#Validation-Curve" target="_blank" rel="noopener">Ek — Şekil kodu</a>') + """
    <p>Bu diyagrama sıkça <em>doğrulama eğrisi</em> denir; şu özellikleri görürüz:</p>
    <ul>
      <li>Eğitim skoru her yerde doğrulama skorundan yüksektir. Genelde model gördüğü veriye görmediğine göre daha iyi uyar.</li>
      <li>Çok düşük model karmaşıklığında (yüksek önyargı) eğitim verisi yetersiz uyumludur; model hem eğitim hem görülmemiş veri için zayıf tahmin edicidir.</li>
      <li>Çok yüksek karmaşıklıkta (yüksek varyans) eğitim verisi aşırı uyumludur; eğitim verisini çok iyi tahmin eder ama görülmemiş veride başarısız olur.</li>
      <li>Ara bir değerde doğrulama eğrisinin maksimumu vardır. Bu karmaşıklık önyargı ve varyans arasında uygun ödünleşimi gösterir.</li>
    </ul>
    <p>Model karmaşıklığını ayarlama yöntemi modele göre değişir; sonraki bölümlerde her modelin nasıl ayarlandığını göreceğiz.</p>""",
    28: """    <h3 id="dogrulama-egrisi-sklearn">Scikit-Learn'de Doğrulama Eğrileri</h3>
    <p>Bir model sınıfı için doğrulama eğrisini çapraz doğrulamayla hesaplamaya bir örnek bakalım.
    Burada <em>polinom regresyon</em> modeli kullanacağız: polinom derecesi ayarlanabilir bir parametredir.
    Örneğin derece-1 polinom düz çizgi uydurur; $a$ ve $b$ parametreleriyle: $y = ax + b$</p>
    <p>Derece-3 polinom kübik eğri uydurur; $a, b, c, d$ ile: $y = ax^3 + bx^2 + cx + d$</p>
    <p>Bunu herhangi sayıda polinom özniteliğine genelleyebiliriz.
    Scikit-Learn'de doğrusal regresyon sınıflandırıcısı ile polinom ön işlemcisini birleştirerek uygularız.
    Bu işlemleri bir <em>pipeline</em> ile zincirleriz (<a href="04-feature-engineering.html">Öznitelik Mühendisliği</a> bölümünde polinom öznitelikleri ve pipeline'ları daha ayrıntılı ele alacağız):</p>""",
    30: """    <p>Şimdi modele uyduracağımız veri oluşturalım:</p>""",
    32: """    <p>Veriyi ve birkaç derecede polinom uyumlarını görselleştirebiliriz (aşağıdaki şekil):</p>""",
    34: """    <p>Bu durumda model karmaşıklığını kontrol eden düğme polinom derecesidir; negatif olmayan herhangi bir tamsayı olabilir.
    Yararlı soru: önyargı (yetersiz uyum) ile varyans (aşırı uyum) arasında uygun ödünleşimi hangi derece sağlar?</p>
    <p>Scikit-Learn'ün sağladığı <code>validation_curve</code> yardımcı rutiniyle bu veri ve model için doğrulama eğrisini görselleştirebiliriz.
    Verilen model, veri, parametre adı ve keşfedilecek aralık için eğitim ve doğrulama skorlarını otomatik hesaplar (aşağıdaki şekil):</p>""",
    36: """    <p>Beklediğimiz nitel davranışı tam gösterir: eğitim skoru her yerde doğrulamadan yüksek, karmaşıklık arttıkça eğitim skoru monoton iyileşir, doğrulama skoru aşırı uyumdan önce maksimuma ulaşır.</p>
    <p>Doğrulama eğrisinden önyargı–varyans arasında optimal ödünleşimin üçüncü derece polinomda olduğunu belirleyebiliriz. Orijinal veri üzerinde bu uyumu hesaplayıp gösterebiliriz (aşağıdaki şekil):</p>""",
    38: """    <p>Optimal modeli bulmak için eğitim skorunu hesaplamamız gerekmediğine dikkat edin; ancak eğitim ve doğrulama skoru ilişkisine bakmak modele dair yararlı içgörü verir.</p>""",
    39: """    <h2 id="ogrenme-egrisi">Öğrenme Eğrileri</h2>
    <p>Model karmaşıklığının önemli bir yönü, optimal modelin genelde eğitim verinizin boyutuna bağlı olmasıdır.
    Örneğin beş kat daha fazla noktayla yeni bir veri kümesi üretelim (aşağıdaki şekil):</p>""",
    41: """    <p>Önceki kodu tekrarlayarak bu büyük veri kümesi için doğrulama eğrisini çizelim; referans için önceki küçük veri sonuçlarını da üstüne çizelim (aşağıdaki şekil):</p>""",
    43: """    <p>Düz çizgiler yeni sonuçları, soluk kesikli çizgiler önceki küçük veri kümesi sonuçlarını gösterir.
    Doğrulama eğrisinden büyük veri kümesinin çok daha karmaşık bir modeli destekleyebileceği açıktır: tepe muhtemelen derece 6 civarındadır; hatta derece-20 model bile ciddi aşırı uyum yapmaz — doğrulama ve eğitim skorları birbirine yakın kalır.</p>
    <p>Doğrulama eğrisi davranışının iki önemli girdisi vardır: model karmaşıklığı ve eğitim noktası sayısı.
    Eğitim noktası sayısına göre model davranışını, modele giderek büyük alt kümelerle uyum yaparak inceleyebiliriz.
    Eğitim kümesi boyutuna göre eğitim/doğrulama skorunun grafiğine bazen <em>öğrenme eğrisi</em> denir.</p>
    <p>Belirli karmaşıklıktaki bir modelden beklediğimiz genel davranış:</p>
    <ul>
      <li>Belirli karmaşıklıktaki model küçük veri kümesini <em>aşırı uyumlar</em>: eğitim skoru nispeten yüksek, doğrulama nispeten düşük.</li>
      <li>Belirli karmaşıklıktaki model büyük veri kümesini <em>yetersiz uyumlar</em>: eğitim skoru düşer, doğrulama skoru artar.</li>
      <li>Model şans dışında doğrulama kümesine eğitimden daha iyi skor vermez: eğriler birbirine yaklaşır ama kesişmemeli.</li>
    </ul>
    <p>Bu özelliklerle öğrenme eğrisinin nitel olarak aşağıdaki şekildeki gibi görünmesini bekleriz:</p>""",
    44: figure("05.03-learning-curve.png", "Öğrenme eğrisi", f'Kaynak: <a href="{FIG}#Learning-Curve" target="_blank" rel="noopener">Ek — Şekil kodu</a>'),
    45: """    <p>Öğrenme eğrisinin dikkat çeken özelliği, eğitim örneği sayısı arttıkça belirli bir skora yakınsamasıdır.
    Özellikle belirli bir model yakınsadığında <em>daha fazla eğitim verisi yardımcı olmaz!</em>
    Bu durumda performansı artırmanın tek yolu başka (genelde daha karmaşık) bir model kullanmaktır.</p>""",
    46: """    <h3 id="ogrenme-egrisi-sklearn">Scikit-Learn'de Öğrenme Eğrileri</h3>
    <p>Scikit-Learn modellerinizden böyle öğrenme eğrilerini hesaplamak için uygun bir araç sunar; orijinal veri kümesi için ikinci derece polinom modeli ve dokuzuncu derece polinom için öğrenme eğrisi hesaplayacağız (aşağıdaki şekil):</p>""",
    48: """    <p>Bu değerli bir tanıdır; modelimizin artan eğitim verisine nasıl yanıt verdiğinin görsel tasvirini verir.
    Özellikle öğrenme eğrisi zaten yakınsadığında (eğitim ve doğrulama eğrileri birbirine yakınsa) <em>daha fazla eğitim verisi uydurmayı anlamlı biçimde iyileştirmez!</em>
    Bu durum sol panelde derece-2 modelinin öğrenme eğrisinde görülür.</p>
    <p>Yakınsama skorunu artırmanın tek yolu farklı (genelde daha karmaşık) bir model kullanmaktır.
    Sağ panelde çok daha karmaşık bir modele geçince yakınsama skoru artar (kesikli çizgiyle gösterilir); ancak daha yüksek model varyansı pahasına (eğitim ve doğrulama skorları arasındaki fark).
    Daha fazla veri noktası eklense daha karmaşık modelin öğrenme eğrisi de yakınsardı.</p>
    <p>Seçtiğiniz model ve veri kümesi için öğrenme eğrisi çizmek analizinizi nasıl ilerleteceğinize karar vermenize yardımcı olabilir.</p>""",
    49: """    <h2 id="grid-search">Pratikte Doğrulama: Grid Search</h2>
    <p>Önceki tartışma önyargı–varyans ödünleşimine ve model karmaşıklığı ile eğitim kümesi boyutuna bağımlılığına sezgi vermek içindi.
    Pratikte modellerin genelde birden fazla ayar düğmesi vardır; doğrulama ve öğrenme eğrileri çizgilerden çok boyutlu yüzeylere dönüşür.
    Bu durumlarda görselleştirmeler zordur; doğrulama skorunu maksimize eden modeli bulmayı tercih ederiz.</p>
    <p>Scikit-Learn bu aramayı kolaylaştıran araçlar sunar; optimal polinom modelini bulmak için grid search kullanacağız.
    İki boyutlu bir model özellik ızgarası keşfedeceğiz: polinom derecesi ve kesişim sığdırılıp sığdırılmayacağını söyleyen bayrak.
    Bunu Scikit-Learn'ün <code>GridSearchCV</code> meta-tahmin edicisiyle kurabiliriz:</p>""",
    51: """    <p>Normal bir tahmin edici gibi henüz hiçbir veriye uygulanmadığına dikkat edin.
    <code>fit</code> yöntemi her ızgara noktasında modeli uydurur ve skorları izler:</p>""",
    53: """    <p>Model uydurulduktan sonra en iyi parametreleri sorabiliriz:</p>""",
    55: """    <p>Son olarak istersek en iyi modeli kullanıp önceki kodla veriye uyumu gösterebiliriz (aşağıdaki şekil):</p>""",
    57: """    <p><code>GridSearchCV</code>'deki diğer seçenekler özel skorlama fonksiyonu, hesaplamaları paralelleştirme, rastgele aramalar vb. içerir.
    Daha fazla bilgi için <a href="13-kernel-density-estimation.html">Derinlemesine: Çekirdek Yoğunluk Tahmini</a> ve <a href="14-image-features.html">Görüntü Öznitelikleri</a> bölümlerindeki örneklere veya Scikit-Learn <a href="http://scikit-learn.org/stable/modules/grid_search.html" target="_blank" rel="noopener">grid search dokümantasyonuna</a> bakın.</p>""",
    58: """    <h2 id="ozet-03">Özet</h2>
    <p>Bu bölümde model doğrulama ve hiperparametre optimizasyonu kavramını incelemeye başladık; önyargı–varyans ödünleşiminin sezgisel yönlerine ve modelleri veriye uydururken nasıl devreye girdiğine odaklandık.
    Özellikle daha karmaşık/esnek modellerde aşırı uyumdan kaçınmak için parametre ayarlarken doğrulama kümesi veya çapraz doğrulama kullanımının hayati olduğunu gördük.</p>
    <p>Sonraki bölümlerde özellikle yararlı modellerin ayrıntılarını, bu modeller için hangi ayarların mevcut olduğunu ve serbest parametrelerin model karmaşıklığını nasıl etkilediğini tartışacağız.
    Bu bölümün derslerini okurken makine öğrenmesi yaklaşımlarını öğrenirken aklınızda tutun!</p>""",
}

CODE_NAMES = {
    4: "load_iris_hparam.py",
    6: "knn_n1.py",
    8: "fit_predict_same_data.py",
    10: "accuracy_same_data.py",
    13: "train_test_split_iris.py",
    16: "two_fold_manual.py",
    18: "cross_val_score_5.py",
    20: "leave_one_out.py",
    22: "loo_mean.py",
    29: "polynomial_pipeline.py",
    31: "make_data_sine.py",
    33: "plot_poly_degrees.py",
    35: "validation_curve_degree.py",
    37: "best_poly_fit.py",
    40: "make_data_large.py",
    42: "validation_curve_large.py",
    47: "learning_curve_poly.py",
    50: "grid_search_poly.py",
    52: "grid_fit.py",
    54: "grid_best_params.py",
    56: "grid_best_plot.py",
}

INSERTS = {
    11: addon("Aynı veride eğitim ve test", "<p>Eğitim skorunun %100 olması genelde <strong>veri sızıntısı</strong> veya örnek tabanlı modellerde (1-NN) beklenen bir durumdur. Gerçek performans için mutlaka tutma veya çapraz doğrulama kullanın.</p>"),
    23: try_it("", "Iris verisinde 5 katlı çapraz doğrulama skorlarının ortalamasını hesaplayın:", """from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
X, y = load_iris(return_X_y=True)
model = KNeighborsClassifier(n_neighbors=1)
scores = cross_val_score(model, X, y, cv=5)
print("Skorlar:", scores)
print("Ortalama:", scores.mean())""", "deneme_cv_iris.py"),
}

if __name__ == "__main__":
    from gen_sklearn_00_02 import load_nb, cell_code, code_block, img_from_md

    nb = load_nb("05.03-Hyperparameters-and-Model-Validation.ipynb")
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
    body = "\n".join(parts) + "\n" + next_link("04-feature-engineering.html", "5.4 Öznitelik Mühendisliği")
    path = write_slug("03-hyperparameters-and-model-validation", body)
    print("wrote", path)
