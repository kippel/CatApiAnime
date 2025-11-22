from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)
from app.schemas import AnimeBase
from app.db.models import Anime, FilmEnum, TipusEnum

router = APIRouter(prefix="/crud", tags=["crud"])

@router.post("/create")
async def create(
    titol: str = Form(...),
    tipus: TipusEnum= Form(...),
    sinopsi: str = Form(""),
    episodis: int = Form(""),
    sortida_dia: int = Form(""),
    sortida_mes: int = Form(""),
    sortida_any: int = Form(""),
    final_dia: int = Form(""),
    final_mes: int = Form(""),
    final_any: int = Form(""),
    film: FilmEnum= Form(""),
    db: db_dependency = Annotated # type: ignore
):
    
    anime_data = Anime(
        titol=titol, 
        sinopsi=sinopsi,
        episodis=episodis,
        sortida_dia=sortida_dia,
        sortida_mes=sortida_mes,
        sortida_any=sortida_any,
        final_dia=final_dia,
        final_mes=final_mes,
        final_any=final_any,
        film=film,
        tipus=tipus
    )

    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return {"msg": anime_data}