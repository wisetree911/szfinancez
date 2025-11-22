from pydantic import BaseModel

class PortfolioPositionScheme(BaseModel):
    portfolio_id: int
    asset_id: int
    quantity: int
    avg_price: int