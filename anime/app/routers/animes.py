from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)   
from app.db.models import Anime, AnimeSerie, Pais
from app.world.crud_anime import UpdateAnime

router = APIRouter(prefix="/animes", tags=["animes"])


@router.get("/")
async def get_animes(db: db_dependency):

    db_animes = db.query(Anime).all()

    db_animes_list = [{"id": anime.id, "titol": anime.titol} for anime in db_animes]

    return db_animes_list


@router.get("/{id}")
async def get_anime(db: db_dependency, id: int):

    anime_data = UpdateAnime(db, id)
    anime_dev = anime_data.update_anime()
    pais_dev = anime_data.update_pais()
    director_dev = anime_data.update_director()
    date_dev = anime_data.update_date()

    anime_dict = {
        "id": anime_dev.id,
        "titol": anime_dev.titol,
        "sinopsi": anime_dev.sinopsi,
        "primer_episodi": anime_dev.primer_episodi,
        "film": anime_dev.film,
        "tipus": anime_dev.tipus,
        "pais": pais_dev,
        "director": director_dev,
        "date": date_dev
    }


    return anime_dict
