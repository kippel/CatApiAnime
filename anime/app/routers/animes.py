from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)   
from app.db.models import Anime, AnimeSerie, Pais, Paraula, AnimeParaula
from app.world.crud_anime import UpdateAnime, update_anime_dict

router = APIRouter(prefix="/animes", tags=["animes"])


@router.get("/")
async def get_animes(db: db_dependency):

    db_animes = db.query(Anime).all()

    db_animes_list = [{"id": anime.id, "titol": anime.titol} for anime in db_animes]

    return db_animes_list


@router.get("/{id}")
async def get_anime(db: db_dependency, id: int):

    anime_dict = update_anime_dict(db, id)

    return anime_dict

@router.post("/paraula")
def paraula(db: db_dependency):
    """
    Bola de drac 
    """
    paraula_dev = db.query(Paraula).all()
    
    return paraula_dev


@router.post("/paraula/{paraula}")
def paraula_id(db: db_dependency, paraula: str ):
    """
    Bola de drac 
    """
    paraula_dev = db.query(Paraula).filter(Paraula.paraula == paraula).first()
    
    if paraula_dev is None:
        return {"error": "No existeix"}

    anime_dev = db.query(AnimeParaula).filter(AnimeParaula.paraula_id == paraula_dev.id).all()
    
    anime_dev_list = []
    for anime in anime_dev:
        anime_dict = update_anime_dict(db, anime.anime_id)
        anime_dev_list.append(anime_dict)
    
    return anime_dev_list