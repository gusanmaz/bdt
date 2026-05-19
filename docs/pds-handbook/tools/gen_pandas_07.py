#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_pandas_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_pandas_chapter import write_chapter

NB = "03.07-Merge-and-Join.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    if not code.strip():
        return ""
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>3.7 Merge ve Join</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html" target="_blank" rel="noopener">Combining Datasets: Merge and Join</a></em></p>

    <p>Pandas'ın sunduğu önemli özelliklerden biri, veritabanlarında tanıdık olabileceğiniz yüksek performanslı bellek içi join ve merge işlemleridir. Ana arayüz <code>pd.merge</code> fonksiyonudur; pratikte nasıl çalıştığını örneklerle göreceğiz.</p>

    <p>Kolaylık için önceki bölümdeki <code>display</code> fonksiyonunu standart içe aktarmalardan sonra yeniden tanımlayalım:</p>
""" + c(2, "imports_display.py") + """
    <h2 id="iliskisel-cebir">İlişkisel Cebir</h2>

    <p><code>pd.merge</code>'de uygulanan davranış, çoğu veritabanındaki işlemlerin kavramsal temeli olan <em>ilişkisel cebirin</em> bir alt kümesidir. Bu yaklaşımın gücü, herhangi bir veri kümesi üzerinde daha karmaşık bileşik işlemlerin yapı taşları olan temel işlemleri tanımlamasıdır.</p>

    <p>Pandas, <code>pd.merge</code> ve <code>Series</code>/<code>DataFrame</code> <code>join</code> yönteminde bu yapı taşlarının birçoğunu uygular; farklı kaynaklardan veriyi verimli biçimde bağlamanızı sağlar.</p>

    <h2 id="join-turleri">Join Türleri</h2>

    <p><code>pd.merge</code> <em>bire bir</em>, <em>çoka bir</em> ve <em>çoğa çok</em> join türlerini destekler. Hepsi aynı arayüzle çağrılır; join türü girdi verisinin biçimine bağlıdır. Önce üç basit örneğe bakalım.</p>

    <h3 id="bire-bir-join">Bire Bir Join</h3>

    <p>En basit merge türü bire bir join'dir; <a href="06-concat-and-append.html">3.6 Concat ve Append</a>'deki sütun yönünde birleştirmeye benzer. Bir şirketteki çalışanlar hakkında iki <code>DataFrame</code> düşünelim:</p>
""" + c(6, "df1_df2_employees.py") + """
    <p>Bu bilgiyi tek bir <code>DataFrame</code>'de birleştirmek için <code>pd.merge</code> kullanılır:</p>
""" + c(8, "pd_merge_df3.py") + """
    <p><code>pd.merge</code>, her iki çerçevede <code>employee</code> sütununu tanır ve otomatik olarak anahtar olarak kullanır. Sonuç iki girdinin bilgisini birleştirir. Sütunlardaki giriş sırası korunmayabilir; <code>pd.merge</code> bunu doğru hesaplar. Genelde merge indeksi atar (indeks üzerinden merge için <code>left_index</code>/<code>right_index</code> istisnası).</p>

    <h3 id="coka-bir-join">Çoka Bir Join</h3>

    <p>Çoka bir join'de iki anahtar sütundan birinde yinelenen girişler vardır; sonuç <code>DataFrame</code>'i bu yinelenmeleri korur:</p>
""" + c(12, "merge_many_to_one.py") + """
    <p>Sonuçta, girdi gerektirdiği yerlerde tekrarlanan “supervisor” bilgisi içeren ek bir sütun vardır.</p>

    <h3 id="coga-cok-join">Çoğa Çok Join</h3>

    <p>Çoğa çok join kavramsal olarak kafa karıştırıcı olabilir ama iyi tanımlıdır. Her iki taraftaki anahtar sütunda yinelenme varsa sonuç çoğa çok merge olur. Bir grupla ilişkili becerileri gösteren çerçeveyle kişi başına becerileri kurtarabiliriz:</p>
""" + c(16, "merge_many_to_many.py") + """
    <p>Bu üç join türü diğer Pandas araçlarıyla geniş işlevsellik sağlar. Gerçek veri kümeleri nadiren bu kadar temizdir; <code>pd.merge</code>'in join'i nasıl ayarlayacağınıza dair seçeneklere geçelim.</p>

    <h2 id="merge-anahtari">Merge Anahtarının Belirtilmesi</h2>

    <p><code>pd.merge</code>'in varsayılan davranışını gördük: iki girdi arasında eşleşen sütun adlarını arar ve anahtar olarak kullanır. Sütun adları genelde bu kadar uyumlu olmaz; Pandas çeşitli seçenekler sunar.</p>

    <h3 id="on-anahtar">on Anahtar Sözcüğü</h3>

    <p>Anahtar sütun adını açıkça <code>on</code> ile verebilirsiniz (tek ad veya liste):</p>
