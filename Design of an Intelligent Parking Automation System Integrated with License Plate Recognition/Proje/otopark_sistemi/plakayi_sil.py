import sqlite3

def plakayi_sil(okunan_plaka):
    conn = sqlite3.connect("kayitli_araclar.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM araclar WHERE plaka = ?", (plaka,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"[BİLGİ] '{okunan_plaka}' plakalı araç sistemden silindi.")
    else:
        print(f"[UYARI] '{okunan_plaka}' plakalı araç kayıtlı değil.")
    conn.close()

if __name__ == "__main__":
    plaka = input("Silinecek plakayı girin: ").strip().upper()
    if len(plaka) >= 6 and plaka.replace(" ", "").isalnum():
        plakayi_sil(plaka)
    else:
        print("[HATA] Geçersiz plaka formatı. En az 6 karakter olmalı ve yalnızca harf/rakam içermelidir.")
