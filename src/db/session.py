from asyncio import current_task
from core.config import settings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)


engine = create_async_engine(settings.db_url, echo=True)

sessionmaker = async_sessionmaker(
    bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
)


def get_scoped_session():
    return async_scoped_session(session_factory=sessionmaker, scopefunc=current_task)


async def session_dep():
    async with sessionmaker() as session:
        yield session
