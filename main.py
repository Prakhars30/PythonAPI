from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

FILE_NAME = "data.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def write_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

@app.post("/send")
def send_data(data: dict):

    current = read_data()
    current.append(data)
    write_data(current)

    return {"status": "stored"}

@app.get("/data")
def get_data():
    return read_data()

'''
const API_URL = "https://unornate-nobuko-unwinking.ngrok-free.dev";
'''