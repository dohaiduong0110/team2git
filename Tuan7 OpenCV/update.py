import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

selected_image = None  # Biến toàn cục để lưu ảnh đã chọn

def select_image():
    global selected_image1
    global selected_image2
    file_path = filedialog.askopenfilename()
    if file_path:
        img1 = cv2.imread(file_path)
        selected_image1 = img1
        img2 = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
        selected_image2 = img2

        # Hiển thị ảnh đã chọn trên giao diện
        image = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image

def zoom_image(x, y):
    if selected_image1 is not None:
        zoomed = cv2.resize(selected_image1, (x, y))
        Titles = ["Original", "Zoomed"]
        images = [selected_image1, zoomed]
        plt.figure(1)
        for i in range(2):
            plt.subplot(2, 1, i + 1)
            plt.title(Titles[i])
            plt.imshow(images[i])
        plt.show()

def rotate_image(degrees):
    if selected_image1 is not None:
        img1 = selected_image1
        height, width = img1.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degrees, 1)
        rotated = cv2.warpAffine(img1, rotation_matrix, (width, height))

        Titles = ["Original", "Rotated"]
        images = [selected_image1, rotated]
        plt.figure(2)
        for i in range(2):
            plt.subplot(2, 1, i + 1)
            plt.title(Titles[i])
            plt.imshow(images[i])
        plt.show()

def normalize_image():
    if selected_image1 is not None and selected_image2 is not None :
        img1 = selected_image1
        normalized_img1 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX)
        img2 = selected_image2
        normalized_img2 = cv2.normalize(img2, None, 0, 255, cv2.NORM_MINMAX)
        cv2.imshow("Original1", img1)
        cv2.imshow("Normalized1", normalized_img1)
        cv2.imshow("Original2", img2)
        cv2.imshow("Normalized2", normalized_img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def edge_detection(ed1, ed2):
    if selected_image1 is not None:
        img = selected_image1
        edges = cv2.Canny(img, ed1, ed2)
        plt.figure(3)
        plt.imshow(edges, cmap='gray')
        plt.title("Edge Detection")
        plt.show()

def get_values1():
    x = int(x_entry.get())
    y = int(y_entry.get())
    zoom_image(x, y)

def get_values2():
    ed1 = int(ed1_entry.get())
    ed2 = int(ed2_entry.get())
    edge_detection(ed1, ed2)

def rotate_from_keyboard():
    degrees = int(rotation_entry.get())
    rotate_image(degrees)

root = tk.Tk()
root.title("Image Zoom, Rotate, and Normalize App")

frame = tk.Frame(root)
frame.pack()

x_label = tk.Label(frame, text="Enter x:")
x_label.pack()
x_entry = tk.Entry(frame)
x_entry.pack()

y_label = tk.Label(frame, text="Enter y:")
y_label.pack()
y_entry = tk.Entry(frame)
y_entry.pack()

ed1_label = tk.Label(frame, text="Enter ed1:")
ed1_label.pack()
ed1_entry = tk.Entry(frame)
ed1_entry.pack()

ed2_label = tk.Label(frame, text="Enter ed2:")
ed2_label.pack()
ed2_entry = tk.Entry(frame)
ed2_entry.pack()

rotation_label = tk.Label(frame, text="Enter rotation angle:")
rotation_label.pack()
rotation_entry = tk.Entry(frame)
rotation_entry.pack()

select_button = tk.Button(frame, text="Select Image", command=select_image)
select_button.pack()

image_label = tk.Label(root)
image_label.pack()

zoom_button = tk.Button(frame, text="Zoom Image", command=get_values1)
zoom_button.pack()

rotate_button = tk.Button(frame, text="Rotate Image", command=rotate_from_keyboard)
rotate_button.pack()

normalize_button = tk.Button(frame, text="Normalize Image", command=normalize_image)
normalize_button.pack()

edge_button = tk.Button(frame, text="Edge Detection", command=get_values2)
edge_button.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()
