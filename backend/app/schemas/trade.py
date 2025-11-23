from pydantic import BaseModel, Field

class TradeSchema(BaseModel):
    portfolio_id: int
    asset_id: int
    direction: str
    quantity: int
    price: int
