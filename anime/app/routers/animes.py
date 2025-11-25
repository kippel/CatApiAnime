from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)   
from app.db.models import Anime, AnimeSerie, Pais, AnimePais

router = APIRouter(prefix="/animes", tags=["animes"])


@router.get("/")
async def get_animes(db: db_dependency):

    db_animes = db.query(Anime).all()

    db_animes_list = [{"id": anime.id, "titol": anime.titol} for anime in db_animes]

    return db_animes_list


@router.get("/{id}")
async def get_anime(db: db_dependency, id: int):

    db_anime = db.query(Anime).filter(Anime.id == id).first()

    

    # Convert to dict to avoid modifying the SQLAlchemy instance
    anime_dict = {
        "id": db_anime.id,
        "titol": db_anime.titol,
        "sinopsi": db_anime.sinopsi,
        "primer_episodi": db_anime.primer_episodi,
        "film": db_anime.film,
        "tipus": db_anime.tipus,
        "series": [],
        "pais": []
        
    }

    db_series = db.query(AnimeSerie).filter(AnimeSerie.anime_id == id).first()
    if db_series:
        anime_dict["series"] = db_series


    db_anime_pais = db.query(AnimePais).filter(AnimePais.anime_id == id).all()
    
    for anime_pais in db_anime_pais:
        pais_dev = db.query(Pais).filter(Pais.id == anime_pais.pais_id).first()
        if pais_dev:
            anime_dict["pais"].append(pais_dev.pais)

    return anime_dict
