#!/usr/bin/env python3
"""Generate 11-working-with-time-series.html."""
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
    ul,
)
from write_pandas_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html"
EN_LABEL = "Working with Time Series"

TR = {
    0: h1("3.11 Zaman Serileri"),
    1: "\n".join(
        [
            orig_line(EN, EN_LABEL),
            p(
                "Pandas başlangıçta finansal modelleme bağlamında geliştirildi; beklenebileceği "
                "gibi tarihler, saatler ve zaman indeksli verilerle çalışmak için kapsamlı "
                "bir araç seti içerir. Tarih ve saat verisi birkaç türde gelir:"
            ),
            ul(
                [
                    "<em>Zaman damgaları</em> (timestamps) belirli anları ifade eder (ör. 4 Temmuz 2021, sabah 7:00).",
                    "<em>Zaman aralıkları</em> ve <em>dönemler</em> (periods) belirli bir başlangıç ve bitiş arasındaki süreyi ifade eder; örneğin Haziran 2021 ayı. Dönemler genelde her aralığın eşit uzunlukta ve çakışmadığı zaman aralıklarının özel bir durumudur (ör. günleri oluşturan 24 saatlik dönemler).",
                    "<em>Zaman farkları</em> veya <em>süreler</em> (deltas/durations) tam bir süre uzunluğunu ifade eder (ör. 22,56 saniye).",
                ]
            ),
            p(
                "Bu bölüm Pandas'ta bu tarih/saat veri türlerinin her biriyle nasıl "
                "çalışılacağını tanıtır. Python veya Pandas'taki zaman serisi araçlarının "
                "eksiksiz bir rehberi değil; kullanıcı olarak zaman serileriyle nasıl "
                "yaklaşmanız gerektiğine dair geniş bir bakış sunar. Python'daki tarih "
                "ve saat araçlarının kısa bir tartışmasıyla başlayacağız; ardından "
                "Pandas'ın sunduğu araçlara geçeceğiz. Daha derin kaynakları listeledikten "
                "sonra Pandas'ta zaman serisi verisiyle çalışmanın kısa örneklerini gözden "
                "geçireceğiz."
            ),
        ]
    ),
    2: "\n".join(
        [
            h2("Python'da Tarihler ve Saatler", "python-tarih-saat"),
            p(
                "Python dünyasında tarih, saat, fark ve zaman aralıklarının birkaç "
                "temsili vardır. Pandas'ın zaman serisi araçları veri bilimi uygulamalarında "
                "genelde en kullanışlı olsa da diğer Python araçlarıyla ilişkisini görmek "
                "faydalıdır."
            ),
        ]
    ),
    3: "\n".join(
        [
            h3("Yerleşik Python Tarih/Saat: datetime ve dateutil", "datetime-dateutil"),
            p(
                "Python'da tarih ve saatle çalışmak için temel nesneler yerleşik "
                "<code>datetime</code> modülündedir. Üçüncü taraf <code>dateutil</code> "
                "modülüyle tarihler üzerinde bir dizi kullanışlı işlemi hızlıca "
                "yapabilirsiniz. Örneğin <code>datetime</code> tipiyle elle tarih "
                "oluşturabilirsiniz:"
            ),
        ]
    ),
    5: p(
        "Esnek biçimde biçimlendirilmiş bir dize tarihini ayrıştırmak için "
        "<code>dateutil</code> modülünü kullanabilirsiniz:"
    ),
    7: p(
        "<code>datetime</code> nesneniz olduktan sonra haftanın gününü yazdırmak gibi "
        "işlemler yapabilirsiniz:"
    ),
    9: "\n".join(
        [
            p(
                "Burada tarihleri yazdırmak için standart dize biçim kodlarından birini "
                "(<code>'%A'</code>) kullandık; bunlar Python "
                '<a href="https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior" '
                'target="_blank" rel="noopener"><code>datetime</code> dokümantasyonundaki '
                "<code>strftime</code> bölümünde</a> açıklanır. Diğer yararlı tarih "
                "yardımcılarının dokümantasyonu "
                '<a href="http://labix.org/python-dateutil" target="_blank" '
                'rel="noopener"><code>dateutil</code> çevrimiçi dokümantasyonunda</a> '
                "bulunur. Bilinmesi gereken ilgili paket "
                '<a href="http://pytz.sourceforge.net/" target="_blank" rel="noopener">'
                "<code>pytz</code></a>; zaman serisi verisinin en baş ağrıtan unsuru olan "
                "saat dilimleriyle çalışma araçlarını içerir."
            ),
            p(
                "<code>datetime</code> ve <code>dateutil</code>'in gücü esneklik ve "
                "kolay sözdizimindedir: ilgilendiğiniz neredeyse her işlemi bu nesneler "
                "ve yerleşik yöntemleriyle kolayca yapabilirsiniz. Zayıf kaldıkları yer "
                "büyük tarih/saat dizileriyle çalışmak istediğinizdedir: Python sayısal "
                "değişken listeleri NumPy tarzı tipli sayısal dizilere göre verimsiz "
                "olduğu gibi Python <code>datetime</code> nesne listeleri de kodlanmış "
                "tarih dizilerine göre verimsizdir."
            ),
        ]
    ),
    10: h3("Zaman Tipli Diziler: NumPy datetime64", "numpy-datetime64"),
    12: p(
        "Tarihleri bu biçimde elde ettikten sonra vektörize işlemleri hızlıca "
        "yapabiliriz:"
    ),
    14: "\n".join(
        [
            p(
                "NumPy <code>datetime64</code> dizilerindeki tekdüze tip sayesinde bu tür "
                "işlem, diziler büyüdükçe özellikle Python <code>datetime</code> nesneleriyle "
                "doğrudan çalışmaktan çok daha hızlı yapılabilir "
                '(vektörizasyonu <a href="../02-numpy/03-computation-ufuncs.html">'
                "2.3 Evrensel Fonksiyonlar</a> bölümünde tanıtmıştık)."
            ),
            p(
                "<code>datetime64</code> ve ilgili <code>timedelta64</code> nesnelerinin "
                "bir ayrıntısı <em>temel zaman birimi</em> üzerine kurulu olmalarıdır. "
                "<code>datetime64</code> 64 bit hassasiyetle sınırlı olduğundan kodlanabilir "
                "zaman aralığı bu temel birimin $2^{64}$ katıdır. Yani <code>datetime64</code> "
                "<em>zaman çözünürlüğü</em> ile <em>maksimum zaman aralığı</em> arasında "
                "ödünleşim dayatır."
            ),
            p(
                "Örneğin 1 nanosaniye çözünürlük istiyorsanız yalnızca $2^{64}$ nanosaniye, "
                "yani yaklaşık 600 yıl kodlayabilirsiniz. NumPy istenen birimi girdiden "
                "çıkarır; örneğin gün tabanlı <code>datetime</code>:"
            ),
        ]
    ),
    16: p("İşte dakika tabanlı bir datetime:"),
    18: p(
        "İstenen temel birimi birçok biçim kodundan biriyle zorlayabilirsiniz; "
        "burada nanosaniye tabanlı zaman zorluyoruz:"
    ),
    20: p(
        "Aşağıdaki tablo NumPy <code>datetime64</code> dokümantasyonundan alınmış olup "
        "kullanılabilir biçim kodlarını ve kodlayabildikleri göreli/mutlak zaman aralıklarını "
        "listeler:"
    ),
    21: """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Kod</th><th>Anlam</th><th>Göreli aralık</th><th>Mutlak aralık</th></tr></thead>
        <tbody>
          <tr><td><code>Y</code></td><td>Yıl</td><td>± 9,2e18 yıl</td><td>[9,2e18 MÖ, 9,2e18 MS]</td></tr>
          <tr><td><code>M</code></td><td>Ay</td><td>± 7,6e17 yıl</td><td>[7,6e17 MÖ, 7,6e17 MS]</td></tr>
          <tr><td><code>W</code></td><td>Hafta</td><td>± 1,7e17 yıl</td><td>[1,7e17 MÖ, 1,7e17 MS]</td></tr>
          <tr><td><code>D</code></td><td>Gün</td><td>± 2,5e16 yıl</td><td>[2,5e16 MÖ, 2,5e16 MS]</td></tr>
          <tr><td><code>h</code></td><td>Saat</td><td>± 1,0e15 yıl</td><td>[1,0e15 MÖ, 1,0e15 MS]</td></tr>
          <tr><td><code>m</code></td><td>Dakika</td><td>± 1,7e13 yıl</td><td>[1,7e13 MÖ, 1,7e13 MS]</td></tr>
          <tr><td><code>s</code></td><td>Saniye</td><td>± 2,9e12 yıl</td><td>[2,9e9 MÖ, 2,9e9 MS]</td></tr>
          <tr><td><code>ms</code></td><td>Milisaniye</td><td>± 2,9e9 yıl</td><td>[2,9e6 MÖ, 2,9e6 MS]</td></tr>
          <tr><td><code>us</code></td><td>Mikrosaniye</td><td>± 2,9e6 yıl</td><td>[290301 MÖ, 294241 MS]</td></tr>
          <tr><td><code>ns</code></td><td>Nanosaniye</td><td>± 292 yıl</td><td>[1678 MS, 2262 MS]</td></tr>
          <tr><td><code>ps</code></td><td>Pikosaniye</td><td>± 106 gün</td><td>[1969 MS, 1970 MS]</td></tr>
          <tr><td><code>fs</code></td><td>Femtosaniye</td><td>± 2,6 saat</td><td>[1969 MS, 1970 MS]</td></tr>
          <tr><td><code>as</code></td><td>Attosaniye</td><td>± 9,2 saniye</td><td>[1969 MS, 1970 MS]</td></tr>
        </tbody>
      </table>
    </div>""",
    22: "\n".join(
        [
            p(
                "Gerçek dünyada gördüğümüz veri türleri için kullanışlı bir varsayılan "
                "<code>datetime64[ns]</code>'dir; modern tarihlerin geniş bir aralığını uygun "
                "ince çözünürlükle kodlayabilir."
            ),
            p(
                "Son olarak <code>datetime64</code> yerleşik Python <code>datetime</code> "
                "tipinin bazı eksikliklerini giderse de <code>datetime</code> ve özellikle "
                "<code>dateutil</code>'in sağladığı birçok kullanışlı yöntem ve fonksiyondan "
                "yoksundur. Daha fazla bilgi "
                '<a href="https://numpy.org/doc/stable/reference/arrays.datetime.html" '
                'target="_blank" rel="noopener">NumPy <code>datetime64</code> dokümantasyonunda</a>.'
            ),
        ]
    ),
    23: "\n".join(
        [
            h3("Pandas'ta Tarih ve Saat: İki Dünyanın En İyisi", "pandas-timestamp"),
            p(
                "Pandas az önce tartışılan tüm araçların üzerine inşa ederek "
                "<code>Timestamp</code> nesnesi sunar; <code>datetime</code> ve "
                "<code>dateutil</code>'in kullanım kolaylığını <code>numpy.datetime64</code>'ün "
                "verimli depolama ve vektörize arayüzüyle birleştirir. Bu "
                "<code>Timestamp</code> nesnelerinden Pandas, <code>Series</code> veya "
                "<code>DataFrame</code>'de veriyi indekslemek için "
                "<code>DatetimeIndex</code> oluşturabilir."
            ),
            p(
                "Örneğin daha önceki gösterimi Pandas araçlarıyla tekrarlayabiliriz. "
                "Esnek biçimli dize tarihini ayrıştırıp gün adını biçim kodlarıyla "
                "yazdırabiliriz:"
            ),
        ]
    ),
    26: p("Ayrıca aynı nesne üzerinde NumPy tarzı vektörize işlemler yapabiliriz:"),
    28: p(
        "Sonraki bölümde Pandas'ın sunduğu araçlarla zaman serisi verisini "
        "manipüle etmeye daha yakından bakacağız."
    ),
    29: "\n".join(
        [
            h2("Pandas Zaman Serisi: Zamana Göre İndeksleme", "zamana-gore-indeks"),
            p(
                "Pandas zaman serisi araçları veriyi zaman damgalarıyla indekslemeye "
                "başladığınızda gerçekten faydalı olur. Örneğin zaman indeksli veri "
                "içeren bir <code>Series</code> oluşturabiliriz:"
            ),
        ]
    ),
    31: p(
        "Veriyi bir <code>Series</code>'te tuttuğumuza göre önceki bölümlerdeki "
        "<code>Series</code> indeksleme kalıplarının herhangi birini, tarihe "
        "dönüştürülebilen değerler geçirerek kullanabiliriz:"
    ),
    33: p(
        "Ek özel yalnızca-tarih indeksleme işlemleri vardır; örneğin bir yıl "
        "geçirerek o yıldaki tüm verinin dilimini almak:"
    ),
    35: p(
        "Daha sonra tarihleri indeks olarak kullanmanın kolaylığının ek örneklerini "
        "göreceğiz. Önce mevcut zaman serisi veri yapılarına daha yakından bakalım."
    ),
    36: h2("Pandas Zaman Serisi Veri Yapıları", "zaman-serisi-yapilari"),
    37: "\n".join(
        [
            p("Bu bölüm zaman serisi verisiyle çalışmak için temel Pandas yapılarını tanıtır:"),
            ul(
                [
                    "<em>Zaman damgaları</em> için Pandas <code>Timestamp</code> tipini sağlar. Daha önce belirtildiği gibi bu esasen Python <code>datetime</code>'ın yerine geçer; daha verimli <code>numpy.datetime64</code> tipine dayanır. İlişkili <code>Index</code> yapısı <code>DatetimeIndex</code>'tir.",
                    "<em>Zaman dönemleri</em> için Pandas <code>Period</code> tipini sağlar. <code>numpy.datetime64</code> tabanlı sabit frekanslı aralık kodlar. İlişkili indeks <code>PeriodIndex</code>'tir.",
                    "<em>Zaman farkları</em> veya <em>süreler</em> için Pandas <code>Timedelta</code> tipini sağlar. Python <code>datetime.timedelta</code>'nın daha verimli yerine geçer; <code>numpy.timedelta64</code>'e dayanır. İlişkili indeks <code>TimedeltaIndex</code>'tir.",
                ]
            ),
        ]
    ),
    39: p(
        "Bu tarih/saat nesnelerinin en temeli <code>Timestamp</code> ve "
        "<code>DatetimeIndex</code>'tir. Doğrudan çağrılabilirler; ancak genelde "
        "çok çeşitli biçimleri ayrıştıran <code>pd.to_datetime</code> kullanılır. "
        "Tek tarih <code>Timestamp</code>, dizi varsayılan olarak <code>DatetimeIndex</code> "
        "verir:"
    ),
    41: p("Örneğin bir tarihten diğeri çıkarıldığında <code>TimedeltaIndex</code> oluşur:"),
    43: "\n".join(
        [
            h2("Düzenli Diziler: pd.date_range", "date-range"),
            p(
                "Düzenli tarih dizileri oluşturmayı kolaylaştırmak için Pandas "
                "<code>pd.date_range</code> (zaman damgaları), <code>pd.period_range</code> "
                "(dönemler) ve <code>pd.timedelta_range</code> (zaman farkları) sunar. "
                "Python <code>range</code> ve NumPy <code>np.arange</code> başlangıç, bitiş "
                "ve isteğe bağlı adım alıp dizi döndürür. Benzer şekilde <code>pd.date_range</code> "
                "başlangıç/bitiş tarihi ve isteğe bağlı frekans kodu ile düzenli tarih dizisi "
                "oluşturur:"
            ),
        ]
    ),
    45: p(
        "Alternatif olarak bitiş yerine başlangıç noktası ve dönem sayısı "
        "belirtilebilir:"
    ),
    47: p(
        "<code>freq</code> argümanı (varsayılan <code>D</code>) aralığı değiştirir. "
        "Örneğin saatlik zaman damgaları dizisi:"
    ),
    49: p(
        "<code>freq</code> argümanı (varsayılan <code>D</code>) aralığı değiştirir. "
        "Örneğin saatlik zaman damgaları dizisi:"
    ),
    51: p(
        "Düzenli <code>Period</code> veya <code>Timedelta</code> dizileri için "
        "<code>pd.period_range</code> ve <code>pd.timedelta_range</code> kullanışlıdır. "
        "Aylık dönemler:"
    ),
    53: p("Saat saat artan süre dizisi:"),
    54: p(
        "Bunların hepsi Pandas frekans kodlarını anlamayı gerektirir; özet bir "
        "sonraki bölümde."
    ),
    55: h2("Frekanslar ve Ofsetler", "frekanslar-ofsetler"),
    56: p(
        "Pandas zaman serisi araçlarının temelinde <em>frekans</em> veya "
        "<em>tarih ofseti</em> kavramı yatar. Ana kodların özeti aşağıdadır; "
        "önceki bölümlerdeki <code>D</code> (gün) ve <code>H</code> (saat) gibi "
        "istediğiniz frekans aralığını belirtmek için kullanılır:"
    ),
    57: """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Kod</th><th>Açıklama</th><th>Kod</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>D</code></td><td>Takvim günü</td><td><code>B</code></td><td>İş günü</td></tr>
          <tr><td><code>W</code></td><td>Haftalık</td><td></td><td></td></tr>
          <tr><td><code>M</code></td><td>Ay sonu</td><td><code>BM</code></td><td>İş ayı sonu</td></tr>
          <tr><td><code>Q</code></td><td>Çeyrek sonu</td><td><code>BQ</code></td><td>İş çeyreği sonu</td></tr>
          <tr><td><code>A</code></td><td>Yıl sonu</td><td><code>BA</code></td><td>İş yılı sonu</td></tr>
          <tr><td><code>H</code></td><td>Saat</td><td><code>BH</code></td><td>İş saati</td></tr>
          <tr><td><code>T</code></td><td>Dakika</td><td></td><td></td></tr>
          <tr><td><code>S</code></td><td>Saniye</td><td></td><td></td></tr>
          <tr><td><code>L</code></td><td>Milisaniye</td><td></td><td></td></tr>
          <tr><td><code>U</code></td><td>Mikrosaniye</td><td></td><td></td></tr>
          <tr><td><code>N</code></td><td>Nanosaniye</td><td></td><td></td></tr>
        </tbody>
      </table>
    </div>""",
    58: p(
        "Aylık, çeyreklik ve yıllık frekansların hepsi belirtilen dönemin "
        "<em>sonunda</em> işaretlenir. Herhangi birine <code>S</code> eki eklemek "
        "bunları dönemin <em>başında</em> işaretler:"
    ),
    59: """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Kod</th><th>Açıklama</th><th>Kod</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>MS</code></td><td>Ay başı</td><td><code>BMS</code></td><td>İş ayı başı</td></tr>
          <tr><td><code>QS</code></td><td>Çeyrek başı</td><td><code>BQS</code></td><td>İş çeyreği başı</td></tr>
          <tr><td><code>AS</code></td><td>Yıl başı</td><td><code>BAS</code></td><td>İş yılı başı</td></tr>
        </tbody>
      </table>
    </div>""",
    58: "\n".join(
        [
            p(
                "Ayrıca çeyreklik veya yıllık kodların hangi ayda işaretleneceğini "
                "üç harfli ay kodu sonekiyle değiştirebilirsiniz:"
            ),
            ul(
                [
                    "<code>Q-JAN</code>, <code>BQ-FEB</code>, <code>QS-MAR</code>, <code>BQS-APR</code> vb.",
                    "<code>A-JAN</code>, <code>BA-FEB</code>, <code>AS-MAR</code>, <code>BAS-APR</code> vb.",
                ]
            ),
            p(
                "Benzer şekilde haftalık frekansın bölünme noktası üç harfli hafta günü "
                "koduyla değiştirilebilir:"
            ),
            ul(["<code>W-SUN</code>, <code>W-MON</code>, <code>W-TUE</code>, <code>W-WED</code> vb."]),
            p(
                "Üstüne kodlar sayılarla birleştirilerek başka frekanslar belirtilebilir. "
                "Örneğin 2 saat 30 dakika için saat (<code>H</code>) ve dakika (<code>T</code>) "
                "kodlarını birleştiririz:"
            ),
        ]
    ),
    60: p(
        "Tüm bu kısa kodlar <code>pd.tseries.offsets</code> modülündeki belirli Pandas "
        "zaman serisi ofset örneklerine referans verir. Örneğin iş günü ofsetini doğrudan "
        "oluşturabiliriz:"
    ),
    62: p(
        "Frekans ve ofset kullanımının daha fazla tartışması için Pandas dokümantasyonundaki "
        '<a href="https://pandas.pydata.org/docs/user_guide/timeseries.html#dateoffset-objects" '
        'target="_blank" rel="noopener"><code>DateOffset</code> bölümüne</a> bakın.'
    ),
    63: "\n".join(
        [
            h2("Yeniden Örnekleme, Kaydırma ve Pencereleme", "resample-shift-window"),
            p(
                "Tarih ve saatleri sezgisel organizasyon ve erişim için indeks olarak "
                "kullanabilme Pandas zaman serisi araçlarının önemli yönüdür. İndeksli "
                "verinin genel faydaları (işlemlerde otomatik hizalama, sezgisel dilimleme "
                "vb.) geçerlidir; Pandas ek zaman serisine özgü işlemler de sunar."
            ),
            p(
                "Bunlardan birkaçına hisse fiyat verisi örneğiyle bakacağız. Pandas "
                "büyük ölçüde finans bağlamında geliştirildiği için finansal veriye özel "
                "araçlar içerir. Örneğeşlik <code>pandas-datareader</code> paketi "
                "(<code>pip install pandas-datareader</code> ile kurulur) çeşitli çevrimiçi "
                "kaynaklardan veri içe aktarabilir. Burada S&amp;P 500 fiyat geçmişinin "
                "bir kısmını yükleyeceğiz:"
            ),
        ]
    ),
    65: p("Basitlik için yalnızca kapanış fiyatını kullanacağız:"),
    67: p(
                "Normal Matplotlib kurulum kodundan sonra <code>plot</code> yöntemiyle "
                "görselleştirebiliriz "
                '(bkz. kitap <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html" '
                'target="_blank" rel="noopener">Bölüm 4</a>):'
    ),
    71: h3("Frekans Yeniden Örnekleme ve Dönüştürme", "resample-asfreq"),
    72: p(
        "Zaman serisi verisinde yaygın ihtiyaç daha yüksek veya daha düşük frekansta "
        "yeniden örneklemedir. <code>resample</code> veya daha basit <code>asfreq</code> "
        "yöntemiyle yapılır. Temel fark: <code>resample</code> esasen <em>veri "
        "agregasyonu</em>, <code>asfreq</code> esasen <em>veri seçimi</em>dir."
    ),
    74: p(
        "S&amp;P 500 kapanış verisini aşağı örneklemede ikisinin döndürdüğünü "
        "karşılaştıralım. İş yılı sonunda yeniden örnekliyoruz:"
    ),
    75: p(
        "Farkı fark edin: her noktada <code>resample</code> <em>önceki yılın ortalamasını</em>, "
        "<code>asfreq</code> <em>yıl sonundaki değeri</em> raporlar."
    ),
    77: p(
        "Yukarı örneklemede <code>resample</code> ve <code>asfreq</code> büyük ölçüde "
        "eşdeğerdir; <code>resample</code>'ın çok daha fazla seçeneği vardır. Her iki "
        "yöntemin varsayılanı yukarı örneklenen noktaları boş bırakmaktır (NA ile doldurulur). "
        '<a href="04-missing-values.html">3.4 Eksik Veri</a> bölümündeki <code>pd.fillna</code> '
        "gibi <code>asfreq</code> değerlerin nasıl doldurulacağını belirten "
        "<code>method</code> argümanı kabul eder. İş günü verisini günlük frekansta "
        "(hafta sonları dahil) yeniden örnekliyoruz:"
    ),
    79: p(
        "S&amp;P 500 verisi yalnızca iş günlerinde olduğundan üst panel NA boşlukları "
        "gösterir. Alt panel iki doldurma stratejisinin farkını gösterir: ileri doldurma "
        "ve geri doldurma."
    ),
    81: h3("Zaman Kaydırma", "zaman-kaydirma"),
    82: p(
        "Başka yaygın zaman serisi işlemi veriyi zamanda kaydırmaktır. Pandas "
        "<code>shift</code> yöntemiyle veriyi verilen giriş sayısı kadar kaydırır. "
        "Düzenli frekansta örneklenmiş zaman serisinde bu, zaman içindeki eğilimleri "
        "incelemenin bir yolunu verir."
    ),
    84: p(
        "Örneğin veriyi günlük değerlere yeniden örnekleyip 364 kaydırarak S&amp;P 500 "
        "üzerinde zaman içinde 1 yıllık yatırım getirisini hesaplayabiliriz:"
    ),
    86: p(
        "En kötü bir yıllık getiri Mart 2019 civarındaydı; koronavirüs kaynaklı "
        "piyasa çöküşü tam bir yıl sonrasındaydı. Beklendiği gibi en iyi bir yıllık "
        "getiri Mart 2020'de, düşükten almak için yeterli öngörü veya şansı olanlar içindi."
    ),
    87: h3("Kayan Pencereleme", "kayan-pencere"),
    88: p(
        "Kayan istatistik hesaplama Pandas'ın uyguladığı üçüncü zaman serisine özgü "
        "işlemdir. <code>Series</code> ve <code>DataFrame</code> nesnelerinin "
        "<code>rolling</code> özniteliği ile yapılır; "
        '<a href="08-aggregation-and-grouping.html">3.8 Agregasyon ve Gruplama</a> '
        "bölümündeki <code>groupby</code> işlemine benzer bir görünüm döndürür. "
        "Bu kayan görünüm varsayılan olarak bir dizi agregasyon işlemi sunar."
    ),
    90: p(
        "Örneğin hisse fiyatlarının bir yıllık merkezli kayan ortalaması ve "
        "standart sapmasına bakabiliriz:"
    ),
    92: p(
        "<code>groupby</code> işlemlerinde olduğu gibi özel kayan hesaplamalar için "
        "<code>aggregate</code> ve <code>apply</code> kullanılabilir."
    ),
    93: h2("Daha Fazlasını Nereden Öğrenilir?", "daha-fazla-kaynak"),
    94: "\n".join(
        [
            p(
                "Bu bölüm Pandas'ın zaman serisi araçlarının en temel özelliklerinin "
                "kısa bir özetini verdi; daha kapsamlı tartışma için Pandas "
                'dokümantasyonundaki <a href="https://pandas.pydata.org/docs/user_guide/timeseries.html" '
                'target="_blank" rel="noopener">"Time Series/Date Functionality"</a> '
                "bölümüne bakın."
            ),
            p(
                'Başka mükemmel kaynak Wes McKinney\'nin <a href="https://learning.oreilly.com/library/view/python-for-data/9781098104023/" '
                'target="_blank" rel="noopener"><em>Python for Data Analysis</em></a> '
                "(O'Reilly) kitabıdır. Pandas kullanımında paha biçilmez bir kaynaktır. "
                "Özellikle iş ve finans bağlamında zaman serisi araçlarına vurgu yapar; "
                "iş takvimleri, saat dilimleri ve ilgili konulara daha çok girer."
            ),
            p(
                "Her zaman IPython yardım işlevselliğiyle burada tartışılan fonksiyon "
                "ve yöntemlerin daha fazla seçeneğini keşfedip deneyebilirsiniz. "
                "Yeni bir Python aracını öğrenmenin en iyi yolunun bu olduğunu düşünüyorum."
            ),
        ]
    ),
    95: "\n".join(
        [
            h2("Örnek: Seattle Bisiklet Sayımları Görselleştirme", "ornek-seattle"),
            p(
                "Zaman serisi verisiyle çalışmanın daha kapsamlı bir örneği olarak "
                "Seattle <a href=\"http://www.openstreetmap.org/#map=17/47.64813/-122.34965\" "
                'target="_blank" rel="noopener">Fremont Köprüsü</a> bisiklet sayımlarına '
                "bakalım. Veri 2012 sonunda kurulan otomatik sayaçtan gelir; doğu ve batı "
                "kaldırımlarında indüktif sensörler vardır. Saatlik sayımlar "
                '<a href="http://data.seattle.gov" target="_blank" rel="noopener">'
                "data.seattle.gov</a> adresinden indirilebilir; Ulaşım kategorisinde "
                "Fremont Bridge Bicycle Counter veri kümesi."
            ),
            p("Kitap için kullanılan CSV şu şekilde indirilebilir (notebook yorumları):"),
        ]
    ),
    97: p(
        "Veri kümesi indirildikten sonra Pandas ile CSV'yi <code>DataFrame</code>'e "
        "okuyabiliriz. <code>Date</code> sütununu indeks olarak ve tarihlerin otomatik "
        "ayrıştırılmasını belirtiriz:"
    ),
    99: p("Kolaylık için sütun adlarını kısaltalım:"),
    101: p("Verinin özet istatistiklerine bakalım:"),
    103: h3("Veriyi Görselleştirme", "veriyi-gorsellestirme"),
    104: p(
        "Veri kümesi hakkında içgörü kazanmak için görselleştirebiliriz. "
        "Ham veriyi çizerek başlayalım:"
    ),
    106: p(
        "Yaklaşık 150.000 saatlik örnek anlam çıkarmak için fazla yoğundur. "
        "Daha kaba bir ızgarada yeniden örnekleyerek daha fazla içgörü elde edebiliriz. "
        "Haftalık yeniden örnekleyelim:"
    ),
    108: p(
        "Bazı eğilimler ortaya çıkar: beklediğiniz gibi yazın kıştan daha çok bisiklet "
        "kullanılır; mevsim içinde bile haftadan haftaya değişim vardır (muhtemelen "
        "hava durumuna bağlı; "
        '<a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html" '
        'target="_blank" rel="noopener">Doğrusal Regresyon</a> bölümünde daha fazla '
        "inceleriz). Ayrıca 2020 başından itibaren COVID-19 salgınının işe gidip gelme "
        "kalıpları üzerindeki etkisi belirgindir."
    ),
    110: p(
        "Veriyi toplamak için kullanışlı bir seçenek kayan ortalama; "
        "<code>pd.rolling_mean</code> fonksiyonu. 30 günlük kayan ortalamayı, pencereyi "
        "ortaya alarak inceleyelim:"
    ),
    112: p(
        "Sonucun tırtıklılığı pencerenin sert kesiminden kaynaklanır. "
        "Pencere fonksiyonu — örneğin Gauss penceresi — ile daha pürüzsüz kayan ortalama "
        "elde edilebilir. Kod hem pencere genişliğini (50 gün) hem Gauss genişliğini "
        "(10 gün) belirtir:"
    ),
    114: h3("Veriye Derinlemesine Bakmak", "veriye-derinlemesine"),
    115: p(
        "Bu yumuşatılmış görünümler genel eğilim fikri için faydalıdır; ancak "
        "yapının çoğunu gizler. Örneğin günün saatine göre ortalama trafiğe bakmak "
        "isteyebiliriz. "
        '<a href="08-aggregation-and-grouping.html">3.8 Agregasyon ve Gruplama</a> '
        "bölümündeki <code>groupby</code> ile yapabiliriz:"
    ),
    117: p(
        "Saatlik trafik güçlü iki tepeli bir dizidir; sabah 8:00 ve akşam 17:00 "
        "civarında. Bu muhtemelen köprüyü geçen yoğun işe gidip gelme trafiğinin "
        "kanıtıdır. Yönsel bileşen de vardır: veriye göre doğu kaldırım sabah işe "
        "gidişte, batı kaldırım akşam dönüşte daha çok kullanılıyor."
    ),
    119: p(
        "Haftanın gününe göre değişimi merak edebiliriz. Yine basit <code>groupby</code> "
        "ile:"
    ),
    121: p(
        "Hafta içi ile hafta sonu toplamları arasında güçlü ayrım görülür; "
        "Pazartesi–Cuma ortalama bisikletçi sayısı Cumartesi–Pazar'dan yaklaşık iki kat fazla."
    ),
    123: p(
        "Buna göre bileşik <code>groupby</code> yapıp hafta içi ve hafta sonu saatlik "
        "eğilimlere bakalım. Hafta sonu bayrağı ve günün saati ile gruplayarak başlayalım:"
    ),
    125: p(
        "Sonra "
        '<a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html" '
        'target="_blank" rel="noopener">Çoklu Alt Grafikler</a> bölümünde açıklanan '
        "Matplotlib araçlarıyla iki paneli yan yana çizeceğiz:"
    ),
    127: p(
        "Sonuç hafta içi iki tepeli işe gidip gelme kalıbını, hafta sonu tek tepeli "
        "rekreasyon kalıbını gösterir. Hava, sıcaklık, yılın zamanı ve diğer faktörlerin "
        "etkisini daha ayrıntılı incelemek ilginç olabilir; "
        '<a href="https://jakevdp.github.io/blog/2014/06/10/is-seattle-really-seeing-an-uptick-in-cycling/" '
        'target="_blank" rel="noopener">"Is Seattle Really Seeing an Uptick in Cycling?"</a> '
        "blog yazımda bu verinin bir alt kümesini kullanırım. Modelleme bağlamında "
        "veri kümesine "
        '<a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html" '
        'target="_blank" rel="noopener">Doğrusal Regresyon</a> bölümünde tekrar döneceğiz.'
    ),
}

