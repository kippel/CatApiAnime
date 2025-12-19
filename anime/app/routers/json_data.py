import os
from fastapi import APIRouter
from app.db.deps import db_dependency
from app.lib import serializes_delete

import json

router = APIRouter(prefix="/json_data", tags=["json_data"])    

@router.get("/write")
async def write_animes(db: db_dependency) -> dict:
    anime = db.animes.find()
    anime_list = [serializes_delete(a) async for a in anime]
    
    with open("data/anime.json", "w", encoding="utf-8") as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=2)
    
    return {"message": "Animes saved to file"}

@router.get("/read")
async def read_animes(db: db_dependency) -> dict:
    
    if not os.path.exists("data/anime.json"):
        raise HTTPException(status_code=404, detail="File data/anime.json not found")

    await db.animes.delete_many({})
    
    with open("data/anime.json", "r", encoding="utf-8") as f:
        anime_list = json.load(f)

    for anime in anime_list:
        await db.animes.insert_one(anime)
    
    return {"message": "Animes read from file"}
