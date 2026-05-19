#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_pandas_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_pandas_chapter import write_chapter

NB = "03.06-Concat-And-Append.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>3.6 Birleştirme: Concat ve Append</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/03.06-concat-and-append.html" target="_blank" rel="noopener">Combining Datasets: Concat and Append</a></em></p>

    <p>Verinin en ilgi çekici analizleri çoğu zaman farklı kaynakların birleştirilmesinden çıkar. Bu işlemler iki veri kümesinin basit yan yana eklenmesinden, örtüşmeleri doğru ele alan veritabanı tarzı birleştirme ve join'lere kadar uzanır. <code>Series</code> ve <code>DataFrame</code> bu tür işlemler için tasarlanmıştır; Pandas bu veri düzenleme işlerini hızlı ve doğrudan kılan fonksiyon ve yöntemler içerir.</p>

    <p>Burada <code>pd.concat</code> ile <code>Series</code> ve <code>DataFrame</code> birleştirmesine bakacağız; daha sonra Pandas'taki bellek içi <code>pd.merge</code> join'lerine geçeceğiz.</p>

    <p>Standart içe aktarmalarla başlayalım:</p>
""" + c(2, "import_pd_np.py") + """
    <p>Kolaylık için aşağıdaki örneklerde kullanacağımız belirli biçimde bir <code>DataFrame</code> üreten yardımcı fonksiyonu tanımlayalım:</p>
""" + c(4, "make_df.py") + """
    <p>Ayrıca birden fazla <code>DataFrame</code>'i yan yana göstermek için kısa bir sınıf tanımlayacağız. Kod, IPython/Jupyter'ın zengin nesne gösterimi için kullandığı özel <code>_repr_html_</code> yönteminden yararlanır:</p>
""" + c(6, "display_class.py") + """
    <p>Kullanımı aşağıdaki bölümlerde netleşecektir.</p>

    <h2 id="numpy-birlestirme-hatirlatma">Hatırlatma: NumPy Dizilerinde Birleştirme</h2>

    <p><code>Series</code> ve <code>DataFrame</code> birleştirmesi, <a href="../02-numpy/02-basics-of-numpy-arrays.html">2.2 NumPy Dizilerinin Temelleri</a>'nde anlatılan <code>np.concatenate</code> ile benzer davranır. İki veya daha fazla dizinin içeriği tek dizide birleştirilebilir:</p>
""" + c(9, "np_concat_1d.py") + """
    <p>İlk argüman birleştirilecek dizilerin listesi veya demetidir. Çok boyutlu dizilerde sonucun hangi eksen boyunca birleştirileceğini belirten <code>axis</code> anahtar sözcüğü vardır:</p>
""" + c(11, "np_concat_axis.py") + """
    <h2 id="pd-concat-basit">pd.concat ile Basit Birleştirme</h2>

    <p><code>pd.concat</code>, <code>np.concatenate</code>'e benzer sözdizimi sunar; birçok seçenek vardır:</p>
""" + cb("""# Pandas v1.3.5 imzası
pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None,
          levels=None, names=None, verify_integrity=False,
          sort=False, copy=True)""", "pd_concat_signature.py", readonly=True) + """
    <p><code>pd.concat</code>, <code>np.concatenate</code> gibi <code>Series</code> veya <code>DataFrame</code> nesnelerinin basit birleştirmesi için kullanılır:</p>
""" + c(14, "concat_series.py") + """
    <p>Daha yüksek boyutlu nesneler (<code>DataFrame</code>) için de çalışır:</p>
""" + c(16, "concat_dataframes.py") + """
    <p>Varsayılan davranış satır bazında birleştirmedir (<code>axis=0</code>). <code>np.concatenate</code> gibi birleştirmenin yapılacağı eksen belirtilebilir:</p>
""" + c(18, "concat_axis_columns.py") + """
    <p><code>axis=1</code> ile eşdeğerdir; burada daha sezgisel olan <code>axis='columns'</code> kullandık.</p>

    <h3 id="yinelenen-indeksler">Yinelenen İndeksler</h3>

    <p><code>np.concatenate</code> ile <code>pd.concat</code> arasındaki önemli farklardan biri: Pandas birleştirme <em>indeksleri korur</em> — sonuçta yinelenen indeksler olsa bile!</p>
