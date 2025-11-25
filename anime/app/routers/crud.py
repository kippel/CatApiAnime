from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)
from app.schemas import AnimeBase
from app.db.models import Anime, FilmEnum, TipusEnum, AnimeSerie, Pais, AnimePais
from typing import Optional


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
    pais: Optional[str] = Form(None),
    db: db_dependency = Annotated # type: ignore
):
    
    anime_data = Anime(
        titol=titol, 
        sinopsi=sinopsi,
        primer_episodi=primer_episodi,
        film=film,
        tipus=tipus
    )

    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return anime_data


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

'''
{
    "pais": "Japones",
}
'''     
@router.post("/pais")
async def pais(
    pais: str = Form(...),
    db: db_dependency = Annotated # type: ignore
):
    db_pais = Pais(
        pais=pais
    )
    db.add(db_pais)
    db.commit()
    db.refresh(db_pais)
    return db_pais    


@router.post("/anime/pais")
async def animepais(
    anime_id: int,  
    pais_id: int,
    db: db_dependency = Annotated # type: ignore
):
    animepais_data = AnimePais(
        anime_id=anime_id,
        pais_id=pais_id
    )
    db.add(animepais_data)
    db.commit()
    db.refresh(animepais_data)
    return animepais_data
    

    