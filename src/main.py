from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.orchestrator import webhook

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhook)