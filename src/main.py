import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"route": "root"}


if __name__ == "__main__":
    uvicorn.run("main:app")
