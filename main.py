from config import LOGIN, PASSWORD, SERVER
import MetaTrader5 as mt5
from strategy import get_signal
from datetime import datetime
import time
from dotenv import load_dotenv
import os


load_dotenv()  # Load variables từ file .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

symbol = "BTCUSD"
lot = 0.01

def send_order(order_type):
    tick = mt5.symbol_info_tick(symbol)
    price = tick.ask if order_type == "BUY" else tick.bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_BUY if order_type == "BUY" else mt5.ORDER_SELL,
        "price": price,
        "deviation": 10,
        "magic": 142000,
        "comment": "KolfLDA Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    print(f"Order sent: {order_type} -> Result: {result.retcode}")
    return result

#connect to MetaTrader 5
if not mt5.initialize(login =LOGIN, password=PASSWORD, server=SERVER):
    print("Connection failed, error code =", mt5.last_error())
    quit()

print("Connected to MetaTrader 5")

while True:
    now = datetime.now()
    if now.minute % 1 == 0:
        signal = get_signal(symbol)
        print(f"Signal: {signal} at {now.strftime('%H:%M:%S')}")
        if signal in ["BUY", "SELL"]:
            send_order(signal)
    
    time.sleep(60)  # Wait for the next minute import datetime
