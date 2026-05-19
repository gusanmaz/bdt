#!/usr/bin/env python3
"""Generate 10-working-with-strings.html from notebook + Turkish prose."""
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

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/03.10-working-with-strings.html"
EN_LABEL = "Working With Strings"

TR = {
    0: h1("3.10 Dizelerle Çalışma"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Python'un güçlü yanlarından biri dize verisini işleme ve dönüştürmedeki "
                "görece kolaylığıdır. Pandas bunun üzerine inşa edilir ve gerçek dünya "
                "verisiyle çalışırken (okuyun: temizlerken) gereken <em>munging</em> "
                "türünün önemli parçası olan kapsamlı bir <em>vektörize dize işlemleri</em> "
                "kümesi sunar. Bu bölümde Pandas dize işlemlerinden bazılarını ele alacağız; "
                "ardından internetten toplanmış çok dağınık bir tarif veri kümesini kısmen "
                "temizlemek için bunları kullanacağız."
            ),
        ]
    ),
    2: "\n".join(
        [
            h2("Pandas Dize İşlemlerine Giriş", "pandas-dize-giris"),
            p(
                "Önceki bölümlerde NumPy ve Pandas gibi araçların aritmetik işlemleri "
                "genelleştirerek aynı işlemi birçok dizi elemanına kolayca ve hızlıca "
                "uygulayabildiğimizi gördük. Örneğin:"
            ),
        ]
    ),
    4: "\n".join(
        [
            p(
                "İşlemlerin bu <em>vektörizasyonu</em>, dizi verisi üzerinde çalışmanın "
                "sözdizimini sadeleştirir: artık dizinin boyutu veya şekliyle değil, "
                "yapılmasını istediğimiz işlemle ilgilenmemiz yeterlidir. Dize dizileri "
                "için NumPy bu kadar basit bir erişim sağlamaz; daha ayrıntılı bir döngü "
                "sözdizimi kullanmak zorunda kalırsınız:"
            ),
        ]
    ),
    6: p(
        "Bazı verilerle bu yeterli olabilir; ancak eksik değer varsa kod kırılır — "
        "bu yüzden ek kontroller gerekir:"
    ),
    8: "\n".join(
        [
            p(
                "Bu tür manuel yaklaşım yalnızca ayrıntılı ve kullanışsız değil, "
                "hata yapmaya da açıktır."
            ),
            p(
                "Pandas, vektörize dize işlemleri ihtiyacını ve dize içeren "
                "<code>Series</code> ile <code>Index</code> nesnelerinin <code>str</code> "
                "özniteliği aracılığıyla eksik veriyi doğru işleme ihtiyacını karşılar. "
                "Örneğin bu veriyle bir Pandas <code>Series</code> oluşturursak, "
                "eksik değer işleme yerleşik olan <code>str.capitalize</code> yöntemini "
                "doğrudan çağırabiliriz:"
            ),
        ]
    ),
    10: "\n".join(
        [
            h2("Pandas Dize Yöntemleri Tabloları", "dize-yontemleri"),
            p(
                "Python'da dize manipülasyonunu iyi biliyorsanız Pandas dize sözdiziminin "
                "çoğu sezgiseldir; yöntemleri listelemek muhtemelen yeterlidir. "
                "Ayrıntılara girmeden önce buradan başlayacağız. Bu bölümdeki örnekler "
                "aşağıdaki <code>Series</code> nesnesini kullanır:"
            ),
        ]
    ),
    12: "\n".join(
        [
            h3("Python Dize Yöntemlerine Benzer Yöntemler", "python-benzeri"),
            p(
                "Python'un yerleşik dize yöntemlerinin neredeyse tamamı Pandas vektörize "
                "dize yöntemiyle eşlenir. Python dize yöntemlerini yansıtan Pandas "
                "<code>str</code> yöntemlerinin bir listesi:"
            ),
            """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th></th><th></th><th></th><th></th></tr></thead>
        <tbody>
          <tr><td><code>len()</code></td><td><code>lower()</code></td><td><code>translate()</code></td><td><code>islower()</code></td></tr>
          <tr><td><code>ljust()</code></td><td><code>upper()</code></td><td><code>startswith()</code></td><td><code>isupper()</code></td></tr>
          <tr><td><code>rjust()</code></td><td><code>find()</code></td><td><code>endswith()</code></td><td><code>isnumeric()</code></td></tr>
          <tr><td><code>center()</code></td><td><code>rfind()</code></td><td><code>isalnum()</code></td><td><code>isdecimal()</code></td></tr>
          <tr><td><code>zfill()</code></td><td><code>index()</code></td><td><code>isalpha()</code></td><td><code>split()</code></td></tr>
          <tr><td><code>strip()</code></td><td><code>rindex()</code></td><td><code>isdigit()</code></td><td><code>rsplit()</code></td></tr>
          <tr><td><code>rstrip()</code></td><td><code>capitalize()</code></td><td><code>isspace()</code></td><td><code>partition()</code></td></tr>
          <tr><td><code>lstrip()</code></td><td><code>swapcase()</code></td><td><code>istitle()</code></td><td><code>rpartition()</code></td></tr>
        </tbody>
      </table>
    </div>""",
            p(
                "Bunların dönüş tipleri farklıdır. <code>lower</code> gibi bazıları "
                "dize <code>Series</code>'i döndürür:"
            ),
        ]
    ),
    14: p("Bazıları sayı döndürür:"),
    16: p("Veya Boolean değerler:"),
    18: p("Diğerleri her eleman için liste veya başka bileşik değerler döndürür:"),
    20: p(
        "Tartışmaya devam ederken bu tür liste-dizisi nesneleri üzerinde daha fazla "
        "manipülasyon göreceğiz."
    ),
    21: "\n".join(
        [
            h3("Düzenli İfadeler Kullanan Yöntemler", "regex-yontemler"),
            p(
                "Ayrıca her dize elemanının içeriğini incelemek için düzenli ifadeler "
                "(regex) kabul eden ve Python'un yerleşik <code>re</code> modülünün API "
                "kurallarının bir kısmını izleyen birkaç yöntem vardır:"
            ),
            """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Yöntem</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>match</code></td><td>Her eleman üzerinde <code>re.match</code> çağırır; Boolean döndürür.</td></tr>
          <tr><td><code>extract</code></td><td>Her eleman üzerinde <code>re.match</code> çağırır; eşleşen grupları dize olarak döndürür.</td></tr>
          <tr><td><code>findall</code></td><td>Her eleman üzerinde <code>re.findall</code> çağırır.</td></tr>
          <tr><td><code>replace</code></td><td>Desenin geçtiği yerleri başka bir dizeyle değiştirir.</td></tr>
          <tr><td><code>contains</code></td><td>Her eleman üzerinde <code>re.search</code> çağırır; boolean döndürür.</td></tr>
          <tr><td><code>count</code></td><td>Desenin geçiş sayısını sayar.</td></tr>
          <tr><td><code>split</code></td><td><code>str.split</code> eşdeğeri; regex kabul eder.</td></tr>
          <tr><td><code>rsplit</code></td><td><code>str.rsplit</code> eşdeğeri; regex kabul eder.</td></tr>
        </tbody>
      </table>
    </div>""",
        ]
    ),
    22: p(
        "Bunlarla geniş bir işlem yelpazesi yapılabilir. Örneğin her elemanın "
        "başındaki ardışık karakter grubunu isteyerek ilk adı çıkarabiliriz:"
    ),
    24: p(
        "Veya daha karmaşık bir şey: ünsüzle başlayıp ünsüzle biten tüm adları bulmak "
        "için dize başı (<code>^</code>) ve dize sonu (<code>$</code>) regex karakterlerini "
        "kullanabiliriz:"
    ),
    26: p(
        "Düzenli ifadeleri <code>Series</code> veya <code>DataFrame</code> girişlerine "
        "özlü biçimde uygulayabilme, veri analizi ve temizliği için birçok olasılık açar."
    ),
    27: "\n".join(
        [
            h3("Çeşitli Yöntemler", "cesitli-yontemler"),
            p("Son olarak diğer kullanışlı işlemlere olanak tanıyan çeşitli yöntemler vardır:"),
            """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Yöntem</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>get</code></td><td>Her elemanı indeksler.</td></tr>
          <tr><td><code>slice</code></td><td>Her elemanı dilimler.</td></tr>
          <tr><td><code>slice_replace</code></td><td>Her elemandaki dilimi verilen değerle değiştirir.</td></tr>
          <tr><td><code>cat</code></td><td>Dizeleri birleştirir.</td></tr>
          <tr><td><code>repeat</code></td><td>Değerleri tekrarlar.</td></tr>
          <tr><td><code>normalize</code></td><td>Dizelerin Unicode biçimini döndürür.</td></tr>
          <tr><td><code>pad</code></td><td>Dizelerin soluna, sağına veya her iki tarafına boşluk ekler.</td></tr>
          <tr><td><code>wrap</code></td><td>Uzun dizeleri verilen genişlikten kısa satırlara böler.</td></tr>
          <tr><td><code>join</code></td><td><code>Series</code>'teki her elemandaki dizeleri verilen ayraçla birleştirir.</td></tr>
          <tr><td><code>get_dummies</code></td><td>Kukla (dummy) değişkenleri <code>DataFrame</code> olarak çıkarır.</td></tr>
        </tbody>
      </table>
    </div>""",
        ]
    ),
    28: "\n".join(
        [
            h4("Vektörize öğe erişimi ve dilimleme", "vektorize-erisim"),
            p(
                "Özellikle <code>get</code> ve <code>slice</code> işlemleri, her diziden "
                "vektörize öğe erişimine olanak tanır. Örneğin <code>str.slice(0, 3)</code> "
                "ile her dizinin ilk üç karakterini alabiliriz. Bu davranış Python'un "
                "normal indeksleme sözdizimiyle de kullanılabilir; "
                "<code>df.str.slice(0, 3)</code> ile <code>df.str[0:3]</code> eşdeğerdir:"
            ),
        ]
    ),
    30: "\n".join(
        [
            p(
                "<code>df.str.get(i)</code> ve <code>df.str[i]</code> ile indeksleme de "
                "benzer şekilde çalışır."
            ),
            p(
                "Bu indeksleme yöntemleri, <code>split</code> ile döndürülen dizi "
                "elemanlarına da erişmenizi sağlar. Örneğin her girişin soyadını "
                "çıkarmak için <code>split</code> ile <code>str</code> indekslemesini "
                "birleştirebiliriz:"
            ),
        ]
    ),
    32: "\n".join(
        [
            h4("Gösterge değişkenleri", "gosterge-degiskenleri"),
            p(
                "Biraz ek açıklama gerektiren bir diğer yöntem <code>get_dummies</code>'tır. "
                "Veriniz bir tür kodlanmış gösterge içeren bir sütuna sahipse kullanışlıdır. "
                "Örneğin A = \"Amerika'da doğdu\", B = \"Birleşik Krallık'ta doğdu\", "
                "C = \"peynir sever\", D = \"spam sever\" gibi kodlar içeren bir veri kümemiz "
                "olabilir:"
            ),
        ]
    ),
    34: p(
        "<code>get_dummies</code> rutini bu gösterge değişkenlerini bir "
        "<code>DataFrame</code>'e ayırmamıza izin verir:"
    ),
    36: "\n".join(
        [
            p(
                "Bu işlemleri yapı taşları olarak kullanarak verinizi temizlerken "
                "sonsuz sayıda dize işleme prosedürü oluşturabilirsiniz."
            ),
            p(
                "Bu yöntemlere daha fazla girmeyeceğiz; Pandas çevrimiçi dokümantasyonundaki "
                '<a href="https://pandas.pydata.org/docs/user_guide/text.html" target="_blank" '
                'rel="noopener">"Working with Text Data"</a> bölümünü okumanızı veya '
                '<a href="13-further-resources.html">3.13 Kaynaklar</a> bölümündeki kaynaklara '
                "başvurmanızı öneririm."
            ),
        ]
    ),
    37: "\n".join(
        [
            h2("Örnek: Tarif Veritabanı", "ornek-tarif"),
            p(
                "Vektörize dize işlemleri dağınık gerçek dünya verisini temizlerken en "
                "faydalı hale gelir. Burada web'deki çeşitli kaynaklardan derlenmiş açık "
                "bir tarif veritabanı örneği üzerinden yürüyeceğiz. Hedefimiz tarif "
                "verisini malzeme listelerine ayrıştırmak; böylece eldeki malzemelere "
                "göre hızlıca tarif bulabiliriz. Derleme betikleri "
                '<a href="https://github.com/fictivekin/openrecipes" target="_blank" '
                'rel="noopener">openrecipes</a> deposunda; veritabanının en güncel '
                "bağlantısı da orada."
            ),
            p(
                "Veritabanı yaklaşık 30 MB'tır; aşağıdaki komutlarla indirilip "
                "açılabilir (notebook'taki yorum satırları):"
            ),
        ]
    ),
    39: p(
        "Veritabanı JSON biçimindedir; <code>pd.read_json</code> ile okuruz "
        "(dosyanın her satırı bir JSON girişi olduğu için <code>lines=True</code> gerekir):"
    ),
    41: p(
        "Yaklaşık 175.000 tarif ve 17 sütun görüyoruz. Ne olduğunu görmek için "
        "bir satıra bakalım:"
    ),
    43: "\n".join(
        [
            p(
                "Orada çok bilgi var; ancak çoğu web'den kazınmış veride tipik olduğu "
                "gibi çok dağınık biçimde. Özellikle malzeme listesi dize biçiminde; "
                "ilgilendiğimiz bilgiyi dikkatle çıkarmamız gerekecek. Malzemelere "
                "yakından bakarak başlayalım:"
            ),
        ]
    ),
    45: "\n".join(
        [
            p(
                "Malzeme listeleri ortalama 250 karakter; minimum 0, maksimum neredeyse "
                "10.000 karakter!"
            ),
            p("Meraktan, en uzun malzeme listesine sahip tarif hangisi bakalım:"),
        ]
    ),
    47: p(
        "Başka toplu keşifler de yapabiliriz; örneğin kaç tarifin kahvaltı yemeği "
        "olduğunu (küçük ve büyük harfi eşleştiren regex ile) görelim:"
    ),
    49: p("Veya kaç tarifte tarçın malzeme olarak geçiyor:"),
    51: p(
        'Hatta "cinamon" yazım hatası yapan tarif var mı diye bakabiliriz:'
    ),
    53: "\n".join(
        [
            p(
                "Pandas dize araçlarıyla mümkün olan veri keşfi türü budur. Python "
                "gerçekten bu tür <em>data munging</em> işlerinde parlar."
            ),
        ]
    ),
    54: "\n".join(
        [
            h3("Basit Bir Tarif Önerici", "tarif-onerici"),
            p(
                "Biraz daha ileri gidip basit bir tarif öneri sistemi yapalım: verilen "
                "malzeme listesi için hepsini kullanan tarifleri bulmak istiyoruz. "
                "Kavramsal olarak basit olsa da verinin heterojenliği görevi zorlaştırır; "
                "örneğin her satırdan temiz malzeme listesi çıkarmak için kolay bir işlem "
                "yok. Bu yüzden biraz hile yapacağız: yaygın malzemeler listesiyle "
                "başlayıp her tarifin malzeme listesinde geçip geçmediklerine bakacağız. "
                "Basitlik için şimdilik yalnızca ot ve baharatlarla sınırlı kalalım:"
            ),
        ]
    ),
    56: p(
        "Ardından her malzemenin listede geçip geçmediğini gösteren <code>True</code> "
        "ve <code>False</code> değerlerinden oluşan Boolean bir <code>DataFrame</code> "
        "oluşturabiliriz:"
    ),
    58: p(
        "Örnek olarak maydanoz, kırmızı biber ve tarhun kullanan bir tarif bulmak "
        "isteyelim. <code>DataFrame</code>'lerin <code>query</code> yöntemiyle "
        "(<a href=\"12-performance-eval-and-query.html\">3.12 Performans ve Sorgu</a> "
        "bölümünde ayrıntılı) çok hızlı hesaplayabiliriz:"
    ),
    60: p(
        "Bu kombinasyonla yalnızca 10 tarif buluyoruz. Seçimin döndürdüğü indeksi "
        "kullanarak bu tariflerin adlarını bulalım:"
    ),
    62: p(
        "175.000 tariften 10'a indirdiğimize göre akşam yemeği için daha bilinçli "
        "karar verebiliriz."
    ),
    63: "\n".join(
        [
            h3("Tariflerle Daha İleriye", "tarif-ileri"),
            p(
                "Umarım bu örnek Pandas dize yöntemlerinin etkin biçimde sağladığı "
                "veri temizleme işlemlerinin türü hakkında fikir vermiştir. Sağlam bir "
                "tarif öneri sistemi kurmak elbette <em>çok</em> daha fazla iş gerektirir! "
                "Her tariften tam malzeme listesi çıkarmak önemli bir parça olurdu; "
                "kullanılan formatların çeşitliliği bunu nispeten zaman alıcı kılar."
            ),
            p(
                "Veri biliminde gerçek dünya verisinin temizlenmesi ve munging'inin "
                "çoğu zaman işin büyük kısmını oluşturduğu gerçeğine işaret eder — "
                "Pandas bunu verimli yapmanıza yardımcı olacak araçları sunar."
            ),
        ]
    ),
}

