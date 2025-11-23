from fastapi import APIRouter, status
from app.schemas.trade import TradeSchema
from app.core.database import SessionDep
from app.services.trades import TradeService

router = APIRouter(prefix="/trades", tags=["Trades"])


@router.get("/{trade_id}")
async def get_trade(session: SessionDep, trade_id: int):
    return await TradeService.get_by_id(session=session, trade_id=trade_id)

@router.get("/")
async def get_trades(session: SessionDep):
    return await TradeService.get_all(session=session)

@router.post("/")
async def create_trade(session: SessionDep, trade_schema: TradeSchema):
    return await TradeService.create(session=session, trade_schema=trade_schema)

@router.delete("/{trade_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trade(session: SessionDep, trade_id: int):
    await TradeService.delete(session=session, trade_id=trade_id)
    return
    
