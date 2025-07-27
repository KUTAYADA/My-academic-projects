import sqlite3
import os

VERITABANI_ADI = 'kayitli_araclar.db'

def veritabani_olustur():
    if os.path.exists(VERITABANI_ADI):
        try:
            with sqlite3.connect(VERITABANI_ADI) as test_conn:
                test_conn.execute("SELECT name FROM sqlite_master LIMIT 1")
        except sqlite3.DatabaseError:
            print("[UYARI] Mevcut veritabanı hatalı. Temizleniyor...")
            os.remove(VERITABANI_ADI)

    conn = sqlite3.connect(VERITABANI_ADI)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS araclar (
            plaka TEXT PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()
    print("[BİLGİ] Veritabanı oluşturma işlemi tamamlandı.")

def ornek_arac_ekle():
    araclar = [
        "06FBK316", "34YA4134", "35BUK185", "41AHZ709", "34DUE721",
        "46ACC412", "34GBY460", "34BJF978", "68AT111", "34ARD19"
    ]
    conn = sqlite3.connect(VERITABANI_ADI)
    cursor = conn.cursor()
    for plaka in araclar:
        cursor.execute("INSERT OR IGNORE INTO araclar (plaka) VALUES (?)", (plaka,))
    conn.commit()
    conn.close()
    print("[BİLGİ] Örnek araç plakaları sisteme eklendi.")

if __name__ == "__main__":
    veritabani_olustur()
    ornek_arac_ekle()