""" + c(21, "concat_duplicate_index.py") + """
    <p>Sonuçta yinelenen indekslere dikkat edin. <code>DataFrame</code> içinde geçerli olsa da sonuç çoğu zaman istenmez. <code>pd.concat</code> bunu yönetmek için seçenekler sunar.</p>

    <h4 id="yinelenen-indeks-hata">Yinelenen indeksleri hata sayma</h4>

    <p>Sonuçta örtüşen indeks olmadığını doğrulamak için <code>verify_integrity=True</code> kullanılabilir; yinelenen indeks varsa birleştirme istisna fırlatır:</p>
""" + c(24, "concat_verify_integrity.py") + """
    <h4 id="indeksi-yoksay">İndeksi yoksayma</h4>

    <p>Bazen indeks önemli değildir; <code>ignore_index=True</code> ile yeni bir tamsayı indeks oluşturulur:</p>
""" + c(26, "concat_ignore_index.py") + """
    <h4 id="multiindex-anahtar">MultiIndex anahtarları ekleme</h4>

    <p><code>keys</code> ile kaynaklara etiket verilebilir; sonuç hiyerarşik indeksli bir yapıdır:</p>
""" + c(28, "concat_keys.py") + """
    <p><a href="05-hierarchical-indexing.html">3.5 Hiyerarşik İndeksleme</a>'deki araçlarla bu çoklu indeksli <code>DataFrame</code> istediğimiz gösterime dönüştürülebilir.</p>

    <h3 id="join-ile-birlestirme">Join ile Birleştirme</h3>

    <p>Kısa örneklerde sütun adları örtüşüyordu. Gerçekte kaynakların sütun kümeleri farklı olabilir; <code>pd.concat</code> bu durumda seçenekler sunar:</p>
""" + c(31, "concat_outer_join.py") + """
    <p>Veri olmayan girişler varsayılan olarak NA ile doldurulur. <code>join</code> parametresi değiştirilebilir: varsayılan birleşim (<code>join='outer'</code>); <code>join='inner'</code> kesişimdir:</p>
""" + c(33, "concat_inner_join.py") + """
    <p>Hangi sütunların düşeceğine daha ince kontrol için birleştirmeden önce <code>reindex</code> kullanılabilir:</p>
""" + c(35, "concat_reindex.py") + """
    <h3 id="append-yontemi">append Yöntemi</h3>

    <p>Dizi birleştirme çok yaygın olduğundan <code>Series</code> ve <code>DataFrame</code>'de <code>append</code> yöntemi vardır; örneğin <code>pd.concat([df1, df2])</code> yerine <code>df1.append(df2)</code>:</p>
""" + c(37, "df_append.py") + addon(
    "append yerine concat",
    "<p>Python listelerindeki <code>append</code>/<code>extend</code> gibi Pandas <code>append</code> orijinal nesneyi <strong>değiştirmez</strong>; yeni nesne üretir ve verimli değildir. Modern Pandas'ta <code>DataFrame.append</code> kaldırılmıştır; <code>pd.concat</code> kullanın.</p>",
) + """
    <p>Python listelerindeki <code>append</code> ve <code>extend</code> yöntemlerinin aksine Pandas'taki <code>append</code> orijinal nesneyi değiştirmez; birleşik veriyle yeni nesne oluşturur. Yeni indeks ve veri tamponu oluşturduğu için verimli değildir — birden fazla <code>append</code> yerine liste oluşturup tek <code>concat</code> çağrısı genelde daha iyidir.</p>

    <p>Sonraki bölümde çoklu kaynaktan veri birleştirmenin daha güçlü yolu olan <code>pd.merge</code> join'lerine bakacağız. <code>concat</code>, <code>append</code> ve ilgili işlevler için Pandas dokümantasyonundaki <a href="https://pandas.pydata.org/docs/user_guide/merging.html" target="_blank" rel="noopener">Merge, join, concat and compare</a> bölümüne bakın.</p>
""" + try_it(
    "Şimdi deneyin",
    "İki küçük <code>DataFrame</code> oluşturup <code>pd.concat</code> ile satır ve sütun ekseninde birleştirin:",
    """import pandas as pd
import numpy as np

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)

a, b = make_df('AB', [0, 1]), make_df('CD', [0, 1])
print("Satır bazında:\\n", pd.concat([a, b]))
print("\\nSütun bazında:\\n", pd.concat([a, b], axis=1))""",
    "deneme_concat.py",
) + next_link("07-merge-and-join.html", "3.7 Merge ve Join")

write_chapter("06-concat-and-append", body)
print("wrote 06-concat-and-append.html")
