from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router

app = FastAPI(title="AI Trader API", version="1.0.0")

origins = [
    "https://jadenreinoehl.com",  # your frontend
    "https://www.jadenreinoehl.com",  # www version if you use it
    "http://localhost:3000",  # for local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)