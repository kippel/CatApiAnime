from pydantic import BaseModel
from fastapi import Form
from typing import Optional
from app.db.models import FilmEnum, TipusEnum


class AnimeBase(BaseModel):
    titol: str = Form(...)
    sinopsi: str = Form("")
    primer_episodi: str = Form("")
    durada_dels_capitols: str = Form("")
    ultim_episodis: str = Form("")
    temporades: int = Form(...)
    pais: str = Form("")
    director: str = Form("")
    date: str = Form("")
    generes: str = Form("")
    paraula: str = Form("")
    musica: str = Form("")
    wiki: str = Form("")
    film: str = Form("")
    tipus: str = Form("")
    
class AnimeCreate(BaseModel):
    titol: str = Form(...)
    sinopsi: str = Form("")
    primer_episodi: str = Form("")
    film: Optional[FilmEnum] = Form(None)
    tipus: Optional[TipusEnum] = Form(None)