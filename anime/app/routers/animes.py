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
    

@router.get("/titol/{titol}")
async def titol(db: db_dependency, titol: str):
    
    animes = await db.animes.find_one({"titol": titol})

    if animes is None:
        raise HTTPException(status_code=404, detail="Anime not found")

    animes_list = serializes(animes)
    
    return animes_list        
    


