from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
import sqlite3

DB = "bot.db"


@Client.on_message(filters.command("addcourse") & filters.user(OWNER_ID))
async def add_course(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text(
            "❌ Usage:\n/addcourse Course Name"
        )
        return

    course_name = " ".join(message.command[1:])

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO courses (course_name) VALUES (?)",
            (course_name,)
        )
        conn.commit()

        await message.reply_text(
            f"✅ Course Added:\n{course_name}"
        )

    except sqlite3.IntegrityError:
        await message.reply_text(
            "❌ Course already exists."
        )

    conn.close()


@Client.on_message(filters.command("delcourse") & filters.user(OWNER_ID))
async def del_course(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text(
            "❌ Usage:\n/delcourse Course Name"
        )
        return

    course_name = " ".join(message.command[1:])

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM courses WHERE course_name=?",
        (course_name,)
    )

    conn.commit()

    if cur.rowcount > 0:
        await message.reply_text(
            f"✅ Deleted:\n{course_name}"
        )
    else:
        await message.reply_text(
            "❌ Course not found."
        )

    conn.close()
