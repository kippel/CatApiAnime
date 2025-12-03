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
    AnimeDate,
    Musica,
    MusicaWiki,
    Wiki,
    Paraula,
    AnimeParaula
)
from typing import Optional
from app.world.crud_anime import CrudAnime, ASeries
from app.schemas import (
    AnimeCreateBase, 
    SeriesBase,
    DateBase,
    PaisBase,
    MusicaBase,
    MusicaWikiBase,
    WikiBase,
    ParaulaBase,
    ParaulaAnimeBase,
    
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

'''
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
'''
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
        raise HTTPException(status_code=404, detail="Series not found")
    
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
        raise HTTPException(status_code=404, detail="Series not found")
    
    
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
        raise HTTPException(status_code=404, detail="Date not found")
    
    return anime_data


@router.put("/dates/{id}", response_model=DateBase)
def update_date_id(
    id: int,
    date_data_update: DateBase,
    db: db_dependency = Annotated # type: ignore)
):
    
    anime = db.query(Anime).filter(Anime.id == id).first()
    if anime == None:
        raise HTTPException(status_code=404, detail="Date not found")

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
        raise HTTPException(status_code=404, detail="Date not found")
    
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
        raise HTTPException(status_code=404, detail="Date not found")

    anime_date = db.query(AnimeDate).filter(AnimeDate.anime_id == id, AnimeDate.date == date).first()
    
    if anime_date == None:
        raise HTTPException(status_code=404, detail="Date not found")
    
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
    pais_data = db.query(Pais).filter(Pais.anime_id == id).all()
    
    if len(pais_data) == 0:
        raise HTTPException(status_code=404, detail="Pais not found")
    
    return pais_data

@router.put("/pais/{id}", response_model=PaisBase)
def update_pais_id(
    id: int,
    pais_data_update: PaisBase,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Pais not found")

    pais = Pais(
        anime_id=anime.id,
        pais=pais_data_update.pais
    )
    
    db.add(pais)
    db.commit()
    db.refresh(pais)
    
    return pais

@router.delete("/pais/{id}")
def delete_pais_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    pais = db.query(Pais).filter(Pais.anime_id == id).all()
    
    if len(pais) == 0:
        raise HTTPException(status_code=404, detail="Pais not found")
    
    for pais_dev in pais:
        db.delete(pais_dev)
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
        raise HTTPException(status_code=404, detail="Pais not found")

    pais = db.query(Pais).filter(Pais.anime_id == id, Pais.pais == pais).first()
    
    if pais == None:
        raise HTTPException(status_code=404, detail="Pais not found")
    
    db.delete(pais)
    db.commit()

    pais_all = db.query(Pais).filter(Pais.anime_id == id).all()
    
    return pais_all

############################################################################

@router.get("/musica/{id}")
def musica_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    musica_data = db.query(Musica).filter(Musica.anime_id == id).all()
    
    if len(musica_data) == 0:
        raise HTTPException(status_code=404, detail="Musica not found")
    
    return musica_data

@router.put("/musica/{id}", response_model=MusicaBase)
def update_musica_id(
    id: int,
    musica_data_update: MusicaBase,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Musica not found")

    musica = Musica(
        anime_id=anime.id,
        musica=musica_data_update.musica
    )
    
    db.add(musica)
    db.commit()
    db.refresh(musica)
    
    return musica

@router.delete("/musica/{id}")
def delete_musica_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    musica = db.query(Musica).filter(Musica.anime_id == id).all()
    
    if len(musica) == 0:
        raise HTTPException(status_code=404, detail="Musica not found")
    
    for musica_dev in musica:
        db.delete(musica_dev)
    db.commit()
    
    return { "message": "Musica deleted"}

@router.delete("/musica_id/{id}")
def delete_musica_id_id(
    id: int,
    musica: str,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Musica not found")

    musica = db.query(Musica).filter(Musica.anime_id == id, Musica.musica == musica).first()
    
    if musica == None:
        raise HTTPException(status_code=404, detail="Musica not found")
    
    db.delete(musica)
    db.commit()

    musica_all = db.query(Musica).filter(Musica.anime_id == id).all()
    
    return musica_all

############################################################################

@router.get("/musica_wiki/{id}")
def musica_wiki_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    musica_wiki_data = db.query(MusicaWiki).filter(MusicaWiki.anime_id == id).all()
    
    if len(musica_wiki_data) == 0:
        raise HTTPException(status_code=404, detail="MusicaWiki not found")
    
    return musica_wiki_data

@router.put("/musica_wiki/{id}", response_model=MusicaWikiBase)
def update_musica_wiki_id(
    id: int,
    musica_wiki_data_update: MusicaWikiBase,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="MusicaWiki not found")

    musica_wiki = MusicaWiki(
        anime_id=anime.id,
        musica_wiki=musica_wiki_data_update.musica_wiki
    )
    
    db.add(musica_wiki)
    db.commit()
    db.refresh(musica_wiki)
    
    return musica_wiki

@router.delete("/musica_wiki/{id}")
def delete_musica_wiki_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    musica_wiki = db.query(MusicaWiki).filter(MusicaWiki.anime_id == id).all()
    
    if len(musica_wiki) == 0:
        raise HTTPException(status_code=404, detail="MusicaWiki not found")
    
    for musica_wiki_dev in musica_wiki:
        db.delete(musica_wiki_dev)
    db.commit()
    
    return { "message": "MusicaWiki deleted"}

@router.delete("/musica_wiki_id/{id}")
def delete_musica_wiki_id_id(
    id: int,
    musica_wiki: str,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="MusicaWiki not found")

    musica_wiki = db.query(MusicaWiki).filter(MusicaWiki.anime_id == id, MusicaWiki.musica_wiki == musica_wiki).first()
    
    if musica_wiki == None:
        raise HTTPException(status_code=404, detail="MusicaWiki not found")
    
    db.delete(musica_wiki)
    db.commit()

    musica_wiki_all = db.query(MusicaWiki).filter(MusicaWiki.anime_id == id).all()
    
    return musica_wiki_all

############################################################################

@router.get("/wiki/{id}")
def wiki_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    wiki_data = db.query(Wiki).filter(Wiki.anime_id == id).all()
    
    if len(wiki_data) == 0:
        raise HTTPException(status_code=404, detail="Wiki not found")
    
    return wiki_data

@router.put("/wiki/{id}", response_model=WikiBase)
def update_wiki_id(
    id: int,
    wiki_data_update: WikiBase,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Wiki not found")

    wiki = Wiki(
        anime_id=anime.id,
        wiki=wiki_data_update.wiki
    )
    
    db.add(wiki)
    db.commit()
    db.refresh(wiki)
    
    return wiki


@router.delete("/wiki/{id}")
def delete_wiki_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    wiki = db.query(Wiki).filter(Wiki.anime_id == id).all()
    
    if len(wiki) == 0:
        raise HTTPException(status_code=404, detail="Wiki not found")
    
    for wiki_dev in wiki:
        db.delete(wiki_dev)
    db.commit()
    
    return { "message": "Wiki deleted"}

@router.delete("/wiki_id/{id}")
def delete_wiki_id(
    id: int,
    wiki: str,
    db: db_dependency = Annotated # type: ignore)
):
    anime = db.query(Anime).filter(Anime.id == id).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Wiki not found")

    wiki = db.query(Wiki).filter(Wiki.anime_id == id, Wiki.wiki == wiki).first()
    
    if wiki == None:
        raise HTTPException(status_code=404, detail="Wiki not found")
    
    db.delete(wiki)
    db.commit()

    wiki_all = db.query(Wiki).filter(Wiki.anime_id == id).all()
    
    return wiki_all

############################################################################

@router.get("/paraula/{id}")
def paraula_id(
    db: db_dependency = Annotated # type: ignore)
):
    """
    Retorna totes les paraules d'un anime
    {
        "paraula": "Bola de drac",
        "volumes": 153
    }
    """
    paraula_data = db.query(Paraula).all()
    
    if len(paraula_data) == 0:
        raise HTTPException(status_code=404, detail="Paraula not found")
    
    return paraula_data


@router.post("/paraula")
def create_paraula(
    paraula_data:ParaulaBase,
    db: db_dependency = Annotated # type: ignore)
):


    paraula = db.query(Paraula).filter(Paraula.id == paraula_data.id).first()
    
    if paraula != None:
        raise HTTPException(status_code=404, detail="Paraula already exists")

    paraula = Paraula(
        id=paraula_data.id,
        paraula=paraula_data.paraula,
        volumes=paraula_data.volumes
    )
    db.add(paraula)
    db.commit()
    db.refresh(paraula)
    
    return paraula



@router.put("/paraula_id")
def update_paraula_id(
    paraula_data_update:ParaulaBase,
    db: db_dependency = Annotated # type: ignore)
):
    paraula = db.query(Paraula).filter(Paraula.id == paraula_data_update.id).first()
           
    if paraula == None:
        raise HTTPException(status_code=404, detail="Paraula not found")
    
    paraula.paraula = paraula_data_update.paraula
    paraula.volumes = paraula_data_update.volumes
    
    db.add(paraula)
    db.commit()
    db.refresh(paraula)
    
    return paraula





@router.get("/anime_paraula/{id}")
def anime_paraula_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_paraula_data = db.query(AnimeParaula).filter(AnimeParaula.paraula_id == id).all()
    
    if len(anime_paraula_data) == 0:
        raise HTTPException(status_code=404, detail="AnimeParaula not found")
    
    anime_paraula_list = []
    for anime_paraula in anime_paraula_data:

        anime = db.query(Anime).filter(Anime.id == anime_paraula.anime_id).first()

        anime_dict = {
            "id": anime.id,
            "titol": anime.titol,
            "paraula id" : anime_paraula.id   
        }
        
        anime_paraula_list.append(anime_dict)
    
    return anime_paraula_list


@router.post("/anime_paraula")
def create_anime_paraula(
    paraula_anime: ParaulaAnimeBase,
    db: db_dependency = Annotated # type: ignore)
):


    anime = db.query(Anime).filter(Anime.titol == paraula_anime.anime).first()
    
    if anime == None:
        raise HTTPException(status_code=404, detail="Anime not found")

    paraula = db.query(Paraula).filter(Paraula.paraula == paraula_anime.paraula).first()
    if paraula == None:
        raise HTTPException(status_code=404, detail="Paraula not found")

    anime_paraula = db.query(AnimeParaula).filter(AnimeParaula.anime_id == anime.id, AnimeParaula.paraula_id == paraula.id).first()
    
    if anime_paraula != None:
        raise HTTPException(status_code=404, detail="AnimeParaula already exists")

    anime_paraula = AnimeParaula(
        anime_id=anime.id,
        paraula_id=paraula.id
    )
    db.add(anime_paraula)
    db.commit()
    db.refresh(anime_paraula)
    
    return anime_paraula


@router.delete("/anime_paraula/{id}")
def anime_paraula_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):
    anime_paraula = db.query(AnimeParaula).filter(AnimeParaula.anime_id == id).first()
    
    if anime_paraula == None:
        raise HTTPException(status_code=404, detail="AnimeParaula not found")
    
    db.delete(anime_paraula)
    db.commit()
    
    return { "message": "AnimeParaula deleted"}


@router.delete("/anime_paraula_id/{id}")
def anime_paraula_id_id(
    id: int,
    db: db_dependency = Annotated # type: ignore)
):

    paraula = db.query(Paraula).filter(Paraula.id == id).first()    
    if paraula == None:
        raise HTTPException(status_code=404, detail="Paraula not found")

    anime_paraula = db.query(AnimeParaula).filter(AnimeParaula.paraula_id == id).all()
    
    for anime_paraula_dev in anime_paraula:
        db.delete(anime_paraula_dev)
    db.commit()

    db.delete(paraula)
    db.commit()
    
    return { "message": "Paraula deleted"}
    