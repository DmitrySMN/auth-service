from db.crud import user_crud
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import User, UserCreate, UserUpdate
from ..dependencies import session_dependency, user_by_id_dep

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(session: AsyncSession = session_dependency):
    return await user_crud.get_users(session=session)


@router.get("/{iser_id}", response_model=User)
async def get_user(
    user: User = Depends(user_by_id_dep),
):
    return user


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = session_dependency,
):
    return await user_crud.create_user(session=session, user_in=user_in)


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_update: UserUpdate,
    session: AsyncSession = session_dependency,
    user: User = Depends(user_by_id_dep),
):
    return await user_crud.update_user(
        session=session, user=user, user_update=user_update
    )


@router.patch("/{user_id}", response_model=User)
async def update_user_partial(
    user_update: UserUpdate,
    session: AsyncSession = session_dependency,
    user: User = Depends(user_by_id_dep),
):
    return await user_crud.update_user(
        session=session, user=user, user_update=user_update, partial=True
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    session: AsyncSession = session_dependency, user: User = Depends(user_by_id_dep)
):
    await user_crud.delete_user(session=session, user=user)
