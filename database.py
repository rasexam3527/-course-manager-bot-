import sqlite3

DB_NAME = "bot.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Users
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Courses
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT UNIQUE,
        channel_id INTEGER,
        demo_link TEXT,
        permanent_link TEXT,
        demo_time INTEGER DEFAULT 300
    )
    """)

    # Sudo Users
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sudo_users (
        user_id INTEGER PRIMARY KEY,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()
