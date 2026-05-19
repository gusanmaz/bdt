#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from _gen_mpl_helpers import addon, try_it
from write_matplotlib_chapter import write_chapter

body = """
<h1>4.15 Daha Fazla Matplotlib Kaynağı</h1>

    <p><em>Orijinal: <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.15-further-matplotlib-resources.html" target="_blank" rel="noopener">Further Resources</a></em></p>

    <p>Kitabın tek bir bölümü Matplotlib'da kullanılabilir tüm özellikleri ve grafik türlerini kapsamayı asla umamaz. Gördüğümüz diğer paketlerde olduğu gibi IPython'ın Tab tamamlama ve yardım işlevlerinin (<a href="../01-ipython/01-help-and-documentation.html">1.1 IPython'da Yardım ve Dokümantasyon</a>) Matplotlib API'sini keşfederken çok yardımcı olabileceğini unutmayın. Ayrıca Matplotlib'ın <a href="https://matplotlib.org/" target="_blank" rel="noopener">çevrimiçi dokümantasyonu</a> faydalı bir referans olabilir. Özellikle yüzlerce farklı grafik türünün küçük resimlerini gösteren ve her birini oluşturmak için kullanılan Python kod parçacığına bağlayan <a href="https://matplotlib.org/stable/gallery/" target="_blank" rel="noopener">Matplotlib galerisine</a> bakın. Bu, geniş bir grafik stili ve görselleştirme tekniği yelpazesini görsel olarak inceleyip öğrenmenize olanak tanır.</p>

    <p>Matplotlib üzerine kitap uzunluğunda bir kaynak için Matplotlib çekirdek geliştiricisi Ben Root'un yazdığı <em>Interactive Applications Using Matplotlib</em> (Packt) kitabını öneririm.</p>

    <h2 id="diger-kutuphaneler">Diğer Python Görselleştirme Kütüphaneleri</h2>

    <p>Matplotlib en belirgin Python görselleştirme kütüphanesi olsa da keşfetmeye değer daha modern araçlar da vardır. Burada birkaçını kısaca anacağım:</p>

    <ul>
      <li><a href="http://bokeh.pydata.org" target="_blank" rel="noopener">Bokeh</a>: Python ön ucu olan bir JavaScript görselleştirme kütüphanesi; çok büyük ve/veya akış veri kümelerini işleyebilen yüksek etkileşimli görselleştirmeler oluşturur.</li>
      <li><a href="http://plot.ly" target="_blank" rel="noopener">Plotly</a>: Plotly şirketinin aynı adlı açık kaynak ürünü; ruh olarak Bokeh'e benzer. Aktif geliştirilir ve geniş bir etkileşimli grafik türü yelpazesi sunar.</li>
      <li><a href="https://holoviews.org/" target="_blank" rel="noopener">HoloViews</a>: Bokeh ve Matplotlib dahil çeşitli arka uçlarda grafik üretmek için daha bildirimsel, birleşik bir API.</li>
      <li><a href="https://vega.github.io/" target="_blank" rel="noopener">Vega</a> ve <a href="https://vega.github.io/vega-lite" target="_blank" rel="noopener">Vega-Lite</a>: bildirimsel grafik gösterimleri; veri görselleştirme ve etkileşim hakkında nasıl düşünüleceğine dair yıllar süren araştırmanın ürünüdür. Referans oluşturma uygulaması JavaScript'tir; <a href="https://altair-viz.github.io/" target="_blank" rel="noopener">Altair paketi</a> bu grafikleri üretmek için Python API'si sağlar.</li>
    </ul>

    <p>Python dünyasındaki görselleştirme ortamı sürekli gelişiyor; bu kitap yayımlandığında bu listenin güncelliğini yitirmiş olabileceğini düşünüyorum. Ayrıca Python birçok alanda kullanıldığı için daha özel kullanım durumları için oluşturulmuş başka görselleştirme araçları da bulacaksınız. Hepsini takip etmek zor olabilir; ancak bu geniş görselleştirme araçları yelpazesini öğrenmek için iyi bir kaynak, birçok farklı görselleştirme aracının öğreticilerini ve örneklerini içeren açık, topluluk odaklı <a href="https://pyviz.org/" target="_blank" rel="noopener">pyviz.org</a> sitesidir.</p>
""" + addon(
    "Matplotlib sonrası yol",
    "<p>Matplotlib temeli + Seaborn istatistiksel keşif + Plotly/Bokeh etkileşim iyi bir üçlüdür. "
    "Önce hangi soruya cevap vereceğinizi netleştirin; ardından pyviz.org veya Matplotlib galerisinden benzer örneği bulun.</p>",
) + try_it(
    "Galeri keşfi",
    "Matplotlib galerisinden bir örneği yerel ortamınızda çalıştırmadan önce API'yi keşfedin:",
    """import matplotlib.pyplot as plt
print('Matplotlib sürümü:', plt.matplotlib.__version__)
print('Stil sayfası sayısı:', len(plt.style.available))
print('İlk 5 stil:', plt.style.available[:5])""",
    "deneme_mpl_kaynak.py",
)

if __name__ == "__main__":
    path = write_chapter("15-further-resources", body)
    print("wrote", path)
