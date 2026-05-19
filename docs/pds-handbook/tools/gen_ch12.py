#!/usr/bin/env python3
"""Generate 12-performance-eval-and-query.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nb_html_utils import (
    addon,
    build_from_notebook,
    h1,
    h2,
    h3,
    h4,
    next_link,
    orig_line,
    p,
    try_it,
)
from write_pandas_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/03.12-performance-eval-and-query.html"
EN_LABEL = "Performance Eval and Query"

TR = {
    0: h1("3.12 Performans: Değerlendirme ve Sorgu"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Önceki bölümlerde gördüğümüz gibi PyData yığınının gücü, NumPy ve "
                "Pandas'ın temel işlemleri sezgisel üst düzey sözdizimiyle alt düzey "
                "derlenmiş koda itme yeteneğine dayanır: NumPy'de vektörize/yayınlanmış "
                "işlemler, Pandas'ta gruplama türü işlemler buna örnektir. Bu soyutlamalar "
                "birçok yaygın kullanım için verimli olsa da genelde geçici ara nesneler "
                "oluşturmaya dayanır; bu da hesaplama süresi ve bellek kullanımında "
                "gereksiz yük yaratabilir."
            ),
            p(
                "Bunu gidermek için Pandas, ara dizilerin maliyetli ayrılması olmadan "
                "doğrudan C hızında işlemlere erişmeyi sağlayan yöntemler içerir: "
                "<code>eval</code> ve <code>query</code>. Bunlar "
                '<a href="https://github.com/pydata/numexpr" target="_blank" '
                'rel="noopener">NumExpr</a> paketine dayanır. Bu bölümde kullanımlarını '
                "ve ne zaman düşünmeniz gerekebileceğine dair pratik kuralları ele alacağız."
            ),
        ]
    ),
    2: "\n".join(
        [
            h2("query ve eval Motivasyonu: Bileşik İfadeler", "motivasyon"),
            p(
                "NumPy ve Pandas'ın hızlı vektörize işlemleri desteklediğini daha önce "
                "gördük; örneğin iki dizinin elemanlarını toplarken:"
            ),
        ]
    ),
    4: p(
        '<a href="../02-numpy/03-computation-ufuncs.html">2.3 Evrensel Fonksiyonlar</a> '
        "bölümünde tartışıldığı gibi bu, Python döngüsü veya comprehension ile "
        "toplama yapmaktan çok daha hızlıdır:"
    ),
    6: p(
        "Ancak bileşik ifadeler hesaplanırken bu soyutlama daha az verimli olabilir. "
        "Şu ifadeyi düşünün:"
    ),
    8: p(
        "NumPy her alt ifadeyi ayrı değerlendirdiği için bu kabaca şuna eşdeğerdir:"
    ),
    10: "\n".join(
        [
            p(
                "Başka bir deyişle, <em>her ara adım bellekte açıkça ayrılır</em>. "
                "<code>x</code> ve <code>y</code> dizileri çok büyükse bu bellek ve "
                "hesaplama yüküne yol açabilir."
            ),
            p(
                "NumExpr kütüphanesi bu tür bileşik ifadeyi tam ara diziler ayırmadan "
                "eleman eleman hesaplamanıza olanak tanır. "
                '<a href="https://github.com/pydata/numexpr" target="_blank" '
                'rel="noopener">NumExpr dokümantasyonu</a> daha fazla ayrıntı içerir; '
                "şimdilik kütüphanenin hesaplamak istediğiniz NumPy tarzı ifadeyi "
                "veren bir <em>dize</em> kabul ettiğini söylemek yeterlidir:"
            ),
        ]
    ),
    12: p(
        "NumExpr ifadeyi mümkün olduğunca geçici dizilerden kaçınarak değerlendirir; "
        "bu yüzden özellikle büyük diziler üzerinde uzun hesaplama dizilerinde NumPy'den "
        "çok daha verimli olabilir. Burada ele alacağımız Pandas <code>eval</code> ve "
        "<code>query</code> araçları kavramsal olarak benzerdir; esasen NumExpr "
        "işlevselliğinin Pandas'a özgü sarmalayıcılarıdır."
    ),
    13: "\n".join(
        [
            h2("Verimli İşlemler için pandas.eval", "pandas-eval"),
            p(
                "Pandas'taki <code>eval</code> fonksiyonu dize ifadeleri kullanarak "
                "<code>DataFrame</code> nesneleri üzerinde verimli hesaplamalar yapar. "
                "Örneğin şu veriyi düşünün:"
            ),
        ]
    ),
    15: p(
        "Dört <code>DataFrame</code>'in toplamını tipik Pandas yaklaşımıyla "
        "yazabiliriz:"
    ),
    17: p("Aynı sonuç <code>pd.eval</code> ile dize olarak ifade kurularak elde edilebilir:"),
    19: p(
        "Bu ifadenin <code>eval</code> sürümü yaklaşık %50 daha hızlıdır (ve çok daha "
        "az bellek kullanır) ve aynı sonucu verir:"
    ),
    21: p(
        "<code>pd.eval</code> geniş bir işlem yelpazesini destekler. Göstermek için "
        "şu tamsayı verisini kullanacağız:"
    ),
    23: h4("Aritmetik operatörler", "aritmetik"),
    24: p("<code>pd.eval</code> tüm aritmetik operatörleri destekler. Örneğin:"),
    25: h4("Karşılaştırma operatörleri", "karsilastirma"),
    26: p(
        "<code>pd.eval</code> zincirli ifadeler dahil tüm karşılaştırma operatörlerini "
        "destekler:"
    ),
    27: h4("Bit düzeyi operatörler", "bitwise"),
    28: p("<code>pd.eval</code> <code>&amp;</code> ve <code>|</code> bit operatörlerini destekler:"),
    29: p(
        "Ayrıca Boolean ifadelerde <code>and</code> ve <code>or</code> kullanımını "
        "destekler:"
    ),
    31: h4("Nesne öznitelikleri ve indeksler", "oznitelik-indeks"),
    32: p(
        "<code>pd.eval</code>, <code>obj.attr</code> sözdizimiyle nesne özniteliklerine "
        "ve <code>obj[index]</code> ile indekslere erişimi destekler:"
    ),
    33: h4("Diğer işlemler", "diger-islemler"),
    34: p(
        "Fonksiyon çağrıları, koşullu ifadeler, döngüler ve daha karmaşık yapılar "
        "şu an <code>pd.eval</code> içinde <em>uygulanmamıştır</em>. Bu tür ifadeleri "
        "çalıştırmak için NumExpr kütüphanesinin kendisini kullanabilirsiniz."
    ),
    35: "\n".join(
        [
            h2("Sütun Bazlı İşlemler için DataFrame.eval", "dataframe-eval"),
            p(
                "Pandas'ın üst düzey <code>pd.eval</code> fonksiyonu gibi "
                "<code>DataFrame</code> nesnelerinin de benzer çalışan bir "
                "<code>eval</code> yöntemi vardır. <code>eval</code> yönteminin "
                "avantajı sütunlara ada göre referans verilebilmesidir. Örnek "
                "etiketli dizi:"
            ),
        ]
    ),
    36: p(
        "Önceki bölümdeki gibi <code>pd.eval</code> ile üç sütunlu ifade "
        "hesaplayabiliriz:"
    ),
    38: p(
                "<code>DataFrame.eval</code> yöntemi sütunlarla ifadelerin çok daha "
                "özlü değerlendirilmesine izin verir:"
    ),
    40: p(
        "Burada sütun adlarını değerlendirilen ifade içinde <em>değişken</em> gibi "
        "ele aldığımıza ve sonucun istediğimiz gibi olduğuna dikkat edin."
    ),
    41: h3("DataFrame.eval'de Atama", "eval-atama"),
    42: p(
        "Az önce tartışılan seçeneklere ek olarak <code>DataFrame.eval</code> herhangi "
        "bir sütuna atamaya da izin verir. Önceki <code>DataFrame</code>'i kullanalım; "
        "sütunları <code>'A'</code>, <code>'B'</code>, <code>'C'</code>:"
    ),
    43: p(
        "<code>df.eval</code> ile diğer sütunlardan hesaplanan yeni bir "
        "<code>'D'</code> sütunu oluşturup atayabiliriz:"
    ),
    45: p("Aynı şekilde mevcut herhangi bir sütun değiştirilebilir:"),
    47: h3("DataFrame.eval'de Yerel Değişkenler", "eval-yerel"),
    48: p(
        "<code>DataFrame.eval</code> yöntemi yerel Python değişkenleriyle çalışmasını "
        "sağlayan ek bir sözdizimi destekler:"
    ),
    49: p(
        "Buradaki <code>@</code> karakteri bir <em>sütun adı</em> değil "
        "<em>değişken adı</em> işaretler; sütun ad alanı ile Python nesne ad alanını "
        "içeren ifadeleri verimli değerlendirmenizi sağlar. Bu <code>@</code> yalnızca "
        "<code>DataFrame.eval</code> <em>yöntemi</em> tarafından desteklenir; "
        "<code>pandas.eval</code> <em>fonksiyonu</em> yalnızca tek (Python) ad alanına "
        "erişebildiği için <code>@</code> desteklemez."
    ),
    50: "\n".join(
        [
            h2("DataFrame.query Yöntemi", "dataframe-query"),
            p(
                "<code>DataFrame</code>'in değerlendirilmiş dizelere dayanan bir başka "
                "yöntemi <code>query</code>'dir:"
            ),
        ]
    ),
    52: p(
        "<code>DataFrame.eval</code> tartışmasındaki örnek gibi bu da "
        "<code>DataFrame</code> sütunlarını içeren bir ifadedir. Ancak "
        "<code>DataFrame.eval</code> sözdizimiyle ifade edilemez! Bu tür filtreleme "
        "için <code>query</code> yöntemini kullanabilirsiniz:"
    ),
    54: p(
        "Daha verimli hesaplamanın yanı sıra maskeleme ifadesine kıyasla okunması "
        "ve anlaşılması çok daha kolaydır. <code>query</code> yöntemi yerel değişkenler "
        "için de <code>@</code> bayrağını kabul eder:"
    ),
    56: "\n".join(
        [
            h2("Performans: Bu Fonksiyonları Ne Zaman Kullanmalı?", "performans-ne-zaman"),
            p(
                "<code>eval</code> ve <code>query</code> kullanılıp kullanılmayacağını "
                "değerlendirirken iki faktör vardır: <em>hesaplama süresi</em> ve "
                "<em>bellek kullanımı</em>. Bellek kullanımı en öngörülebilir yöndür. "
                "Daha önce belirtildiği gibi NumPy dizileri veya Pandas "
                "<code>DataFrame</code>'leri içeren her bileşik ifade geçici dizilerin "
                "örtük oluşturulmasına yol açar. Örneğin şu:"
            ),
        ]
    ),
    58: p("kabaca şuna eşdeğerdir:"),
    60: p(
        "Geçici <code>DataFrame</code>'lerin boyutu kullanılabilir sistem belleğinize "
        "(genelde birkaç gigabayt) göre önemliyse <code>eval</code> veya "
        "<code>query</code> ifadesi kullanmak iyi bir fikirdir. Dizinizin yaklaşık "
        "bayt cinsinden boyutunu şununla kontrol edebilirsiniz:"
    ),
    62: "\n".join(
        [
            p(
                "Performans tarafında, sistem belleğinizi doldurmasanız bile "
                "<code>eval</code> daha hızlı olabilir. Sorun geçici nesnelerinizin "
                "sisteminizdeki L1 veya L2 CPU önbelleği boyutuyla (genelde birkaç "
                "megabayt) karşılaştırmasıdır; çok daha büyüklerse <code>eval</code> "
                "farklı bellek önbellekleri arasında yavaş değer taşınmasını "
                "önleyebilir."
            ),
            p(
                "Pratikte geleneksel yöntemler ile <code>eval</code>/<code>query</code> "
                "arasındaki hesaplama süresi farkı genelde önemli değildir — hatta "
                "küçük dizilerde geleneksel yöntem daha hızlı olabilir! "
                "<code>eval</code>/<code>query</code>'nin asıl faydası tasarruf edilen "
                "bellek ve bazen daha temiz sözdizimidir."
            ),
            p(
                "Burada <code>eval</code> ve <code>query</code>'nin çoğu ayrıntısını "
                "ele aldık; daha fazlası için Pandas dokümantasyonuna bakabilirsiniz. "
                "Özellikle bu sorguları çalıştırmak için farklı ayrıştırıcılar ve "
                "motorlar belirtilebilir; ayrıntılar için dokümantasyondaki "
                '<a href="https://pandas.pydata.org/docs/user_guide/enhancingperf.html" '
                'target="_blank" rel="noopener">"Enhancing Performance"</a> bölümüne bakın.'
            ),
        ]
    ),
}

INSERTS = {
    12: addon(
        "NumExpr",
        "NumExpr ifadeyi dize olarak alır — sütun adları yerine değişken adları "
        "kullanılır. Pandas <code>eval</code>/<code>query</code> bu katmanı "
        "<code>DataFrame</code> bağlamına taşır.",
    ),
    40: try_it(
        "",
        "<code>DataFrame.eval</code> ile sütun adlarını değişken gibi kullanın:",
        """import pandas as pd
