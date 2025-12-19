from fastapi import APIRouter
from app.db.deps import db_dependency
from app.workouts.animes_list import anime_delete_bar

router = APIRouter(prefix="/delete", tags=["delete"])

@router.delete("/anime/{id}")
async def delete_anime(id: str, db: db_dependency):

    await anime_delete_bar(id, db)
    
    return {"message": "Anime deleted"}


@router.delete("/anime")
async def delete_all_animes(db: db_dependency):

    await db.animes.delete_many({})
    return {"message": "All animes deleted"}
