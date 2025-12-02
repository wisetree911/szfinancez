from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi import Depends
from typing import Annotated

DATABASE_URL = "postgresql+asyncpg://gagelang:toor@localhost:5432/portfolio_db"

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    DATABASE_URL,
    echo = True,
    future = True
)

async_session_maker = sessionmaker(
    engine, 
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session():
    async with async_session_maker() as session:
        yield session

