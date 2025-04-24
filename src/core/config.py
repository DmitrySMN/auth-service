from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://root:pgpwd@localhost:5432/postgres"
    api_v1_prefix: str = "/api/v1"

settings = Settings()
