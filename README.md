# Görsel İşleme Projesi

Bu proje, bilgisayarlı görü ve görsel işleme tekniklerini kullanarak çeşitli uygulamalar geliştiren bir Python projesidir. Proje üç ana modülden oluşmaktadır.

## 📁 Proje Yapısı

```
gorsel-isleme/
├── maskeleme.py          # Görsel maskeleme ve perspektif düzeltme
├── mısırsayma.py         # Mısır taneleri sayma ve segmentasyon
├── optikformokuma.py     # Optik form okuma ve değerlendirme
└── README.md             # Bu dosya
```

## 🚀 Modüller

### 1. Maskeleme (maskeleme.py)

Bu modül, görsel işleme teknikleri kullanarak kitap görsellerini işler ve düzeltir.

**Özellikler:**
- Kitap köşe noktalarının tespiti
- Maske oluşturma ve uygulama
- Kontrast artırımı (LAB renk uzayında)
- Perspektif düzeltme
- Beyaz zemin uygulama

**Kullanılan Teknikler:**
- OpenCV ile görsel işleme
- NumPy ile matris işlemleri
- Matplotlib ile görselleştirme
- Perspektif transformasyon

### 2. Mısır Sayma (mısırsayma.py)

Bu modül, mısır tanelerini tespit etmek ve saymak için geliştirilmiştir.

**Özellikler:**
- HSV renk uzayında sarı ton tespiti
- Morfolojik işlemler (açma/kapama)
- Distance transform
- Watershed segmentasyonu
- Bağlantılı bileşen analizi

**Kullanılan Teknikler:**
- HSV renk filtreleme
- Morfolojik işlemler
- Distance transform
- Watershed algoritması

### 3. Optik Form Okuma (optikformokuma.py)

Bu modül, optik formları otomatik olarak okumak ve değerlendirmek için tasarlanmıştır.

**Özellikler:**
- Öğrenci numarası okuma
- Cevap şıklarının tespiti
- Otomatik puanlama
- Çoklu form işleme

**Kullanılan Teknikler:**
- Görsel iyileştirme (histogram eşitleme)
- Koyuluk analizi
- Şık tespiti algoritması

## 📋 Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install opencv-python
pip install numpy
pip install matplotlib
```

## 🛠️ Kurulum

1. Projeyi klonlayın:
```bash
git clone [repository-url]
cd gorsel-isleme
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## 📖 Kullanım

### Maskeleme Modülü
```python
# Görsel yolu belirtin
image_path = "kitap.jpg"
# maskeleme.py dosyasını çalıştırın
```

### Mısır Sayma Modülü
```python
# Mısır görseli yolu belirtin
image_path = "misir.jpg"
# mısırsayma.py dosyasını çalıştırın
```

### Optik Form Okuma
```python
# Optik form görsellerini hazırlayın
# optikformokuma.py dosyasını çalıştırın
```

## 🔧 Özelleştirme

### Maskeleme için:
- `points` değişkenini kendi görselinize göre ayarlayın
- `width` ve `height` değerlerini istenen çıktı boyutuna göre değiştirin

### Mısır Sayma için:
- `lower_yellow` ve `upper_yellow` değerlerini mısır rengine göre ayarlayın
- Morfolojik işlem parametrelerini görsel kalitesine göre optimize edin

### Optik Form için:
- Form yapısına göre sütun/satır sayılarını ayarlayın
- Cevap anahtarını güncelleyin

## 📊 Çıktılar

- **Maskeleme**: Düzeltilmiş ve iyileştirilmiş görsel
- **Mısır Sayma**: Tespit edilen mısır taneleri sayısı
- **Optik Form**: Öğrenci numarası, cevaplar ve puanlar

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

Bu proje bilgisayarlı görü ve görsel işleme alanında eğitim amaçlı geliştirilmiştir.

## 📞 İletişim

Sorularınız için issue açabilir veya iletişime geçebilirsiniz.

---

**Not:** Bu proje eğitim amaçlı geliştirilmiştir ve gerçek uygulamalarda kullanılmadan önce test edilmesi önerilir. 