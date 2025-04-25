from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from schemas.user import UserCreate
from ..models.user import Users
from sqlalchemy import select


async def get_users(session: AsyncSession) -> list[Users]:
    result: Result = await session.execute(select(Users).order_by(Users.id))
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(session: AsyncSession, user_id: int) -> Users | None:
    return session.get(Users, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> Users:
    user = Users(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
