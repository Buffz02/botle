import os
from flask import Flask, request
from telegram import Bot, Update

# otteniamo il token obbligatorio
TOKEN = os.environ["TELEGRAM_TOKEN"]
print(f"TOKEN = {TOKEN}")

# istanza bot
bot = Bot(token=TOKEN)

# istanza Flask
app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, bot)
        message = update.message

        if message and message.text:
            text = message.text.strip()
            chat_id = message.chat.id
            if text == "/start":
                bot.send_message(chat_id=chat_id, text="hello world")
        return "OK", 200

    except Exception as e:
        print("Errore nel webhook:", e)
        return "ERROR", 500

@app.route("/", methods=["GET"])
def index():
    return "Bot is alive!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
