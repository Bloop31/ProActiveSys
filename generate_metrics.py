import random
import time
import sqlite3
from datetime import datetime
conn = sqlite3.connect("metrics.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS metrics")

cur.execute("""
CREATE TABLE metrics (
    timestamp TEXT,
    cpu REAL,
    memory REAL,
    disk REAL,
    network REAL,
    swap REAL
)
""")
conn.commit()
print("Table created successfully")
while True:
    cpu = random.uniform(10, 95)
    memory = random.uniform(30, 98)
    disk = random.uniform(5, 400)
    network = random.uniform(100, 5000)
    swap = random.choice([0, 0, 0, random.uniform(1, 8)])

    cur.execute(
        "INSERT INTO metrics VALUES (?, ?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), cpu, memory, disk, network, swap)
    )
    conn.commit()

    print("Inserted metrics")
    time.sleep(5)
