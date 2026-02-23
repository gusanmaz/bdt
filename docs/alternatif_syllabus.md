# BÜYÜK VERİ TEKNOLOJİLERİ — Alternatif Ders İçeriği (2025–2026)

| | |
|---|---|
| **Dersin Adı** | Büyük Veri Teknolojileri |
| **Dersin Saati** | 2+2 (Teori + Uygulama) |
| **Dersin AKTS** | 4 |
| **Dil/Araç** | Python (temel araç), Google Colab / Jupyter Notebook |
| **Hedef Kitle** | Temel Python bilgisi olan, veritabanı ve ileri programlama deneyimi sınırlı öğrenciler |

---

## Dersin Amacı

Öğrencilerin büyük veri kavramını, temel teknolojilerini ve ekosistemini **Python ekseninde**, seviyelerine uygun şekilde öğrenmelerini sağlamak. Öğrenciler dönem sonunda veri toplama, depolama, işleme, analiz ve görselleştirme süreçlerini uçtan uca deneyimlemiş olacaklar.

---

## Öğrenme Çıktıları

| | |
|---|---|
| **ÖÇ1** | Büyük veri kavramını, V'lerini ve ekosistemini açıklayabilir |
| **ÖÇ2** | Python ile veri okuma, temizleme ve dönüştürme işlemleri yapabilir |
| **ÖÇ3** | Temel veritabanı (SQL ve NoSQL) kavramlarını anlayabilir ve basit sorgular yazabilir |
| **ÖÇ4** | Büyük veri araçlarını (Spark, Kafka vb.) kavramsal düzeyde tanır, PySpark ile temel işlemler yapabilir |
| **ÖÇ5** | Veri görselleştirme ve temel analitik uygulamalar gerçekleştirebilir |

---

## Haftalık İçerik

### 📌 Hafta 1 — Python Hatırlatma ve Veri Dünyasına Giriş
**Teori:**
- Dersin tanıtımı, beklentiler ve değerlendirme
- Veri nedir? Veri türleri ve veri hiyerarşisi (veri → bilgi → bilgelik)
- Büyük veriye neden ihtiyaç duyuyoruz? Günlük hayattan örnekler

**Uygulama:**
- Python tekrarı: değişkenler, listeler, döngüler, fonksiyonlar
- Basit veri yapıları ile küçük örnekler (liste, sözlük)
- Jupyter Notebook / Google Colab kullanımına giriş

> *Neden:* Öğrencilerin Python temelleri zayıf; ilk hafta hem ısınma hem motivasyon.

---

### 📌 Hafta 2 — Veri Yapıları Tekrarı ve Dosya İşlemleri
**Teori:**
- Python'da temel veri yapıları: list, dict, set, tuple
- Dosya okuma/yazma (txt, CSV)

**Uygulama:**
- CSV dosyasından veri okuma (built-in `csv` modülü)
- Basit veri filtreleme ve dönüştürme örnekleri
- Sözlük (dict) ile basit veri modelleme

> *Neden:* Veri yapıları dersi gördüler ama pratikte zayıflar; dosya işlemleri büyük veri pipeline'ının ilk adımı.

---

### 📌 Hafta 3 — Veri Modelleme ve Pandas'a Giriş
**Teori:**
- Veri modelleme nedir? Kavramsal, mantıksal, fiziksel modeller (yüzeysel)
- Yapılandırılmış vs yapılandırılmamış veri
- Pandas kütüphanesine giriş: DataFrame ve Series kavramları

**Uygulama:**
- `pandas` ile CSV okuma, ilk keşif (`head()`, `info()`, `describe()`)
- Sütun seçme, filtreleme, sıralama
- Basit istatistiksel özet çıkarma

---

### 📌 Hafta 4 — Veri Temizleme ve Dönüştürme
**Teori:**
- Veri kalitesi nedir? Eksik veri, tutarsız veri, aykırı değerler
- Veri temizleme süreci ve önemi
- ETL kavramına giriş (Extract, Transform, Load — yüzeysel)

**Uygulama:**
- Pandas ile eksik veri tespiti ve doldurma (`fillna`, `dropna`)
- Veri tipi dönüşümleri, string işlemleri
- `groupby`, `merge`, `pivot_table` ile veri dönüştürme

---

### 📌 Hafta 5 — Veri Görselleştirme
**Teori:**
- Veri görselleştirme neden önemli?
- Görselleştirme türleri ve ne zaman hangisi kullanılır
- Matplotlib ve Seaborn kütüphanelerine giriş

**Uygulama:**
- Çubuk grafik, histogram, scatter plot, pie chart
- Seaborn ile daha estetik grafikler
- Gerçek bir veri seti üzerinde keşifsel veri analizi (EDA) uygulaması

---

