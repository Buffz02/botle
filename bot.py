import os
from flask import Flask, request
from telegram import Bot, Update

TOKEN = os.environ["TELEGRAM_TOKEN"]   # così esplode se mancante
print("TOKEN =", TOKEN)

bot = Bot(token=TOKEN)
app = Flask(__name__)

def handle_start(update, context):
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
