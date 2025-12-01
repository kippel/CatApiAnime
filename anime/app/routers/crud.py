from fastapi import APIRouter, Form, Depends, HTTPException
from app.db.deps import (
    db_dependency,
    Annotated
)

from app.db.models import (
    Anime, 
    FilmEnum, 
    TipusEnum, 
    AnimeSerie, 
    Pais, 
    AnimeDate
)
from typing import Optional
from app.world.crud_anime import CrudAnime, ASeries
from app.schemas import (
    AnimeCreateBase, 
    SeriesBase,
    DateBase,
    PaisBase
)


router = APIRouter(prefix="/crud", tags=["crud"])

'''
{
  "titol": "Bola de drac",
  "sinopsi": "",
  "primer_episodi": "26-02-1986",
  "film": "MANGA",
  "tipus": "SERIE",
}
'''
@router.post("/create")
async def create(
    titol: str = Form(...),
    sinopsi: str = Form(""),
    primer_episodi: str = Form(""),
    film: Optional[FilmEnum] = Form(None),
    tipus: Optional[TipusEnum] = Form(None),
    pais: Optional[str] = Form(""),
    director: Optional[str] = Form(""),
    date: Optional[str] = Form(""),    
    generes: Optional[str] = Form(""),
    paraula: Optional[str] = Form(""),
    musica: Optional[str] = Form(""),
    musica_wiki: Optional[str] = Form(""),
    wiki: Optional[str] = Form(""),
    db: db_dependency = Annotated # type: ignore
):
    

    anime_data = CrudAnime(db)
    animes_dev = anime_data.create_anime(
        titol=titol,
        sinopsi=sinopsi,
        primer_episodi=primer_episodi,
        film=film,
        tipus=tipus
    )
    pais_dev = anime_data.create_pais(pais=pais)
    director_dev = anime_data.create_director(director=director)
    date_dev = anime_data.create_date(date=date)
    generes_dev = anime_data.create_generes(generes=generes)
    paraula_dev = anime_data.create_paraula(paraula=paraula)
    musica_dev = anime_data.create_musica(musica=musica)
    musica_wiki_dev = anime_data.create_musica_wiki(musica_wiki=musica_wiki)
    wiki_dev = anime_data.create_wiki(wiki=wiki)

    anime_run = {
        "id": animes_dev.id,
        "titol": animes_dev.titol,
        "sinopsi": animes_dev.sinopsi,
        "primer_episodi": animes_dev.primer_episodi,
        "film": animes_dev.film,
        "tipus": animes_dev.tipus,
        "pais": pais_dev,
        "director": director_dev,
        "date" : date_dev,
        "generes" : generes_dev,
        "paraula" : paraula_dev,
        "musica" : musica_dev,
        "musica_wiki" : musica_wiki_dev,
        "wiki" : wiki_dev
        
    }

    return anime_run

@router.post("/paraula/{id}")
async def create_director_id(
    id: int,
    volumes: int = Form(...),
    db: db_dependency = Annotated # type: ignore)
):

    anime_data = db.query(Paraula).filter(Paraula.anime_id == id).first()
    
    if anime_data == None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    anime_data.volumes = volumes
    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)

    return anime_data

@router.get("/anime/{id}")
def update_anime_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_data = db.query(Anime).filter(Anime.id == id).first()
    
    if anime_data == None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    return anime_data

@router.put("/anime/{id}", response_model=AnimeCreateBase)
def update_anime_id(
    id: int,
    anime_data_update: AnimeCreateBase,
    db: db_dependency = Annotated # type: ignore)
):
    anime_data = db.query(Anime).filter(Anime.id == id).first()
    
    if anime_data == None:
        raise HTTPException(status_code=404, detail="Anime not found")
            

    anime_data.titol = anime_data_update.titol
    anime_data.sinopsi = anime_data_update.sinopsi
    anime_data.primer_episodi = anime_data_update.primer_episodi
    anime_data.film = anime_data_update.film
    anime_data.tipus = anime_data_update.tipus

    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)
    
    return anime_data


