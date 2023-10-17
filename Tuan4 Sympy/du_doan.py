import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp Excel
data = pd.read_csv('Student_Performance.csv')

# Chia dữ liệu thành các đặc trưng và nhãn
X = data.drop('Hours Studied', axis=1)
y = data['Performance Index']

# Chuẩn hóa dữ liệu
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1)
])

# Biên dịch mô hình với hàm mất mát MSE và trình tối ưu
model.compile(optimizer='adam', loss='mean_squared_error')

# Huấn luyện mô hình
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Đánh giá mô hình trên tập kiểm tra
loss = model.evaluate(X_test, y_test)
print(f'Mean Squared Error on Test Data: {loss}')

# Lấy giá trị mất mát trong quá trình huấn luyện
train_loss = history.history['loss']
val_loss = history.history['val_loss']

# Vẽ biểu đồ mất mát
epochs = range(1, len(train_loss) + 1)
plt.plot(epochs, train_loss, 'b', label='Training Loss')
plt.plot(epochs, val_loss, 'r', label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

