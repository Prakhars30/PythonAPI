from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

data_store = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/send")
def send_data(data: dict):
    data_store.append(data)
    return {"status": "stored"}

@app.get("/data")
def get_data():
    return data_store

'''
const API_URL = "https://unornate-nobuko-unwinking.ngrok-free.dev";
'''
