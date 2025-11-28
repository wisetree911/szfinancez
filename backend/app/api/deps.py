from sqlalchemy.ext.asyncio import AsyncSession
from app.services.users import UserService
from fastapi import Depends
from app.core.database import get_session

def get_user_service(
        session: AsyncSession = Depends(get_session)
) -> UserService:
    return UserService(session=session)