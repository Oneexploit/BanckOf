# deep_learning_model.py
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from data_collection import get_stock_data
from sklearn.preprocessing import MinMaxScaler

# دریافت داده‌ها
data = get_stock_data('AAPL', '2020-01-01', '2021-01-01')

# آماده‌سازی داده‌ها
data['Date'] = pd.to_datetime(data.index)
data['Date'] = data['Date'].map(pd.Timestamp.toordinal)
X = data[['Date']]
y = data['Close']

# مقیاس‌بندی داده‌ها
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))

# تقسیم داده‌ها به آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# ساخت مدل شبکه عصبی
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# کامپایل مدل
model.compile(optimizer='adam', loss='mean_squared_error')

# آموزش مدل
model.fit(X_train, y_train, epochs=50, batch_size=32)

# پیش‌بینی
predictions = model.predict(X_test)

# تبدیل نتایج پیش‌بینی به مقیاس اصلی
predictions = scaler.inverse_transform(predictions)
y_test = scaler.inverse_transform(y_test)

# نمایش نتایج
import matplotlib.pyplot as plt
plt.plot(y_test, label='True Price')
plt.plot(predictions, label='Predicted Price')
plt.legend()
plt.show()
