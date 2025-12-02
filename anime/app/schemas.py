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
    
class AnimeCreateBase(BaseModel):
    titol: str = Form(...)
    sinopsi: str = Form("")
    primer_episodi: str = Form("")
    film: Optional[FilmEnum] = Form(None)
    tipus: Optional[TipusEnum] = Form(None)


class SeriesBase(BaseModel):
    ultim_episodis: str = Form("")
    durada_dels_capitols: str = Form("")
    episodis: int = Form(...)
    temporades: int = Form(...)

class DateBase(BaseModel):
    date: str = Form("")

class PaisBase(BaseModel):
    pais: str = Form("")

class MusicaBase(BaseModel):
    musica: str = Form("")
    
class MusicaWikiBase(BaseModel):
    musica_wiki: str = Form("")
    
class WikiBase(BaseModel):
    wiki: str = Form("")

