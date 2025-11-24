from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)
from app.schemas import AnimeBase
from app.db.models import Anime, FilmEnum, TipusEnum
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

