import sqlite3

def analyze_logs():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    # Check if table exists and has data
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='logs';")
    if not cursor.fetchone():
        print("⚠️ No 'logs' table found. Run main.py first.")
        return

    cursor.execute("SELECT COUNT(*) FROM logs;")
    total = cursor.fetchone()[0]
    if total == 0:
        print("⚠️ No data found in logs table. Run main.py first.")
        return

    print(f"📦 Total log entries: {total}\n")

    cursor.execute("SELECT level, COUNT(*) FROM logs GROUP BY level;")
    results = cursor.fetchall()

    print("📊 Log Level Summary:")
    for level, count in results:
        print(f"  {level}: {count}")

    conn.close()


if __name__ == "__main__":
    analyze_logs()
