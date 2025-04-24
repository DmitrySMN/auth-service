from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from db.session import *
from db.models import Base

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all())
    yield

@app.get("/")
def main():
    return {"route": "root"}


if __name__ == "__main__":
    uvicorn.run("main:app")
