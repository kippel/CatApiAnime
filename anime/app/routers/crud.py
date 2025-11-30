from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)

from app.db.models import Anime, FilmEnum, TipusEnum, AnimeSerie, Pais, AnimeDate
from typing import Optional
from app.world.crud_anime import CrudAnime, ASeries

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
    date: Optional[str] = Form(""),    
    generes: Optional[str] = Form(""),
    paraula: Optional[str] = Form(""),
    musica: Optional[str] = Form(""),
    wiki: Optional[str] = Form(""),
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
    date_dev = anime_data.create_date(date=date)
    generes_dev = anime_data.create_generes(generes=generes)
    paraula_dev = anime_data.create_paraula(paraula=paraula)
    musica_dev = anime_data.create_musica(musica=musica)
    wiki_dev = anime_data.create_wiki(wiki=wiki)

    anime_run = {
        "id": animes_dev.id,
        "titol": animes_dev.titol,
        "sinopsi": animes_dev.sinopsi,
        "primer_episodi": animes_dev.primer_episodi,
        "film": animes_dev.film,
        "tipus": animes_dev.tipus,
        "pais": pais_dev,
        "director": director_dev,
        "date" : date_dev,
        "generes" : generes_dev,
        "paraula" : paraula_dev,
        "musica" : musica_dev,
        "wiki" : wiki_dev
        
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
async def create_series_id(
    id: int,
    durada_dels_capitols: str = Form(""),
    ultim_episodis: str = Form(""),
    temporades: int = Form(...),
    episodis: int = Form(...),
    db: db_dependency = Annotated # type: ignore)
):

    anime_data = ASeries(db, id)
    anime_data.series(
        durada_dels_capitols=durada_dels_capitols,
        ultim_episodis=ultim_episodis,
        temporades=temporades,
        episodis=episodis
    )
    
    return anime_data.update_serie()


@router.post("/paraula/{id}")
async def create_director_id(
    id: int,
    volumes: int = Form(...),
    db: db_dependency = Annotated # type: ignore)
):

    anime_data = db.query(Paraula).filter(Paraula.anime_id == id).first()
    
    if anime_data == None:
        return { "error": "No existeix"}
    
    anime_data.volumes = volumes
    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return anime_data

    