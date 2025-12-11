from pydantic import BaseModel, Field
import enum
from typing import Literal





class TipusEnum(str, enum.Enum):
    SERIES = "Series"
    PELLICULA = "Pel·licula"
    OVA = "OVA"

class Anime(BaseModel):
    titol: str = Field("", example="")
    descripcio: str = Field("", example="")
    primer_episodi: str = Field("", example="")


class AnimePellicula(Anime):
    tipus: Literal["Pel·licula"]


"""
{
 "durada_dels_capiols" : "25 min",
 "ultim_episodis" : "20 abril 1976",
 "temporades" : 2,
 "episodis" : 104,
}
"""
class AnimeSeries(Anime):
    tipus: Literal["Series", "OVA"]
    durada_dels_capiols: str = Field("", example="")
    ultim_episodis: str = Field("", example="")
    temporades: int = Field(0, example=0)
    episodis: int = Field(0, example=0)

    