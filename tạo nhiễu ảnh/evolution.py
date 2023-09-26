import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def open_image():
    # Hiển thị hộp thoại chọn tệp tin
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    # Lấy tên tệp tin từ đường dẫn
    file_name = os.path.basename(file_path)
    print("Tên tệp tin:", file_name)
    # Kiểm tra nếu người dùng đã chọn một tệp tin ảnh
    if file_name:
        # Đọc ảnh
        img = cv2.imread(file_name, 0)
        m, n = img.shape[:2]

        # Thêm nhiễu Gaussian vào ảnh img
        gia_tri_TB = 10
        phuong_sai = 25
        noise = np.random.normal(loc=gia_tri_TB, scale=phuong_sai, size=(m, n))
        Gau_noisy_img = img + noise.astype(np.uint8)

        # Thêm nhiễu muối tiêu (add salt and pepper) vào ảnh img
        number_black = int(m * n * 0.05)  # định nghĩa số điểm đen
        number_white = int(m * n * 0.05)  # định nghĩa số điểm trắng
        # Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..m
        # Giá trị này sẽ biểu diễn tọa độ điểm đen theo hàng
        m_blacks = np.random.randint(0, m, number_black)
        # Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..n
        # Giá trị này sẽ biểu diễn tọa độ điểm đen theo cột
        n_blacks = np.random.randint(0, n, number_black)
        # Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..m
        # Giá trị này sẽ biểu diễn tọa độ điểm trắng theo hàng
        m_whites = np.random.randint(0, m, number_white)
        # Lấy giá trị nguyên ngẫu nhiên trong đoạn 0..n
        # Giá trị này sẽ biểu diễn tọa độ điểm trắng theo cột
        n_whites = np.random.randint(0, n, number_white)

        SP_noisy_img = np.copy(img)  # Sao chép ảnh img để tạo ảnh SP_noisy_img
        # Thiết lập mức xám = 0 (điểm đen) cho điểm ảnh có tọa độ (m_blacks,n_blacks)
        SP_noisy_img[m_blacks, n_blacks] = 0
        # Thiết lập mức xám = 255 (điểm trắng) cho điểm ảnh có tọa độ (m_whites,n_whites)
        SP_noisy_img[m_whites, n_whites] = 255

        # Hiển thị ảnh gốc, ảnh nhiễu và histogram
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        axes[0, 0].imshow(img, cmap='gray')
        axes[0, 0].set_title('Ảnh gốc')
        axes[0, 0].axis('off')
        axes[0, 1].hist(img.flatten(), bins=256)
        axes[0, 1].set_title('Histogram ảnh gốc')
        axes[1, 0].imshow(Gau_noisy_img, cmap='gray')
        axes[1, 0].set_title('Ảnh nhiễu Gaussian')
        axes[1, 0].axis('off')
        axes[1, 1].hist(Gau_noisy_img.flatten(), bins=256)
        axes[1, 1].set_title('Histogram ảnh nhiễu Gaussian')
        # Tạo figure và axes
        fig, axes = plt.subplots(1, 2, figsize=(6, 8))

        # In ma trận số của ảnh gốc
        axes[0].axis('off')
        axes[0].text(0.5, 0.5, 'Ma trận ảnh gốc:\n\n{}'.format(img), ha='center', va='center', fontsize=8)

        # In ma trận số sau khi tạo nhiễu
        axes[1].axis('off')
        axes[1].text(0.5, 0.5, 'Ma trận ảnh sau khi tạo nhiễu:\n\n{}'.format(Gau_noisy_img), ha='center', va='center',
                     fontsize=8)
        plt.tight_layout()
        plt.show()


# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Xử lý ảnh")
window.geometry("300x100")

# Tạo nút "Mở ảnh"
btn_open = tk.Button(window, text="Mở ảnh", command=open_image)
btn_open.pack()

window.mainloop()