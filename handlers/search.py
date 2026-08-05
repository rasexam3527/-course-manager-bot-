from pyrogram import Client, filters
from pyrogram.types import Message
import sqlite3

DB = "bot.db"

@Client.on_message(filters.command("search"))
async def search_course(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("❌ Usage:\n/search course_name")
        return

    query = " ".join(message.command[1:]).lower()

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT course_name FROM courses WHERE LOWER(course_name) LIKE ?",
        (f"%{query}%",)
    )

    rows = cur.fetchall()
    conn.close()

    if not rows:
        await message.reply_text("❌ No course found.")
        return

    text = "📚 **Available Courses**\n\n"
    for row in rows:
        text += f"• {row[0]}\n"

    await message.reply_text(text)
