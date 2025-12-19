from bson.objectid import ObjectId
from app.schemes import Anime
from app.lib import serializes
from fastapi import HTTPException
from app.schemes import TipusEnum
from app.db.deps import db_dependency
from bson.errors import InvalidId

async def animes_tipus(
    id: str, 
    db: db_dependency,
    anime: Anime,
    tipus: str
):
    try:
        oid = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=404, detail="Anime not found")


    anime_db = await db.animes.find_one({"_id": oid})
    
    if anime_db is None:
        raise HTTPException(status_code=404, detail="Anime not found")

    
    if anime_db['tipus'] != tipus:
        raise HTTPException(status_code=404, detail="Anime not found")

    await db.animes.update_one({"_id": oid}, {"$set": anime.dict()})





async def anime_delete_bar(
    id: str, 
    db: db_dependency
):
    try:
        oid = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=404, detail="Anime not found")

    anime_db = await db.animes.find_one({"_id": oid})
    
    if anime_db is None:
        raise HTTPException(status_code=404, detail="Anime not found")

    await db.animes.delete_one({"_id": oid})
    