# Düzeltmeler: yanlış anahtarları kaldır, eksik hücreleri ekle
for _k in [4, 59, 84, 86, 88, 90, 92, 94, 104, 106, 108, 110, 112, 114, 115, 117, 119, 121, 123, 125, 127]:
    TR.pop(_k, None)

TR.update({
    39: p(
        "Herhangi bir <code>DatetimeIndex</code>, frekans kodu eklenerek "
        "<code>to_period</code> ile <code>PeriodIndex</code>'e dönüştürülebilir; "
        "burada günlük frekans için <code>'D'</code> kullanıyoruz:"
    ),
    47: p(
        "<code>freq</code> argümanı (varsayılan <code>D</code>) aralığı değiştirir. "
        "Örneğin saatlik zaman damgaları dizisi:"
    ),
    54: h2("Frekanslar ve Ofsetler", "frekanslar-ofsetler"),
    55: p(
        "Pandas zaman serisi araçlarının temelinde <em>frekans</em> veya "
        "<em>tarih ofseti</em> kavramı yatar. Ana kodların özeti aşağıdadır; "
        "önceki bölümlerdeki <code>D</code> (gün) ve <code>H</code> (saat) gibi "
        "istediğiniz frekans aralığını belirtmek için kullanılır:"
    ),
    56: """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Kod</th><th>Açıklama</th><th>Kod</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>D</code></td><td>Takvim günü</td><td><code>B</code></td><td>İş günü</td></tr>
          <tr><td><code>W</code></td><td>Haftalık</td><td></td><td></td></tr>
          <tr><td><code>M</code></td><td>Ay sonu</td><td><code>BM</code></td><td>İş ayı sonu</td></tr>
          <tr><td><code>Q</code></td><td>Çeyrek sonu</td><td><code>BQ</code></td><td>İş çeyreği sonu</td></tr>
          <tr><td><code>A</code></td><td>Yıl sonu</td><td><code>BA</code></td><td>İş yılı sonu</td></tr>
          <tr><td><code>H</code></td><td>Saat</td><td><code>BH</code></td><td>İş saati</td></tr>
          <tr><td><code>T</code></td><td>Dakika</td><td></td><td></td></tr>
          <tr><td><code>S</code></td><td>Saniye</td><td></td><td></td></tr>
          <tr><td><code>L</code></td><td>Milisaniye</td><td></td><td></td></tr>
          <tr><td><code>U</code></td><td>Mikrosaniye</td><td></td><td></td></tr>
          <tr><td><code>N</code></td><td>Nanosaniye</td><td></td><td></td></tr>
        </tbody>
      </table>
    </div>""",
    57: p(
        "Aylık, çeyreklik ve yıllık frekansların hepsi belirtilen dönemin "
        "<em>sonunda</em> işaretlenir. Herhangi birine <code>S</code> eki eklemek "
        "bunları dönemin <em>başında</em> işaretler:"
    ),
    58: """    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Kod</th><th>Açıklama</th><th>Kod</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>MS</code></td><td>Ay başı</td><td><code>BMS</code></td><td>İş ayı başı</td></tr>
          <tr><td><code>QS</code></td><td>Çeyrek başı</td><td><code>BQS</code></td><td>İş çeyreği başı</td></tr>
          <tr><td><code>AS</code></td><td>Yıl başı</td><td><code>BAS</code></td><td>İş yılı başı</td></tr>
        </tbody>
      </table>
    </div>"""
    + p(
        "Ayrıca çeyreklik veya yıllık kodların ayını üç harfli ay koduyla, haftalık "
        "frekansın bölünme gününü üç harfli gün koduyla değiştirebilirsiniz "
        "(<code>Q-JAN</code>, <code>W-MON</code> vb.). Kodlar sayılarla birleştirilerek "
        "başka frekanslar da belirtilebilir; örneğin 2 saat 30 dakika:"
    ),
    60: p(
        "Tüm bu kısa kodlar <code>pd.tseries.offsets</code> modülündeki Pandas "
        "zaman serisi ofset örneklerine referans verir:"
    ),
    62: p(
        "Frekans ve ofset kullanımının daha fazla tartışması için Pandas "
        'dokümantasyonundaki <a href="https://pandas.pydata.org/docs/user_guide/timeseries.html#dateoffset-objects" '
        'target="_blank" rel="noopener"><code>DateOffset</code> bölümüne</a> bakın.'
    ),
    63: "\n".join([
        h2("Yeniden Örnekleme, Kaydırma ve Pencereleme", "resample-shift-window"),
        p(
            "Tarih/saat indeksleri sezgisel veri organizasyonu sağlar. Pandas ek "
            "olarak yeniden örnekleme, kaydırma ve pencereleme sunar. Hisse fiyat "
            "örneği için <code>pandas-datareader</code> ile S&amp;P 500 verisi yüklenir:"
        ),
    ]),
    69: h3("Frekans Yeniden Örnekleme ve Dönüştürme", "resample-asfreq"),
    72: p(
        "Yukarı örneklemede <code>resample</code> ve <code>asfreq</code> büyük ölçüde "
        "eşdeğerdir. Varsayılan olarak boş noktalar NA ile doldurulur; "
        '<a href="04-missing-values.html">3.4 Eksik Veri</a> bölümündeki gibi '
        "<code>asfreq</code> <code>method</code> ile doldurma yapılabilir:"
    ),
    75: h3("Zaman Kaydırma", "zaman-kaydirma"),
    78: "\n".join([
        h3("Kayan Pencereleme", "kayan-pencere"),
        p(
            "Kayan istatistikler <code>rolling</code> özniteliğiyle hesaplanır "
            '(<a href="08-aggregation-and-grouping.html">3.8 Agregasyon ve Gruplama</a>):'
        ),
    ]),
    79: p(
        "Örneğin bir yıllık merkezli kayan ortalama ve medyan:"
    ),
    82: "\n".join([
        h2("Daha Fazlasını Nereden Öğrenilir?", "daha-fazla-kaynak"),
        p(
            'Kapsamlı tartışma: Pandas <a href="https://pandas.pydata.org/docs/user_guide/timeseries.html" '
            'target="_blank" rel="noopener">zaman serisi dokümantasyonu</a> ve Wes McKinney '
            '<em>Python for Data Analysis</em>. IPython <code>?</code> ile keşfetmeyi unutmayın.'
        ),
    ]),
    83: "\n".join([
        h2("Örnek: Seattle Bisiklet Sayımları", "ornek-seattle"),
        p(
            "Seattle Fremont Köprüsü saatlik bisiklet sayım verisi (2012+). "
            "CSV indirme notebook'taki yorum satırlarında:"
        ),
    ]),
    85: p(
        "CSV'yi <code>Date</code> indeksli ve <code>parse_dates=True</code> ile okuyoruz:"
    ),
    87: p("Sütun adlarını kısaltıyoruz:"),
    89: p("Özet istatistikler:"),
    91: h3("Veriyi Görselleştirme", "veriyi-gorsellestirme"),
    93: p(
        "~150.000 saatlik örnek çok yoğundur; haftalık <code>resample</code> ile "
        "eğilimleri görelim:"
    ),
    95: p(
        "Yaz/kış farkı, hava etkisi ve 2020'de COVID-19'un işe gidip gelme "
        "kalıplarına etkisi görülür."
    ),
    97: p(
        "Kayan ortalama penceresinin sert kesimi tırtıklılık yaratır; Gauss "
        "<code>win_type</code> ile yumuşatma yapılabilir:"
    ),
    99: h3("Veriye Derinlemesine Bakmak", "veriye-derinlemesine"),
    101: p(
        "Saatlik trafik iki tepelidir (08:00 ve 17:00) — işe gidip gelme kanıtı. "
        "Doğu kaldırım sabah, batı akşam daha yoğun."
    ),
    103: p("Haftanın gününe göre <code>groupby</code>:"),
    105: p(
        "Hafta içi/sonu ve saat bazında bileşik <code>groupby</code>; sonuçları "
        "Matplotlib ile iki panelde çiziyoruz:"
    ),
    107: p(
        "Hafta içi iki tepeli, hafta sonu tek tepeli kalıp ortaya çıkar. "
        "Veri kümesine modelleme bölümünde tekrar döneceğiz."
    ),
})