############################################################################

"""
{
  "durada_dels_capiols" : "25 min",
  "ultim_episodi : "19-05-1989",
  "temporades" : 5,
  "episodis" : 153,
}
"""
@router.get("/series/{id}")
def get_series_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_data = db.query(AnimeSerie).filter(AnimeSerie.anime_id == id).first()
    
    if anime_data == None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    return anime_data

@router.put("/series/{id}", response_model=SeriesBase)
def update_series_id(
    id: int,
    series_data_update: SeriesBase,
    db: db_dependency = Annotated # type: ignore)
):

    anime_data = ASeries(db, id)
    anime_data.series(
        durada_dels_capitols=series_data_update.durada_dels_capitols,
        ultim_episodis=series_data_update.ultim_episodis,
        temporades=series_data_update.temporades,
        episodis=series_data_update.episodis
    )
    
    return anime_data.update_serie()

@router.delete("/series/{id}")
def delete_series_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_data = db.query(AnimeSerie).filter(AnimeSerie.anime_id == id).first()
    
    if anime_data == None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    
    db.delete(anime_data)
    db.commit()
    
    return { "message": "Anime deleted"}
    
############################################################################

@router.get("/dates/{id}")
def get_date_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_data = db.query(AnimeDate).filter(AnimeDate.anime_id == id).all()
    
    if len(anime_data) == 0:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    return anime_data


@router.put("/dates/{id}", response_model=DateBase)
def update_date_id(
    id: int,
    date_data_update: DateBase,
    db: db_dependency = Annotated # type: ignore)
):
    
    anime = db.query(Anime).filter(Anime.id == id).first()
    print(anime == None)
    if anime == None:

        raise HTTPException(status_code=404, detail="Anime not found")

    anime_date = AnimeDate(
        anime_id=anime.id,
        date=date_data_update.date
    )
    
    db.add(anime_date)
    db.commit()
    db.refresh(anime_date)
    
    return anime_date

@router.delete("/dates/{id}")
def delete_date_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_date = db.query(AnimeDate).filter(AnimeDate.anime_id == id).all()
    
    if len(anime_date) == 0:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    for anime in anime_date:
        db.delete(anime)
    db.commit()
    
    return { "message": "Dates deleted"}

@router.delete("/dates_id/{id}")
def delete_date_id_id(
    id: int,
    date: str,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(AnimeDate).filter(AnimeDate.anime_id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Anime not found")

    anime_date = db.query(AnimeDate).filter(AnimeDate.anime_id == id, AnimeDate.date == date).first()
    
    if anime_date == None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    db.delete(anime_date)
    db.commit()

    anime_date_all = db.query(AnimeDate).filter(AnimeDate.anime_id == id).all()
    
    return anime_date_all

############################################################################

@router.get("/pais/{id}")
def pais_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_data = db.query(Pais).filter(Pais.anime_id == id).all()
    
    if len(anime_data) == 0:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    return anime_data

@router.put("/pais/{id}", response_model=PaisBase)
def update_pais_id(
    id: int,
    pais_data_update: PaisBase,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Anime not found")

    anime_pais = Pais(
        anime_id=anime.id,
        pais=pais_data_update.pais
    )
    
    db.add(anime_pais)
    db.commit()
    db.refresh(anime_pais)
    
    return anime_pais

@router.delete("/pais/{id}")
def delete_pais_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_pais = db.query(Pais).filter(Pais.anime_id == id).all()
    
    if len(anime_pais) == 0:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    for anime in anime_pais:
        db.delete(anime)
    db.commit()
    
    return { "message": "Pais deleted"}

@router.delete("/pais_id/{id}")
def delete_pais_id_id(
    id: int,
    pais: str,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Anime not found")

    anime_pais = db.query(Pais).filter(Pais.anime_id == id, Pais.pais == pais).first()
    
    if anime_pais == None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    db.delete(anime_pais)
    db.commit()

    anime_pais_all = db.query(Pais).filter(Pais.anime_id == id).all()
    
    return anime_pais_all

