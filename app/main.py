from fastapi import FastAPI
from .routers import card


app = FastAPI()


app.include_router(card.router)
