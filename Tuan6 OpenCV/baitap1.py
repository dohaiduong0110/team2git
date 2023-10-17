import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Hàm để cập nhật và hiển thị ảnh sau khi zoom và xoay
def update_image():
    if original_img is not None:
        # Áp dụng zoom và xoay vào ảnh gốc
        zoomed_img = original_img.resize((int(original_img.width * current_scale), int(original_img.height * current_scale)), Image.LANCZOS)
        rotated_img = zoomed_img.rotate(rotation_angle)

        img = ImageTk.PhotoImage(rotated_img)
        img_label.config(image=img)
        img_label.image = img

        # Cập nhật tỷ lệ zoom
        zoom_label.config(text=f"Zoom: {current_scale:.1f}")


# Hàm xử lý sự kiện khi thanh trượt thay đổi giá trị
def on_scale_change(event):
    global current_scale
    current_scale = scale.get()
    update_image()


# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def select_image():
    global original_img, current_scale
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = Image.open(file_path)
        current_scale = 1.0
        rotation_angle = 0  # Đặt góc xoay về 0 độ
        update_image()


# Hàm xử lý sự kiện khi nút "Xoay trái" được nhấn
def rotate_left():
    global rotation_angle
    rotation_angle -= 90
    update_image()


# Hàm xử lý sự kiện khi nút "Xoay phải" được nhấn
def rotate_right():
    global rotation_angle
    rotation_angle += 90
    update_image()


# Tạo cửa sổ
window = tk.Tk()
window.title("Zoom and Rotate Image")
window.geometry('950x450')

# Khai báo biến toàn cục
current_scale = 1.0
original_img = None
rotation_angle = 0

# Tạo frame chứa thanh trượt và nút chọn ảnh
control_frame = tk.Frame(window)
control_frame.pack(side="left")

# Tạo thanh trượt
scale = tk.Scale(control_frame, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=on_scale_change)
scale.set(current_scale)
scale.pack()

# Tạo nút "Chọn ảnh" và đặt sự kiện khi nút này được nhấn
select_button = tk.Button(control_frame, text="Chọn ảnh", command=select_image)
select_button.pack()

# Tạo nút "Xoay trái" và đặt sự kiện khi nút này được nhấn
rotate_left_button = tk.Button(control_frame, text="Xoay trái", command=rotate_left)
rotate_left_button.pack()

# Tạo nút "Xoay phải" và đặt sự kiện khi nút này được nhấn
rotate_right_button = tk.Button(control_frame, text="Xoay phải", command=rotate_right)
rotate_right_button.pack()

# Label hiển thị ảnh
img_label = tk.Label(window)
img_label.pack()

# Label hiển thị tỷ lệ zoom
zoom_label = tk.Label(control_frame, text=f"Zoom: {current_scale:.1f}")
zoom_label.pack()

window.mainloop()