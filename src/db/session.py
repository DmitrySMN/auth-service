from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(settings.db_url, echo=True)

sessionmaker = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
