import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to open a file dialog and load an image
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        original_image = Image.fromarray(original_image)
        original_image = ImageTk.PhotoImage(original_image)
        original_label.config(image=original_image)
        original_label.image = original_image

# Function to apply the sharpening filters
def apply_filters():
    if 'img' in globals():
        output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
        output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
        output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)
        sharpened_image = cv2.cvtColor(output_1, cv2.COLOR_BGR2RGB)
        sharpened_image = Image.fromarray(sharpened_image)
        sharpened_image = ImageTk.PhotoImage(sharpened_image)
        sharpened_label.config(image=sharpened_image)
        sharpened_label.image = sharpened_image

# Create a tkinter window
window = tk.Tk()
window.title("Image Sharpening")

# Create buttons for opening an image and applying filters
open_button = tk.Button(window, text="Open Image", command=open_image)
apply_button = tk.Button(window, text="Apply Filters", command=apply_filters)

# Create labels for displaying the original and sharpened images
original_label = tk.Label(window)
sharpened_label = tk.Label(window)

# Place widgets in the window
open_button.pack(pady=10)
apply_button.pack(pady=10)
original_label.pack()
sharpened_label.pack()

# Define the sharpening kernels
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
 [-1,2,2,2,-1],
 [-1,2,8,2,-1],
 [-1,2,2,2,-1],
 [-1,-1,-1,-1,-1]]) / 8.0

# Start the tkinter main loop
window.mainloop()
