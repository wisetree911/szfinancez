
from fastapi import FastAPI
from app.routers import all
from app.routers import users
app = FastAPI()
app.include_router(users.router)
# app.include_router(all.router)


