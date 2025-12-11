from app.schemes import AnimeSeries, AnimePellicula
from fastapi import APIRouter
from app.db.deps import db_dependency

router = APIRouter(prefix="/crud", tags=["crud"])



@router.post("/series", response_model=AnimeSeries)
async def create_series(db: db_dependency, anime: AnimeSeries):
    await db.animes.insert_one(anime.dict())
    return anime


@router.post("/pellicula", response_model=AnimePellicula)
async def create_pellicula(db: db_dependency, anime: AnimePellicula):
    await db.animes.insert_one(anime.dict())
    return anime
