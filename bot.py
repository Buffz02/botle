 import os
from pyrogram import Client, filters

app = Client(
    "my_bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("hello world")

app.run()
