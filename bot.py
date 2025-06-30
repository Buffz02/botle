from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = "INSERISCI_IL_TUO_TOKEN"
bot = Bot(token=TOKEN)

app = Flask(__name__)
dispatcher = Dispatcher(bot=bot, update_queue=None)

# definisci la funzione di risposta
def start(update, context):
    update.message.reply_text("hello world")

# collega il comando /start
dispatcher.add_handler(CommandHandler("start", start))

# endpoint del webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# endpoint di test
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(port=10000, host="0.0.0.0")
