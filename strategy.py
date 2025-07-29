import MetaTrader5 as mt5

def get_signal(symbol="BTCUSD", timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 50)
    if rates is None or len(rates) < 21:
        return "WAIT"
    
    close_prices = [rate.close for rate in rates]

    # Calculate moving averages
    ema_fast = sum(close_prices[-5:]) / 5
    ema_slow = sum(close_prices[-20:]) / 20

    # Calculate RSI
    deltas = [close_prices[i+1] - close_prices[i] for i in range(-15, -1)]
    up = sum([d for d in deltas if d > 0])
    down = -sum([d for d in deltas if d < 0])
    rsi = 100 - 100 / (1 + (up / down)) if down != 0 else 100

    print(f"EMA5: {ema_fast: .2f}, EMA20: {ema_slow: .2f}, RSI: {rsi:.2f}")

    if ema_fast > ema_slow and rsi < 70:
        return "BUY"
    elif ema_fast < ema_slow and rsi > 30:
        return "SELL"
    else:
        return "WAIT"