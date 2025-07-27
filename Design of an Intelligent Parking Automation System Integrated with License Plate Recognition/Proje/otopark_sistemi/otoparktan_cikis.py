import cv2
import pytesseract

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

def otoparktan_cikis(okunan_plaka):
    with open("otopark_hali.txt", "r+") as file:
        araclar = file.read().splitlines()
        if okunan_plaka in araclar:
            araclar.remove(okunan_plaka)
            file.seek(0)
            file.truncate()
            file.write("\n".join(araclar) + ("\n" if araclar else ""))
            doluluk = len(araclar) * 10
            print(f"[ÇIKIŞ] Araç çıkışı onaylandı. İyi yolculuklar.")
            print(f"[DURUM] Güncel doluluk oranı: %{doluluk}")
        else:
            print(f"[UYARI] '{okunan_plaka}' plakalı araç içeride kayıtlı değil.")

if __name__ == "__main__":
    plaka = plaka_okuma()
    if plaka:
        otoparktan_cikis(plaka)
    else:
        print("[HATA] Plaka algılanamadı.")
