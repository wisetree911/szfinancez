from shared.repositories.trade import TradeRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.schemas.trade import TradeCreate, TradeUpdate
class TradeService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = TradeRepository(session=session)

    async def get_all_trades(self):
        return await self.repo.get_all()
    
    async def get_trade_by_trade_id(self, trade_id: int):
        trade = await self.repo.get_by_id(trade_id=trade_id)
        if trade is None:
            raise HTTPException(404, "SZ trade not found")
        return trade

    async def create(self, obj_in: TradeCreate):
        return await self.repo.create(obj_in=obj_in)

    async def delete_trade(self, trade_id: int):
        trade = await self.get_trade_by_trade_id(trade_id=trade_id)
        if trade is None:
            raise HTTPException(404, "SZ trade not found")
        
        await self.repo.delete(trade=trade)

    async def update(self, trade_id: int, payload: TradeUpdate):
        trade = await self.repo.get_by_id(trade_id=trade_id)
        if trade is None: raise HTTPException(404, "SZ trade not found")
        await self.repo.update(trade=trade, obj_in=payload)
        return trade