INSERTS = {
    9: addon(
        "str erişimcisi",
        "Dize sütunlarında <code>.str</code> olmadan vektörize yöntem çağrılamaz. "
        "<code>names.capitalize()</code> hata verir; <code>names.str.capitalize()</code> "
        "eksik değerleri atlayarak çalışır.",
    ),
    31: try_it(
        "",
        "<code>split</code> + zincirleme <code>str</code> indekslemesi — basit ad-soyad "
        "ayırma:",
        """import pandas as pd
s = pd.Series(["Ali Yılmaz", "Ayşe Kaya", "Mehmet Demir"])
print(s.str.split().str[-1])""",
        "deneme_str_split.py",
    ),
    53: try_it(
        "",
        "Küçük bir metin <code>Series</code>'inde regex ile filtreleme deneyin:",
        """import pandas as pd
s = pd.Series(["Python", "pandas", "NumPy", "pydata"])
print(s[s.str.contains("py", case=False, regex=True)])""",
        "deneme_str_contains.py",
    ),
    61: try_it(
        "",
        "Basit malzeme eşleştirmesi — elinizdeki malzemelerle tarif arama mantığını "
        "küçük ölçekte deneyin:",
        """import pandas as pd
recipes = pd.DataFrame({
    "name": ["Omlet", "Çorba", "Salata"],
    "ingredients": ["yumurta, tuz, biber", "tuz, soğan, biber", "marul, limon"]
})
have = ["tuz", "biber"]
mask = recipes.ingredients.str.contains("|".join(have), case=False)
print(recipes[mask])""",
        "deneme_tarif_ara.py",
    ),
}

