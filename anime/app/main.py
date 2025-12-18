from fastapi import FastAPI, APIRouter


from app.db.database import db
from app.lib import serializes, serializes_list
from app.routers import (
    animes, 
    create, 
    update,
    delete
)


app = FastAPI()

@app.get("/")
async def read_root():

    users = db.users.find()    

    async for user in users:
        print(user)
    return {"Hello": "World"}


    

api_router = APIRouter(prefix="/api")

# Incloem els routers de cada mòdul

api_router.include_router(animes.router)
api_router.include_router(create.router)
api_router.include_router(update.router)
api_router.include_router(delete.router)

app.include_router(api_router)