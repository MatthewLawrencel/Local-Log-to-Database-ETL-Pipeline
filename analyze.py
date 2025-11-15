import sqlite3

def analyze_logs():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs")
    total = cursor.fetchone()[0]
    print(f"\n Total log entries: {total}\n")

    cursor.execute("SELECT level, COUNT(*) FROM logs GROUP BY level")
    print(" Log Level Summary:")
    for level, count in cursor.fetchall():
        print(f"  {level}: {count}")

    conn.close()

if __name__ == "__main__":
    analyze_logs()
