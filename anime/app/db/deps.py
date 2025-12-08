from typing import Annotated
from fastapi import Depends

# 🔹 Dependència de Mongo
def get_db():
    return db

db_dependency = Annotated[any, Depends(get_db)]