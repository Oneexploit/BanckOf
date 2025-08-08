# trade_scheduler.py
import schedule
import time
from execute_trade import buy_stock, sell_stock
from predict_market import model, get_stock_data
import numpy as np

# تابع برای انجام پیش‌بینی و ارسال دستور خرید/فروش
def trade_logic():
    data = get_stock_data('AAPL', '2020-01-01', '2021-01-01')
    data['Date'] = pd.to_datetime(data.index)
    data['Date'] = data['Date'].map(pd.Timestamp.toordinal)
    
    # پیش‌بینی قیمت آینده
    X = data[['Date']]
    current_price = data['Close'].iloc[-1]
    prediction = model.predict([[X.iloc[-1, 0]]])

    # ارسال دستور خرید یا فروش بر اساس پیش‌بینی
    if prediction > current_price:
        buy_stock('AAPL', 10)
    else:
        sell_stock('AAPL', 10)

# زمان‌بندی انجام معاملات هر 5 دقیقه یکبار
schedule.every(5).minutes.do(trade_logic)

# اجرای زمان‌بند
while True:
    schedule.run_pending()
    time.sleep(1)
