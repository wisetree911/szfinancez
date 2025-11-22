
from fastapi import FastAPI
from app.routers import all

app = FastAPI()

app.include_router(all.router)


