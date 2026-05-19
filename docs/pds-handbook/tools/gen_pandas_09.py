#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_pandas_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_pandas_chapter import write_chapter

NB = "03.09-Pivot-Tables.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    if not code.strip():
        return ""
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>3.9 Pivot Tablolar</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html" target="_blank" rel="noopener">Pivot Tables</a></em></p>

    <p><code>groupby</code> soyutlamasının veri kümesi içindeki ilişkileri keşfetmeye nasıl yardımcı olduğunu gördük. <em>Pivot tablo</em>, elektronik tablolarda ve tablo verisiyle çalışan programlarda yaygın benzer bir işlemdir: sütun yönelimli veriyi alır, girişleri verinin çok boyutlu özetini veren iki boyutlu bir tabloda gruplar. Pivot tablolar ile <code>groupby</code> bazen karıştırılır; pivot tabloyu <code>groupby</code> agregasyonunun <em>çok boyutlu</em> sürümü olarak düşünmek yardımcı olur — böl ve birleştir hem tek boyutlu indeks yerine iki boyutlu ızgarada olur.</p>

    <h2 id="pivot-motivasyon">Pivot Tablolara Giriş</h2>

    <p>Bu bölümdeki örnekler için Seaborn üzerinden <em>Titanic</em> yolcu veri tabanını kullanacağız:</p>
""" + c(3, "import_titanic.py") + c(4, "titanic_head.py") + """
    <p>Çıktıda, felaketli yolculuktaki her yolcu için cinsiyet, yaş, sınıf, ödenen ücret ve daha fazlası yer alır.</p>

    <h2 id="elle-pivot">Elle Pivot Tablo</h2>

    <p>Veriyi anlamak için cinsiyet, hayatta kalma durumu veya bunların birleşimine göre gruplamak isteyebiliriz. Önceki bölümü okuduysanız <code>groupby</code> kullanmaya meyillisiniz — cinsiyete göre hayatta kalma oranı:</p>
""" + c(7, "titanic_survival_sex.py") + """
    <p>İlk içgörü: gemideki kadınların dörtte üçü, erkeklerin ise yaklaşık beşte biri hayatta kalmış!</p>

    <p>Bir adım daha gidip hem cinsiyet hem sınıfa göre hayatta kalma oranına bakalım. <code>groupby</code> sözcüğüyle: sınıf ve cinsiyete göre <em>grupla</em>, hayatta kalmayı <em>seç</em>, ortalama <em>uygula</em>, grupları <em>birleştir</em>, hiyerarşik indeksi <em>unstack</em> ile aç:</p>
""" + c(9, "titanic_groupby_unstack.py") + """
    <p>Cinsiyet ve sınıfın hayatta kalmayı nasıl etkilediğine dair daha iyi bir fikir verir; kod ise okunması zor bir dizi haline gelmeye başlar. Bu iki boyutlu <code>groupby</code> yeterince yaygındır; Pandas <code>pivot_table</code> adlı kısa yolu içerir.</p>

    <h2 id="pivot-sozdizimi">Pivot Tablo Sözdizimi</h2>

    <p>Önceki işlemin <code>DataFrame.pivot_table</code> ile eşdeğeri:</p>
""" + c(12, "titanic_pivot_table.py") + """
    <p>Elle <code>groupby</code> yaklaşımından çok daha okunaklıdır; aynı sonucu üretir. 20. yüzyıl başı transatlantik yolculuğunda hayatta kalma eğilimi hem üst sınıfları hem de veride kadın olarak kayıtlı yolcuları kayırır. Birinci sınıf kadınlar neredeyse kesin hayatta kalmış (merhaba Rose!); üçüncü sınıf erkeklerin yaklaşık sekizde biri (üzgünüz Jack!).</p>

    <h3 id="cok-duzeyli-pivot">Çok Düzeyli Pivot Tablolar</h3>

    <p><code>groupby</code>'da olduğu gibi pivot tablolarda gruplama birden fazla düzeyle ve seçeneklerle belirtilebilir. Yaşı üçüncü boyut olarak ekleyelim; <code>pd.cut</code> ile kutulayalım:</p>
