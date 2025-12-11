from fastapi import FastAPI, APIRouter


from app.db.database import db
from app.lib import serializes, serializes_list
from app.routers import crud, animes


app = FastAPI()

@app.get("/")
async def read_root():

    users = db.users.find()    

    async for user in users:
        print(user)
    return {"Hello": "World"}

@app.post("/create-user")
async def create_user():
    create = await db.users.insert_one({"name": "John Doe"})
    
    return {"message": "User created"}
    

api_router = APIRouter(prefix="/api")

# Incloem els routers de cada mòdul

#if TEST_CRUD:
api_router.include_router(crud.router)
api_router.include_router(animes.router)

app.include_router(api_router)