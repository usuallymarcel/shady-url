from pathlib import Path

from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import env, r

app = FastAPI()

origins = [
    'http://localhost:5173',
    'http://localhost:8000',
    'https://url.marcel.co.nz'
]

BASE_DIR = Path(__file__).resolve().parent

app.mount('/static', StaticFiles(directory=BASE_DIR / 'static'), name = 'static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def index():
    return FileResponse(BASE_DIR / 'static' / 'index.html')

@app.get("/config.js")
async def config_js():
    return Response(content=f"""window.ENV = {{API_URL: "{env.api_url}"}};""", media_type="application/javascript")