### 📌 Hafta 6 — Veritabanlarına Giriş: SQL Temelleri
**Teori:**
- Veritabanı nedir? İlişkisel veritabanı kavramı
- Tablo, satır, sütun, birincil anahtar, yabancı anahtar
- SQL nedir? Temel SQL komutları

**Uygulama:**
- SQLite ile Python'da veritabanı oluşturma (`sqlite3` modülü)
- `CREATE TABLE`, `INSERT`, `SELECT`, `WHERE`, `ORDER BY`
- Pandas ile SQL sorgu sonuçlarını DataFrame'e aktarma

> *Neden:* SQL bilmiyorlar; büyük veri ekosisteminin temeli olan veritabanını burada öğretmek şart.

---

### 📌 Hafta 7 — NoSQL ve MongoDB'ye Giriş
**Teori:**
- SQL vs NoSQL: Farklar, avantajlar, kullanım alanları
- Doküman tabanlı veritabanı kavramı
- MongoDB nedir? Temel kavramlar (collection, document, BSON)

**Uygulama:**
- MongoDB Atlas (ücretsiz cloud) kurulumu
- Python `pymongo` ile bağlantı, veri ekleme, sorgulama
- Basit CRUD işlemleri

---

### 📌 Hafta 8 — ARA SINAV + Büyük Veri Kavramları
**Teori (sınav sonrası kısa ders):**
- Büyük Veri nedir? 5V (Volume, Velocity, Variety, Veracity, Value)
- Büyük veri vs geleneksel veri
- Büyük veri ekosistemi haritası: genel bakış

**Uygulama:**
- **Ara Sınav** (Hafta 1-7 arası konular)

> *Not:* Ara sınav bu haftada yapılarak öğrencilerin temel konuları pekiştirmesi sağlanır. Sınav sonrası büyük veri dünyasına geçiş yapılır.

---

### 📌 Hafta 9 — Dağıtık Sistemler ve Hadoop'a Giriş
**Teori:**
- Dağıtık sistemler nedir? Neden ihtiyaç duyulur?
- Hadoop ekosistemi: HDFS, MapReduce, YARN (kavramsal)
- Hadoop'un tarihçesi ve günümüzdeki yeri

**Uygulama:**
- MapReduce mantığını Python ile simüle etme (word count örneği)
- `map()`, `reduce()` fonksiyonları ile paralel işleme konsepti
- Küçük ölçekli dağıtık hesaplama demo

> *Neden:* Hadoop kurulumu karmaşık; kavramsal anlat, Python ile mantığını göster.

---

### 📌 Hafta 10 — Apache Spark ve PySpark'a Giriş
**Teori:**
- Apache Spark nedir? Hadoop ile farkları
- Spark mimarisi: Driver, Executor, RDD, DataFrame
- Lazy evaluation kavramı

**Uygulama:**
- Google Colab'da PySpark kurulumu
- RDD oluşturma ve temel dönüşümler (`map`, `filter`, `flatMap`)
- PySpark DataFrame'e giriş: CSV okuma, `select`, `filter`, `show`

---

### 📌 Hafta 11 — PySpark ile Veri Analizi
**Teori:**
- Spark SQL kavramı
- DataFrame API vs SQL API
- Spark'ta `groupBy`, `agg`, `join` işlemleri

**Uygulama:**
- PySpark SQL ile sorgulama (`createOrReplaceTempView`)
- GroupBy, aggregation örnekleri
- Gerçek bir veri seti üzerinde analiz projesi (örn. e-ticaret, uçuş verisi)

---

### 📌 Hafta 12 — Gerçek Zamanlı Veri Akışı (Streaming) Kavramları
**Teori:**
- Batch processing vs Stream processing
- Apache Kafka nedir? Temel kavramlar (topic, producer, consumer)
- Spark Streaming / Structured Streaming kavramı

**Uygulama:**
- Kafka kavramsal demo (docker ile basit örnek veya simülasyon)
- Python ile basit bir producer-consumer simülasyonu (soket veya kuyruk ile)
- Gerçek zamanlı veri akışı senaryoları tartışma

> *Neden:* Kafka kurulumu ağır olabilir; kavramsal + hafif demo yeterli bu seviye için.

---

### 📌 Hafta 13 — Büyük Veri ile Makine Öğrenmesine Giriş
**Teori:**
- Makine öğrenmesi nedir? Temel kavramlar
- Denetimli öğrenme: Regresyon ve sınıflandırma
- Büyük veride ML: Spark MLlib kavramı (yüzeysel)

**Uygulama:**
- Scikit-learn ile basit bir Linear Regression örneği
- Train/test split, model değerlendirme (R², RMSE)
- PySpark MLlib ile basit bir örnek (opsiyonel, zaman kalırsa)

---

