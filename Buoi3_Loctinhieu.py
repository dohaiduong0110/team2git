import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import tkinter as tk
from tkinter import ttk
from sympy import symbols, lambdify
from sympy import sin, pi

# Import data
Fs, signal = wavfile.read('Music2.mp3')
signal = signal[:, 1]  # Right channel
signalLen = len(signal)

plt.figure(figsize=(10, 10))

# Original Signal
plt.subplot(5, 1, 1)
stepLen = 1
range = np.arange(0, signalLen, stepLen)
plt.plot(range, signal[range])
plt.title('Original Signal')
plt.ylabel('Amp')

# Initialization
mu = 0.1
noise = np.random.randn(len(signal))  # Gaussian noise
noise1 = signal.filtfilt([1, 0.5], 1, noise)  # Noise 1
noise2 = signal.filtfilt([1, -0.5], 1, noise)  # Noise 2
sn = signal + noise1  # Signal + Noise

plt.subplot(5, 1, 2)
plt.plot(range, sn[range])
plt.title('Signal + Noise')
plt.ylabel('Amp')

# Filtering
numWeights = 32
LMS_filter = signal.dlti([1], [1, -0.5], dt=1)  # Discrete LTI Filter
_, s_output, _ = signal.dlsim(LMS_filter, noise2, x0=None)
s_output = s_output[:, 0]

# Results
plt.subplot(5, 1, 3)
plt.plot(range, s_output[range])
plt.title('Filtered Signal')
plt.ylabel('Amp')

plt.subplot(5, 1, 4)
plt.plot(range, noise2[range])
plt.title('Filtering Error')
plt.ylabel('Amp')

plt.subplot(5, 1, 5)
plt.plot(range, np.abs(s_output[range] - signal[range]))
plt.title('System Error')
plt.xlabel('Time index')
plt.ylabel('Amp')

plt.figure()
plt.stem(LMS_filter.B, use_line_collection=True)
plt.title('Filter Weights')
plt.xlabel('ith weight')
plt.ylabel('Value')
plt.grid(True)

plt.show()
# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Nhập thông số")

# Tạo các thành phần giao diện
label_fs = tk.Label(window, text="Tần số lấy mẫu (Fs):")
label_fs.pack()
entry_fs = tk.Entry(window)
entry_fs.pack()

label_T = tk.Label(window, text="Thời gian thu thập (T):")
label_T.pack()
entry_T = tk.Entry(window)
entry_T.pack()

label_ff1 = tk.Label(window, text="Tần số ff1:")
label_ff1.pack()
entry_ff1 = tk.Entry(window)
entry_ff1.pack()

label_ff2 = tk.Label(window, text="Tần số ff2:")
label_ff2.pack()
entry_ff2 = tk.Entry(window)
entry_ff2.pack()

label_ff3 = tk.Label(window, text="Tần số ff3:")
label_ff3.pack()
entry_ff3 = tk.Entry(window)
entry_ff3.pack()

label_filter = tk.Label(window, text="Chọn bộ lọc:")
label_filter.pack()
combo_filter = ttk.Combobox(window, values=["Thông cao", "Thông dải", "Dải chắn", "Thông thấp"])
combo_filter.pack()

button_apply = tk.Button(window, text="Áp dụng bộ lọc", command=apply_filter)
button_apply.pack()

# Hiển thị cửa sổ
window.mainloop()
