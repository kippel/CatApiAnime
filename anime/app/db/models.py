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
    film: Mapped[FilmEnum] = mapped_column(Enum(FilmEnum))
    tipus: Mapped[TipusEnum] = mapped_column(Enum(TipusEnum))
    anime_dates: Mapped[list["AnimeDate"]] = relationship("AnimeDate", back_populates="anime")
    anime_directors: Mapped[list["AnimeDirector"]] = relationship("AnimeDirector", back_populates="anime")
    anime_genres: Mapped[list["AnimeGeneres"]] = relationship("AnimeGeneres", back_populates="anime")
    anime_series: Mapped[list["AnimeSerie"]] = relationship("AnimeSerie", back_populates="anime")
    anime_pais: Mapped[list["AnimePais"]] = relationship("AnimePais", back_populates="anime")


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
    ultim_episodi: Mapped[str] = mapped_column(String)
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

class NomAnime(Base):
    __tablename__ = "nom_animes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom_id: Mapped[int] = mapped_column(ForeignKey("noms.id"))
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    nom: Mapped["Nom"] = relationship("Nom", backref=backref("animes", cascade="all, delete-orphan"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("noms", cascade="all, delete-orphan"))

#########################################################################
class Nom(Base):
    __tablename__ = "noms"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom: Mapped[str] = mapped_column(String)
    sortida_date: Mapped[str] = mapped_column(String)
    final_date: Mapped[str] = mapped_column(String)
    nom_animes: Mapped[list["NomAnime"]] = relationship("NomAnime", back_populates="nom")
    
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

class Manga(Base):
    __tablename__ = "mangas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    noms_mangas: Mapped[str] = mapped_column(String)
    anime_mangas: Mapped[list["AnimeManga"]] = relationship("AnimeManga", back_populates="manga")

class MangaGeneres(Base):
    __tablename__ = "manga_genres"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    manga_id: Mapped[int] = mapped_column(ForeignKey("mangas.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))
    manga: Mapped["Manga"] = relationship("Manga", backref=backref("genres", cascade="all, delete-orphan"))
    genre: Mapped["Generes"] = relationship("Generes", backref=backref("mangas", cascade="all, delete-orphan"))
    
#########################################################################

#########################################################################

class AnimeManga(Base):
    __tablename__ = "anime_mangas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    manga_id: Mapped[int] = mapped_column(ForeignKey("mangas.id"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("mangas", cascade="all, delete-orphan"))
    manga: Mapped["Manga"] = relationship("Manga", back_populates="anime_mangas")

#########################################################################

class Pais(Base):
    __tablename__ = "pais"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    pais: Mapped[str] = mapped_column(String)
    anime_pais: Mapped[list["AnimePais"]] = relationship("AnimePais", back_populates="pais")

class AnimePais(Base):
    __tablename__ = "anime_pais"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("animes.id"))
    pais_id: Mapped[int] = mapped_column(ForeignKey("pais.id"))
    anime: Mapped["Anime"] = relationship("Anime", backref=backref("pais", cascade="all, delete-orphan"))
    pais: Mapped["Pais"] = relationship("Pais", backref=backref("animes", cascade="all, delete-orphan"))