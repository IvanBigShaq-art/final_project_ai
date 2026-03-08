import sqlite3
import os

DB_NAME = "database.db"


def init_db():
    print("DB path:", os.path.abspath(DB_NAME))
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                deadline TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                summary TEXT
            )
            """)

            conn.commit()
            print("Database initialized successfully.")

    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")