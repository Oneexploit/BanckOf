import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, start_date: str, end_date: str, period: str = "1d") -> pd.DataFrame:
    """
    دریافت داده‌های تاریخی سهام از Yahoo Finance.

    :param ticker: نماد سهام (مثال: 'AAPL' برای شرکت اپل)
    :param start_date: تاریخ شروع به فرمت 'YYYY-MM-DD'
    :param end_date: تاریخ پایان به فرمت 'YYYY-MM-DD'
    :param period: بازه زمانی داده‌ها (مثال: '1d' برای روزانه، '1mo' برای ماهانه)
    :return: DataFrame حاوی داده‌های تاریخی سهام
    """
    try:
        # دریافت داده‌های سهام
        stock = yf.Ticker(ticker)
        data = stock.history(period=period, start=start_date, end=end_date)
        
        # بررسی اینکه آیا داده‌ای دریافت شده است یا خیر
        if data.empty:
            print(f"هشدار: هیچ داده‌ای برای نماد {ticker} در بازه زمانی مشخص یافت نشد.")
        return data
    
    except Exception as e:
        print(f"خطا در دریافت داده‌های سهام: {e}")
        return pd.DataFrame()  # بازگرداندن یک DataFrame خالی در صورت خطا

# مثال استفاده از تابع
if __name__ == "__main__":
    ticker = 'AAPL'  # نماد سهام شرکت اپل
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    
    # دریافت داده‌های روزانه
    data = get_stock_data(ticker, start_date, end_date, period="1d")
    
    # نمایش ۵ ردیف اول داده‌ها
    if not data.empty:
        print(data.head())