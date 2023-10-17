import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('BannerHaUI.jpg', cv2.IMREAD_GRAYSCALE)
def resize_image(image, scale_x, scale_y):
    return cv2.resize(image, (0, 0), fx=scale_x, fy=scale_y)
scale_x = float(input("Nhập tỉ lệ x (zoom in > 1, zoom out < 1): "))
scale_y = float(input("Nhập tỉ lệ y (zoom in > 1, zoom out < 1): "))
zoomed_image = resize_image(img, scale_x, scale_y)
plt.figure(figsize=(10, 5))
plt.figure(1)
plt.title("Anh goc")
plt.imshow(img, cmap='gray')
plt.figure(2)
plt.title(" Anh zoom")
plt.imshow(zoomed_image, cmap='gray')

plt.show()
