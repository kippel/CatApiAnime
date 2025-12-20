from pydantic import BaseModel, Field
import enum
from typing import Literal, Union




class TipusEnum(str, enum.Enum):
    SERIES = "Series"
    PELLICULA = "Pel·licula"
    OVA = "OVA"



"""
{
 "titol" : "Bloa de drac",
 "descripcio" : "",
 "primer_episodi" : "",
 "date" : [],
 "director" : [],
 "generes" : [],
 "pais" : [],
 "musica" : [],
 "musica_wiki" : [],
 "wiki" : [],
 "paraula" : [],
}
"""
class Anime(BaseModel):
    titol: str = Field(..., json_schema_extra={"example": ""})
    descripcio: str = Field("", json_schema_extra={"example": ""})
    primer_episodi: str = Field("", json_schema_extra={"example": ""})
    date: list[str] = []
    director: list[str] = []
    generes: list[str] = []
    pais: list[str] = []
    musica: list[str] = []
    musica_wiki: list[str] = []
    wiki: list[str] = []
    paraula: list[str] = []




"""
{
 "tipus" : "Pel·licula",
}
"""
class AnimePellicula(Anime):
    tipus: Literal["Pel·licula"] = "Pel·licula"


"""
{
 "tipus" : "Series",
 "durada_dels_capiols" : "25 min",
 "ultim_episodis" : "20 abril 1976",
 "temporades" : 2,
 "episodis" : 104,
}
"""
class AnimeSeries(Anime):
    tipus: Literal["Series"] = "Series"
    durada_dels_capiols: str = Field("", json_schema_extra={"example": ""})
    ultim_episodis: str = Field("", json_schema_extra={"example": ""})
    temporades: int = Field(0, json_schema_extra={"example": 0})
    episodis: int = Field(0, json_schema_extra={"example": 0})


"""
{
 "tipus" : "OVA",
 "durada_dels_capiols" : "25 min",
 "ultim_episodis" : "20 abril 1976",
 "episodis" : 104,
}
"""
class AnimeOVA(Anime):
    tipus: Literal["OVA"] = "OVA"
    durada_dels_capiols: str = Field("", json_schema_extra={"example": ""})
    ultim_episodis: str = Field("", json_schema_extra={"example": ""})
    episodis: int = Field(0, json_schema_extra={"example": 0})
