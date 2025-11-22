from sqlalchemy import Text, ForeignKey, DateTime
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class PortfolioModel(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )