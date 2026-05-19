#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_pandas_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_pandas_chapter import write_chapter

NB = "03.08-Aggregation-and-Grouping.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    if not code.strip():
        return ""
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


AGG_TABLE = """
    <motion-TABLE class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Agregasyon</th><th>Döndürdüğü</th></tr></thead>
        <tbody>
          <tr><td><code>count</code></td><td>Toplam öğe sayısı</td></tr>
          <tr><td><code>first</code>, <code>last</code></td><td>İlk ve son öğe</td></tr>
          <tr><td><code>mean</code>, <code>median</code></td><td>Ortalama ve medyan</td></tr>
          <tr><td><code>min</code>, <code>max</code></td><td>Minimum ve maksimum</td></tr>
          <tr><td><code>std</code>, <code>var</code></td><td>Standart sapma ve varyans</td></tr>
          <tr><td><code>mad</code></td><td>Ortalama mutlak sapma</td></tr>
          <tr><td><code>prod</code></td><td>Tüm öğelerin çarpımı</td></tr>
          <tr><td><code>sum</code></td><td>Tüm öğelerin toplamı</td></tr>
        </tbody>
      </table>
    </motion-TABLE>
""".replace("motion-TABLE", "div")


body = """
<h1>3.8 Agregasyon ve Gruplama</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html" target="_blank" rel="noopener">Aggregation and Grouping</a></em></p>

    <p>Birçok veri analizi görevinin temel parçası verimli özetlemedir: büyük bir veri kümesinin belirli yönlerini tek sayıyla özetleyen <code>sum</code>, <code>mean</code>, <code>median</code>, <code>min</code>, <code>max</code> gibi agregasyonlar. Bu bölümde Pandas'ta NumPy dizilerindekine benzer basit işlemlerden <code>groupby</code> kavramına dayalı daha gelişmiş işlemlere geçeceğiz.</p>

    <p>Kolaylık için önceki bölümlerdeki <code>display</code> yardımcı sınıfını kullanacağız:</p>
""" + c(3, "imports_display.py") + """
    <h2 id="planets-verisi">Planets Verisi</h2>

    <p>Seaborn paketindeki Planets veri kümesini kullanacağız (bkz. görselleştirme bölümleri). Diğer yıldızların çevresinde keşfedilen <em>ötegezegen</em>lere ilişkin bilgi içerir; Seaborn ile indirilebilir:</p>
""" + c(5, "load_planets.py") + c(6, "planets_head.py") + addon(
    "Seaborn ve Pyodide",
    "<p>Pyodide ortamında <code>seaborn</code> yüklüyse <code>sns.load_dataset('planets')</code> çalışır; aksi halde örnekleri okuyarak ilerleyin.</p>",
) + """
    <p>2014'e kadar keşfedilen 1000'den fazla ötegezegene ilişkin ayrıntılar içerir.</p>

    <h2 id="basit-agregasyon">Pandas'ta Basit Agregasyon</h2>

    <p><a href="../02-numpy/04-aggregates.html">2.4 Agregasyonlar</a>'da NumPy dizileri için agregasyonları gördük. Tek boyutlu <code>Series</code> için agregatlar tek değer döndürür:</p>
""" + c(10, "ser_random.py") + c(11, "ser_sum.py") + c(12, "ser_mean.py") + """
    <p><code>DataFrame</code> için varsayılan olarak agregatlar her sütun içinde sonuç üretir:</p>
""" + c(14, "df_random.py") + c(15, "df_mean.py") + """
    <p><code>axis</code> ile satırlar boyunca da agregasyon yapılabilir:</p>
""" + c(17, "df_mean_axis_columns.py") + """
    <p>Pandas <code>Series</code> ve <code>DataFrame</code> ortak agregasyonların yanı sıra her sütun için birkaç özet veren <code>describe</code> yöntemini içerir. Eksik satırları düşürerek Planets verisinde deneyelim:</p>
""" + c(19, "planets_describe.py") + """
    <p>Bu yöntem veri kümesinin genel özelliklerini anlamaya yardımcı olur. Örneğin <code>year</code> sütununda ötegezegenler 1989'dan beri keşfedilmiş olsa da veri kümesindeki gezegenlerin yarısı 2010 veya sonrasında keşfedilmiş — büyük ölçüde <em>Kepler</em> görevi sayesinde.</p>

    <p>Pandas'taki diğer yerleşik agregasyonların özeti:</p>
""" + AGG_TABLE + """
    <p>Bunların hepsi <code>DataFrame</code> ve <code>Series</code> yöntemleridir.</p>

    <p>Daha derine inmek için basit agregatlar çoğu zaman yeterli değildir. Bir sonraki düzey <code>groupby</code> işlemidir — verinin alt kümeleri üzerinde hızlı ve verimli agregasyon.</p>

    <h2 id="groupby">groupby: Böl, Uygula, Birleştir</h2>

    <p>Basit agregatlar veri kümesinin tadını verir; çoğu zaman etiket veya indekse göre koşullu agregasyon isteriz — SQL'deki “group by” komutundan gelen ad; Hadley Wickham'ın ifadesiyle <em>split, apply, combine</em> (böl, uygula, birleştir).</p>

    <h3 id="split-apply-combine">Split, Apply, Combine</h3>

    <p>“Uygula” adımının toplama agregasyonu olduğu kanonik örnek aşağıdaki şekilde gösterilir:</p>

    <figure class="handbook-figure">
      <img src="../../assets/images/03.08-split-apply-combine.png" alt="Split-apply-combine: veriyi gruplara bölme, agregasyon uygulama ve sonuçları birleştirme" width="700" loading="lazy">
      <figcaption>Split-apply-combine şeması (<a href="https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/06.00-Figure-Code.ipynb#Split-Apply-Combine" target="_blank" rel="noopener">kitap ek kodu</a>)</figcaption>
    </figure>

    <p><code>groupby</code> şunları yapar:</p>
    <ul>
      <li><strong>Böl (split):</strong> <code>DataFrame</code> belirtilen anahtar değerine göre parçalanır ve gruplanır.</li>
      <li><strong>Uygula (apply):</strong> Her grupta genelde agregasyon, dönüşüm veya filtreleme hesaplanır.</li>
      <li><strong>Birleştir (combine):</strong> Sonuçlar çıktı dizisinde birleştirilir.</li>
    </ul>

    <p>Bunu maskeleme, agregasyon ve birleştirme ile elle yapabilirdiniz; önemli nokta: ara bölümlerin açıkça oluşturulması gerekmez. <code>groupby</code> çoğu zaman tek geçişte her grup için toplam, ortalama, sayım vb. günceller. Gücü, kullanıcının alttaki hesabı düşünmeden işlemi bir bütün olarak görmesidir.</p>

    <p>Somut örnek için girdi <code>DataFrame</code>'ini oluşturalım:</p>
""" + c(27, "groupby_df_example.py") + """
    <p>En temel split-apply-combine, <code>DataFrame</code>'in <code>groupby</code> yöntemiyle istenen anahtar sütun adının verilmesiyle hesaplanır:</p>
""" + c(29, "df_groupby_key.py") + """
    <p>Dönen nesne bir <code>DataFrameGroupBy</code> nesnesidir, <code>DataFrame</code> kümesi değil. Gruplara “hazır” özel bir görünüm düşünün; agregasyon uygulanana kadar hesap yapılmaz (tembel değerlendirme).</p>
""" + c(31, "df_groupby_sum.py") + """
    <p><code>sum</code> yalnızca bir seçenektir; çoğu Pandas/NumPy agregasyonu ve birçok <code>DataFrame</code> işlemi uygulanabilir.</p>

    <h3 id="groupby-nesnesi">GroupBy Nesnesi</h3>

    <p><code>GroupBy</code> esnek bir soyutlamadır; altta daha gelişmiş işlemler yapılır. Planets verisiyle örnekler: <em>aggregate</em>, <em>filter</em>, <em>transform</em>, <em>apply</em> — sonraki alt bölümde; önce temel <code>GroupBy</code> işlevleri.</p>

    <h4 id="sutun-indeksleme">Sütun indeksleme</h4>

    <p><code>GroupBy</code>, <code>DataFrame</code> gibi sütun indekslemesini destekler:</p>
""" + c(35, "planets_groupby_method.py") + c(36, "planets_groupby_orbital.py") + """
    <p>Orijinal gruptan belirli bir <code>Series</code> seçildi; agregasyon çağrılana kadar hesap yok:</p>
""" + c(38, "planets_orbital_median.py") + """
    <p>Her yöntemin duyarlı olduğu yörünge periyodu (gün) ölçeğine dair fikir verir.</p>

    <h4 id="gruplar-uzerinde-dongu">Gruplar üzerinde döngü</h4>

    <p><code>GroupBy</code> gruplar üzerinde doğrudan yineleme destekler:</p>
""" + c(41, "planets_groupby_iter.py") + """
    <p>Hata ayıklma için elle incelemede yararlıdır; çoğu zaman yerleşik <code>apply</code> daha hızlıdır.</p>

    <h4 id="dispatch-yontemleri">Dispatch yöntemleri</h4>

    <p><code>GroupBy</code>'da açıkça tanımlanmayan yöntemler gruplara iletilir; <code>describe</code> her grup için <code>describe</code> çağırmaya eşdeğerdir:</p>
""" + c(44, "planets_year_describe.py") + """
    <p>Bu tablo veriyi anlamaya yardımcı olur: 2014'e kadar gezegenlerin büyük çoğunluğu Radial Velocity ve Transit yöntemleriyle keşfedilmiş; Transit son yıllarda yaygınlaşmış. Transit Timing Variation ve Orbital Brightness Modulation 2011'den sonra kullanılmış.</p>

    <h3 id="agg-filter-transform-apply">Aggregate, Filter, Transform, Apply</h3>

    <p>Önceki tartışma birleştirme için agregasyona odaklandı; <code>GroupBy</code>'da <code>aggregate</code>, <code>filter</code>, <code>transform</code> ve <code>apply</code> de vardır. Aşağıdaki alt bölümler için örnek <code>DataFrame</code>:</p>
""" + c(47, "agg_filter_df.py") + """
    <h4 id="aggregation">Aggregation</h4>

    <p><code>sum</code>, <code>median</code> ile tanıdık agregasyonların ötesinde <code>aggregate</code> daha fazla esneklik sunar — dize, fonksiyon veya liste alıp hepsini birden hesaplayabilir:</p>
""" + c(49, "groupby_aggregate_multi.py") + """
    <p>Yaygın desen: sütun adlarını o sütuna uygulanacak işlemlere eşleyen sözlük:</p>
""" + c(51, "groupby_aggregate_dict.py") + """
    <h4 id="filtering">Filtering</h4>

    <p>Filtreleme, grup özelliklerine göre veriyi düşürür. Örneğin standart sapması eşiğin üstündeki grupları tutmak:</p>
""" + c(53, "groupby_filter_func.py") + """
    <p>Filtre fonksiyonu grubun geçip geçmeyeceğini belirten Boolean döndürmelidir. Burada A grubunun standart sapması 4'ten büyük olmadığı için düşürülür.</p>

    <h4 id="transformation">Transformation</h4>

    <p>Agregasyon verinin küçültülmüş biçimini döndürürken dönüşüm, birleştirmek için tam verinin dönüştürülmüş biçimini döndürür — çıktı girişle aynı şekildedir. Yaygın örnek: grup ortalamasını çıkararak ortalamak:</p>
""" + c(56, "groupby_transform_center.py") + """
    <h4 id="apply-yontemi">apply yöntemi</h4>

    <p><code>apply</code>, gruba keyfi bir fonksiyon uygular. Fonksiyon <code>DataFrame</code> alıp Pandas nesnesi veya skaler döndürmelidir. Örneğin ilk sütunu ikincinin toplamına göre normalize etmek:</p>
""" + c(58, "groupby_apply_norm.py") + addon(
    "apply ve SettingWithCopy",
    "<p><code>apply</code> içinde sütunlara atama yapmak bazen uyarı üretir; üretim kodunda <code>transform</code> veya açık döngü tercih edin.</p>",
) + """
    <p><code>GroupBy</code> içinde <code>apply</code> esnektir; tek ölçüt fonksiyonun <code>DataFrame</code> alıp Pandas nesnesi veya skaler döndürmesidir.</p>

    <h3 id="split-anahtari">Bölme Anahtarının Belirtilmesi</h3>

    <p>Basit örneklerde <code>DataFrame</code> tek sütun adına göre bölündü. Gruplar başka yollarla da tanımlanabilir.</p>

    <h4 id="liste-dizi-seri-indeks">Liste, dizi, seri veya indeks</h4>

    <p>Anahtar, <code>DataFrame</code> uzunluğuyla eşleşen herhangi bir seri veya liste olabilir:</p>
""" + c(62, "groupby_list_L.py") + """
    <p>Bu, <code>df.groupby('key')</code>'nin daha ayrıntılı eşdeğeridir:</p>
""" + c(64, "groupby_df_key.py") + """
    <h4 id="sozluk-seri-esleme">Sözlük veya seri ile indeks eşlemesi</h4>

    <p>İndeks değerlerini grup anahtarlarına eşleyen sözlük de verilebilir:</p>
""" + c(66, "groupby_mapping.py") + """
    <h4 id="python-fonksiyonu">Herhangi bir Python fonksiyonu</h4>

    <p>İndeks değerini alıp grup döndüren herhangi bir fonksiyon:</p>
""" + c(68, "groupby_str_lower.py") + """
    <h4 id="gecerli-anahtar-listesi">Geçerli anahtarların listesi</h4>

    <p>Önceki anahtar seçenekleri çoklu indeks için birleştirilebilir:</p>
""" + c(70, "groupby_multi_keys.py") + """
    <h3 id="gruplama-ornegi">Gruplama Örneği</h3>

    <p>Birkaç satır Python ile yöntem ve on yıla göre keşfedilen gezegen sayısını sayabiliriz:</p>
""" + c(72, "planets_decade_method.py") + """
    <p>Bu, gerçekçi veri kümelerinde öğrendiğimiz işlemleri birleştirmenin gücünü gösterir: ötegezegenlerin ilk keşfinden sonra ne zaman ve nasıl tespit edildiğine dair kaba bir resim hızla elde edilir.</p>

    <p>Bu kod satırlarını adım adım inceleyip her adımın sonuca ne yaptığını anlamanızı öneririm — karmaşık görünse de parçaları anlamak kendi verinizi keşfetmenin yolunu açar.</p>
""" + try_it(
    "Şimdi deneyin",
    "<code>planets</code> verisinde (veya küçük bir örnek çerçevede) <code>groupby('method')['distance'].median()</code> hesaplayın:",
    """import pandas as pd
try:
    import seaborn as sns
    planets = sns.load_dataset('planets')
    print(planets.groupby('method')['distance'].median())
except Exception as e:
    df = pd.DataFrame({'method': ['A','A','B'], 'distance': [1.0, 2.0, 5.0]})
    print(df.groupby('method')['distance'].median())""",
    "deneme_groupby_median.py",
) + next_link("09-pivot-tables.html", "3.9 Pivot Tablolar")

write_chapter("08-aggregation-and-grouping", body)
print("wrote 08-aggregation-and-grouping.html")
