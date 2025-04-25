from db.crud import user_crud
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import User, UserCreate
from ..dependencies import session_dependency

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(session: AsyncSession = session_dependency):
    return await user_crud.get_users(session=session)


@router.get("/{iser_id}", response_model=User)
async def get_users(user_id: int, session: AsyncSession = session_dependency):
    return await user_crud.get_user_by_id(session=session, user_id=user_id)


@router.post("/", response_model=User)
async def create_user(user_in: UserCreate, session: AsyncSession = session_dependency):
    user = await user.create_user(session=session, user_in=user_in)
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
