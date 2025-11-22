from sqlalchemy import select
from fastapi import HTTPException, APIRouter
from app.schemas.user import UserSchema
from app.core.database import SessionDep
from app.models.user import UserModel
from app.services.all import Service
from app.services.users import UsersService
from fastapi import status
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}")
async def get_user(session: SessionDep, user_id: int):
    return await UsersService.get_one(session=session, user_id=user_id)

@router.post("/")
async def create_user(session: SessionDep, user_schema: UserSchema):
    return await UsersService.create(session=session, user_schema=user_schema)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(session: SessionDep, user_id: int):
    query = select(UserModel).where(UserModel.id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none() # geht weiter nicht

    if user is None:
        raise HTTPException(404, "SZ user not found")
    
    await session.delete(user)
    await session.commit()
    return
    

@router.get("/")
async def get_users(session: SessionDep):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()