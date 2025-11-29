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

'''
{
  "titol": "Bola de drac",
  "sinopsi": "",
  "primer_episodi": "26-02-1986",
  "film": "MANGA",
  "tipus": "SERIE",
}
'''
class Anime(Base):
    __tablename__ = "animes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titol: Mapped[str] = mapped_column(String, unique=True, index=True)
    sinopsi: Mapped[str] = mapped_column(String)
    primer_episodi: Mapped[str] = mapped_column(String)
    film: Mapped[ FilmEnum] = mapped_column(Enum(FilmEnum))
    tipus: Mapped[TipusEnum] = mapped_column(Enum(TipusEnum))
    anime_dates: Mapped[list["AnimeDate"]] = relationship("AnimeDate", back_populates="anime")
    anime_directors: Mapped[list["AnimeDirector"]] = relationship("AnimeDirector", back_populates="anime")
    anime_genres: Mapped[list["AnimeGeneres"]] = relationship("AnimeGeneres", back_populates="anime")
    anime_series: Mapped[list["AnimeSerie"]] = relationship("AnimeSerie", back_populates="anime")
    anime_paraula: Mapped[list["AnimeParaula"]] = relationship("AnimeParaula", back_populates="anime")
    
    
    


"""
{
  "durada_dels_capiols" : "25 min",
  "ultim_episodi : "20 abril 1976",
  "temporades" : 2,
  "episodis" : 104,
}
"""

class AnimeSerie(Base):
    __tablename__ = "anime_series"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    durada_dels_capitols: Mapped[str]   = mapped_column(String) 
    ultim_episodis: Mapped[str] = mapped_column(String)
    temporades: Mapped[int] = mapped_column(Integer)
    episodis: Mapped[int] = mapped_column(Integer)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    anime: Mapped["Anime"] = relationship("Anime", back_populates="anime_series")





#########################################################################
class Director(Base):
    __tablename__ = "directors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom: Mapped[str] = mapped_column(String)
    anime_directors: Mapped[list["AnimeDirector"]] = relationship("AnimeDirector", back_populates="director")

class AnimeDirector(Base):
    __tablename__ = "anime_directors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    director_id: Mapped[int] = mapped_column(ForeignKey("directors.id"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("directors", cascade="all, delete-orphan"))
    director: Mapped["Director"] = relationship("Director", backref=backref("animes", cascade="all, delete-orphan"))

#########################################################################

class AnimeDate(Base):
    __tablename__ = "anime_dates"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[str] = mapped_column(String)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))  
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("dates", cascade="all, delete-orphan"))

#########################################################################

class Generes(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    generes: Mapped[str] = mapped_column(String)
    anime_genres: Mapped[list["AnimeGeneres"]] = relationship("AnimeGeneres", back_populates="genre")
    
class AnimeGeneres(Base):
    __tablename__ = "anime_genres"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("genres", cascade="all, delete-orphan"))
    genre: Mapped["Generes"] = relationship("Generes", backref=backref("animes", cascade="all, delete-orphan"))

#########################################################################

## paraula

class Paraula(Base):
    __tablename__ = "paraula"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    paraula: Mapped[str] = mapped_column(String)
    volumes: Mapped[int] = mapped_column(Integer)
    anime_paraula: Mapped[list["AnimeParaula"]] = relationship("AnimeParaula", back_populates="paraula")
    
class AnimeParaula(Base):
    __tablename__ = "anime_paraula"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    paraula_id: Mapped[int] = mapped_column(ForeignKey("paraula.id"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("paraula", cascade="all, delete-orphan"))
    paraula: Mapped["Paraula"] = relationship("Paraula", backref=backref("animes", cascade="all, delete-orphan"))
   

#########################################################################

class Pais(Base):
    __tablename__ = "anime_pais"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    pais: Mapped[str] = mapped_column(String)   
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    

#########################################################################

class Musica(Base):
    __tablename__ = "anime_musica"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    musica: Mapped[str] = mapped_column(String)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))

#########################################################################

class Wiki(Base):
    __tablename__ = "anime_wiki"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    wiki: Mapped[str] = mapped_column(String)
    