from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship, backref, mapped_column, Mapped, DeclarativeBase
from .database import Base
# Define the association table for the many-to-many relationship
import enum

class FilmEnum(str, enum.Enum):
    NEUTRAL = "..."
    LA_2 = "La 2"
    SUPER_3 = "Super 3"
    MANGA = "Manga"
    OVA = "OVA"
    OVA_MANGA = "OVA Manga"
    CAT_3XL = "3xl"
    CINEMES = "Cinemes"
    DVD = "DVD"
    ANIMEBOX = "Anime Box"
    OVA_SX3 = "OVA SX3"

class TipusEnum(str, enum.Enum):
    SERIE = "Series"
    PELICULA = "Pel·licula"
    OVA = "OVA"

class Anime(Base):
    __tablename__ = "animes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titol: Mapped[str] = mapped_column(String, unique=True, index=True)
    sinopsi: Mapped[str] = mapped_column(String)
    episodis: Mapped[int] = mapped_column(Integer)
    sortida_dia: Mapped[int] = mapped_column(Integer)
    sortida_mes: Mapped[int] = mapped_column(Integer)
    sortida_any: Mapped[int] = mapped_column(Integer)
    final_dia: Mapped[int] = mapped_column(Integer)
    final_mes: Mapped[int] = mapped_column(Integer)
    final_any: Mapped[int] = mapped_column(Integer)
    film: Mapped[FilmEnum] = mapped_column(Enum(FilmEnum))
    tipus: Mapped[TipusEnum] = mapped_column(Enum(TipusEnum))
    anime_dates: Mapped[list["AnimeDate"]] = relationship("AnimeDate", back_populates="anime")

class AnimeDate(Base):
    __tablename__ = "anime_dates"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dia: Mapped[int] = mapped_column(Integer)
    mes: Mapped[int] = mapped_column(Integer)
    any: Mapped[int] = mapped_column(Integer)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))  
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("dates", cascade="all, delete-orphan"))

class NomAnime(Base):
    __tablename__ = "nom_animes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom_id: Mapped[int] = mapped_column(ForeignKey("noms.id"))
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    nom: Mapped["Nom"] = relationship("Nom", backref=backref("animes", cascade="all, delete-orphan"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("noms", cascade="all, delete-orphan"))


class Nom(Base):
    __tablename__ = "noms"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom: Mapped[str] = mapped_column(String)
    sortida_dia: Mapped[int] = mapped_column(Integer)
    sortida_mes: Mapped[int] = mapped_column(Integer)
    sortida_any: Mapped[int] = mapped_column(Integer)
    final_dia: Mapped[int] = mapped_column(Integer)
    final_mes: Mapped[int] = mapped_column(Integer)
    final_any: Mapped[int] = mapped_column(Integer)
    nom_animes: Mapped[list["NomAnime"]] = relationship("NomAnime", back_populates="nom")
    
    