# BÜYÜK VERİ TEKNOLOJİLERİ — Alternatif Syllabus v2

> **Güncelleme:** Bu versiyon, resmi syllabus'taki 15 haftalık konu başlıklarına mümkün olduğunca sadık kalarak, öğrenci seviyesine uygun bir şekilde yeniden yapılandırılmıştır. Ders 2+3 (5 AKTS), Python ağırlıklıdır. **Sınav haftalarında ders işlenmez.**

---

| | |
|---|---|
| **Dersin Adı** | Büyük Veri Teknolojileri |
| **Dersin Saati** | 2+3 (Teori + Uygulama) |
| **Dersin AKTS** | 5 |
| **Dil/Araç** | Python · Jupyter/Colab · PySpark · Pandas |
| **Ön Koşul Seviye** | Temel Python (değişken, döngü, liste, fonksiyon) |

---

## ⚖️ Yasal Mevzuat ve Disiplin

Bu ders kapsamındaki tüm sınavlar, ödevler ve projeler **2547 sayılı Yükseköğretim Kanunu** ve ilgili yönetmelikler çerçevesinde değerlendirilir.

> 📄 **2547 Sayılı Yükseköğretim Kanunu:**  
> [https://cdn.anadolu.edu.tr/files/anadolu-cms/7gldkYw1/file/2547-sayili-yuksekogretim-kanunu-3befcc7ff61806b0.pdf](https://cdn.anadolu.edu.tr/files/anadolu-cms/7gldkYw1/file/2547-sayili-yuksekogretim-kanunu-3befcc7ff61806b0.pdf)

### 🚨 Kopya ve Akademik Dürüstlük

Sınavlarda, ödevlerde ve proje çalışmalarında **kopya çekmek, kopya vermek veya buna teşebbüs etmek** disiplin suçudur. Bu tür durumlar, **Yükseköğretim Kurumları Öğrenci Disiplin Yönetmeliği** kapsamında işlem görür.

- 📌 Sınavda kopya çekenler veya verenler hakkında tutanak tutulur ve ilgili sınav **geçersiz** sayılır.
- 📌 Kopya fiili, yönetmeliğe göre **kınama** veya daha ağır disiplin cezalarına yol açabilir.
- 📌 Tekrarlayan durumlarda **uzaklaştırma** cezası uygulanabilir.
- 📌 Ödev ve projelerde **intihal (plagiarism)** tespit edilmesi de aynı kapsamda değerlendirilir.

> ⚠️ **Öğrencilerin sorumluluğu:** Tüm öğrenciler, kayıtlı oldukları üniversitenin **öğrenci disiplin yönetmeliği**ni okumuş ve kabul etmiş sayılır. Disiplin işleri hakkında detaylı bilgi için üniversitenizin öğrenci işleri birimine başvurunuz.

---

## Resmi Syllabus ile Eşleştirme Stratejisi

Resmi syllabus'ta her hafta "Gelişmiş" ibaresiyle başlayan ağır başlıklar var. Öğrenci profiline bakıldığında bunları olduğu gibi anlatmak mümkün değil. Strateji şu:

1. **Her haftanın resmi başlığı korunuyor** — böylece syllabus uyumu sağlanıyor
2. **İçerik öğrenci seviyesine göre seviyelendiriliyor** — "gelişmiş" konular "giriş + temel uygulama" olarak planlanıyor
3. **İlk 2 hafta rampa** — Python ve veri temellerini tazeleyerek öğrencileri hazırlıyor
4. **3 saatlik uygulama** avantajı kullanılıyor — her hafta elle tutulur bir lab/proje var
5. **Java yerine Python** — tüm araç entegrasyonları Python kütüphaneleriyle

---

## Haftalık İçerik

---

### Hafta 1 — Gelişmiş Dağıtık Sistemler
*Resmi başlık korunuyor; öğrenciye "dağıtık sistem nedir" seviyesinden başlanıyor*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Dersin tanıtımı, araçlar, değerlendirme | Python & Jupyter/Colab hatırlatma |
| Dağıtık sistem nedir? Tek makine vs çok makine | Temel Python tekrarı: list, dict, döngü, fonksiyon |
| Hadoop ekosistemi: HDFS, MapReduce, YARN (kavramsal) | Python `map()`, `filter()`, `reduce()` ile MapReduce simülasyonu |
| Günümüzde dağıtık sistemler: neden bulut, neden Spark? | Word Count örneği: önce saf Python, sonra mantığı açıklama |

**Lab Çıktısı:** Python ile basit bir MapReduce word count uygulaması

---

### Hafta 2 — Gelişmiş Veri Modelleme
*"Gelişmiş" yerine "veri modellemeye giriş" seviyesinde; veri kavramından başlanıyor*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veri hiyerarşisi: veri → bilgi → bilgelik | CSV/JSON dosya okuma-yazma (Python built-in) |
| Veri türleri: yapılandırılmış, yarı-yapılandırılmış, yapılandırılmamış | Pandas'a giriş: `read_csv`, `head()`, `info()`, `describe()` |
| Kavramsal, mantıksal, fiziksel veri modeli (genel bakış) | DataFrame üzerinde sütun seçme, filtreleme, sıralama |
| Veri modeli diyagramı fikri (ER diyagramı tanıtım) | Basit bir veri seti keşfi (Kaggle'dan hazır veri) |

**Lab Çıktısı:** Bir CSV veri setini Pandas ile yükleyip temel keşif raporu

---

### Hafta 3 — Gelişmiş Veri İşleme Çerçeveleri
*Spark'ı "gelişmiş çerçeve" olarak tanıtım; PySpark ile ilk temas*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veri işleme nedir? Batch vs Stream kavramı | Pandas ile veri temizleme: eksik veri, tip dönüşümü |
| Apache Spark nedir? Neden Hadoop'tan hızlı? | Google Colab'da PySpark kurulumu |
| Spark mimarisi: Driver, Executor, RDD, DataFrame | İlk PySpark uygulaması: CSV okuma, `show()`, `select()` |
| Lazy evaluation kavramı | Pandas vs PySpark karşılaştırma: aynı işlemi ikisinde yapma |

**Lab Çıktısı:** Colab'da PySpark ile bir veri setini okuyup temel işlemler

---

### Hafta 4 — Ölçeklenebilir Veri Depolama Çözümleri
*SQL ve NoSQL'e giriş; öğrenciler veritabanını bilmiyor, sıfırdan başlanıyor*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veritabanı nedir? Neden dosya yerine veritabanı? | SQLite ile Python'da ilk veritabanı (`sqlite3`) |
| İlişkisel veritabanı: tablo, satır, sütun, PK, FK | `CREATE TABLE`, `INSERT`, `SELECT`, `WHERE`, `ORDER BY` |
| SQL vs NoSQL farkları ve kullanım alanları | MongoDB Atlas (ücretsiz) hesap açma ve tanıtım |
| NoSQL türleri: doküman, anahtar-değer, sütun, graf | `pymongo` ile MongoDB'ye bağlanma ve ilk CRUD |

**Lab Çıktısı:** Aynı veriyi hem SQLite'a hem MongoDB'ye yazıp okuma

---

### Hafta 5 — Gerçek Zamanlı Veri Akışı
*Kafka ve Streaming kavramsal düzeyde; ağır kurulum yerine Python simülasyonu*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Batch processing vs Real-time/Stream processing | Python `queue` modülü ile producer-consumer simülasyonu |
| Apache Kafka: topic, partition, producer, consumer (kavramsal) | Basit soket programlama ile anlık veri akışı demo |
| Spark Streaming / Structured Streaming kavramı | (Opsiyonel) Docker ile basit Kafka demo |
| Kullanım alanları: IoT, log analizi, finansal veriler | Gerçek zamanlı veri akışı senaryosu tasarlama (kâğıt üstü) |

**Lab Çıktısı:** Python ile producer-consumer simülasyonu + senaryo tasarımı

---

### Hafta 6 — Gelişmiş Veri Analiz Teknikleri
*Makine öğrenmesine giriş; Scikit-learn ile temel örnekler*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veri analizi nedir? Keşifsel veri analizi (EDA) | Pandas ile EDA: `groupby`, `value_counts`, `corr` |
| Makine öğrenmesine giriş: denetimli / denetimsiz | Scikit-learn ile Linear Regression (basit örnek) |
| Regresyon vs Sınıflandırma kavramı | Train/Test split, model eğitme, tahmin yapma |
| Spark MLlib tanıtımı (kavramsal) | Model değerlendirme: R², RMSE |

**Lab Çıktısı:** Bir veri seti üzerinde basit bir regresyon modeli

---

### Hafta 7 — Büyük Veri Altyapı Yönetimi
*Büyük veri ekosistemi, V'ler, araçlar haritası — "büyük resim" haftası*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Büyük Veri nedir? 5V: Volume, Velocity, Variety, Veracity, Value | Gerçek bir büyük veri senaryosu analizi (case study) |
| Büyük veri ekosistemi haritası: ingestion → storage → processing → analysis | PySpark ile daha büyük veri seti üzerinde `groupBy`, `agg` |
| Araçlar: Hadoop, Spark, Kafka, Hive, Airflow... ne işe yarar? | PySpark SQL: `createOrReplaceTempView`, SQL sorguları |
| Altyapı seçimi: on-premise vs cloud | Spark UI kavramsal tanıtım |

**Lab Çıktısı:** PySpark SQL ile bir veri seti üzerinde analitik sorgular

---

### Hafta 8 — ARA SINAV
*Bu hafta ders işlenmez. Tüm ders saati sınav için ayrılmıştır.*

| Bölüm | İçerik |
|---|---|
| **Ara Sınav (5 saat)** | Hafta 1-7 konuları (Python, Pandas, SQL, PySpark temelleri, kavramlar) |

**Sınav Formatı:** Yazılı ve/veya bilgisayar ortamında (lab sınavı). Ayrıntılar sınav öncesi duyurulacaktır.

> ⚠️ Sınavda kopya çekme/verme disiplin suçudur (bkz. Yasal Mevzuat ve Disiplin bölümü).

---

### Hafta 9 — Gelişmiş Veri Görselleştirme ve Keşif
*Ara sınav sonrası ilk ders; veri görselleştirme ile ikinci yarıya yumuşak geçiş*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veri görselleştirme neden önemli? | Matplotlib ile temel grafikler: bar, line, scatter, hist |
| Grafik türleri ve ne zaman hangisi kullanılır | Seaborn ile estetik grafikler: heatmap, boxplot, pairplot |
| Dashboard kavramı | Plotly ile interaktif grafik (tanıtım) |
| Keşifsel analiz + görselleştirme birlikte | Gerçek veri seti üzerinde EDA + görselleştirme projesi |

**Lab Çıktısı:** Bir veri setinin kapsamlı görsel analiz raporu

---

### Hafta 10 — Büyük Veri Güvenliği ve Gizliliği

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veri güvenliği temel kavramları: CIA üçgeni | Python ile veri anonimleştirme: maskeleme, hashing |
| KVKK ve GDPR nedir? Temel kurallar | `hashlib` ile veri hashleme örneği |
| Kişisel veri, hassas veri, anonimleştirme | MongoDB'de kullanıcı yetkilendirme (Atlas üzerinde) |
| Büyük veri ortamlarında güvenlik zorlukları | Veri erişim kontrol senaryosu tasarlama |

**Lab Çıktısı:** Kişisel veri içeren bir veri setini anonimleştirme uygulaması

---

### Hafta 11 — Bulut Tabanlı Büyük Veri Çözümleri

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Bulut bilişim nedir? IaaS, PaaS, SaaS | Databricks Community Edition kayıt ve kullanım |
| Büyük veri için bulut: AWS EMR, GCP Dataproc, Azure HDInsight (tanıtım) | Databricks'te PySpark notebook çalıştırma |
| Databricks nedir? Neden popüler? | Google Colab vs Databricks karşılaştırma |
| Maliyet, ölçeklenebilirlik, esneklik avantajları | Bulutta bir veri analizi pipeline'ı oluşturma |

**Lab Çıktısı:** Databricks üzerinde uçtan uca bir PySpark analizi

---

### Hafta 12 — Gelişmiş Veri Entegrasyonu ve ETL Süreçleri

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| ETL nedir? Extract – Transform – Load | Python ile basit bir ETL pipeline'ı yazma |
| Veri kaynakları: API, dosya, veritabanı, web scraping | `requests` ile API'den veri çekme (JSON) |
| Veri entegrasyonu zorlukları: format, şema, kalite | Çekilen veriyi temizleme (Pandas) ve veritabanına yazma |
| Apache Airflow / workflow kavramı (tanıtım) | Farklı kaynaklardan veri birleştirme (`merge`, `concat`) |

**Lab Çıktısı:** API → Pandas (temizle) → SQLite/MongoDB pipeline'ı

---

### Hafta 13 — Büyük Veri Yönetişimi, Uyumluluk ve Optimizasyon
*Yönetişim ve performans konuları birleştirilerek ele alınıyor*

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Veri kalitesi: eksiksizlik, tutarlılık, doğruluk, zamanlılık | Veri kalitesi denetimi scripti yazma (Python) |
| Veri yönetişimi: politikalar, standartlar, sorumluluklar | Veri temizleme pipeline'ı: eksik, tutarsız, aykırı veri |
| Performans: partitioning, caching, format karşılaştırma | CSV vs Parquet performans testi |
| Veri ambarı kavramı, metadata yönetimi | Python'da `time` modülü ile performans ölçme |

**Lab Çıktısı:** Kirli veri seti üzerinde kalite kontrol + CSV vs Parquet karşılaştırma raporu

---

### Hafta 14 — Gelişmiş Analitik Uygulamaları

| Teori (2 saat) | Uygulama (3 saat) |
|---|---|
| Sınıflandırma problemi: Naive Bayes, Decision Tree (kavramsal) | Scikit-learn ile bir sınıflandırma uygulaması |
| Metin analizi / NLP'ye giriş (temel kavramlar) | Basit metin ön-işleme: tokenization, stopwords |
| Sentiment analysis kavramı | Hazır bir kütüphane ile basit duygu analizi |
| Sektörlerde büyük veri: e-ticaret, finans, sağlık, sosyal medya | Proje son kontrol ve sunum hazırlığı |

**Lab Çıktısı:** Bir metin veri seti üzerinde basit duygu analizi + proje finalize

---

### Hafta 15 — Proje Sunumları ve Dönem Değerlendirmesi

| Bölüm | İçerik |
|---|---|
| **Proje Sunumları (4 saat)** | Her grup 10-15 dakika sunar + soru-cevap |
| **Dönem Değerlendirmesi (1 saat)** | Dönemin genel değerlendirmesi, kariyer tavsiyeleri, öğrenme yol haritası |

**Not:** Bu hafta normal ders işlenmez, tüm süre proje sunumlarına ayrılmıştır.

---

### Final Sınavı Haftası
*Bu hafta ders işlenmez. Tüm ders saati sınav için ayrılmıştır.*

| Bölüm | İçerik |
|---|---|
| **Final Sınavı** | Tüm dönem konuları (Hafta 1-14) |

**Sınav Formatı:** Yazılı ve/veya bilgisayar ortamında (lab sınavı). Ayrıntılar sınav öncesi duyurulacaktır.

> ⚠️ Sınavda kopya çekme/verme disiplin suçudur (bkz. Yasal Mevzuat ve Disiplin bölümü).

---

## Dönem Projesi (Hafta 4'te Duyuru → Hafta 15'te Sunum)

Öğrenciler **2-3 kişilik gruplar** halinde bir **uçtan uca veri projesi** yapacaklar:

| Aşama | Açıklama | İlgili Haftalar |
|---|---|---|
| 1. Veri Toplama | Kaggle, açık veri, API veya web scraping ile veri toplama | 2, 12 |
| 2. Veri Depolama | SQLite veya MongoDB'ye kaydetme | 4 |
| 3. Veri Temizleme | Eksik/hatalı veri, tip dönüşümü, standartlaştırma | 2, 13 |
| 4. Veri Analizi | Pandas ve/veya PySpark ile analiz | 3, 6, 7 |
| 5. Görselleştirme | Matplotlib/Seaborn ile görsel rapor | 9 |
| 6. (Bonus) ML Modeli | Basit bir tahmin veya sınıflandırma modeli | 6, 14 |
| 7. Sunum | 10-15 dakikalık sunum + rapor | 15 |

---

## Değerlendirme Sistemi

| Etkinlik | Katkı Yüzdesi |
|---|---|
| Derse Katılım & Haftalık Lab Çalışmaları | %10 |
| Ara Sınav (Hafta 8) | %25 |
| Dönem Projesi (Hafta 15) | %25 |
| Final Sınavı | %40 |

---

## Kullanılacak Araç ve Teknolojiler

| Kategori | Araç | Amaç |
|---|---|---|
| **Programlama** | Python 3.x | Ana dil |
| **Ortam** | Jupyter Notebook / Google Colab | İnteraktif kodlama |
| **Veri İşleme** | Pandas, NumPy | Veri temizleme ve analiz |
| **Büyük Veri** | PySpark (Colab/Databricks) | Dağıtık veri işleme |
| **Veritabanı** | SQLite (`sqlite3`) | İlişkisel veritabanı temelleri |
| **NoSQL** | MongoDB Atlas + `pymongo` | Doküman tabanlı veritabanı |
| **Görselleştirme** | Matplotlib, Seaborn, Plotly | Grafik ve dashboard |
| **ML** | Scikit-learn | Temel makine öğrenmesi |
| **Bulut** | Databricks Community Edition | Bulut tabanlı Spark |
| **Diğer** | `requests`, `hashlib` | API, güvenlik örnekleri |

---

## Resmi Syllabus Eşleştirme Tablosu

| Hafta | Resmi Syllabus Başlığı | Bu Alternatifteki Yaklaşım | Seviye |
|---|---|---|---|
| 1 | Gelişmiş Dağıtık Sistemler | Dağıtık sistem kavramı + Python MapReduce simülasyonu | Giriş |
| 2 | Gelişmiş Veri Modelleme | Veri hiyerarşisi, veri türleri, Pandas'a giriş | Giriş |
| 3 | Gelişmiş Veri İşleme Çerçeveleri | Spark tanıtım + PySpark ilk adımlar | Giriş-Orta |
| 4 | Ölçeklenebilir Veri Depolama Çözümleri | SQL temelleri (SQLite) + NoSQL giriş (MongoDB) | Giriş |
| 5 | Gerçek Zamanlı Veri Akışı | Kafka kavramsal + Python producer-consumer simülasyonu | Kavramsal |
| 6 | Gelişmiş Veri Analiz Teknikleri | EDA + Scikit-learn ile temel ML | Giriş-Orta |
| 7 | Büyük Veri Altyapı Yönetimi | 5V, ekosistem haritası, PySpark SQL | Orta |
| **8** | **ARA SINAV** | **Ders yapılmaz — Hafta 1-7 konularından sınav** | **Sınav** |
| 9 | Gelişmiş Veri Görselleştirme ve Keşif | Matplotlib/Seaborn/Plotly ile EDA | Giriş-Orta |
| 10 | Büyük Veri Güvenliği ve Gizliliği | KVKK/GDPR, anonimleştirme, hashing | Giriş |
| 11 | Bulut Tabanlı Büyük Veri Çözümleri | Databricks, bulut kavramları, bulutta PySpark | Giriş-Orta |
| 12 | Gelişmiş Veri Entegrasyonu ve ETL | Python ile ETL pipeline, API veri çekme | Orta |
| 13 | Yönetişim + Optimizasyon | Veri kalitesi, performans, CSV vs Parquet | Giriş-Orta |
| 14 | Gelişmiş Analitik Uygulamaları | Sınıflandırma, metin analizi, duygu analizi | Orta |
| 15 | Proje Sunumları | Öğrenci proje sunumları + dönem değerlendirmesi | Genel |
| **Final** | **FİNAL SINAVI** | **Ders yapılmaz — Hafta 1-14 konularından sınav** | **Sınav** |

---

## v1 ile v2 Arasındaki Farklar

| Özellik | Alternatif v1 | Alternatif v2 |
|---|---|---|
| **Syllabus uyumu** | Kendi başlıklarını oluşturuyordu | Resmi syllabus başlıklarını birebir koruyor |
| **Ders saati** | 2+2 (4 AKTS) | 2+3 (5 AKTS) — daha fazla lab zamanı |
| **İlk yarı** | 7 hafta tamamen temel hazırlık | Temeller var ama resmi konuları da kapsıyor |
| **Büyük veri konuları** | 8. haftadan sonra başlıyordu | 1. haftadan itibaren (kavramsal da olsa) büyük veri var |
| **Ara sınav** | Ayrı hafta | 8. hafta tamamen sınava ayrılmış (ders yok) |
| **Kazanımlar** | Kendi ÖÇ'leri | Resmi ÖÇ'lere (ÖÇ1-ÖÇ5) uyumlu |

---

> 💡 **Temel Felsefe:** Resmi syllabus'un her haftalık başlığına sadık kal, ama içeriği öğrenci seviyesine göre "giriş" seviyesinde anlat. "Gelişmiş" konuları kavramsal düzeyde tanıt, Python ile elle tutulur örneklerle destekle. Böylece hem resmi uyumluluk sağlanır hem de öğrenciler gerçekten bir şey öğrenmiş olur.
