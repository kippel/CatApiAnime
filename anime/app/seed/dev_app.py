from app.db.database import engine, Base, SessionLocal
from app.db.deps import db_dependency
from app.world.crud_anime import CrudAnime, ASeries

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def bola_de_drac(db):
    anime = CrudAnime(db)

    anime.create_anime(
        titol="Bola de drac",
        sinopsi="",
        primer_episodi="26-02-1986",
        film="MANGA",
        tipus="SERIE",
    )

    anime.create_pais("Japo")
    anime.create_director("Minoru Okazaki, Daisuke Nishio")
    #anime.create_date("")
    anime.create_generes("Action")
    anime.create_paraula("Bola de drac")
    anime.create_musica("Shunsuke Kikuchi")
    anime.create_musica_wiki("https://www.youtube.com/watch?v=cENvh9nQjNc, https://www.youtube.com/watch?v=puSHHK8LOlQ")
    anime.create_wiki("https://en.wikipedia.org/wiki/Bola_de_drac")
    
    serie_anime = ASeries(db, anime.id)
    serie_anime.series(
        durada_dels_capitols="",
        ultim_episodis="19 de abril de 1989",
        temporades=0,
        episodis=153,
    )

'''
Primer episodi: 1r-04-1975
  Film: Manga
  Tipus: SERIE
  Pais: Japo
  Director: Hiroshi Saito
  Date: 05-02-2004
  Generes: 
  Paraula: 
  Musica: https://www.youtube.com/watch?v=CNZ-vyQaGAg

'''
def abella_maia(db):
    anime = CrudAnime(db)

    anime.create_anime(
        titol="L'abella Maia",
        sinopsi="",
        primer_episodi="1r-04-1975",
        film="MANGA",
        tipus="SERIE",
    )

    anime.create_pais("Japo")
    anime.create_director("Hiroshi Saito")
    anime.create_date("05-02-2004")
    anime.create_generes("Fantasia")
    #anime.create_paraula("")
    #anime.create_musica("")
    anime.create_musica_wiki("https://www.youtube.com/watch?v=CNZ-vyQaGAg")
    anime.create_wiki("https://ca.wikipedia.org/wiki/Abella_Maia")
    

    serie_anime = ASeries(db, anime.id)
    serie_anime.series(
        durada_dels_capitols="25 min",
        ultim_episodis="20-04-1976",
        temporades=2,
        episodis=52,
    )


def dev_app():
    print("Dev App")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    abella_maia(db)
    bola_de_drac(db)
    

if __name__ == "__main__":
    dev_app()