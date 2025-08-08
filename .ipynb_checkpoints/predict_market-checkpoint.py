# predict_market.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from data_collection import get_stock_data

# دریافت داده‌های سهام
data = get_stock_data('AAPL', '2020-01-01', '2021-01-01')

# آماده‌سازی داده‌ها
data['Date'] = pd.to_datetime(data.index)
data['Date'] = data['Date'].map(pd.Timestamp.toordinal)
X = data[['Date']]
y = data['Close']

# ساخت مدل رگرسیون خطی
model = LinearRegression()

# آموزش مدل
model.fit(X, y)

# پیش‌بینی قیمت‌های آینده
predictions = model.predict(X)

# ترسیم نمودار
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], y, label='True Price')
plt.plot(data['Date'], predictions, label='Predicted Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Prediction')
plt.legend()

# نمایش نمودار
plt.show()
