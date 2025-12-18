from fastapi import APIRouter
from app.db.deps import db_dependency

router = APIRouter(prefix="/delete", tags=["delete"])

@router.delete("/anime/{id}")
async def delete_anime(id: str, db: db_dependency):
    await db.animes.delete_one({"_id": id})
    return {"message": "Anime deleted"}


@router.delete("/anime")
async def delete_all_animes(db: db_dependency):
    await db.animes.delete_many({})
    return {"message": "All animes deleted"}
