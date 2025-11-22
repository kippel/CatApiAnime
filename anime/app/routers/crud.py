from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)
from app.schemas import AnimeBase
from app.db.models import Anime, FilmEnum, TipusEnum
from typing import Optional


router = APIRouter(prefix="/crud", tags=["crud"])

@router.post("/create")
async def create(
    titol: str = Form(...),
    tipus: TipusEnum = Form(...),
    sinopsi: str = Form(""),
    episodis: Optional[int] = Form(None),
    sortida_date: str = Form(""),
    final_date: str = Form(""),
    film: Optional[FilmEnum] = Form(None),
    db: db_dependency = Annotated # type: ignore
):
    
    anime_data = Anime(
        titol=titol, 
        sinopsi=sinopsi,
        episodis=episodis,
        sortida_date=sortida_date,
        final_date=final_date,
        film=film,
        tipus=tipus
    )

    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return {"msg": anime_data}

