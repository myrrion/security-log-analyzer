# 🛡️ Security Log Analyzer (Siber Güvenlik Log Analizcisi)

Bu proje, yapay zeka ve veri bilimi teknikleri kullanılarak siber güvenlik loglarının analiz edilmesini sağlayan bir Python aracıdır. Rastgele oluşturulan saldırı senaryoları üzerinden risk analizi yapar ve görsel raporlar sunar.

## 🚀 Özellikler

* **Veri Simülasyonu:** DDoS, Phishing, Malware gibi 6 farklı saldırı türü için gerçekçi log verisi üretir.
* **Akıllı Temizlik:** Eksik veya hatalı verileri (NaN) tespit eder ve istatistiksel yöntemlerle (ortalama değer atama) onarır.
* **Görsel Raporlama:**
    * 📊 Saldırı türlerinin dağılımı ve engellenme oranları.
    * 📈 Risk puanlarının histogram analizi.
    * 📦 Saldırı türlerine göre risk aralıkları (Boxplot).

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **Pandas:** Veri manipülasyonu ve temizliği.
* **Seaborn & Matplotlib:** Veri görselleştirme.
* **Random:** Stokastik veri üretimi.

## 💻 Nasıl Çalıştırılır?

1.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pandas seaborn matplotlib
    ```
2.  Projeyi çalıştırın:
    ```bash
    python security_log_analyzer.py
    ```

## 📈 Örnek Analiz Çıktısı

Proje çalıştırıldığında `temiz_guvenlik_loglari.csv` adında temizlenmiş bir veri seti oluşturur ve saldırı analiz grafiklerini ekrana yansıtır (veya `png` olarak kaydeder).

---
*Geliştirici: [Muhammed Emir Tohumcu/Myrrion]*