### 📌 Hafta 14 — Bulut Ortamları ve Büyük Veri Güvenliği
**Teori:**
- Bulut bilişim nedir? IaaS, PaaS, SaaS
- Büyük veri için bulut çözümleri: AWS, GCP, Azure (tanıtım düzeyinde)
- Veri güvenliği ve gizliliği: KVKK/GDPR, veri anonimleştirme, erişim kontrolü

**Uygulama:**
- Databricks Community Edition ile PySpark denemesi
- Google Colab üzerinde bulut tabanlı veri analizi
- Veri güvenliği senaryoları tartışma

---

### 📌 Hafta 15 — Dönem Projesi Sunumları ve Genel Değerlendirme
**Teori:**
- Büyük veri ekosistemi genel tekrar
- Sektörlerde büyük veri kullanımları: e-ticaret, finans, sağlık, sosyal medya
- Kariyer yolları ve öğrenme kaynakları

**Uygulama:**
- Öğrenci projelerinin sunumu
- Dönemin değerlendirmesi ve geri bildirim

---

## Proje Ödevi (Dönem Boyunca)

Öğrenciler 2-3 kişilik gruplar halinde bir **uçtan uca veri projesi** gerçekleştirecekler:

1. Bir veri kaynağı seçme (Kaggle, açık veri portalları, web scraping)
2. Veriyi temizleme ve dönüştürme (Pandas)
3. Veritabanına kaydetme (SQLite veya MongoDB)
4. Analiz ve görselleştirme
5. (Bonus) PySpark ile büyük ölçekli analiz denemesi
6. Sunumla raporlama

---

## Değerlendirme Sistemi

| Etkinlik | Katkı Yüzdesi |
|---|---|
| Derse Katılım & Haftalık Uygulamalar | %10 |
| Ara Sınav | %25 |
| Dönem Projesi | %25 |
| Final Sınavı | %40 |

---

## Kullanılacak Araçlar ve Teknolojiler

| Araç | Kullanım Amacı |
|---|---|
| **Python 3.x** | Ana programlama dili |
| **Jupyter Notebook / Google Colab** | İnteraktif kodlama ortamı |
| **Pandas** | Veri işleme ve analiz |
| **Matplotlib / Seaborn** | Veri görselleştirme |
| **SQLite** | İlişkisel veritabanı temelleri |
| **MongoDB Atlas + PyMongo** | NoSQL veritabanı |
| **PySpark (Colab)** | Dağıtık veri işleme |
| **Scikit-learn** | Temel makine öğrenmesi |
| **Databricks Community** | Bulut tabanlı Spark ortamı |

---

## Önerilen Kaynaklar

- *Python for Data Analysis* — Wes McKinney
- *Learning Spark, 2nd Edition* — O'Reilly
- Kaggle Learn (ücretsiz modüller)
- Databricks Academy (ücretsiz kurslar)
- MongoDB University (ücretsiz kurslar)

---

## Tasarım Felsefesi — Neden Bu İçerik?

| Mevcut Syllabus Konusu | Bu İçerikteki Karşılığı | Açıklama |
|---|---|---|
| Hadoop HDFS, Cloudera | Hafta 9 (Kavramsal) | Kurulum yerine mantık anlatımı, Python simülasyonu |
| Veri Modelleme | Hafta 3 (Yüzeysel) | Kavramsal-mantıksal-fiziksel model kısaca |
| Big Data & V'leri | Hafta 8 | Motivasyon ve büyük resim |
| Spark (Java) | Hafta 10-11 (PySpark) | Java yerine Python ile |
| MongoDB (Java) | Hafta 7 (PyMongo) | Python ile CRUD |
| Elasticsearch/Kafka | Hafta 12 (Kavramsal) | Ağır kurulum yerine kavram + demo |
| ML / MLlib | Hafta 13 | Scikit-learn + yüzeysel MLlib |
| Veri Görselleştirme | Hafta 5 | Matplotlib/Seaborn |
| Veri Güvenliği | Hafta 14 | KVKK/GDPR odaklı teorik |
| Bulut Çözümleri | Hafta 14 | Databricks/Colab pratik |
| Veri Kalitesi/Temizleme | Hafta 4 | Pandas ile uygulamalı |
| SQL/Veritabanı | Hafta 6 | Sıfırdan SQLite ile |
| Sektörel Uygulamalar | Hafta 15 | Proje sunumları ile |

> ⚠️ **Önemli Not:** Öğrenci seviyesi göz önüne alındığında, ilk 7 hafta tamamen **temel hazırlık** olarak tasarlanmıştır. Büyük veri spesifik konular Hafta 8'den itibaren başlar. Bu yaklaşım, öğrencilerin "büyük veri" kavramını gerçekten anlayabilmesi için gerekli altyapıyı sağlamayı hedefler.
