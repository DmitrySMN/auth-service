import uvicorn
from fastapi import FastAPI
from db.session import *
from db.models import Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def index():
    return {"route": "root"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
