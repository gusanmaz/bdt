#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_pandas_helpers import code_block as cb, addon, try_it, next_link
from write_pandas_chapter import write_chapter

body = """
<h1>3.4 Eksik Veri</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html" target="_blank" rel="noopener">Handling Missing Data</a></em></p>

    <p>Eğitimlerdeki veri ile gerçek dünyadaki veri arasındaki fark, gerçek verinin nadiren temiz ve homojen olmasıdır. Özellikle ilginç veri kümelerinde bir miktar eksik veri bulunur. Daha da karmaşıklaştıran şey, farklı kaynakların eksik veriyi farklı biçimlerde göstermesidir.</p>

    <p>Bu bölümde eksik veri için genel düşünceleri, Pandas'ın bunu nasıl temsil ettiğini ve Python'da eksik veriyi işlemek için Pandas'ın yerleşik araçlarını ele alacağız. Kitap boyunca eksik veriyi genel olarak <em>null</em>, <em>NaN</em> veya <em>NA</em> değerleri diye anacağız.</p>

    <h2 id="eksik-veri-sozlesmeleri">Eksik Veri Sözleşmelerinde Ödünleşimler</h2>

    <p>Bir tablo veya <code>DataFrame</code>'de eksik verinin varlığını izlemek için çeşitli yaklaşımlar geliştirilmiştir. Genelde iki stratejiden biri etrafında döner: eksik değerleri genel olarak gösteren bir <em>maske</em> kullanmak veya eksik girişi belirten bir <em>gösterge değeri</em> (sentinel) seçmek.</p>

    <p>Maskeleme yaklaşımında maske tamamen ayrı bir Boolean dizi olabilir veya veri gösteriminde bir bit ayrılarak değerin yerel null durumu belirtilebilir.</p>

    <p>Sentinel yaklaşımında gösterge, eksik tamsayı için –9999 gibi veriye özgü bir kural veya kayan nokta için <code>NaN</code> (Not a Number) gibi IEEE kayan nokta standardının parçası olan özel bir değer olabilir.</p>

    <p>Hiçbir yaklaşım ödünsüz değildir. Ayrı maske dizisi ek Boolean depolama ve hesaplama yükü getirir. Sentinel, temsil edilebilir geçerli değer aralığını daraltır ve <code>NaN</code> gibi özel değerler her veri tipinde olmadığı için ek mantık gerekebilir.</p>

    <p>Farklı diller ve sistemler farklı sözleşmeler kullanır: R her veri tipinde ayrılmış bit desenleri kullanır; SciDB her hücreye NA durumu için ek bir bayt ekler.</p>

    <h2 id="pandas-eksik-veri">Pandas'ta Eksik Veri</h2>

    <p>Pandas'ın eksik değerleri işleme biçimi, kayan nokta dışı tipler için yerleşik NA kavramı olmayan NumPy paketine bağımlılığıyla sınırlıdır.</p>

    <p>R'nin her tip için bit deseni ayırması NumPy'nin 14 temel tamsayı tipi (bit genişliği, işaret, endianness) gibi çok daha fazla tipi desteklemesi nedeniyle hantal olurdu. Tüm NumPy tiplerinde özel bit ayırmak büyük ek yük ve muhtemelen NumPy çatallaması gerektirirdi; 8 bit tamsayılarda bir biti maske olarak kullanmak temsil aralığını ciddi daraltır.</p>

    <p>Bu kısıtlar nedeniyle Pandas eksik değerleri iki \"modda\" saklar ve işler:</p>
    <ul>
      <li>Varsayılan: sentinel tabanlı şema — <code>NaN</code> veya <code>None</code> (veri tipine göre).</li>
      <li>İsteğe bağlı: Pandas'ın sunduğu nullable dtype'lar; eşlik eden maske dizisi ve kullanıcıya <code>pd.NA</code> olarak sunulan eksik girişler.</li>
    </ul>
    <p>Her iki durumda da Pandas API işlemleri eksik girişleri öngörülebilir biçimde işler ve yayar. Seçimlerin nedenini anlamak için <code>None</code>, <code>NaN</code> ve <code>NA</code> ödünleşimlerine kısaca bakalım. Her zamanki gibi NumPy ve Pandas'ı içe aktararak başlayalım:</p>
""" + cb("""import numpy as np
import pandas as pd""", "import_np_pd.py") + """
    <h3 id="none-sentinel">None Gösterge Değeri Olarak</h3>

    <p>Bazı veri tiplerinde Pandas gösterge olarak <code>None</code> kullanır. <code>None</code> bir Python nesnesidir; <code>None</code> içeren her dizi <code>dtype=object</code> olmalıdır — Python nesneleri dizisi.</p>

    <p>Örneğin <code>None</code>'ı NumPy dizisine geçirirseniz:</p>
""" + cb("""vals1 = np.array([1, None, 2, 3])
vals1""", "vals1_none.py") + """
    <p><code>dtype=object</code>, NumPy'nin içerik için çıkardığı en iyi ortak temsilin Python nesneleri olduğu anlamına gelir. <code>None</code> kullanmanın dezavantajı, işlemlerin Python düzeyinde, yerel tiplerdeki hızlı işlemlere göre çok daha yavaş yapılmasıdır:</p>
""" + cb("%timeit np.arange(1E6, dtype=int).sum()", "timeit_int.py", readonly=True) + cb("%timeit np.arange(1E6, dtype=object).sum()", "timeit_object.py", readonly=True) + """
    <p>Python <code>None</code> ile aritmetik desteklemediğinden <code>sum</code> veya <code>min</code> gibi toplamalar genelde hata verir:</p>
""" + cb("vals1.sum()", "vals1_sum.py") + addon("IPython %timeit", "<p><code>%timeit</code> satırları yalnızca IPython/Jupyter'de çalışır; bu sayfada salt okunur gösterilir. Pyodide'da benzer karşılaştırma için <code>time.perf_counter()</code> kullanın.</p>") + """
    <p>Bu nedenle Pandas sayısal dizilerinde gösterge olarak <code>None</code> kullanmaz.</p>

    <h3 id="nan-sayisal">NaN: Eksik Sayısal Veri</h3>

    <p>Diğer gösterge <code>NaN</code> farklıdır; IEEE kayan nokta standardını kullanan tüm sistemler tarafından tanınan özel bir kayan nokta değeridir:</p>
""" + cb("""vals2 = np.array([1, np.nan, 3, 4])
vals2""", "vals2_nan.py") + """
    <p>NumPy bu dizi için yerel kayan nokta tipi seçti: nesne dizisinin aksine derlenmiş kodda hızlı işlemler desteklenir. <code>NaN</code> bir veri virüsü gibidir — dokunduğu her işlemin sonucu yine <code>NaN</code> olur:</p>
""" + cb("1 + np.nan", "one_plus_nan.py") + cb("0 * np.nan", "zero_times_nan.py") + """
    <p>Toplamlar tanımlıdır (hata vermez) ancak her zaman yararlı değildir:</p>
""" + cb("vals2.sum(), vals2.min(), vals2.max()", "vals2_agg.py") + """
    <p>NumPy eksik değerleri yok sayan <code>nan*</code> toplama sürümleri sağlar:</p>
""" + cb("np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)", "nan_agg.py") + addon("NaN toplamları", "<p><code>np.nansum</code>, <code>np.nanmean</code> vb. eksik veriyi atlar. Pandas'ta <code>skipna=True</code> varsayılandır.</p>") + """
    <p><code>NaN</code>'ın ana dezavantajı özellikle kayan nokta değeri olmasıdır; tamsayı, dize vb. için eşdeğer yoktur.</p>

    <h3 id="nan-none-pandas">Pandas'ta NaN ve None</h3>

    <p><code>NaN</code> ve <code>None</code> ikisi de yer bulur; Pandas ikisini neredeyse birbirinin yerine kullanılabilir şekilde işler, uygun yerde dönüştürür:</p>
""" + cb("pd.Series([1, np.nan, 2, None])", "series_nan_none.py") + """
    <p>Sentinel değeri olmayan tiplerde NA varken Pandas otomatik tip yükseltmesi yapar. Tamsayı dizisine <code>np.nan</code> atanırsa kayan noktaya yükseltilir:</p>
""" + cb("""x = pd.Series(range(2), dtype=int)
x""", "series_int.py") + cb("""x[0] = None
x""", "series_int_none.py") + """
    <p>Tamsayı dizisinin kayan noktaya yükseltilmesine ek olarak Pandas <code>None</code>'ı <code>NaN</code>'a dönüştürür. R gibi alan dillere göre sihirli görünebilir; pratikte nadiren sorun çıkarır.</p>

    <p>NA girildiğinde Pandas yükseltme kuralları:</p>
    <motion-placeholder class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Tip sınıfı</th><th>NA saklanırken dönüşüm</th><th>NA göstergesi</th></tr></thead>
        <tbody>
          <tr><td><code>floating</code></td><td>Değişmez</td><td><code>np.nan</code></td></tr>
          <tr><td><code>object</code></td><td>Değişmez</td><td><code>None</code> veya <code>np.nan</code></td></tr>
          <tr><td><code>integer</code></td><td><code>float64</code>'e yükselir</td><td><code>np.nan</code></td></tr>
          <tr><td><code>boolean</code></td><td><code>object</code>'e yükselir</td><td><code>None</code> veya <code>np.nan</code></td></tr>
        </tbody>
      </table>
    </motion-placeholder>
    <p>Pandas'ta dize verisi her zaman <code>object</code> dtype ile saklanır.</p>
""".replace("motion-placeholder", "div") + """
    <h2 id="nullable-dtypes">Pandas Nullable Dtype'lar</h2>

    <p>Erken Pandas sürümlerinde yalnızca <code>NaN</code> ve <code>None</code> sentinel değerleri vardı; örtük tip yükseltmesi (ör. gerçek eksik verili tamsayı dizisi yoktu) zordu. Bunun için <em>nullable dtype</em>'lar eklendi — adları büyük harfle yazılır (<code>pd.Int32</code> vs <code>np.int32</code>). Geriye uyumluluk için yalnızca açıkça istenince kullanılır.</p>

    <p>Üç eksik veri göstergesini içeren tamsayı <code>Series</code> örneği:</p>
""" + cb("pd.Series([1, np.nan, 2, None, pd.NA], dtype='Int32')", "nullable_int32.py") + """
    <p>Bu gösterim bölümün geri kalanındaki tüm işlemlerde diğerleriyle birbirinin yerine kullanılabilir.</p>

    <h2 id="null-islemler">Null Değerler Üzerinde İşlem</h2>

    <p>Pandas <code>None</code>, <code>NaN</code> ve <code>NA</code>'yı eksik/null için esasen birbirinin yerine kullanılabilir sayar. Kolaylık için şu yöntemler vardır:</p>
    <ul>
      <li><code>isnull</code> / <code>isna</code>: eksik değerler için Boolean maske</li>
      <li><code>notnull</code> / <code>notna</code>: <code>isnull</code>'un tersi</li>
      <li><code>dropna</code>: filtrelenmiş veri</li>
      <li><code>fillna</code>: eksik değerler doldurulmuş kopya</li>
    </ul>
    <p>Bu bölümü bu rutinlerin kısa gösterimiyle bitiriyoruz.</p>

    <h3 id="null-tespit">Null Değerleri Tespit Etme</h3>
    <p><code>isnull</code> ve <code>notnull</code> (veya <code>isna</code> / <code>notna</code>) Boolean maske döndürür:</p>
""" + cb("data = pd.Series([1, np.nan, 'hello', None])", "data_series.py") + cb("data.isnull()", "data_isnull.py") + """
    <p><a href="02-data-indexing-and-selection.html">3.2 Veri İndeksleme ve Seçimi</a>'nde anlatıldığı gibi Boolean maskeler doğrudan <code>Series</code> veya <code>DataFrame</code> indeksi olarak kullanılabilir:</p>
""" + cb("data[data.notnull()]", "data_notnull_mask.py") + """
    <p><code>DataFrame</code> için de benzer Boolean sonuçlar üretilir.</p>

    <h3 id="null-silme">Null Değerleri Silme</h3>
    <p><code>dropna</code> (NA kaldırır) ve <code>fillna</code> (NA doldurur) vardır. <code>Series</code> için sonuç doğrudandır:</p>
""" + cb("data.dropna()", "data_dropna.py") + """
    <p><code>DataFrame</code> için daha fazla seçenek vardır. Örnek:</p>
""" + cb("""df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
df""", "df_nan.py") + """
    <p><code>DataFrame</code>'den tek değer değil yalnızca tüm satır veya sütun silinebilir. <code>dropna</code> birçok seçenek sunar.</p>
    <p>Varsayılan olarak <em>herhangi</em> null içeren tüm satırlar silinir:</p>
""" + cb("df.dropna()", "df_dropna_rows.py") + """
    <p><code>axis=1</code> veya <code>axis='columns'</code> ile null içeren sütunlar silinir:</p>
""" + cb("df.dropna(axis='columns')", "df_dropna_cols.py") + """
    <p>Bu iyi veriyi de atar; yalnızca <em>tüm</em> veya çoğunlukla NA olan satır/sütunları silmek isteyebilirsiniz — <code>how</code> veya <code>thresh</code> ile.</p>
    <p>Varsayılan <code>how='any'</code>: herhangi bir null varsa satır/sütun gider. <code>how='all'</code> yalnızca <em>hepsi</em> null ise siler:</p>
""" + cb("""df[3] = np.nan
df""", "df_col3_nan.py") + cb("df.dropna(axis='columns', how='all')", "df_dropna_how_all.py") + """
    <p><code>thresh</code> satır/sütunun tutulması için gereken minimum null olmayan sayısını belirtir:</p>
""" + cb("df.dropna(axis='rows', thresh=3)", "df_dropna_thresh.py") + """
    <p>İlk ve son satır yalnızca iki null olmayan değer içerdiği için silindi.</p>

    <h3 id="null-doldurma">Null Değerleri Doldurma</h3>
    <p>Bazen NA silmek yerine geçerli bir değerle değiştirmek istersiniz — sıfır, imputasyon veya interpolasyon. <code>isnull</code> maskesiyle yapılabilir; yaygın olduğu için <code>fillna</code> null değerlerin değiştirildiği kopya döndürür.</p>
""" + cb("""data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'), dtype='Int32')
data""", "data_fill_series.py") + """
    <p>Tek değerle doldurma (ör. sıfır):</p>
""" + cb("data.fillna(0)", "fillna_zero.py") + """
    <p>İleri doldurma (önceki değeri yayma):</p>
""" + cb("""# forward fill
data.fillna(method='ffill')""", "fillna_ffill.py") + """
    <p>Geri doldurma (sonraki değeri geriye yayma):</p>
""" + cb("""# back fill
data.fillna(method='bfill')""", "fillna_bfill.py") + addon("fillna method", "<p>Yeni Pandas sürümlerinde <code>method='ffill'</code> yerine <code>ffill()</code> / <code>bfill()</code> tercih edilir; kitap not defteri eski API'yi gösterir.</p>") + """
    <p><code>DataFrame</code>'de benzer seçenekler ve doldurmanın yapılacağı <code>axis</code>:</p>
""" + cb("df", "df_refill.py") + cb("df.fillna(method='ffill', axis=1)", "df_fillna_ffill_axis1.py") + """
    <p>İleri doldurmada önceki değer yoksa NA kalır.</p>
""" + try_it("Şimdi deneyin", "Eksik değerli küçük bir <code>DataFrame</code> oluşturup <code>dropna</code> ve <code>fillna(0)</code> sonuçlarını karşılaştırın:", """import pandas as pd
import numpy as np
df = pd.DataFrame({'a': [1, np.nan, 3], 'b': [4, 5, np.nan]})
print(df)
print("\\ndropna:\\n", df.dropna())
print("\\nfillna(0):\\n", df.fillna(0))""", "deneme_drop_fill.py") + try_it("Şimdi deneyin", "<code>isnull()</code> maskesiyle yalnızca eksik olmayan satırları seçin:", """import pandas as pd
import numpy as np
s = pd.Series([1, np.nan, 3, None])
print(s[s.notnull()])""", "deneme_notnull.py") + addon("isna ve isnull", "<p><code>isna()</code> ile <code>isnull()</code> aynıdır; modern kodda <code>isna</code> / <code>notna</code> daha yaygındır.</p>") + next_link("05-hierarchical-indexing.html", "3.5 Hiyerarşik İndeksleme")

write_chapter("04-missing-values", body)
print("ch04 code blocks:", body.count("code-block"))
