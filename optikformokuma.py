import cv2
import numpy as np

# Görüntü İyileştirme
gray = cv2.equalizeHist(gray)

# Öğrenci Numarası Okuma (sözde kod, fonksiyon örneği)
def oku_ogrenci_numarasi(image):
    # 5 sütun, 10 satır üzerinden en koyu kutu tespit edilir
    ogr_no = ""
    for col in range(5):
        # her sütunda koyuluk analiz edilir
        pass
    return ogr_no

# Cevap Okuma
def oku_cevaplar(image):
    cevaplar = []
    for soru in range(30):
        # 4 şıktan en koyusu seçilir
        pass
    return cevaplar

# Puanlama
def puanla(cevaplar, cevap_anahtari):
    dogru, yanlis, bos = 0, 0, 0
    for ogr, dogru_cevap in zip(cevaplar, cevap_anahtari):
        if ogr == "":
            bos += 1
        elif ogr == dogru_cevap:
            dogru += 1
        else:
            yanlis += 1
    return dogru, yanlis, bos

# Tüm Optik Formlar İçin
for i in range(1, 11):
    filename = f"optik{i}.jpg"
    image = cv2.imread(filename)
    ogr_no = oku_ogrenci_numarasi(image)
    cevaplar = oku_cevaplar(image)
    d, y, b = puanla(cevaplar, cevap_anahtari)
    print(f"{filename} - {ogr_no} - D:{d} Y:{y} B:{b}")