INSERTS = {
    27: addon(
        "Timestamp",
        "Pandas <code>Timestamp</code>, <code>datetime</code> kolaylığını "
        "<code>datetime64</code> verimliliğiyle birleştirir — zaman serisi "
        "analizinde en sık kullanılan tip budur.",
    ),
    34: try_it(
        "",
        "Zaman indeksli <code>Series</code> ile dilimleme deneyin:",
        """import pandas as pd
idx = pd.DatetimeIndex(["2020-01-01", "2020-06-01", "2021-01-01"])
s = pd.Series([10, 20, 30], index=idx)
print(s["2020":"2020-12-31"])""",
        "deneme_datetime_index.py",
    ),
    52: try_it(
        "",
        "<code>pd.date_range</code> ile haftalık tarih dizisi oluşturun:",
        """import pandas as pd
dr = pd.date_range("2024-01-01", periods=5, freq="W-MON")
print(dr)""",
        "deneme_date_range.py",
    ),
    80: addon(
        "resample vs asfreq",
        "<code>resample</code> agregasyon (ortalama, toplam vb.) yapar; "
        "<code>asfreq</code> belirli frekanstaki mevcut değeri seçer veya NA bırakır.",
    ),
    98: try_it(
        "",
        "Kayan ortalama ile basit zaman serisi yumuşatma:",
        """import pandas as pd
import numpy as np
rng = np.random.default_rng(0)
idx = pd.date_range("2020-01-01", periods=100, freq="D")
s = pd.Series(rng.random(100).cumsum(), index=idx)
print(s.rolling(7, center=True).mean().tail())""",
        "deneme_rolling.py",
    ),
}

