from asyncio import current_task
from core.config import settings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)


engine = create_async_engine(settings.db_url, echo=True)

sessionmaker = async_sessionmaker(
    bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
)


async def get_scoped_session() -> AsyncSession:    
    return async_scoped_session(session_factory=sessionmaker, scopefunc=current_task)


async def session_dep() -> AsyncSession:
    async with sessionmaker() as session:
        yield session
    await session.close()


async def scoped_session_dep() -> AsyncSession:
    scoped_session = get_scoped_session()
    yield scoped_session
    await scoped_session.close()