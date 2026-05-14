from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
from app.config import r

app = FastAPI()

origins = [
    'http://localhost:5173',
    'http://localhost:8000',
    'https://url.marcel.co.nz'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def index():
    r.set("hello", "world")
    return {'piss': 'poo'}