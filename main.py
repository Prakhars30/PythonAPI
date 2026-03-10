from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB = "database.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()


init_db()


@app.post("/send")
def send_data(data: dict):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO messages (message) VALUES (?)",
        (data["message"],)
    )

    conn.commit()
    conn.close()

    return {"status": "stored"}


@app.get("/data")
def get_data():

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT message FROM messages")

    rows = c.fetchall()

    conn.close()

    return [{"message": r[0]} for r in rows]
    
'''
const API_URL = "https://unornate-nobuko-unwinking.ngrok-free.dev";
'''
