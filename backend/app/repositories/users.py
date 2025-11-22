from sqlalchemy import select
from app.models.portfolio import PortfolioModel
from app.models.asset import Asset
from app.models.portfolio_position import PortfolioPositionModel
from app.models.user import UserModel

class UsersRepository:
    @staticmethod
    async def get_one(user_id: int, session):
        query = select(UserModel).where(UserModel.id == user_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        return user
    
    @staticmethod
    async def create(session, name: str, age: int):
        new_user = UserModel(
            name=name, 
            age=age
            )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user) # достать + айдишник от бд
        return new_user
    
    @staticmethod
    async def delete(session, user_id: int):
        ...
    
    @staticmethod
    async def get_all(session):
        ...
