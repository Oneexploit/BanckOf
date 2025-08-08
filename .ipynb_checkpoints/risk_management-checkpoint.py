# risk_management.py

def check_stop_loss_take_profit(current_price, buy_price, stop_loss_percent, take_profit_percent):
    stop_loss_price = buy_price * (1 - stop_loss_percent / 100)
    take_profit_price = buy_price * (1 + take_profit_percent / 100)
    
    if current_price <= stop_loss_price:
        return 'Stop-Loss Triggered'
    elif current_price >= take_profit_price:
        return 'Take-Profit Triggered'
    else:
        return 'Hold'
    
# مثال استفاده
if __name__ == "__main__":
    current_price = 150
    buy_price = 155
    stop_loss_percent = 3  # درصد
    take_profit_percent = 5  # درصد

    print(check_stop_loss_take_profit(current_price, buy_price, stop_loss_percent, take_profit_percent))
