# 🤖 MT5xGPT – AI-Powered Trading Bot for MetaTrader 5

**MT5xGPT** is an experimental, intelligent trading bot that integrates **MetaTrader 5** with **OpenAI GPT** to analyze market signals and execute live trades based on real-time data and algorithmic strategy.

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
MT5xGPT/
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
    py -m pip install MetaTrader5 openai python-dotenv


⚙️ Setup
    1.Clone repo
        git clone https://github.com/ducanhlv142/MT5xGPT.git
        cd MT5xGPT
    2.Create config.py
        LOGIN = 12345678
        PASSWORD = "your_password"
        SERVER = "your_mt5_server"
        API_KEY = "sk-xxxxx"  # from OpenAI
    3.Run bot
        py main.py


🧪 Example output
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
    🤝 Assisted by GPT (Kun)x


## 🙏 Acknowledgments

Special thanks to:

- The [MetaTrader 5](https://www.metatrader5.com/en) team for providing a powerful trading platform and Python API
- [OpenAI](https://openai.com/) for enabling AI-driven decision making via GPT models
- All open-source contributors whose libraries made this project possible
- Myself – for dreaming big, learning hard, and building with ❤️

> “Code is poetry, and trading is an art. This project brings both together.” – Kolf
