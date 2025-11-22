from app.repositories.all import Repository
from fastapi import HTTPException

class Service:
    @staticmethod
    async def get_user_assets(session, user_id: int):
        return await Repository.get_user_assets(session=session, user_id=user_id)
    
    # @staticmethod
    # async def 