import numpy as np
rng = np.random.default_rng(0)
df = pd.DataFrame(rng.random((5, 3)), columns=["A", "B", "C"])
df.eval("D = (A + B) / C", inplace=True)
print(df.head())""",
        "deneme_df_eval.py",
    ),
    54: try_it(
        "",
        "<code>query</code> ile okunabilir filtreleme:",
        """import pandas as pd
import numpy as np
rng = np.random.default_rng(1)
df = pd.DataFrame(rng.random((100, 3)), columns=["A", "B", "C"])
sub = df.query("A < 0.3 and B > 0.5")
print(len(sub), "satır seçildi")""",
        "deneme_df_query.py",
    ),
    62: addon(
        "ne zaman eval?",
        "Küçük <code>DataFrame</code>'lerde geleneksel maskeleme genelde yeterlidir. "
        "Bellek baskısı veya çok uzun bileşik ifadelerde <code>eval</code>/<code>query</code> "
        "düşünün.",
    ),
}

CODE_NAMES = {
    3: "timeit_numpy_add.py",
    5: "timeit_loop_add.py",
    7: "compound_mask.py",
    9: "compound_tmp.py",
    11: "numexpr_eval.py",
    14: "eval_dataframes.py",
    16: "timeit_df_sum.py",
    18: "timeit_pd_eval.py",
    20: "eval_allclose.py",
    22: "eval_int_data.py",
    24: "eval_arithmetic.py",
    26: "eval_comparison.py",
    28: "eval_bitwise.py",
    30: "eval_and_or.py",
    32: "eval_attr_index.py",
    35: "df_eval_ornek.py",
    37: "pd_eval_columns.py",
    39: "df_eval_columns.py",
    42: "df_head.py",
    44: "df_eval_assign.py",
    46: "df_eval_modify.py",
    48: "eval_local_var.py",
    51: "query_mask_equiv.py",
    53: "df_query.py",
    55: "query_local_var.py",
    57: "mask_filter.py",
    59: "mask_tmp_steps.py",
    61: "df_nbytes.py",
}

if __name__ == "__main__":
    body = build_from_notebook(
        "03.12-Performance-Eval-and-Query.ipynb", TR, CODE_NAMES, INSERTS
    )
    body += "\n\n" + next_link("13-further-resources.html", "3.13 Kaynaklar")
    path = write_chapter("12-performance-eval-and-query", body)
    print("wrote", path)
