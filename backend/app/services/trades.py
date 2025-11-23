from app.repositories.trades import TradeRepository

from fastapi import HTTPException

class TradeService:
    @staticmethod
    async def get_all(session):
        return await TradeRepository.get_all(session=session)
    
    @staticmethod
    async def get_by_id(session, trade_id: int):
        trade = await TradeRepository.get_by_id(session=session, trade_id=trade_id)
        if trade is None:
            raise HTTPException(404, "SZ trade not found")
        return trade

    @staticmethod
    async def create(session, trade_schema):
        return await TradeRepository.create(
            session=session,
            portfolio_id=trade_schema.portfolio_id,
            asset_id=trade_schema.asset_id,
            direction=trade_schema.direction,
            quantity=trade_schema.quantity,
            price=trade_schema.price
            )

    @staticmethod
    async def delete(session, trade_id: int):
        trade = await TradeRepository.get_by_id(session=session, trade_id=trade_id)
        if trade is None:
            raise HTTPException(404, "SZ trade not found")
        
        await TradeRepository.delete(session=session, trade=trade)