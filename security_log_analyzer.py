import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random as rnd


# --- 1. VERİ ÜRETİM FONKSİYONU ---
def veri_olustur(kayit_sayisi):
    """
    Belirtilen sayıda rastgele siber güvenlik log verisi üretir.
    """
    saldiri_turleri = ["DDoS", "Phishing", "Malware", "SQL Injection", "Brute Force", "XSS"]
    ip_listesi = ["192.168.1.1", "10.0.0.5", "172.16.0.3", "192.168.0.45", "10.1.1.20"]

    # Python List Comprehension ile hızlı veri üretimi
    veriler = {
        "IP Adresleri": rnd.choices(ip_listesi, k=kayit_sayisi),
        "Saldırı Türleri": rnd.choices(saldiri_turleri, k=kayit_sayisi),
        "Engellendi Mi": rnd.choices([True, False], k=kayit_sayisi),
        "Risk Puanları": []
    }

    # Risk puanlarında %15 eksik veri (NaN) simülasyonu
    for _ in range(kayit_sayisi):
        if rnd.random() < 0.15:
            veriler["Risk Puanları"].append(None)
        else:
            veriler["Risk Puanları"].append(rnd.randint(10, 100))

    return pd.DataFrame(veriler)


# --- 2. VERİ TEMİZLİK FONKSİYONU ---
def veri_temizle(df):
    """
    Eksik verileri doldurur ve veri tiplerini düzeltir.
    """
    # Eksik risk puanlarını ortalama ile doldurma (Imputation)
    risk_ort = df["Risk Puanları"].mean()
    df["Risk Puanları"] = df["Risk Puanları"].fillna(risk_ort)

    # Risk puanını tam sayıya (int) çevirme
    df["Risk Puanları"] = df["Risk Puanları"].astype(int)

    return df


# --- 3. GÖRSELLEŞTİRME FONKSİYONU ---
def veri_gorsellestir(df):
    """
    Veriyi analiz eder ve 3 temel grafik çizer.
    """
    sns.set_style("whitegrid")  # Arka planı ızgaralı yapalım, şık dursun

    # Grafik 1: Saldırı Türleri ve Engellenme Durumu
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Saldırı Türleri", hue="Engellendi Mi", data=df, palette="viridis")
    plt.title("Saldırı Türlerine ve Engellenme Durumuna Göre Dağılım")
    plt.savefig("saldırı_türleri_engelleme_durumu.png")
    plt.show()

    # Grafik 2: Risk Puanı Dağılımı (Histogram)
    plt.figure(figsize=(10, 6))
    sns.histplot(x="Risk Puanları", data=df, kde=True, color="darkred")
    plt.title("Risk Puanı Dağılımı ve Yoğunluğu")
    plt.savefig("risk_dagilimi.png")
    plt.show()

    # Grafik 3: Saldırı Türü ve Risk İlişkisi (Boxplot)
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Saldırı Türleri", y="Risk Puanları", data=df, palette="coolwarm", hue="Saldırı Türleri", legend=False)
    plt.title("Hangi Saldırı Türü Daha Riskli?")
    plt.savefig("saldiri_turleri.png")
    plt.show()


# --- ANA PROGRAM AKIŞI ---
if __name__ == "__main__":
    print("--- Siber Güvenlik Log Analiz Aracı Başlatılıyor ---")

    # 1. Veri Üret
    print("LOG: 1000 adet ham veri üretiliyor...")
    df_ham = veri_olustur(1000)

    # 2. Veri Temizle
    print(f"UYARI: {df_ham['Risk Puanları'].isnull().sum()} adet eksik veri tespit edildi.")
    print("LOG: Temizlik işlemi yapılıyor...")
    df_temiz = veri_temizle(df_ham)

    # 3. Sonuçları Göster
    print("-" * 30)
    print(df_temiz.info())
    print("-" * 30)

    # İsteğe bağlı: Veriyi kaydet
    df_temiz.to_csv("temiz_guvenlik_loglari.csv", index=False)
    print("LOG: Veriler 'temiz_guvenlik_loglari.csv' olarak kaydedildi.")

    # 4. Görselleştir
    print("LOG: Grafikler çiziliyor...")
    veri_gorsellestir(df_temiz)
    print("--- Analiz Tamamlandı ---")