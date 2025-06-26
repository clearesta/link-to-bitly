import re
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Ganti token kamu di sini
BITLY_TOKEN = "ISI_BITLY_TOKEN_KAMU"
TELEGRAM_TOKEN = "ISI_TELEGRAM_BOT_TOKEN_KAMU"

def shorten_link(long_url: str) -> str:
    headers = {
        "Authorization": f"Bearer {BITLY_TOKEN}",
        "Content-Type": "application/json"
    }
    json_data = {
        "long_url": long_url
    }

    try:
        response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, json=json_data)
        response.raise_for_status()
        return response.json()["link"]
    except requests.exceptions.HTTPError:
        return None
    except Exception:
        return None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    urls = re.findall(r'(https?://\S+)', message_text)

    if urls:
        for url in urls:
            short_link = shorten_link(url)
            if short_link:
                await update.message.reply_text(short_link)
            else:
                await update.message.reply_text("Gagal memendekkan link.")
    else:
        await update.message.reply_text("Tidak ada link ditemukan dalam pesanmu.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirimkan link dan aku akan mengubahnya menjadi Bit.ly!")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    app.run_polling()

if __name__ == '__main__':
    main()
