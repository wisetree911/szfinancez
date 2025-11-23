from fastapi import APIRouter, status
from app.schemas.user import UserSchema
from app.core.database import SessionDep
from app.services.users import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}")
async def get_user(session: SessionDep, user_id: int):
    return await UsersService.get_one(session=session, user_id=user_id)

@router.post("/")
async def create_user(session: SessionDep, user_schema: UserSchema):
    return await UsersService.create(session=session, user_schema=user_schema)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(session: SessionDep, user_id: int):
    await UsersService.delete(session=session, user_id=user_id)
    return
    
@router.get("/")
async def get_users(session: SessionDep):
    return await UsersService.get_all(session=session)