""" + c(22, "merge_on_employee.py") + """
    <p>Bu seçenek yalnızca sol ve sağ <code>DataFrame</code>'de belirtilen sütun varsa çalışır.</p>

    <h3 id="left-on-right-on">left_on ve right_on</h3>

    <p>Farklı sütun adlarıyla birleştirmek gerekebilir; örneğin çalışan adı “name” olarak etiketlenmiş olabilir. <code>left_on</code> ve <code>right_on</code> kullanılır:</p>
""" + c(25, "merge_left_right_on.py") + """
    <p>Sonuçta gereksiz bir sütun kalabilir; <code>DataFrame.drop()</code> ile düşürülebilir:</p>
""" + c(27, "merge_drop_name.py") + """
    <h3 id="left-index-right-index">left_index ve right_index</h3>

    <p>Bazen sütun yerine indeks üzerinden birleştirmek istersiniz:</p>
""" + c(29, "df1a_df2a_index.py") + """
    <p><code>pd.merge()</code> içinde <code>left_index</code> ve/veya <code>right_index</code> ile indeks anahtar olarak kullanılır:</p>
""" + c(31, "merge_by_index.py") + """
    <p>Pandas, ek anahtar sözcük olmadan indeks tabanlı merge için <code>DataFrame.join()</code> yöntemini de sunar:</p>
""" + c(33, "df1a_join_df2a.py") + """
    <p>İndeks ve sütunları karıştırmak için <code>left_index</code> ile <code>right_on</code> veya <code>left_on</code> ile <code>right_index</code> birleştirilebilir:</p>
""" + c(35, "merge_left_index_right_on.py") + addon(
    "join vs merge",
    "<p><code>df.join(other)</code> indeks hizalı birleştirme içindir; farklı sütun adları veya SQL tarzı join türleri için <code>pd.merge</code> daha esnektir.</p>",
) + """
    <p>Tüm bu seçenekler çoklu indeks ve/veya çoklu sütunla da çalışır. Ayrıntılar için Pandas dokümantasyonundaki <a href="https://pandas.pydata.org/docs/user_guide/merging.html" target="_blank" rel="noopener">merge bölümüne</a> bakın.</p>

    <h2 id="kume-aritmetigi">Küme Aritmetiği ile Join</h2>

    <p>Önceki örneklerde göz ardı ettiğimiz konu: join'de kullanılan küme aritmetiği türü. Bir anahtar sütunda değer varken diğerinde yoksa ne olur?</p>
""" + c(39, "df6_df7_food_drink.py") + """
    <p>Yalnızca ortak “name” girişi Mary olan iki veri kümesi birleştirildi. Varsayılan sonuç iki girdinin <em>kesişimidir</em> — <em>iç birleşim</em> (inner join). <code>how</code> ile açıkça belirtilebilir (varsayılan <code>"inner"</code>):</p>
""" + c(41, "merge_how_inner.py") + """
    <p><code>how</code> için diğer seçenekler <code>'outer'</code>, <code>'left'</code> ve <code>'right'</code>'tır. <em>Dış birleşim</em> (outer join) girdi sütunlarının birleşimini döndürür; eksik değerler NA ile doldurulur:</p>
""" + c(43, "merge_how_outer.py") + """
    <p><em>Sol</em> ve <em>sağ</em> join sırasıyla sol ve sağ girdinin girişleri üzerinden birleşim döndürür:</p>
""" + c(45, "merge_how_left.py") + """
    <p>Çıktı satırları artık sol girdideki girişlere karşılık gelir. <code>how='right'</code> benzer şekilde sağ girdi için çalışır. Tüm seçenekler önceki join türlerine doğrudan uygulanabilir.</p>

    <h2 id="suffixes">Çakışan Sütun Adları: suffixes</h2>

    <p>İki girdide çakışan sütun adları olabilir:</p>
""" + c(49, "df8_df9_rank.py") + """
    <p>Çıktıda iki <code>rank</code> sütunu çakışacağından <code>merge</code> otomatik olarak <code>_x</code> ve <code>_y</code> son eklerini ekler. Özel son ekler <code>suffixes</code> ile verilebilir:</p>
""" + c(51, "merge_suffixes.py") + """
    <p>Bu son ekler tüm join desenlerinde ve birden fazla çakışan sütunda çalışır.</p>

    <p>Bu desenler için <a href="08-aggregation-and-grouping.html">3.8 Agregasyon ve Gruplama</a>'da ilişkisel cebire daha derin bakılır. Ayrıca Pandas dokümantasyonundaki <a href="https://pandas.pydata.org/docs/user_guide/merging.html" target="_blank" rel="noopener">Merge, join, concat and compare</a> bölümüne bakın.</p>

    <h2 id="ornek-abd-eyaletleri">Örnek: ABD Eyalet Verisi</h2>

    <p>Merge ve join en çok farklı kaynaklardan veri birleştirirken gündeme gelir. ABD eyaletleri ve nüfusları hakkında örnek veri kullanacağız. Veri dosyaları <a href="http://github.com/jakevdp/data-USstates" target="_blank" rel="noopener">github.com/jakevdp/data-USstates</a> adresindedir:</p>
