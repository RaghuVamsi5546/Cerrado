import psutil
import sqlite3
import time
from datetime import datetime

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events(
id INTEGER PRIMARY KEY AUTOINCREMENT,
timestamp TEXT,
source TEXT,
severity TEXT,
message TEXT
)
""")

conn.commit()

print("Observer started... collecting system metrics")

while True:

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    severity = "INFO"

    if cpu > 80 or memory > 80:
        severity = "HIGH"

    message = f"CPU={cpu} MEMORY={memory} DISK={disk}"

    cursor.execute(
        "INSERT INTO events(timestamp,source,severity,message) VALUES(?,?,?,?)",
        (datetime.now().isoformat(),"system_metrics",severity,message)
    )

    conn.commit()

    print(message)

    time.sleep(5)