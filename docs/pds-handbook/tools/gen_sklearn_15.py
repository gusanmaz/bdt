#!/usr/bin/env python3
"""Generate 15-learning-more.html."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nb_html_utils import addon, h1, next_link, orig_line, p, try_it, ul
from write_sklearn_chapter import write_chapter

EN = "https://jakevdp.github.io/PythonDataScienceHandbook/05.15-learning-more.html"
EN_LABEL = "05.15 Learning More"

body = "\n\n".join(
    [
        h1("5.15 Daha Fazla Makine Öğrenmesi Kaynağı"),
        orig_line(EN, EN_LABEL),
        p(
            "Kitabın bu bölümü Python'da makine öğrenmesine hızlı bir tur oldu; "
            "esas olarak Scikit-Learn kütüphanesindeki araçları kullandık. "
            "Bu bölümler ne kadar uzun olsa da birçok ilginç ve önemli algoritma, "
            "yaklaşım ve tartışmayı kapsamak için hâlâ çok kısa. "
            "İlgilenenler için Python'da makine öğrenmesi hakkında daha fazla "
            "bilgi edinmek üzere şu kaynakları öneririm:"
        ),
        ul(
            [
                '<a href="https://scikit-learn.org/" target="_blank" rel="noopener">Scikit-Learn web sitesi</a>: '
                "Burada ele aldığımız modellerin birçoğunu ve çok daha fazlasını kapsayan "
                "etkileyici genişlikte dokümantasyon ve örnekler vardır. "
                "En önemli ve sık kullanılan makine öğrenmesi algoritmalarına kısa bir "
                "genel bakış istiyorsanız iyi bir başlangıç noktasıdır.",
                "<em>SciPy, PyCon ve PyData eğitim videoları</em>: Scikit-Learn ve diğer "
                "makine öğrenmesi konuları birçok Python odaklı konferans serisinin "
                "eğitim programlarında sürekli favoridir; özellikle PyCon, SciPy ve PyData. "
                "Bu konferansların çoğu keynote, konuşma ve eğitim videolarını ücretsiz "
                "yayınlar; uygun bir web aramasıyla (ör. \"PyCon 2022 videos\") kolayca bulunabilir.",
                '<a href="https://learning.oreilly.com/library/view/introduction-to-machine/9781449377939/" '
                'target="_blank" rel="noopener"><em>Introduction to Machine Learning with Python</em></a>, '
                "Andreas C. Müller ve Sarah Guido (O'Reilly). Bu kitap bu bölümlerde "
                "tartışılan makine öğrenmesi temellerinin çoğunu kapsar; özellikle "
                "Scikit-Learn'in ek tahminciler, model doğrulama yaklaşımları ve "
                "pipeline'lar gibi daha gelişmiş özellikleri için uygundur.",
                '<a href="https://www.packtpub.com/product/machine-learning-with-pytorch-and-scikit-learn/9781801819312" '
                'target="_blank" rel="noopener"><em>Machine Learning with PyTorch and Scikit-Learn</em></a>, '
                "Sebastian Raschka (Packt). Raschka'nın en yeni kitabı bu bölümlerde "
                "kapsanan bazı temel konularla başlar; ardından bu kavramların "
                '<a href="https://pytorch.org/" target="_blank" rel="noopener">PyTorch</a> '
                "kütüphanesiyle daha sofistike ve hesaplama açısından yoğun derin "
                "öğrenme ve pekiştirmeli öğrenme modellerine nasıl uygulandığını gösterir.",
            ]
        ),
        addon(
            "Pyodide sınırı",
            "Bu handbook'taki interaktif hücreler tarayıcıda Pyodide ile çalışır; "
            "PyTorch, büyük veri kümeleri ve GPU hızlandırması gibi konular için "
            "yerel Jupyter ortamı veya tam Python kurulumu gerekir.",
        ),
        try_it(
            "",
            "Scikit-Learn dokümantasyonuna hızlı erişim — bir tahmincinin "
            "hiperparametrelerini keşfedin:",
            """from sklearn.cluster import KMeans
print(KMeans.__doc__[:400], "...")
print("n_init =", KMeans().n_init)""",
            "deneme_sklearn_kaynak.py",
        ),
    ]
)

if __name__ == "__main__":
    path = write_chapter("15-learning-more", body)
    print("wrote", path.relative_to(Path(__file__).resolve().parent.parent))
