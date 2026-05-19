#!/usr/bin/env python3
"""Generate 13-further-resources.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nb_html_utils import addon, h1, next_link, orig_line, p, try_it, ul
from write_pandas_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/03.13-further-pandas-resources.html"

body = "\n\n".join(
    [
        h1("3.13 Daha Fazla Pandas Kaynağı"),
        orig_line(EN, "Further Resources"),
        p(
            "Kitabın bu bölümünde veri analizinde Pandas'ı etkili kullanmanın temellerinin "
            "çoğunu ele aldık. Yine de tartışmamızdan pek çok konu bilinçli olarak dışarıda "
            "bırakıldı. Pandas hakkında daha fazla bilgi edinmek için şu kaynakları öneririm:"
        ),
        ul(
            [
                '<a href="https://pandas.pydata.org/" target="_blank" rel="noopener">Pandas çevrimiçi dokümantasyonu</a>: Paketin eksiksiz dokümantasyonu için birincil kaynak. Dokümantasyondaki örnekler genelde küçük sentetik veri kümelerine dayansa da seçeneklerin açıklaması kapsamlıdır ve çeşitli fonksiyonların kullanımını anlamak için çok faydalıdır.',
                '<a href="https://learning.oreilly.com/library/view/python-for-data/9781098104023/" target="_blank" rel="noopener"><em>Python for Data Analysis</em></a>: Wes McKinney (Pandas\'ın yaratıcısı) tarafından yazılmıştır; bu bölümde yer veremediğimiz Pandas ayrıntılarının çoğunu içerir. Özellikle McKinney, finansal danışmanlık deneyiminden gelen zaman serisi araçlarına derinlemesine girer. Kitap ayrıca gerçek dünya veri kümelerinden içgörü kazanmak için Pandas uygulayan eğlenceli örnekler sunar.',
                '<a href="https://leanpub.com/effective-pandas" target="_blank" rel="noopener"><em>Effective Pandas</em></a>: Pandas geliştiricisi Tom Augspurger\'ın kısa e-kitabı; Pandas kütüphanesinin tam gücünü etkili ve idiomatik biçimde kullanmanın özünü sunar.',
                '<a href="http://pyvideo.org/search?q=pandas" target="_blank" rel="noopener">PyVideo\'da Pandas</a>: PyCon\'dan SciPy\'ye, PyData\'ya kadar birçok konferansta Pandas geliştiricileri ve ileri düzey kullanıcılar tarafından verilen eğitimler bulunur. Özellikle PyCon eğitimleri genelde iyi seçilmiş sunucular tarafından verilir.',
            ]
        ),
        p(
            "Bu kaynakları, bu bölümlerde verilen yürüyüşle birlikte kullanarak umarım "
            "karşınıza çıkan herhangi bir veri analizi probleminde Pandas'ı kullanmaya "
            "hazır olursunuz!"
        ),
        addon(
            "öğrenme yolu",
            "Resmi dokümantasyon + McKinney kitabı + bu handbook bölümleri birlikte "
            "en sağlam Pandas temelini verir. Takıldığınız yerde IPython'da "
            "<code>pd.DataFrame?</code> ve Tab tamamlama alışkanlığını sürdürün.",
        ),
        try_it(
            "",
            "Pandas dokümantasyonuna hızlı erişim alıştırması — bir <code>Series</code> "
            "üzerinde <code>str</code> erişimcisini keşfedin:",
            """import pandas as pd
s = pd.Series(["Merhaba", "Dünya"])
print(s.str.upper())
print([m for m in dir(s.str) if not m.startswith("_")][:8], "...")""",
            "deneme_pandas_kaynak.py",
        ),
    ]
)

if __name__ == "__main__":
    path = write_chapter("13-further-resources", body)
    print("wrote", path)
