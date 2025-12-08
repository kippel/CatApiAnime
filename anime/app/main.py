from fastapi import FastAPI


from app.db.database import db
from app.lib import serializes, serializes_list


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