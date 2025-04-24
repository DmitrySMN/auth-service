import uvicorn
from fastapi import FastAPI
from db.session import *
from db.models import Base
from contextlib import asynccontextmanager
from api.v1 import router as user_router
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=user_router, prefix=settings.api_v1_prefix)

@app.get("/")
def index():
    return {"route": "root"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
