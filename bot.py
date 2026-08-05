from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from database import init_db

# Import Handlers
import handlers.start
import handlers.owner
import handlers.search
import handlers.courses
import handlers.sudo
import handlers.supersudo
import handlers.normalsudo
import handlers.rmsudo

# Initialize Database
init_db()

app = Client(
    "CourseManagerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("✅ Course Manager Bot Started...")
print(app.me)
app.run()
