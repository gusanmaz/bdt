# Büyük Veri Teknolojileri — Ödev Teslim Rehberi

Bu dosya, dönem boyunca verilen üç ödevin teslim kurallarını, son tarihlerini ve alternatif gönderim yöntemlerini tek bir yerde toplar.

**Ders notları:** [Hafta 1 — Büyük Veri Teknolojileri](https://gusanmaz.github.io/bdt/ders-notlari/hafta1.html)

---

## Genel Bilgiler

| Ödev | Konu | Zorunluluk | Son Teslim |
|------|------|------------|------------|
| Ödev 1 | Büyük Veride İlginç Keşifler | Zorunlu | **30 Mayıs 2026, Cumartesi — 23:59** |
| Ödev 2 | Proje Geliştirme (Geri Bildirim Sonrası) | İsteğe bağlı | **30 Mayıs 2026, Cumartesi — 23:59** |
| Ödev 3 | NumPy Notları | Zorunlu | **30 Mayıs 2026, Cumartesi — 23:59** |

> **Ödev 1 hakkında:** Ödev 1'in orijinal son teslim tarihi 12 Nisan 2026 idi ve sınıf sunumları yapıldı. Öğrencilerin büyük çoğunluğu kodlarını çok önceden repoya commit etti. Kod göndermeyen öğrencilere bir şans daha tanımak amacıyla son teslim tarihi **30 Mayıs 2026**'ya uzatıldı. Daha önce teslim etmiş ancak dosyalarının eksik olduğunu düşünen öğrenciler de bu süre içinde repolarına **yeniden commit yaparak** proje dosyalarını güncelleyebilir.

---

## Grup Çalışması Kuralları

- Ödevler **2–5 kişilik gruplar** halinde yapılabilir.
- **GitHub üzerinden teslim:** Gruptan **yalnızca bir kişinin** repo oluşturup commit etmesi yeterlidir. Grup üyeleri ilgili dosyada (Ödev 1'de `README.md`, Ödev 2 ve 3'te notebook) belirtilmelidir.
- **E-posta ile teslim:** GitHub'dan gönderemeyen öğrenciler için **grubun her üyesi ayrı ayrı** e-posta göndermelidir (bkz. [Alternatif Teslim Yöntemi](#alternatif-teslim-yöntemi-e-posta)).

---

## Yapay Zeka Kullanımı

| Ödev | Yapay Zeka |
|------|------------|
| Ödev 1 | ✅ Kullanılabilir |
| Ödev 2 | ✅ Kullanılabilir |
| Ödev 3 | ❌ Kullanılamaz |

Ödev 1 ve 2'de yapay zeka araçlarından (ChatGPT, GitHub Copilot, Claude vb.) yardım alınabilir. Ancak hipotez oluşturma, bulguları yorumlama ve ödev 3'teki notların kendi gözünüzden yazılması sizden beklenir.

---

## Kimlik Bilgileri

Her ödevde ödevi yapan kişinin **adı, soyadı ve öğrenci numarası** belirtilmelidir:

| Ödev | Nereye yazılacak? |
|------|-------------------|
| Ödev 1 | `README.md` dosyası |
| Ödev 2 | Jupyter Notebook içinde |
| Ödev 3 | Jupyter Notebook içinde |

Grup çalışmalarında tüm grup üyelerinin bilgileri yazılmalıdır.

---

## Ödev 1: Büyük Veride İlginç Keşifler

**Detaylı açıklama:** [Ödev 1 sayfası](https://gusanmaz.github.io/bdt/ders-notlari/odev1.html)

**GitHub Classroom davet linki:** https://classroom.github.com/a/FODBhjUj

### Amaç

Açık veri platformlarındaki büyük veri setlerinden ilginç ve beklenmedik bir gözlem (insight) keşfetmek. Bir hipotez oluşturup Python ile test etmek, bulguları görselleştirmek ve sınıfta sunmak.

### Nasıl Yapılır?

1. Kaggle, HuggingFace, GitHub gibi platformlardaki açık veri setlerini keşfedin.
2. İlginç bir hipotez veya soru oluşturun.
3. Python (`pandas`, `matplotlib`, `seaborn` vb.) ile analiz edin.
4. Bulgularınızı yorumlayın ve bir veri hikayesi anlatın.
5. Rapor ve sunum hazırlayın.

### Teslim Edilecekler

| Dosya/Klasör | Açıklama | Zorunlu? |
|--------------|----------|----------|
| `README.md` | Grup üyeleri (ad, soyad, öğrenci no), hipotez, kısa özet, çalıştırma talimatları | ✅ |
| `analiz.ipynb` veya `.py` | Veri analizi Python kodu | ✅ |
| `rapor.md` veya `rapor.pdf` | Bulgular, yorumlar, grafikler, veri kaynakları | ✅ |
| `sunum.pptx` veya `sunum.pdf` | Sınıf sunumu dosyası | ✅ |
| `data/` | Kullanılan veri seti (çok büyükse link verin) | ⭐ Önerilir |
| `requirements.txt` | Kullanılan Python kütüphaneleri | ⭐ Önerilir |

> Sınıf sunumları yapılmıştır. Repoda **sunum dosyası** ve **kodlar** bulunmalıdır. Kendi oluşturduğunuz bir veri seti varsa o da repoya eklenmelidir.

> **Dosya güncelleme:** Daha önce repoya commit yapmış ancak teslim dosyalarının eksik veya hatalı olduğunu düşünen öğrenciler, son teslim tarihi uzatıldığı için **30 Mayıs 2026, 23:59**'a kadar eksik dosyalarını ekleyebilir veya mevcut dosyalarını düzelterek **yeniden commit** edebilir. Değerlendirme, son teslim tarihindeki repo durumuna göre yapılacaktır.

---

## Ödev 2: Proje Geliştirme (İsteğe Bağlı)

**GitHub Classroom davet linki:** https://classroom.github.com/a/8cz9U_sc

### Amaç

Ödev 1 sunumlarında yapılan eleştiriler doğrultusunda projenizi daha üst bir noktaya taşımak. Bu ödev **isteğe bağlıdır**; eleştiriler üzerinden projesini geliştirmek isteyen öğrenciler teslim edebilir.

### Ödev 1'den Farkları

- Teslim formatı **yalnızca bir Jupyter Notebook** dosyasıdır.
- Tüm proje kodları bu notebook üzerinden çalıştırılmalıdır.
- Proje fikri ve elde edilen sonuçlar, notebook içindeki hücrelerde **metin olarak** paylaşılmalıdır.
- Notebook'un çalışması için başka dosyalara ihtiyaç duyuluyorsa (örneğin veri seti), bu dosyalar repoya yüklenebilir.

### Teslim Edilecekler

| Dosya/Klasör | Açıklama | Zorunlu? |
|--------------|----------|----------|
| `*.ipynb` | Tüm kod, proje açıklaması ve sonuçlar bu notebook'ta | ✅ |
| Ek dosyalar (ör. `data/`) | Notebook'un çalışması için gerekli dosyalar | Gerektiğinde |

Notebook'un başında veya uygun bir hücrede **ad, soyad, öğrenci numarası** ve grup üyeleri belirtilmelidir.

---

## Ödev 3: NumPy Notları (Zorunlu)

**GitHub Classroom davet linki:** https://classroom.github.com/a/twiY3bdy

**Referans kaynaklar:**

- [Python Data Science Handbook — NumPy bölümü](https://jakevdp.github.io/PythonDataScienceHandbook/) (Jake VanderPlas, orijinal İngilizce)
- [PDS Handbook — Türkçe](https://gusanmaz.github.io/bdt/pds-handbook/index.html) (ders kapsamında hazırlanan Türkçe uyarlamamız; Bölüm 2 — NumPy)

### Amaç

Ders kapsamında yukarıdaki kaynakların NumPy bölümü üzerinden anlatılan konuları kendi gözünüzden, kendi dilinizle not haline getirmek. Referans olarak orijinal İngilizce kitabı veya ders için hazırladığımız [Türkçe PDS Handbook](https://gusanmaz.github.io/bdt/pds-handbook/index.html) sürümünü kullanabilirsiniz.

### Beklentiler

- Kaynaklardaki notebook veya sayfaları **kopyalamayın**; kendi NumPy notlarınızı oluşturun.
- Farklı kodlar deneyin, kendi örneklerinizi yazın.
- Her NumPy konusuna değinmek zorunda değilsiniz; **önemli bulduğunuz konulara odaklanabilirsiniz**.
- **Yapay zeka kullanılamaz.**

### Teslim Edilecekler

| Dosya/Klasör | Açıklama | Zorunlu? |
|--------------|----------|----------|
| `*.ipynb` | Kendi NumPy notlarınız (açıklamalar + kod hücreleri) | ✅ |

Notebook'un başında veya uygun bir hücrede **ad, soyad, öğrenci numarası** ve grup üyeleri belirtilmelidir.

---

## GitHub Classroom ile Teslim

1. İlgili ödevin davet linkine tıklayın ve GitHub Classroom üzerinden repo oluşturun.
2. Çalışmalarınızı repoya **commit** ve **push** edin.
3. Son teslim tarihinden **sonraki commit'ler değerlendirmeye alınmayacaktır**.

| Ödev | Davet Linki |
|------|-------------|
| Ödev 1 | https://classroom.github.com/a/FODBhjUj |
| Ödev 2 | https://classroom.github.com/a/8cz9U_sc |
| Ödev 3 | https://classroom.github.com/a/twiY3bdy |

---

## Alternatif Teslim Yöntemi (E-posta)

Bazı öğrenciler GitHub Classroom davet linki ile repo oluştururken hata aldıklarını bildirmişlerdir. Bu durumdaki öğrenciler aşağıdaki yöntemi kullanabilir:

### Kimler kullanabilir?

Yalnızca **GitHub üzerinden teslim edemediği ödevleri** e-posta ile gönderebilirsiniz. GitHub'dan başarıyla teslim ettiğiniz ödevleri tekrar e-posta ile göndermenize gerek yoktur.

### Nasıl gönderilir?

1. Her ödev için **ayrı bir klasör** oluşturun (ör. `odev1/`, `odev2/`, `odev3/`).
2. İlgili ödev dosyalarını bu klasöre koyun.
3. Klasörü **zip** dosyası haline getirin.
4. GitHub'da aldığınız **hata mesajının ekran görüntüsünü** ekleyin.
5. **30 Mayıs 2026, 23:59**'dan önce **guvencu@anadolu.edu.tr** adresine e-posta ile gönderin.

### Önemli farklar

| | GitHub | E-posta |
|---|--------|---------|
| Grup teslimi | Gruptan **bir kişi** commit etmesi yeterli | Grubun **her üyesi ayrı ayrı** e-posta göndermeli |
| Hata kanıtı | Gerekmez | GitHub hata ekran görüntüsü **zorunlu** |
| Kapsam | Tüm ödevler | Yalnızca GitHub'dan gönderilemeyen ödevler |

---

## Özet Kontrol Listesi

### Ödev 1
- [ ] GitHub Classroom reposu oluşturuldu veya e-posta ile gönderildi
- [ ] `README.md` — ad, soyad, öğrenci no, grup üyeleri, hipotez, özet
- [ ] Analiz kodu (`analiz.ipynb` veya `.py`)
- [ ] Rapor (`rapor.md` veya `rapor.pdf`)
- [ ] Sunum dosyası (`sunum.pptx` veya `sunum.pdf`)
- [ ] Veri seti (varsa)

### Ödev 2 (isteğe bağlı)
- [ ] GitHub Classroom reposu oluşturuldu veya e-posta ile gönderildi
- [ ] Tek bir Jupyter Notebook — kod, proje fikri ve sonuçlar hücrelerde
- [ ] Ad, soyad, öğrenci no notebook içinde
- [ ] Gerekli ek dosyalar (varsa)

### Ödev 3 (zorunlu)
- [ ] GitHub Classroom reposu oluşturuldu veya e-posta ile gönderildi
- [ ] Kendi NumPy notları — kopya değil, kendi örnekleriniz
- [ ] Ad, soyad, öğrenci no notebook içinde
- [ ] Yapay zeka kullanılmadı

---

## İletişim

Sorularınız için: **guvencu@anadolu.edu.tr**
