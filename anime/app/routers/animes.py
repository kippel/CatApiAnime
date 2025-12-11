from fastapi import APIRouter
from app.db.deps import db_dependency
from app.lib import serializes_list

router = APIRouter(prefix="/animes", tags=["animes"])

@router.get("/")
async def get_animes(db: db_dependency) -> list:

    animes = db.animes.find()

    animes_list = await serializes_list(animes)


    return animes_list

