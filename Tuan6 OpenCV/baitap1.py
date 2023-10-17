import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def zoom_image(x, y):
    img = cv2.imread('meo.jpg', cv2.IMREAD_GRAYSCALE)
    zoomed = cv2.resize(img, (x, y))
    Titles = ["Original", "Zoomed"]
    images = [img, zoomed]

    for i in range(2):
        plt.subplot(2, 1, i+1)
        plt.title(Titles[i])
        plt.imshow(images[i])
    plt.show()

def get_values():
    x = int(x_entry.get())
    y = int(y_entry.get())
    zoom_image(x, y)

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.image = img

root = tk.Tk()
root.title("Image Zoom App")

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

zoom_button = tk.Button(frame, text="Zoom Image", command=get_values)
zoom_button.pack()

load_button = tk.Button(frame, text="Load Image", command=load_image)
load_button.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()
