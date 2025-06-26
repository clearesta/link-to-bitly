# 🤖 Telegram Bot: Bitly URL Shortener

This is a simple Telegram bot that automatically detects any URLs in your messages and replies with a shortened version using the Bitly API. The bot is kept intentionally minimal — it returns only the shortened link as plain text, making it easy for users to copy.

---

## ✨ Features

- 🔗 Automatically shortens any URL using Bit.ly
- 📎 Detects links in messages with regex
- ⚙️ Built with `python-telegram-bot` and Bitly API
- ❌ No buttons — simple output, easy to copy manually

---

## 🧰 Prerequisites

### 1. Create a Telegram Bot
- Open Telegram
- Search for `@BotFather`
- Run the `/newbot` command, set a name and username
- Copy the **Telegram Bot Token**

### 2. Get a Bitly Access Token
- Visit https://bitly.com
- Log in, go to **Settings > API**
- Create a **Generic Access Token**
- Copy and save the token

---

## 🚀 Installation & Usage

### 1. Clone this Repository

git clone https://github.com/clearesta/link-to-bitly.git

cd telegram-bitly-bot

### 2. Install Dependencies
pip install -r requirements.txt

Or manually:

pip install python-telegram-bot requests

### 3. Set Your Tokens
Edit the bot.py file and update the following lines:

BITLY_TOKEN = "YOUR_BITLY_ACCESS_TOKEN"

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

### 4. Run the Bot
python bot.py / python3 bot.py

For server environments, you can use screen, tmux, or create a systemd service to keep it running.

🧠 How It Works

The bot listens to incoming text messages.
If any links are found (via regex), it:
Sends the link to Bitly for shortening.
Replies with the shortened link.
If no link is detected, it notifies the user.

🧾 Example

You send:
https://example.com/my-long-url

Bot replies:
https://bit.ly/abc123
