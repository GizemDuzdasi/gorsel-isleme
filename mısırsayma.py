import cv2
import numpy as np

image = cv2.imread(image_path)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Sarı Tonları Maskesi
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Morfolojik İşlemler
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=2)

# Distance Transform ve Eşikleme
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# Marker Hazırlığı
sure_bg = cv2.dilate(opening, kernel, iterations=3)
unknown = cv2.subtract(sure_bg, sure_fg)
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Watershed Segmentasyonu
image_marked = image.copy()
markers = cv2.watershed(image_marked, markers)
