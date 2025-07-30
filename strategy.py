import MetaTrader5 as mt5
import os
import openai
import re

def ask_gpt_decision(ema_fast=66000, ema_slow=64000, rsi=28):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
    
    openai.api_key = openai_api_key

    prompt = (
        f"Chào bạn, hiện tại thị trường BTCUSD có:\n"
        f"- EMA5: {ema_fast:.2f}\n"
        f"- EMA20: {ema_slow:.2f}\n"
        f"- RSI: {rsi:.2f}\n\n"
        "Dựa trên dữ liệu này, bạn có thể đưa ra phân tích và lời khuyên nên BUY, SELL hay WAIT không?\n"
        "Hãy giải thích chi tiết tại sao và kết thúc bằng đề xuất hành động trong dấu [ ] như [BUY], [SELL], hoặc [WAIT]."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Bạn là một chuyên gia phân tích kỹ thuật."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        reply = response['choices'][0]['message']['content'].strip()
        print(f"GPT Response: {reply}")
        return reply.upper()
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        return "WAIT"


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

    reply = ask_gpt_decision(ema_fast, ema_slow, rsi)
    print(f"GPT Decision: {reply}")
    
    matches = re.findall(r'\[(BUY|SELL|WAIT)\]', reply.upper())
    return matches[0] if matches else "WAIT"