""" + c(55, "download_us_states.sh",) + """
    <p>Üç veri kümesine Pandas <code>read_csv</code> ile bakalım (dosyalar <code>data/</code> altında olmalıdır):</p>
""" + c(57, "read_us_states_csv.py") + addon(
    "Pyodide ve CSV",
    "<p>Tarayıcıdaki Pyodide ortamında <code>data/</code> dosyaları yoksa bu hücreler çalışmayabilir; mantığı anlamak için kodu okuyun veya veriyi yerel Jupyter'de indirin.</p>",
) + """
    <p>Bu bilgiyle 2010 nüfus yoğunluğuna göre ABD eyalet ve bölgelerini sıralamak isteyelim. Veri elimizde; birleştirmemiz gerekir.</p>

    <p>Önce <code>pop</code> ile <code>abbrevs</code> arasında çoka bir merge yaparak tam eyalet adlarını alalım. <code>pop</code>'taki <code>state/region</code> ile <code>abbrevs</code>'teki <code>abbreviation</code> üzerinden birleştiririz; etiket uyumsuzluğunda veri kaybı olmasın diye <code>how='outer'</code>:</p>
""" + c(59, "merge_pop_abbrevs.py") + """
    <p>Uyumsuzluk olup olmadığını null satırlara bakarak kontrol edelim:</p>
""" + c(61, "merged_isnull.py") + """
    <p>Bazı <code>population</code> değerleri null; hangileri olduğuna bakalım:</p>
""" + c(63, "merged_null_population.py") + """
    <p>Null nüfus değerlerinin çoğu 2000 öncesi Porto Riko kayıtlarından geliyor olabilir. Daha önemlisi bazı yeni <code>state</code> girişleri de null — <code>abbrevs</code> anahtarında karşılık yok:</p>
""" + c(65, "merged_null_state_region.py") + """
    <p>Sorun: nüfus verisinde Porto Riko (PR) ve bir bütün olarak ABD (USA) var; kısaltma tablosunda yok. Hızlıca doldurabiliriz:</p>
""" + c(67, "fill_pr_usa.py") + """
    <p><code>state</code> sütununda artık null yok; devam edebiliriz.</p>

    <p>Şimdi alan verisiyle <code>state</code> sütunu üzerinden birleştirelim:</p>
""" + c(69, "merge_final_areas.py") + """
    <p>Yine uyumsuzluk için null kontrolü:</p>
""" + c(71, "final_isnull.py") + """
    <p><code>area</code> sütununda null var; hangi bölgelerin atlandığına bakalım:</p>
""" + c(73, "final_null_area_states.py") + """
    <p><code>areas</code> çerçevesinde ABD bütününün alanı yok. Toplam eyalet alanı eklenebilir; burada tüm ABD yoğunluğu tartışmamızla ilgili olmadığı için null satırları düşüyoruz:</p>
""" + c(75, "final_dropna.py") + """
    <p>Artık gereken veri hazır. 2010 yılı ve toplam nüfus dilimini <code>query</code> ile seçelim (<a href="12-performance-eval-and-query.html">3.12 Performans: eval ve query</a> — NumExpr gerekebilir):</p>
""" + c(77, "data2010_query.py") + """
    <p>Nüfus yoğunluğunu hesaplayıp sıralayalım; eyalet üzerinden yeniden indeksleyerek:</p>
""" + c(79, "density_compute.py") + c(80, "density_sort.py") + """
    <p>Sonuç, 2010 nüfus yoğunluğuna göre (km² başına kişi) ABD eyaletleri, Washington DC ve Porto Riko sıralamasıdır. En yoğun bölge Washington DC; eyaletler arasında en yoğun New Jersey.</p>

    <p>Listenin sonuna da bakalım:</p>
""" + c(82, "density_tail.py") + """
    <p>En seyrek eyalet açık ara Alaska — km² başına bir kişiden biraz fazla.</p>

    <p>Bu tür veri birleştirme, gerçek dünya kaynaklarıyla soru yanıtlarken yaygındır. Bu örnek, öğrendiğimiz araçları birleştirerek veriden içgörü kazanmanın yollarından birini göstermiştir.</p>
""" + try_it(
    "Şimdi deneyin",
    "İki küçük çerçeveyi <code>pd.merge</code> ile <code>how='inner'</code> ve <code>how='outer'</code> karşılaştırın:",
    """import pandas as pd
left = pd.DataFrame({'k': [1, 2, 3], 'v': ['a', 'b', 'c']})
right = pd.DataFrame({'k': [2, 3, 4], 'w': [10, 20, 30]})
print("inner:\\n", pd.merge(left, right, on='k', how='inner'))
print("\\nouter:\\n", pd.merge(left, right, on='k', how='outer'))""",
    "deneme_merge_how.py",
) + next_link("08-aggregation-and-grouping.html", "3.8 Agregasyon ve Gruplama")

write_chapter("07-merge-and-join", body)
print("wrote 07-merge-and-join.html")