""" + c(15, "titanic_pivot_age.py") + """
    <p>Sütunlar için de aynı strateji: ücret için <code>pd.qcut</code> ile otomatik niceleme:</p>
""" + c(17, "titanic_pivot_fare.py") + """
    <p>Sonuç, değerler arasındaki ilişkiyi ızgara düzeninde gösteren hiyerarşik indeksli (<a href="05-hierarchical-indexing.html">3.5 Hiyerarşik İndeksleme</a>) dört boyutlu bir agregasyondur.</p>

    <h3 id="pivot-ek-secenekler">Ek Pivot Tablo Seçenekleri</h3>

    <p><code>DataFrame.pivot_table</code> tam imzası (Pandas 1.3.5):</p>
""" + cb("""# Pandas 1.3.5 imzası
DataFrame.pivot_table(data, values=None, index=None, columns=None,
                      aggfunc='mean', fill_value=None, margins=False,
                      dropna=True, margins_name='All', observed=False,
                      sort=True)""", "pivot_table_signature.py", readonly=True) + """
    <p>İlk üç argümanı gördük; <code>fill_value</code> ve <code>dropna</code> eksik veriyle ilgilidir.</p>

    <p><code>aggfunc</code> hangi agregasyonun uygulanacağını denetler (varsayılan ortalama). <code>groupby</code>'da olduğu gibi dize (<code>'sum'</code>, <code>'mean'</code>, <code>'count'</code> vb.) veya fonksiyon olabilir; sütunlara eşleme sözlüğü de verilebilir:</p>
""" + c(20, "titanic_pivot_aggfunc_dict.py") + """
    <p><code>aggfunc</code> için eşleme verildiğinde <code>values</code> anahtar sözcüğü çoğu zaman otomatik belirlenir.</p>

    <p>Bazen her gruplama boyunca toplamlar yararlıdır; <code>margins</code> anahtar sözcüğü ile:</p>
""" + c(23, "titanic_pivot_margins.py") + """
    <p>Bu, sınıftan bağımsız cinsiyete göre hayatta kalma, cinsiyetten bağımsız sınıfa göre hayatta kalma ve genel %38 hayatta kalma oranını verir. Kenar etiketi <code>margins_name</code> ile değiştirilir (varsayılan <code>"All"</code>).</p>

    <h2 id="ornek-dogum">Örnek: Doğum Oranı Verisi</h2>

    <p>Başka bir örnek: ABD Hastalık Kontrol Merkezleri (CDC) doğum verisi. Veri <a href="https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv" target="_blank" rel="noopener">burada</a> bulunur (Andrew Gelman ve grubu tarafından kapsamlı analiz edilmiştir).</p>
""" + c(26, "download_births.sh") + c(27, "read_births_csv.py") + addon(
    "CDC verisi ve Pyodide",
    "<p><code>data/births.csv</code> yerel veya indirilmiş olmalıdır; Pyodide'da dosya yoksa indirme hücresini okuyun.</p>",
) + """
    <p>Veri görece basit — tarih ve cinsiyete göre gruplanmış doğum sayıları.</p>
""" + c(29, "births_head.py") + """
    <p><code>decade</code> sütunu ekleyip on yıllara göre erkek/kadın doğumlarına pivot tablo ile bakalım:</p>
""" + c(31, "births_pivot_decade.py") + """
    <p>Her on yılda erkek doğumları kadın doğumlarından fazladır. Pandas yerleşik <code>plot</code> ile yıllık trend görselleştirilebilir (Matplotlib bölümüne bakın):</p>
""" + c(33, "births_plot_year.py",) + """
    <p>Basit pivot tablo ve <code>plot</code> ile cinsiyete göre yıllık doğum eğilimi hemen görülür; son 50 yılda erkek doğumları kadın doğumlardan yaklaşık %5 fazla gibi görünür.</p>

    <p>Pivot tabloyla doğrudan ilgili olmasa da bu veri kümesinden Pandas araçlarıyla birkaç ilginç özellik daha çıkarılabilir. Önce veriyi temizleyelim — yanlış yazılmış tarihler (ör. 31 Haziran) veya eksik günler (99 Haziran) gibi aykırıları kırpma (robust sigma-clipping) ile kaldıralım:</p>
