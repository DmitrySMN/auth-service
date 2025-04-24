from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://root:pgpwd@localhost:5432/postgres"


settings = Settings()
