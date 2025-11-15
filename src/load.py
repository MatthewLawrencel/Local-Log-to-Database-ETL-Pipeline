import sqlite3

def load_to_db(data):
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            message TEXT
        );
    """)

    if data:
        cursor.executemany(
            "INSERT INTO logs (timestamp, level, message) VALUES (?, ?, ?)",
            data
        )

    conn.commit()
    conn.close()
