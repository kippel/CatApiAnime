from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship, backref, mapped_column, Mapped, DeclarativeBase
from .database import Base
# Define the association table for the many-to-many relationship
import enum

class Anime(Base):
    __tablename__ = "animes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titol: Mapped[str] = mapped_column(String, unique=True, index=True)
    episodis: Mapped[int] = mapped_column(String)


   