import numpy as np 
import cv2
import matplotlib.pyplot as plt 

# Đọc ảnh
img = cv2.imread('mahiru1.jpg',0)
m,n = img.shape[:2]

# Thêm nhiễu Gaussian vào ảnh img
gia_tri_TB = 10
phuong_sai = 25
noise = np.random.normal(loc=gia_tri_TB,scale=phuong_sai,size=(m,n))
Gau_noisy_img = img + noise


# Thêm nhiễu muối tiêu (add salt and pepper) vào ảnh img
number_black = int(m*n*0.05)  # định nghĩa số điểm đen
number_white = int(m*n*0.05)  # định nghĩa số điểm trắng
# Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..m
# Giá trị này sẽ biểu diễn tọa độ điểm đen theo hàng
m_blacks = np.random.randint(0,m,number_black)
# Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..n
# Giá trị này sẽ biểu diễn tọa độ điểm đen theo cột
n_blacks = np.random.randint(0,n,number_black)
# Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..m
# Giá trị này sẽ biểu diễn tọa độ điểm trắng theo hàng
m_whites = np.random.randint(0,m,number_white)
# Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..n
# Giá trị này sẽ biểu diễn tọa độ điểm trắng theo cột
n_whites = np.random.randint(0,n,number_white)

SP_noisy_img = np.copy(img) # Sao chép ảnh img để tạo ảnh SP_noisy_img
# Thiết lập mức xám = 0 (điểm đen) cho điểm ảnh có tọa độ (m_blacks,n_blacks)
SP_noisy_img[m_blacks,n_blacks] = 0
# Thiết lập mức xám = 255 (điểm trắng) cho điểm ảnh có tọa độ (m_whites,n_whites)
SP_noisy_img[m_whites,n_whites] = 255

# 1. Hiển thị ảnh gốc, ảnh nhiễu và histogram
# Tạo cửa số 1 để hiển thị ảnh cho nhiễu Gaussian
fig1 = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9
#Tạo 9 vùng vẽ con
(ax1, ax2), (ax3, ax4) = fig1.subplots(2, 2)
# Hiển thị ảnh gốc
ax1.imshow(img, cmap='gray')
ax1.set_title('Ảnh gốc')
ax1.axis('off')
# Hiển thị histogram ảnh gốc
ax2.hist(img.flatten(),bins=256)
ax2.set_title('Histogram')
# Hiển thị ảnh nhiễu Gaussian
ax3.imshow(Gau_noisy_img, cmap='gray')
ax3.set_title('Ảnh nhiễu Gaussian')
ax3.axis('off')
# Hiển thị histogram ảnh nhiễu gaussian
ax4.hist(Gau_noisy_img.flatten(),bins=256)
ax4.set_title('Hitogram')
plt.show()
