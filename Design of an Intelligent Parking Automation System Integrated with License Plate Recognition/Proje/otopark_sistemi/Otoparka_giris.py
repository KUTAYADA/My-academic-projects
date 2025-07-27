import cv2
import pytesseract
import sqlite3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def plaka_okuma():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Plaka Tanıma", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, config='--psm 11')
        text = text.strip().replace(" ", "").upper()

        if len(text) >= 6:
            print(f"[TANIMLAMA] Okunan plaka: {text}")
            cap.release()
            cv2.destroyAllWindows()
            return text

    cap.release()
    cv2.destroyAllWindows()
    return None

def veritabani_kontrol(okunan_plaka):
    conn = sqlite3.connect('kayitli_araclar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM araclar WHERE plaka=?", (okunan_plaka,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def otoparka_giris(okunan_plaka):
    with open("otopark_hali.txt", "a+") as file:
        file.seek(0)
        araclar = file.read().splitlines()
        if okunan_plaka in araclar:
            print(f"[BİLGİ] '{okunan_plaka}' plakalı araç otoparkta zaten mevcut.")
        elif len(araclar) >= 10:
            print("[UYARI] Otopark kapasitesi dolu. Giriş reddedildi.")
        else:
            file.write(f"{okunan_plaka}\n")
            doluluk = (len(araclar) + 1) * 10
            print(f"[GİRİŞ] Erişim onaylandı. Otoparka hoş geldiniz.")
            print(f"[DURUM] Anlık doluluk oranı: %{doluluk}")

if __name__ == "__main__":
    plaka = plaka_okuma()
    if plaka and veritabani_kontrol(plaka):
        otoparka_giris(plaka)
    else:
        print("[RED] Plaka doğrulanamadı veya sistemde kayıtlı değil.")