""" + c(36, "births_quartiles.py") + """
    <p>Son satır, 0,74 çarpanı Gauss dağılımının çeyreklikler aralığından gelen örneklem standart sapmasının sağlam bir tahminidir.</p>

    <p>Bu değerlerle <code>query</code> (<a href="12-performance-eval-and-query.html">3.12 eval ve query</a>) kullanarak aykırı satırları filtreleyebiliriz:</p>
""" + c(38, "births_query_clip.py") + """
    <p><code>day</code> sütununu tamsayı yapalım; bazı satırlarda <code>'null'</code> olduğu için önceden metindi:</p>
""" + c(40, "births_day_int.py") + """
    <p>Son olarak gün, ay ve yılı birleştirip tarih indeksi oluşturalım (<a href="11-working-with-time-series.html">3.11 Zaman Serileri</a>):</p>
""" + c(42, "births_datetime_index.py") + """
    <p>Bununla on yıllar boyunca haftanın gününe göre doğumları çizebiliriz:</p>
""" + c(44, "births_weekday_plot.py") + """
    <p>Görünüşe göre hafta sonları doğumlar hafta içinden biraz daha az! 1990 ve 2000'ler eksik — 1989'dan itibaren CDC verisi yalnızca doğum ayını içeriyor.</p>

    <p>İlginç bir başka görünüm: yılın gününe göre ortalama doğum sayısı. Önce ay ve güne göre gruplayalım:</p>
""" + c(46, "births_by_date_pivot.py") + """
    <p>Sonuç ay ve gün üzerinde çoklu indekstir. Görselleştirmek için ay ve günleri şubat 29'u doğru işleyen artık yıl ile birleştirip tarihe dönüştürelim:</p>
""" + c(48, "births_by_date_index.py") + """
    <p>Yalnızca ay ve güne odaklanınca yılın gününe göre ortalama doğum sayısını yansıtan bir zaman serimiz olur. <code>plot</code> ile çizildiğinde ilginç eğilimler görülür:</p>
""" + c(50, "births_by_date_plot.py") + addon(
    "Tatil düşüşü",
    "<p>Grafikte ABD tatillerinde (Bağımsızlık Günü, İşçi Bayramı, Şükran, Noel, Yılbaşı) doğum düşüşü belirgindir — çoğunlukla planlı doğumlar yerine kayıt/veri etkisini yansıtır.</p>",
) + """
    <p>Özellikle grafikte ABD tatillerinde doğum oranı düşüşü çarpıcıdır — büyük olasılıkla doğal doğumdan çok planlı/indüklenmiş doğum eğilimlerini yansıtır. Konuyla ilgili Andrew Gelman'ın blog yazısına bakın. Bu grafiğe Matplotlib araçlarıyla not eklemek için kitabın ilerleyen bölümlerine bakılacaktır.</p>

    <p>Bu kısa örnek, şimdiye kadar gördüğümüz Python ve Pandas araçlarının birleştirilerek çeşitli veri kümelerinden içgörü elde edilebileceğini gösterir. Bu veri manipülasyonlarının daha gelişmiş uygulamalarını sonraki bölümlerde göreceğiz!</p>
""" + try_it(
    "Şimdi deneyin",
    "Titanic verisinde (Seaborn yüklüyse) cinsiyet × sınıf hayatta kalma pivot tablosu oluşturun:",
    """import pandas as pd
try:
    import seaborn as sns
    t = sns.load_dataset('titanic')
    print(t.pivot_table('survived', index='sex', columns='class', aggfunc='mean'))
except Exception:
    df = pd.DataFrame({
        'sex': ['female','female','male','male'],
        'class': ['First','Third','First','Third'],
        'survived': [1, 0, 1, 0]
    })
    print(df.pivot_table('survived', index='sex', columns='class', aggfunc='mean'))""",
    "deneme_pivot_titanic.py",
) + next_link("10-working-with-strings.html", "3.10 Dizelerle Çalışma")

write_chapter("09-pivot-tables", body)
print("wrote 09-pivot-tables.html")
