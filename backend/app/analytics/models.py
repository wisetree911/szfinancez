from collections import deque
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Deque, Literal

@dataclass(frozen=True)
class TradeDTO:
    asset_id: int
    direction: Literal["buy", "sell"]
    quantity: float
    price: float

    @classmethod
    def from_orm(cls, trade):
        return cls(
            asset_id=trade.asset_id,
            direction=trade.direction,
            quantity=trade.quantity,
            price=trade.price,
        )


@dataclass
class Lot:
    qty: int
    price: float

@dataclass
class AssetPosition:
    asset_id: int
    asset_market_price: float
    lots: Deque[Lot] = field(default_factory=deque)
    
    @property
    def mid_price(self):
        total = 0
        qty = 0
        for lot in self.lots:
            total += lot.qty * lot.price
            qty += lot.qty
        return total/qty
    
    @property
    def quantity(self):
        qty = 0
        for lot in self.lots:
            qty += lot.qty
        return qty
    
    @property
    def cost_basis(self):
        cost_basis = 0
        for lot in self.lots:
            cost_basis += lot.qty * lot.price
        return cost_basis
    
    @property
    def unrealized_pnl(self):
        absolute_profit = self.market_price - self.mid_price * self.quantity
        return absolute_profit
    
    @property
    def unrealized_return_pct(self):
        return (self.unrealized_pnl / self.cost_basis) * 100

    @property
    def market_price(self):
        return self.quantity * self.asset_market_price
