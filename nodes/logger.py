import sqlite3
import os
from datetime import datetime

DB_PATH = "logs.db"

def log_status(state):
    print("LOGGER NODE STARTED")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            video_path TEXT,
            video_id TEXT,
            status TEXT,
            created_at TEXT
        )
    """)

    cur.execute("""
        INSERT INTO logs (topic, video_path, video_id, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        state.get("topic"),
        state.get("video"),
        state.get("video_id"),
        "uploaded",
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

    print("LOGGER NODE COMPLETE")

    return state
