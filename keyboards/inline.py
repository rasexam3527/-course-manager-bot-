from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🔍 Search Course",
                switch_inline_query_current_chat=""
            )
        ],
        [
            InlineKeyboardButton(
                "📚 All Courses",
                callback_data="courses"
            )
        ],
        [
            InlineKeyboardButton(
                "👤 Admin Panel",
                callback_data="admin"
            )
        ]
    ]
)
