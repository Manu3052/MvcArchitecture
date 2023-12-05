from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import auth, users

app = FastAPI()

# Cors settings

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(users.router, tags=["Users"])
app.include_router(auth.router, tags=["Auth"])