CODE_NAMES = {
    3: "numpy_vektor.py",
    5: "liste_capitalize.py",
    7: "none_capitalize.py",
    9: "str_capitalize.py",
    11: "monte_series.py",
    13: "str_lower.py",
    15: "str_len.py",
    17: "str_startswith.py",
    19: "str_split.py",
    23: "str_extract.py",
    25: "str_findall.py",
    29: "str_slice.py",
    31: "str_split_soyad.py",
    33: "full_monte.py",
    35: "get_dummies.py",
    38: "tarif_indir.py",
    40: "read_recipes.py",
    42: "recipes_iloc0.py",
    44: "ingredients_len.py",
    46: "en_uzun_tarif.py",
    48: "breakfast_count.py",
    50: "cinnamon_count.py",
    52: "cinamon_typo.py",
    55: "spice_list.py",
    57: "spice_df.py",
    59: "spice_query.py",
    61: "recipe_names.py",
}

if __name__ == "__main__":
    body = build_from_notebook(
        "03.10-Working-With-Strings.ipynb", TR, CODE_NAMES, INSERTS
    )
    body += "\n\n" + next_link(
        "11-working-with-time-series.html", "3.11 Zaman Serileri"
    )
    path = write_chapter("10-working-with-strings", body)
    print("wrote", path)
