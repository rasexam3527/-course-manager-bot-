from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔍 Search Course", switch_inline_query_current_chat="")
            ],
            [
                InlineKeyboardButton("📚 All Courses", callback_data="all_courses")
            ],
            [
                InlineKeyboardButton("👨‍💻 Admin Panel", callback_data="admin_panel")
            ]
        ]
    )
