from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
import sqlite3

DB = "bot.db"

@Client.on_message(filters.command("rmsudo") & filters.user(OWNER_ID))
async def remove_sudo(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage:\n/rmsudo user_id")
        return

    user_id = int(message.command[1])

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM sudo_users WHERE user_id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()

    await message.reply_text(f"🗑️ User `{user_id}` removed from sudo list.")
