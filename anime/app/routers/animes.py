import json, os
from pathlib import Path
from fastapi import APIRouter, HTTPException
from app.db.deps import db_dependency
from app.lib import serializes_list, serializes
from bson.objectid import ObjectId
from bson.errors import InvalidId

router = APIRouter(prefix="/animes", tags=["animes"])

@router.get("/")
async def get_animes(db: db_dependency) -> list:

    animes = db.animes.find()

    animes_list = await serializes_list(animes)

    bar = [
        {"id": anime["_id"], 
        "titol": anime["titol"], 
        "tipus": anime["tipus"]} 
        for anime in animes_list]

    return bar


@router.get("/json")
async def get_anime(db: db_dependency) -> dict:
    anime = db.animes.find()


    anime_list = await serializes_list(anime)

    with open("anime.json", "w", encoding="utf-8") as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=2)
    
    return {"message": "Animes saved to file"}


@router.get("/{id}")
async def anime_id(db: db_dependency, id: str):
    try:
        oid = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=404, detail="Anime not found")

    anime = await db.animes.find_one({"_id": oid})
    
    if anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")

    return serializes(anime)

@router.get("/paraula/{paraula}")
async def paraula(db: db_dependency, paraula: str):

    animes = db.animes.find({"paraula": {"$in": [paraula]}})
        
    animes_list = await serializes_list(animes)
    
    return animes_list
    

@router.get("/json")
async def get_anime(db: db_dependency) -> dict:
    anime = db.animes.find()


    anime_list = await serializes_list(anime)
    print(f"DEBUG: CWD is {os.getcwd()}")
    print(f"DEBUG: Writing {len(anime_list)} items to data/anime.json")

    with open("data/anime.json", "w", encoding="utf-8") as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=2)
    
    return {"message": "Animes saved to file"}


