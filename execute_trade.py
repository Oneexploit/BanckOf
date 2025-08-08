import alpaca_trade_api as tradeapi

API_KEY = 'PKYI04G4E31KKV514W3O'  # کلید API خود را وارد کنید
API_SECRET = 'ZzbhRrW8HPWeE3xA8bxvZyz6sbyr2knKVoEApBcs'  # کلید API مخفی خود را وارد کنید

# ایجاد اتصال به Alpaca
api = tradeapi.REST(API_KEY, API_SECRET, base_url='https://paper-api.alpaca.markets')  # برای حساب Paper Trading

# خرید سهام
def buy_stock(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"Successfully bought {qty} shares of {symbol}")
    except Exception as e:
        print(f"Error buying stock: {e}")

# فراخوانی تابع خرید برای سهام AAPL
buy_stock('AAPL', 10)
