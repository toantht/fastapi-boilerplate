from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import initial_data
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI()

@app.on_event("startup")
async def init_db():
    initial_data.init()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def hello():
    return {'message': 'Hi there'}

app.include_router(api_router, prefix=settings.API_V1_STR)
