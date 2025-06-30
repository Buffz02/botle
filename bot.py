from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

# funzione per gestire il comando /start
def handle_start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text="hello world")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    if update.message and update.message.text:
        if update.message.text.startswith("/start"):
            handle_start(update, None)
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

print("TOKEN =", TOKEN)
