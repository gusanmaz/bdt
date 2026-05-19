#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_pandas_helpers import code_block as cb, addon, try_it, next_link
from write_pandas_chapter import write_chapter

body = """
<h1>3.5 Hiyerarşik İndeksleme</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/03.05-hierarchical-indexing.html" target="_blank" rel="noopener">Hierarchical Indexing</a></em></p>

    <p>Şimdiye kadar esas olarak Pandas <code>Series</code> ve <code>DataFrame</code> nesnelerinde bir ve iki boyutlu veriye odaklandık. Çoğu zaman bir veya iki anahtardan fazla indekslenmiş daha yüksek boyutlu veri saklamak yararlıdır. Erken Pandas sürümleri <code>Panel</code> ve <code>Panel4D</code> sundu; pratikte hantal kaldılar. Daha yaygın desen, tek bir indekste birden fazla indeks <em>düzeyi</em> barındıran <em>hiyerarşik indeksleme</em> (çoklu indeksleme) kullanmaktır. Böylece yüksek boyutlu veri tanıdık bir ve iki boyutlu nesnelerde kompakt temsil edilir. (Pandas tarzı esnek indeksli gerçek <em>N</em> boyutlu diziler için <a href="https://xarray.pydata.org/" target="_blank" rel="noopener">Xarray</a> paketine bakın.)</p>

    <p>Bu bölümde <code>MultiIndex</code> nesnelerinin doğrudan oluşturulması, çoklu indeksli veride indeksleme, dilimleme ve istatistik, basit ile hiyerarşik gösterimler arası dönüşüm rutinleri ele alınır.</p>

    <p>Standart içe aktarmalarla başlayalım:</p>
""" + cb("""import pandas as pd
import numpy as np""", "import_pd_np.py") + """
    <h2 id="coklu-indeksli-series">Çoklu İndeksli Series</h2>

    <p>İki boyutlu veriyi tek boyutlu <code>Series</code> içinde nasıl temsil edebileceğimizi düşünelim. Somut örnek: her noktanın metin ve sayısal anahtarı olan bir dizi.</p>

    <h3 id="kotu-yol">Kötü Yol</h3>

    <p>İki farklı yıldan eyalet verisi izlemek isteyelim. Mevcut araçlarla Python demetlerini anahtar olarak kullanmaya meyillisiniz:</p>
""" + cb("""index = [('California', 2010), ('California', 2020),
         ('New York', 2010), ('New York', 2020),
         ('Texas', 2010), ('Texas', 2020)]
populations = [37253956, 39538223,
               19378102, 20201249,
               25145561, 29145505]
pop = pd.Series(populations, index=index)
pop""", "pop_tuple_index.py") + """
    <p>Bu şemayla seriyi demet indeksine göre dilimleyebilirsiniz:</p>
""" + cb("pop[('California', 2020):('Texas', 2010)]", "pop_slice_tuple.py") + """
    <p>Kolaylık burada biter. 2010'daki tüm değerleri seçmek için dağınık (ve büyük veride yavaş) dönüşüm gerekir:</p>
""" + cb("pop[[i for i in pop.index if i[1] == 2010]]", "pop_filter_2010.py") + """
    <p>İstenen sonuç gelir ama Pandas'ın sevdiğimiz dilimleme sözdizimi kadar temiz veya verimli değildir.</p>

    <h3 id="multiindex-daha-iyi">Daha İyi Yol: Pandas MultiIndex</h3>
    <p>Neyse ki Pandas daha iyi bir yol sunar. Demet tabanlı indeksleme ilkel bir çoklu indekstir; <code>MultiIndex</code> istediğimiz işlemleri sağlar:</p>
""" + cb("index = pd.MultiIndex.from_tuples(index)", "multiindex_from_tuples.py") + """
    <p><code>MultiIndex</code> birden fazla <em>düzey</em> (burada eyalet ve yıl) ve her veri noktası için bu düzeyleri kodlayan <em>etiketler</em> temsil eder.</p>
""" + cb("""pop = pop.reindex(index)
pop""", "pop_reindex_multi.py") + """
    <p>Series gösteriminin ilk iki sütunu çoklu indeks değerlerini, üçüncüsü veriyi gösterir. İlk sütunda boş girişler, bir üst satırla aynı değeri gösterir.</p>
""" + addon("boş satır = tekrar", "<p>Çoklu indeks görünümünde boş hücre, bir üstteki etiketin devamıdır — okunabilirlik içindir.</p>") + """
    <p>İkinci indeksi 2020 olan tüm verilere Pandas dilimleme ile erişelim:</p>
""" + cb("pop[:, 2020]", "pop_slice_2020.py") + """
    <p>Sonuç, ilgilendiğimiz anahtarlarla tek indeksli bir <code>Series</code>'tir. Bu sözdizimi demet tabanlı çözümden çok daha kullanışlı ve verimlidir.</p>

    <h3 id="multiindex-ek-boyut">MultiIndex Ek Boyut Olarak</h3>

    <p>Aynı veriyi indeks ve sütun etiketli basit <code>DataFrame</code> ile de saklayabilirdik. Pandas bu eşdeğerliği göz önünde bulundurur. <code>unstack</code> çoklu indeksli <code>Series</code>'i geleneksel <code>DataFrame</code>'e çevirir:</p>
""" + cb("""pop_df = pop.unstack()
pop_df""", "pop_unstack.py") + """
    <p><code>stack</code> ters işlemdir:</p>
""" + cb("pop_df.stack()", "pop_stack.py") + """
    <p>Neden hiyerarşik indeksleme? İki boyutlu veriyi <code>Series</code> içinde çoklu indeksle yönettiğimiz gibi, üç veya daha fazla boyutu <code>Series</code> veya <code>DataFrame</code>'de yönetebiliriz. Her ek düzey ek bir veri boyutudur:</p>
""" + cb("""pop_df = pd.DataFrame({'total': pop,
                       'under18': [9284094, 8898092,
                                   4318033, 4181528,
                                   6879014, 7432474]})
pop_df""", "pop_df_under18.py") + """
    <p><a href="03-operations-in-pandas.html">3.3 Pandas'ta İşlemler</a>'deki ufunc'lar ve diğer işlevler hiyerarşik indekslerle de çalışır. 18 yaş altı oranı:</p>
""" + cb("""f_u18 = pop_df['under18'] / pop_df['total']
f_u18.unstack()""", "f_u18_unstack.py") + """
    <p>Böylece yüksek boyutlu veriyi kolayca keşfedip işleyebiliriz.</p>

    <h2 id="multiindex-olusturma">MultiIndex Oluşturma Yöntemleri</h2>

    <p>En doğrudan yol, oluşturucuya iki veya daha fazla indeks dizisi vermektir:</p>
""" + cb("""df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
df""", "df_multiindex_ctor.py") + """
    <p><code>MultiIndex</code> oluşturma arka planda yapılır. Uygun demet anahtarlı sözlük verilirse Pandas otomatik <code>MultiIndex</code> kullanır:</p>
""" + cb("""data = {('California', 2010): 37253956,
        ('California', 2020): 39538223,
        ('New York', 2010): 19378102,
        ('New York', 2020): 20201249,
        ('Texas', 2010): 25145561,
        ('Texas', 2020): 29145505}
pd.Series(data)""", "series_from_dict_tuples.py") + """
    <p>Bazen <code>MultiIndex</code>'i açıkça oluşturmak yararlıdır.</p>

    <h3 id="acik-multiindex">Açık MultiIndex Oluşturucuları</h3>

    <p><code>pd.MultiIndex</code> sınıfı oluşturucuları daha esnek indeks yapısı sağlar:</p>
""" + cb("pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])", "mi_from_arrays.py") + """
    <p>Her noktanın çoklu indeks değerlerini veren demet listesinden:</p>
""" + cb("pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])", "mi_from_tuples.py") + """
    <p>Tek indekslerin Kartezyen çarpımından:</p>
""" + cb("pd.MultiIndex.from_product([['a', 'b'], [1, 2]])", "mi_from_product.py") + """
    <p><code>levels</code> (her düzeydeki etiket listeleri) ve <code>codes</code> (bu etiketlere referans) ile:</p>
""" + cb("""pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              codes=[[0, 0, 1, 1], [0, 1, 0, 1]])""", "mi_levels_codes.py") + """
    <p>Bunların hepsi <code>Series</code> veya <code>DataFrame</code> oluştururken <code>index</code> olarak veya <code>reindex</code> ile verilebilir.</p>

    <h3 id="duzey-isimleri">MultiIndex Düzey İsimleri</h3>

    <p>Düzeylere isim vermek için <code>names</code> argümanı veya sonradan <code>names</code> özniteliği:</p>
""" + cb("""pop.index.names = ['state', 'year']
pop""", "pop_index_names.py") + """
    <p>Karmaşık veri kümelerinde indeks anlamını takip etmeye yardımcı olur.</p>

    <h3 id="sutun-multiindex">Sütunlar için MultiIndex</h3>

    <p><code>DataFrame</code>'de satır ve sütun simetriktir; sütunlar da çoklu düzeyli olabilir. Örnek tıbbi veri:</p>
""" + cb("""# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data""", "health_data.py") + """
    <p>Temelde dört boyutlu veri: konu, ölçüm tipi, yıl, ziyaret. Üst düzey sütunla kişi adına göre indeksleyebiliriz:</p>
""" + cb("health_data['Guido']", "health_guido.py") + """
    <h2 id="multiindex-indeksleme">MultiIndex'te İndeksleme ve Dilimleme</h2>

    <p>Çoklu indeksli veride indeksleme sezgiseldir; indeksleri ek boyutlar gibi düşünmek yardımcı olur. Önce <code>Series</code>, sonra <code>DataFrame</code>.</p>

    <h3 id="coklu-series-indeks">Çoklu İndeksli Series</h3>
""" + cb("pop", "pop_ref.py") + """
    <p>Birden fazla terimle tek elemana erişim:</p>
""" + cb("pop['California', 2010]", "pop_cal_2010.py") + """
    <p><em>Kısmi indeksleme</em>: yalnızca bir düzey — sonuç alt düzeyleri koruyan başka bir <code>Series</code>:</p>
""" + cb("pop['California']", "pop_california.py") + """
    <p>Kısmi dilimleme, <code>MultiIndex</code> sıralı olduğunda mümkündür (<a href="#sirali-indeksler">Sıralı ve Sırasız İndeksler</a>):</p>
""" + cb("pop.loc['California':'New York']", "pop_loc_slice.py") + """
    <p>Sıralı indekslerde alt düzeyde kısmi indeksleme için ilk indekste boş dilim:</p>
""" + cb("pop[:, 2010]", "pop_partial_2010.py") + """
    <p><a href="02-data-indexing-and-selection.html">3.2 Veri İndeksleme ve Seçimi</a>'ndeki Boolean maske seçimi:</p>
""" + cb("pop[pop > 22000000]", "pop_bool_mask.py") + """
    <p>Fancy indexing de çalışır:</p>
""" + cb("pop[['California', 'Texas']]", "pop_fancy.py") + """
    <h3 id="coklu-df-indeks">Çoklu İndeksli DataFrame</h3>
""" + cb("health_data", "health_data_ref.py") + """
    <p><code>DataFrame</code>'de sütunlar önceliklidir; çoklu indeksli <code>Series</code> sözdizimi sütunlara uygulanır:</p>
""" + cb("health_data['Guido', 'HR']", "health_guido_hr.py") + """
    <p>Tek indeks durumunda olduğu gibi <code>loc</code>, <code>iloc</code> kullanılabilir (<a href="02-data-indexing-and-selection.html">3.2</a>):</p>
""" + cb("health_data.iloc[:2, :2]", "health_iloc.py") + """
    <p><code>loc</code>/<code>iloc</code>'a her indeks için demet verilebilir:</p>
""" + cb("health_data.loc[:, ('Bob', 'HR')]", "health_loc_bob_hr.py") + """
    <p>Demet içinde dilim sözdizimi hatası verir:</p>
""" + cb("health_data.loc[(:, 1), (:, 'HR')]", "health_bad_slice.py") + """
    <p>Python <code>slice</code> ile çözülebilir; bu bağlamda <code>IndexSlice</code> daha iyidir:</p>
""" + cb("""idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, 'HR']]""", "health_index_slice.py") + addon("IndexSlice", "<p><code>pd.IndexSlice</code>, çoklu indeksli <code>loc</code> dilimlerinde <code>:</code> kullanımını kolaylaştırır.</p>") + """
    <p>Çoklu indeksli <code>Series</code> ve <code>DataFrame</code> ile etkileşimin en iyi yolu denemektir!</p>

    <h2 id="multiindex-yeniden-duzenleme">Çoklu İndeksleri Yeniden Düzenleme</h2>

    <p>Çoklu indeksli veride bilgi koruyup düzeni değiştiren işlemler önemlidir. <code>stack</code> / <code>unstack</code> bunlardan biridir.</p>

    <h3 id="sirali-indeksler">Sıralı ve Sırasız İndeksler</h3>

    <p><em>Çoğu <code>MultiIndex</code> dilimleme işlemi indeks sıralı değilse başarısız olur.</em> Sözlük sırası olmayan çoklu indeksli veri:</p>
""" + cb("""index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data""", "data_unsorted.py") + """
    <p>Kısmi dilim denemesi hata verir:</p>
""" + cb("""try:
    data['a':'b']
except KeyError as e:
    print("KeyError", e)""", "data_slice_error.py") + """
    <p>Hata mesajından net olmasa da <code>MultiIndex</code> sıralı değildir. Kısmi dilimler için düzeyler sözlük (leksikografik) sırada olmalıdır. <code>sort_index</code> kullanın:</p>
""" + cb("""data = data.sort_index()
data""", "data_sort_index.py") + """
    <p>Sıralandıktan sonra kısmi dilimleme beklenen gibi çalışır:</p>
""" + cb("data['a':'b']", "data_slice_ok.py") + """
    <h3 id="stack-unstack">İndeksleri Yığma ve Açma</h3>

    <p>Veri kümesini yığılmış çoklu indeksten iki boyutlu gösterime dönüştürmek mümkün; düzey belirtilebilir:</p>
""" + cb("pop.unstack(level=0)", "pop_unstack_l0.py") + cb("pop.unstack(level=1)", "pop_unstack_l1.py") + """
    <p><code>unstack</code>'in tersi <code>stack</code> — orijinal seriyi geri alır:</p>
""" + cb("pop.unstack().stack()", "pop_unstack_stack.py") + """
    <h3 id="indeks-ayar-sifirla">İndeks Ayarlama ve Sıfırlama</h3>

    <p>İndeks etiketlerini sütunlara çevirmek için <code>reset_index</code>:</p>
""" + cb("""pop_flat = pop.reset_index(name='population')
pop_flat""", "pop_reset_index.py") + """
    <p>Sütun değerlerinden <code>MultiIndex</code> oluşturmak için <code>set_index</code>:</p>
""" + cb("pop_flat.set_index(['state', 'year'])", "pop_set_index.py") + """
    <p>Gerçek veri kümelerini keşfederken bu yeniden indeksleme desenlerinden biri en yararlılarındandır.</p>
""" + try_it("Şimdi deneyin", "İki düzeyli <code>MultiIndex</code> ile küçük bir <code>Series</code> oluşturup <code>unstack</code> ve <code>stack</code> deneyin:", """import pandas as pd
idx = pd.MultiIndex.from_product([['X','Y'], [1,2]])
s = pd.Series([10, 20, 30, 40], index=idx)
print(s)
print("\\nunstack:\\n", s.unstack())
print("\\nstack:\\n", s.unstack().stack())""", "deneme_stack.py") + try_it("Şimdi deneyin", "Sırasız çoklu indeks oluşturup <code>sort_index()</code> sonrası dilimlemeyi deneyin:", """import pandas as pd
import numpy as np
idx = pd.MultiIndex.from_product([['a','c','b'], [1,2]])
s = pd.Series(np.arange(6), index=idx)
try:
    print(s['a':'b'])
except KeyError:
    print("Sırasız dilimleme hata verdi")
print("\\nSıralı:\\n", s.sort_index()['a':'b'])""", "deneme_sort_slice.py") + addon("ix kaldırıldı", "<p>Eski kitap sürümlerinde <code>ix</code> geçer; modern Pandas'ta <code>loc</code> ve <code>iloc</code> kullanın.</p>") + addon("Panel nesneleri", "<p><code>Panel</code>/<code>Panel4D</code> kaldırıldı; çok boyutlu veri için <code>MultiIndex</code> veya Xarray tercih edin.</p>") + next_link("06-concat-and-append.html", "3.6 Birleştirme: Concat ve Append")

write_chapter("05-hierarchical-indexing", body)
print("ch05 code blocks:", body.count("code-block"))
