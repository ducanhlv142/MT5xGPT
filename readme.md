# 🤖 GPTMT5xKun – AI-Powered Trading Bot for MetaTrader 5

**GPTMT5xKun** is an experimental, intelligent trading bot that integrates **MetaTrader 5** with **OpenAI GPT** to analyze market signals and execute live trades based on real-time data and algorithmic strategy.

---

## 🚀 Features

- ✅ **Real-time connection** to MetaTrader 5 via official `MetaTrader5` Python API
- 📈 **Strategy engine** using EMA (5/20) and RSI logic
- 🧠 Optional **GPT-powered market sentiment analysis** (custom prompt injection)
- 🔒 Secure configuration with `.gitignore` to hide sensitive credentials
- 🔁 Modular architecture: separate files for logic, execution, config
- 📦 Ready for deployment on both **real** and **demo** accounts (e.g., ICMarkets)

---

## 🧠 Architecture

```bash
GPTMT5xKun/
├── main.py             # Entry point: init MT5 + run signal loop
├── strategy.py         # Trading strategy: EMA, RSI, GPT logic
├── config.py           # Contains login credentials and API keys (excluded from Git)
├── .gitignore          # Excludes config.py, env, cache
├── readme.md           # You’re reading it 😊
🛠 Requirements
Python 3.11

MetaTrader 5 platform (installed & logged in)

Python packages:

MetaTrader5

openai

python-dotenv (optional)

Install them using:

bash
Sao chép
Chỉnh sửa
py -m pip install MetaTrader5 openai python-dotenv
⚙️ Setup
Clone repo

bash
Sao chép
Chỉnh sửa
git clone https://github.com/ducanhlv142/MT5xGPT.git
cd MT5xGPT
Create config.py

python
Sao chép
Chỉnh sửa
LOGIN = 12345678
PASSWORD = "your_password"
SERVER = "your_mt5_server"
API_KEY = "sk-xxxxx"  # from OpenAI
Run bot

bash
Sao chép
Chỉnh sửa
py main.py
🧪 Example output
bash
Sao chép
Chỉnh sửa
Connected to MetaTrader 5
Signal: BUY at 15:04:00
EMA5:  64321.24, EMA20:  64109.80, RSI: 28.52
Order sent: BUY -> Result: 10009
🔒 Security
Your API keys and MT5 credentials are stored locally in config.py, which is excluded from Git with .gitignore. Never push secrets to remote!

📌 To-Do (Next Steps)
 Add support for multi-timeframe analysis

 Enable Telegram notifications

 Add GPT decision explanation logging

 Build basic UI panel for manual override

📄 License
This project is for educational and research purposes only.
Use at your own risk. The author is not responsible for financial loss or account issues.

💬 Author
KolfLDA
🧠 Built with ❤️ and AI by ducanhlv142 (KolfLDA)
🤝 Assisted by GPT (Kun)
