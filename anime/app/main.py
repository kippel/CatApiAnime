from fastapi import FastAPI
from .db.database import Base, engine
from app.db.deps import db_dependency
from app.db.models import User


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_root(db: db_dependency):
    

    return {"user": "sample_user"}
