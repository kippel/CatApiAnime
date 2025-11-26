from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)
from app.schemas import AnimeBase
from app.db.models import Anime, FilmEnum, TipusEnum, AnimeSerie, Pais
from typing import Optional
from app.world.crud_anime import CrudAnime

router = APIRouter(prefix="/crud", tags=["crud"])

'''
{
  "titol": "Bola de drac",
  "sinopsi": "",
  "primer_episodi": "26-02-1986",
  "film": "MANGA",
  "tipus": "SERIE",
}
'''
@router.post("/create")
async def create(
    titol: str = Form(...),
    sinopsi: str = Form(""),
    primer_episodi: str = Form(""),
    film: Optional[FilmEnum] = Form(None),
    tipus: Optional[TipusEnum] = Form(None),
    pais: Optional[str] = Form(""),
    director: Optional[str] = Form(""),
    db: db_dependency = Annotated # type: ignore
):
    

    anime_data = CrudAnime(db)
    animes_dev = anime_data.create_anime(
        titol=titol,
        sinopsi=sinopsi,
        primer_episodi=primer_episodi,
        film=film,
        tipus=tipus
    )
    pais_dev = anime_data.create_pais(pais=pais)
    director_dev = anime_data.create_director(director=director)

   

    anime_run = {
        "id": animes_dev.id,
        "titol": animes_dev.titol,
        "sinopsi": animes_dev.sinopsi,
        "primer_episodi": animes_dev.primer_episodi,
        "film": animes_dev.film,
        "tipus": animes_dev.tipus,
        "pais": pais_dev,
        "director": director_dev
    }

    return anime_run


"""
{
  "durada_dels_capiols" : "25 min",
  "ultim_episodi : "19-05-1989",
  "temporades" : 5,
  "episodis" : 153,
}
"""
@router.post("/serie/{id}")
async def create_id(
    id: int,
    durada_dels_capitols: str = Form(""),
    ultim_episodis: str = Form(""),
    temporades: int = Form(...),
    episodis: int = Form(...),
    db: db_dependency = Annotated # type: ignore)
):

    anime_data = AnimeSerie(
        durada_dels_capitols=durada_dels_capitols,
        ultim_episodis=ultim_episodis,
        temporades=temporades,
        episodis=episodis,
        anime_id=id
    )

    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return anime_data




    