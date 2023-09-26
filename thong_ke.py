import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk









tongsv= in_data[:,1]
print('Tong so sinh vien di thi :',np.sum(tongsv),"học sinh")
diemA = in_data[:,3]
diemBc = in_data[:,4]
print('Tong sv:',tongsv)
maxa = diemA.max()
i, = np.where(diemA == maxa)
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
plt.plot(range(len(diemA)),diemA,'r-',label="Điểm A")
plt.plot(range(len(diemBc)),diemBc,'g-',label="Điểm B +")
plt.xlabel('Lớp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
 #Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Số sinh viên trường DHCNHN")
window.geometry("600x600")
# Tạo widget Text để hiển thị ma trận số
text_widget = tk.Text(window)
text_widget.pack()
# Đọc dữ liệu từ tệp CSV và lưu vào DataFrame
df = pd.read_csv('diemPython.csv', index_col=0, header=0)

# Trích xuất ma trận số từ DataFrame
in_data = df.values
# Chuyển đổi ma trận số thành chuỗi văn bản
matrix_text = str(in_data)

# Ghi chuỗi văn bản vào widget Text
text_widget.insert(tk.END, matrix_text)
window.mainloop()
