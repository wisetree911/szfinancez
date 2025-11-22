from pydantic import BaseModel

class PortfolioSchema(BaseModel):
    user_id: int
    name: str