from fastapi import FastAPI, APIRouter


from app.db.database import db
from app.lib import serializes, serializes_list
from app.routers import (
    animes, 
    create, 
    update,
    delete,
    json_data
)


app = FastAPI()

api_router = APIRouter(prefix="/api")

# Incloem els routers de cada mòdul

api_router.include_router(animes.router)
api_router.include_router(create.router)
api_router.include_router(update.router)
api_router.include_router(delete.router)
api_router.include_router(json_data.router)

app.include_router(api_router)