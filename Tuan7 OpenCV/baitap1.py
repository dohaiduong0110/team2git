import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        return image
    return None

def blur_image():
    image = open_image()
    if image is not None:
        x, y, width, height = 100, 270, 150, 150
        roi = image[y:y+height, x:x+width]
        ksize = (21, 21)
        sigma = 0
        blurred_roi = cv2.GaussianBlur(roi, ksize, sigma)
        image[y:y+height, x:x+width] = blurred_roi
        cv2.imwrite('blurred_image.jpg', image)
        messagebox.showinfo("Success", "Image blurred and saved as 'blurred_image.jpg'")
        cv2.imshow('Original Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Image Blurring")

# Tạo nút để mở bức ảnh
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Tạo nút để làm mờ bức ảnh
blur_button = tk.Button(root, text="Blur Image", command=blur_image)
blur_button.pack()

root.mainloop()
