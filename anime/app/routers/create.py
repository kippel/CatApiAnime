from fastapi import APIRouter, Query
from typing import Annotated

from app.schemes import AnimeSeries, AnimePellicula, AnimeOVA
from app.db.deps import db_dependency

router = APIRouter(prefix="/create", tags=["create"])


@router.post("/series", response_model=AnimeSeries)
async def create_series(
    db: db_dependency, 
    anime: Annotated[AnimeSeries, Query()]
):

    await db.animes.insert_one(anime.dict())
    return anime


@router.post("/pellicula", response_model=AnimePellicula)
async def create_pellicula(
    db: db_dependency, 
    anime: Annotated[AnimePellicula, Query()]
):

    await db.animes.insert_one(anime.dict())
    return anime


@router.post("/ova", response_model=AnimeOVA)
async def create_ova(
    db: db_dependency, 
    anime: Annotated[AnimeOVA, Query()]
):

    await db.animes.insert_one(anime.dict())
    return anime
