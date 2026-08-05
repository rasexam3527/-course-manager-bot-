from pyrogram import Client
from pyrogram.filters import command
from pyrogram.types import Message

from config import API_ID, API_HASH, BOT_TOKEN
from database import init_db

app = Client(
    "CourseManagerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Database Initialize
init_db()

@app.on_message(command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        "👋 Welcome to Course Manager Bot!\n\n"
        "Use /search to search courses."
    )

@app.on_message(command("ping"))
async def ping_handler(client: Client, message: Message):
    await message.reply_text("🏓 Pong!")

print("✅ Bot is starting...")

app.run()
