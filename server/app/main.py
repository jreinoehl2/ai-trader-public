from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router

app = FastAPI(title="AI Trader API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # change to domain in prod (would be something like 'https://jadenreinoehl/ai-trader.com')
    allow_credentials=False, 
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)