from pydantic import BaseModel
from fastapi import Form

class AnimeBase(BaseModel):
    titol: str = Form(...)
    episodis: str = Form("")