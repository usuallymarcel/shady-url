from datetime import timedelta
from pathlib import Path

from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.config import env, r
from app.static.generate import generate_url_path

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

class GenerateRequestSchema(BaseModel):
    url: str

@app.get("/")
def index():
    return FileResponse(BASE_DIR / 'static' / 'index.html')

@app.post("/generate")
def generate(data: GenerateRequestSchema):
    path = generate_url_path()
    r.set(path, data.url)
    r.expire(path, timedelta(days=7))

    return { "url": path}

@app.get("/config.js")
def config_js():
    return Response(content=f"""window.ENV = {{API_URL: "{env.api_url}"}};""", media_type="application/javascript")

@app.get("/{key}")
def redirect(key: str):
    response = r.get(key)
    if not response:
        raise HTTPException(404, 'Url not found')
    
    url = response.decode("utf-8")

    if 'https' not in url:
        url = 'https://' + url
    return RedirectResponse(url=url)
