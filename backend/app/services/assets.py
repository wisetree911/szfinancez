from app.schemas.asset import AssetCreate, AssetUpdate
from shared.repositories.asset import AssetRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class AssetService:
    def __init__(self, session: AsyncSession):
        self.session=session
        self.repo=AssetRepository(session=session)

    async def get_all(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, asset_id: int):
        asset = await self.repo.get_by_id(asset_id=asset_id)
        if asset is None: raise HTTPException(404, "SZ asset not found")
        return asset
    
    async def get_by_ticker(self, ticker: str):
        asset = await self.repo.get_by_ticker(ticker=ticker)
        if asset is None: raise HTTPException(404, "SZ asset not found")
        return asset
    
    async def create(self, obj_in: AssetCreate):
        return await self.repo.create(obj_in=obj_in)

    async def delete(self, asset_id: int):
        asset = await self.repo.get_by_id(asset_id=asset_id)
        if asset is None: raise HTTPException(404, "SZ asset not found")
        await self.repo.delete(asset=asset)
    
    async def update(self, asset_id: int, payload: AssetUpdate):
        asset = await self.repo.get_by_id(asset_id=asset_id)
        if asset is None: raise HTTPException(404, "SZ asset not found")
        await self.repo.update(asset=asset, obj_in=payload)
        return asset