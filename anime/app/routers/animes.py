from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)   
from app.db.models import Anime

router = APIRouter(prefix="/animes", tags=["animes"])


@router.get("/")
async def get_animes(db: db_dependency):

    db_animes = db.query(Anime).all()

    db_animes_list = [{"id": anime.id, "titol": anime.titol} for anime in db_animes]

    return db_animes_list