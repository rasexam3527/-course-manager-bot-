from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
import sqlite3

DB = "bot.db"

@Client.on_message(filters.command("addsupersudo") & filters.user(OWNER_ID))
async def add_super_sudo(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage:\n/addsupersudo user_id")
        return

    user_id = int(message.command[1])

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT OR REPLACE INTO sudo_users(user_id, role) VALUES(?, ?)",
        (user_id, "supersudo")
    )

    conn.commit()
    conn.close()

    await message.reply_text(f"👑 Super Sudo Added\nUser ID: `{user_id}`")
