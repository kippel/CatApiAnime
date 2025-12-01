from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase #, declarative_base

import os

from app.config import SQLITE

if SQLITE:
    DATABASE = os.getenv("DATABASE_URL", "sqlite:///sql_app_test.db")
else:
    DATABASE = os.getenv("DATABASE_URL", "sqlite:///sql_app.db")

 

DATABASE_URL = os.getenv("DATABASE_URL", DATABASE)
# Exemple PostgreSQL:
# DATABASE_URL = "postgresql+psycopg2://user:password@localhost/mydb"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass