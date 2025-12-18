from fastapi import APIRouter
from app.schemes import AnimeSeries, AnimePellicula, AnimeOVA
from app.db.deps import db_dependency
from bson.objectid import ObjectId
from app.workouts.animes_list import animes_tipus

router = APIRouter(prefix="/update", tags=["update"])


@router.put("/anime/series/{id}", response_model=AnimeSeries)
async def update_anime_series(
    id: str, 
    db: db_dependency, 
    anime: AnimeSeries
):

    await animes_tipus(id, db, anime, "Series")
    
    return anime


@router.put("/anime/pellicula/{id}", response_model=AnimePellicula)
async def update_anime_pellicula(
    id: str, 
    db: db_dependency, 
    anime: AnimePellicula
):

    await animes_tipus(id, db, anime, "Pel·licula")
    
    return anime


@router.put("/anime/ova/{id}", response_model=AnimeOVA)
async def update_anime_ova(
    id: str, 
    db: db_dependency, 
    anime: AnimeOVA
):

    await animes_tipus(id, db, anime, "OVA")
    
    return anime
