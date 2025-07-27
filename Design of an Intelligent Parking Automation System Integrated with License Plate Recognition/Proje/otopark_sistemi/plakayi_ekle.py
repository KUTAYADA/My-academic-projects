import sqlite3


def veritabani_baglantisi(db_adi="kayitli_araclar.db"):
    try:
        return sqlite3.connect(db_adi)
    except sqlite3.Error as e:
        print(f"[HATA] Veritabanına bağlanılamadı: {e}")
        return None


def plaka_ekle(plaka):
    conn = veritabani_baglantisi()
    if conn is None:
        return

    try:
        with conn:
            conn.execute("INSERT OR IGNORE INTO araclar (plaka) VALUES (?)", (plaka,))
            print(f"[BİLGİ] '{plaka}' plakalı araç veritabanına eklendi (veya zaten kayıtlı).")
    except sqlite3.Error as e:
        print(f"[HATA] Plaka eklenirken bir sorun oluştu: {e}")
    finally:
        conn.close()


def plaka_girisi():
    plaka = input("Lütfen eklemek istediğiniz plakayı girin: ").strip().upper()

    if len(plaka) < 6:
        print("[UYARI] Plaka en az 6 karakter olmalıdır. Lütfen tekrar deneyin.")
        return

    if not plaka.replace(" ", "").isalnum():
        print("[UYARI] Plaka yalnızca harf ve rakamlardan oluşmalıdır.")
        return

    plaka_ekle(plaka)


if __name__ == "__main__":
    plaka_girisi()
