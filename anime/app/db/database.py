from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase #, declarative_base

DATABASE_URL = "sqlite:///sql_app_test.db"
# Exemple PostgreSQL:
# DATABASE_URL = "postgresql+psycopg2://user:password@localhost/mydb"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass