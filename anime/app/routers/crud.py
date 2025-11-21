from fastapi import APIRouter, Form, Depends
from app.db.deps import (
    db_dependency,
    Annotated
)
from app.schemas import AnimeBase
from app.db.models import Anime

router = APIRouter(prefix="/crud", tags=["crud"])

@router.post("/create")
async def create(
    titol: str = Form(...),
    episodis: str = Form(""),
    db: db_dependency = Annotated # type: ignore
):
    
    anime_data = Anime(
        titol=titol, 
        episodis=episodis
    )

    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return {"msg": anime_data}