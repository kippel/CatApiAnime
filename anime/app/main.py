from fastapi import FastAPI, APIRouter
from .db.database import Base, engine
from app.db.deps import db_dependency

from app.routers import crud, animes

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_root(db: db_dependency):
    

    return {"user": "sample_user"}


api_router = APIRouter(prefix="/api")

# Incloem els routers de cada mòdul

api_router.include_router(crud.router)
api_router.include_router(animes.router)
    

app.include_router(api_router)
