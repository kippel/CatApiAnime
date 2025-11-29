from pydantic import BaseModel
from fastapi import Form

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
    
   