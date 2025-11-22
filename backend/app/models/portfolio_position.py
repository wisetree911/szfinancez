
from sqlalchemy import ForeignKey, DateTime, Numeric
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class PortfolioPositionModel(Base):
    __tablename__ = "portfolio_positions"

    id: Mapped[int] = mapped_column(primary_key=True)
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolios.id", ondelete="CASCADE")
    )
    asset_id: Mapped[int] = mapped_column(ForeignKey("assets.id"))
    quantity: Mapped[float] = mapped_column(Numeric, nullable=False)
    avg_price: Mapped[float] = mapped_column(Numeric, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
