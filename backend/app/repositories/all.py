from sqlalchemy import select
from app.models.portfolio import PortfolioModel
from app.models.asset import Asset
from app.models.portfolio_position import PortfolioPositionModel
from app.models.user import UserModel

class Repository:
    @staticmethod
    async def get_user_assets(session, user_id: int):
        query = select(Asset).join(PortfolioPositionModel, PortfolioPositionModel.asset_id == Asset.id).join(PortfolioModel, PortfolioPositionModel.portfolio_id == PortfolioModel.id).join(UserModel, PortfolioModel.user_id == UserModel.id).where(UserModel.id == user_id)
        result = await session.execute(query)
        return result.scalars().all()