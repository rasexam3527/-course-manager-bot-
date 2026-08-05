from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

@Client.on_message(filters.command("panel") & filters.user(OWNER_ID))
async def owner_panel(client: Client, message: Message):
    await message.reply_text(
        "👑 Owner Panel\n\n"
        "✅ /addsudo\n"
        "✅ /addsupersudo\n"
        "✅ /normalsudo\n"
        "✅ /rmsudo\n"
        "✅ /addcourse\n"
        "✅ /delcourse\n"
        "✅ /broadcast\n"
        "✅ /stats"
    )
