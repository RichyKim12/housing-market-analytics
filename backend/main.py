from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import Base, engine
import models



@asynccontextmanager # Startup function
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = "127.0.0.1", port=8000)