CODE_NAMES = {
    4: "datetime_ornek.py",
    6: "dateutil_parse.py",
    8: "strftime_gun.py",
    11: "np_datetime64.py",
    13: "datetime64_arange.py",
    15: "datetime64_gun.py",
    17: "datetime64_dakika.py",
    19: "datetime64_ns.py",
    24: "pd_to_datetime.py",
    25: "pd_strftime.py",
    27: "pd_timedelta.py",
    30: "datetime_index_series.py",
    32: "series_date_slice.py",
    34: "series_year_slice.py",
    38: "to_datetime_coklu.py",
    40: "to_period.py",
    42: "dates_fark.py",
    44: "date_range.py",
    46: "date_range_periods.py",
    48: "date_range_hourly.py",
    50: "period_range.py",
    52: "timedelta_range.py",
    59: "timedelta_2h30t.py",
    61: "bday_offset.py",
    64: "sp500_datareader.py",
    66: "sp500_close.py",
    68: "sp500_plot.py",
    70: "resample_asfreq.py",
    73: "asfreq_fill.py",
    76: "shift_roi.py",
    80: "rolling_mean_median.py",
    84: "fremont_curl.py",
    86: "read_fremont.py",
    88: "fremont_columns.py",
    90: "fremont_describe.py",
    92: "fremont_plot_raw.py",
    94: "fremont_weekly.py",
    96: "fremont_rolling30.py",
    98: "fremont_gaussian.py",
    100: "fremont_by_time.py",
    102: "fremont_by_weekday.py",
    104: "fremont_weekend_group.py",
    106: "fremont_subplots.py",
}

if __name__ == "__main__":
    body = build_from_notebook(
        "03.11-Working-with-Time-Series.ipynb", TR, CODE_NAMES, INSERTS
    )
    body += "\n\n" + next_link(
        "12-performance-eval-and-query.html", "3.12 Performans ve Sorgu"
    )
    path = write_chapter("11-working-with-time-series", body)
    print("wrote", path)
