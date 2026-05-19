#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_mpl_helpers import code_block as cb, addon, try_it, next_link
from _nb_code import nb_code, code_meta
from write_matplotlib_chapter import write_chapter

NB = "04.10-Customizing-Ticks.ipynb"


def c(idx: int, fname: str) -> str:
    code = nb_code(NB, idx)
    lang, ro = code_meta(code)
    return cb(code, fname, lang=lang, readonly=ro)


body = """
<h1>4.10 Eksen İşaretleri Özelleştirme</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html" target="_blank" rel="noopener">Customizing Ticks</a></em></p>

    <p>Matplotlib'ın varsayılan tick konumlandırıcıları (locator) ve biçimlendiricileri (formatter) birçok yaygın durumda genel olarak yeterli olacak şekilde tasarlanmıştır; ancak hiçbir grafik türü için ideal değildir. Bu bölüm, ilgilendiğiniz grafik türü için tick konumlarını ve biçimlendirmesini ayarlamaya yönelik birkaç örnek sunar.</p>

    <p>Örneklere geçmeden önce Matplotlib grafiklerinin nesne hiyerarşisinden biraz daha söz edelim. Matplotlib, grafikte görünen her şeyi temsil eden bir Python nesnesine sahip olmayı hedefler: örneğin <code>Figure</code>'ın grafik öğelerinin göründüğü sınır kutusu olduğunu hatırlayın. Her Matplotlib nesnesi alt nesnelerin konteyneri de olabilir: örneğin her <code>Figure</code> bir veya daha fazla <code>Axes</code> içerebilir; her biri de grafik içeriğini temsil eden diğer nesneleri barındırır.</p>

    <p>Tick işaretleri de istisna değildir. Her eksenin <code>xaxis</code> ve <code>yaxis</code> öznitelikleri vardır; bunlar da ekseni oluşturan çizgiler, tick'ler ve etiketlerin tüm özelliklerini içeren alt özniteliklere sahiptir.</p>

    <h2 id="major-minor-ticks">Ana ve İkincil Tick'ler</h2>

    <p>Her eksen içinde <em>ana</em> (major) tick ve <em>ikincil</em> (minor) tick kavramı vardır. Adlarından anlaşılacağı gibi ana tick'ler genelde daha büyük veya belirgindir; ikincil tick'ler daha küçüktür. Varsayılan olarak Matplotlib ikincil tick'leri nadiren kullanır; ancak logaritmik grafiklerde görebilirsiniz (aşağıdaki şekil):</p>
""" + c(3, "import_mpl_np.py") + c(4, "log_axes.py") + """
    <p>Bu grafikte her ana tick büyük bir işaret, etiket ve ızgara çizgisi gösterir; her ikincil tick daha küçük bir işaret gösterir, etiket veya ızgara çizgisi yoktur.</p>

    <p>Bu tick özellikleri — konumlar ve etiketler — her eksenin <code>formatter</code> ve <code>locator</code> nesneleri ayarlanarak özelleştirilebilir. Az önce gösterilen grafiğin x ekseni için bunları inceleyelim:</p>
""" + c(6, "print_locators.py") + c(7, "print_formatters.py") + """
    <p>Hem ana hem ikincil tick konumlarının bir <code>LogLocator</code> ile belirlendiğini görüyoruz (logaritmik grafik için mantıklı). İkincil tick'lerin etiketleri ise <code>NullFormatter</code> ile biçimlendirilmiş: yani etiket gösterilmeyecek.</p>

    <p>Şimdi çeşitli grafikler için bu locator ve formatter'ları ayarlamaya yönelik birkaç örneğe bakalım.</p>

    <h2 id="hiding-ticks">Tick veya Etiketleri Gizleme</h2>

    <p>Belki de en yaygın tick/etiket biçimlendirme işlemi tick veya etiketleri gizlemektir. Bu, burada gösterildiği gibi <code>plt.NullLocator</code> ve <code>plt.NullFormatter</code> ile yapılabilir (aşağıdaki şekil):</p>
""" + c(10, "hide_ticks_labels.py") + """
    <p>x ekseninden etiketleri (tick/ızgara çizgilerini koruyarak) kaldırdık; y ekseninden tick'leri (dolayısıyla etiket ve ızgara çizgilerini de) kaldırdık. Hiç tick olmaması birçok durumda yararlıdır — örneğin bir görüntü ızgarası göstermek istediğinizde.</p>

    <p>Örneğin aşağıdaki şekil, denetimli makine öğrenmesi problemlerinde sık kullanılan farklı yüz görüntülerini içerir (bkz. örneğin <a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.07-support-vector-machines.html" target="_blank" rel="noopener">Derinlemesine: Destek Vektör Makineleri</a>):</p>
""" + c(12, "face_grid.py") + """
    <p>Her görüntü kendi ekseninde gösterilir; tick konumlandırıcılarını null yaptık çünkü tick değerleri (bu durumda piksel numaraları) bu görselleştirme için anlamlı bilgi taşımaz.</p>

    <h2 id="tick-count">Tick Sayısını Azaltma veya Artırma</h2>

    <p>Varsayılan ayarlarla yaygın bir sorun, küçük alt grafiklerde etiketlerin kalabalıklaşmasıdır. Aşağıdaki grafik ızgarasında bunu görebiliriz (aşağıdaki şekil):</p>
""" + c(15, "subplots_4x4.py") + """
    <p>Özellikle x ekseni tick'lerinde sayılar neredeyse üst üste binerek okunması zor hale gelir. Bunu <code>plt.MaxNLocator</code> ile ayarlayabiliriz; gösterilecek maksimum tick sayısını belirtmemize izin verir. Bu sayıya göre Matplotlib uygun tick konumlarını seçer (aşağıdaki şekil):</p>
""" + c(17, "maxn_locator.py") + """
    <p>Bu işleri çok daha temiz hale getirir. Düzenli aralıklı tick konumları üzerinde daha fazla kontrol istiyorsanız bir sonraki bölümde ele alacağımız <code>plt.MultipleLocator</code>'ı da kullanabilirsiniz.</p>

    <h2 id="fancy-formats">Gelişmiş Tick Biçimlendirme</h2>

    <p>Matplotlib'ın varsayılan tick biçimlendirmesi çoğu zaman yetersiz kalabilir: geniş bir varsayılan olarak iyi çalışır, ancak bazen farklı bir şey istersiniz. Aşağıdaki sinüs ve kosinüs eğrisi grafiğini düşünün (aşağıdaki şekil):</p>
""" + c(20, "sin_cos_plot.py") + """
    <p>Burada birkaç değişiklik yapmak isteyebiliriz. İlk olarak, bu veri için tick ve ızgara çizgilerini $\\pi$ katlarında aralamak daha doğaldır. Bunu, verdiğimiz sayının katlarında tick konumlandıran <code>MultipleLocator</code> ile yapabiliriz. İyi ölçüde hem $\\pi/2$ hem $\\pi/4$ katlarında ana ve ikincil tick ekleyelim (aşağıdaki şekil):</p>
""" + c(22, "multiple_locator_pi.py") + """
    <p>Ancak şimdi tick etiketleri biraz saçma görünüyor: $\\pi$ katları olduklarını görebiliyoruz, ancak ondalık gösterim bunu hemen iletmiyor. Bunu tick biçimlendiricisini değiştirerek düzeltebiliriz. İstediğimiz için yerleşik bir biçimlendirici yok; bunun yerine tick çıktıları üzerinde ince kontrol sağlayan kullanıcı tanımlı bir fonksiyon kabul eden <code>plt.FuncFormatter</code> kullanacağız (aşağıdaki şekil):</p>
""" + c(24, "func_formatter_pi.py") + """
    <p>Bu çok daha iyi! Dizeyi dolar işaretleri içine alarak Matplotlib'ın LaTeX desteğinden yararlandık. Matematiksel sembol ve formüllerin gösterimi için çok uygundur: bu durumda <code>"$\\pi$"</code> Yunan harfi $\\pi$ olarak işlenir.</p>

    <h2 id="formatters-locators-ozet">Biçimlendiriciler ve Konumlandırıcılar Özeti</h2>

    <p>Mevcut birkaç biçimlendirici ve konumlandırıcıyı gördük; bu bölümü, yerleşik locator ve formatter seçeneklerinin kısa listesiyle bitireceğim. Ayrıntılar için docstring'lere veya Matplotlib çevrimiçi dokümantasyonuna bakın. Aşağıdakilerin her biri <code>plt</code> ad alanında kullanılabilir:</p>

    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Locator sınıfı</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>NullLocator</code></td><td>Tick yok</td></tr>
          <tr><td><code>FixedLocator</code></td><td>Tick konumları sabit</td></tr>
          <tr><td><code>IndexLocator</code></td><td>İndeks grafikleri için locator (örn. <code>x = range(len(y))</code>)</td></tr>
          <tr><td><code>LinearLocator</code></td><td>Min'den max'a eşit aralıklı tick'ler</td></tr>
          <tr><td><code>LogLocator</code></td><td>Min'den max'a logaritmik aralıklı tick'ler</td></tr>
          <tr><td><code>MultipleLocator</code></td><td>Tick'ler ve aralık tabanın katı</td></tr>
          <tr><td><code>MaxNLocator</code></td><td>Güzel konumlarda en fazla belirtilen sayıda tick bulur</td></tr>
          <tr><td><code>AutoLocator</code></td><td>(Varsayılan) basit varsayılanlarla <code>MaxNLocator</code></td></tr>
          <tr><td><code>AutoMinorLocator</code></td><td>İkincil tick'ler için locator</td></tr>
        </tbody>
      </table>
    </div>

    <div class="table-wrapper">
      <table class="vocab-table">
        <thead><tr><th>Formatter sınıfı</th><th>Açıklama</th></tr></thead>
        <tbody>
          <tr><td><code>NullFormatter</code></td><td>Tick'lerde etiket yok</td></tr>
          <tr><td><code>IndexFormatter</code></td><td>Etiket dizisinden dize ayarlar</td></tr>
          <tr><td><code>FixedFormatter</code></td><td>Etiketleri elle ayarlar</td></tr>
          <tr><td><code>FuncFormatter</code></td><td>Kullanıcı tanımlı fonksiyon etiketleri belirler</td></tr>
          <tr><td><code>FormatStrFormatter</code></td><td>Her değer için biçim dizesi kullanır</td></tr>
          <tr><td><code>ScalarFormatter</code></td><td>Skaler değerler için varsayılan biçimlendirici</td></tr>
          <tr><td><code>LogFormatter</code></td><td>Log eksenleri için varsayılan biçimlendirici</td></tr>
        </tbody>
      </table>
    </div>

    <p>Bu seçeneklerin daha fazla örneğini kitabın geri kalanında göreceğiz.</p>
""" + addon(
    "Locator vs formatter",
    "<p><strong>Locator</strong> tick'in <em>nerede</em> olduğunu belirler; <strong>formatter</strong> o konumda <em>ne yazılacağını</em> belirler. "
    "Gizlemek için locator'ı <code>NullLocator</code>, etiketi gizlemek için formatter'ı <code>NullFormatter</code> yapın — ikisi farklıdır.</p>",
) + try_it(
    "π ekseninde tick",
    "Basit bir sinüs grafiğinde x eksenini π katlarında işaretleyin:",
    """import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.set_xlim(0, 2 * np.pi)
fig""",
    "deneme_pi_ticks.py",
) + next_link("11-settings-and-stylesheets.html", "4.11 Ayarlar ve Stil Sayfaları")

if __name__ == "__main__":
    path = write_chapter("10-customizing-ticks", body)
    print("wrote", path)
