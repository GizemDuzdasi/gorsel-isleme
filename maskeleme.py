import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görselin Yüklenmesi
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kitap Köşe Noktaları (manuel alındı)
points = np.array([
    [190, 250],   # Sol Üst
    [999, 229],   # Sağ Üst
    [1076, 1486], # Sağ Alt
    [128, 1484]   # Sol Alt
])

# Maske Oluşturma
mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.fillPoly(mask, [points], 255)

# Maskeyi Uygula
black_background = np.zeros_like(image_rgb)
masked_result = np.where(mask[:, :, np.newaxis] == 255, image_rgb, black_background)

# Kontrast Artırımı (LAB)
lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2LAB)
l, a, b = cv2.split(lab)
l_eq = cv2.equalizeHist(l)
lab_eq = cv2.merge((l_eq, a, b))
enhanced_rgb = cv2.cvtColor(lab_eq, cv2.COLOR_LAB2RGB)

# Beyaz Zemin Uygulama
white_background = np.ones_like(image_rgb) * 255
white_background[mask == 255] = enhanced_rgb[mask == 255]

# Perspektif Düzeltme
points = np.array([
    [190, 250],   # Sol Üst
    [999, 229],   # Sağ Üst
    [1076, 1486], # Sağ Alt
    [128, 1484]   # Sol Alt
], dtype=np.float32)

width = 900
height = 1250
dst_points = np.array([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(points, dst_points)
warped = cv2.warpPerspective(image_rgb, matrix, (width, height))
