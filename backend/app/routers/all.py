from sqlalchemy import select
from fastapi import HTTPException, APIRouter
from app.schemas.user import UserSchema
from app.schemas.portfolio import PortfolioSchema
from app.core.database import SessionDep
from app.models.user import UserModel
from app.models.portfolio_position import PortfolioPositionModel
from app.models.portfolio import PortfolioModel
from app.models.asset import Asset
from app.services.all import Service
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/users/{user_id}")
async def get_user():
    ...

@router.post("/users")
async def create_user():
    ...

@router.delete("/users/{user_id}")
async def delete_user():
    ...

@router.get("/users")
async def get_users():
    ...









@router.post("/user/{user_id}/assets")
async def get_user_assets(user_id: int, session: SessionDep):
    return await Service.get_user_assets(session=session, user_id=user_id)

@router.post("/users/create")
async def add_users(user_schema: UserSchema, session: SessionDep):
    new_user = UserModel(
        name=user_schema.name,
        age=user_schema.age,
    )
    session.add(new_user)
    await session.commit()
    return "Aight"
    
@router.get("/users/list")
async def get_users(session: SessionDep):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()

@router.get("/users/{user_id}/portfolio", summary="Get concrete user portfolio")
async def get_user_portfolio(user_id: int, session: SessionDep):
    query = select(PortfolioModel).where(PortfolioModel.user_id == user_id)
    result = await session.execute(query)
    return result.scalars().all()

@router.post("/users/add_portfolio")
async def get_portfolios(portfolio_schema: PortfolioSchema, session: SessionDep):
    new_portfolio = PortfolioModel(
        user_id = portfolio_schema.user_id,
        name = portfolio_schema.name,
    )
    session.add(new_portfolio)
    await session.commit()
    return "Aight"

@router.get("/users/{portfolio_id}/positions", summary="Get concrete user concrete porfolio positions")
async def get_position(portfolio_id:int, session: SessionDep):
    query = select(PortfolioPositionModel).where(PortfolioPositionModel.portfolio_id == portfolio_id)
    result = await session.execute(query)
    return result.scalars().all()


