from asyncio import current_task
from core.config import settings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)


engine = create_async_engine(settings.db_url, echo=True)

sessionmaker = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_scoped_session():
    return async_scoped_session(session_factory=sessionmaker, scopefunc=current_task)


async def session_dep():
    session = sessionmaker()
    try:
        yield session
    finally:
        await session.close()
