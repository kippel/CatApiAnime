from app.db.models import (
    Anime, 
    Pais, 
    Director, 
    AnimeDirector, 
    AnimeDate, 
    Generes, 
    AnimeGeneres,
    Paraula,
    AnimeParaula,
    Musica,
    MusicaWiki,
    AnimeSerie,
    Wiki
    
)
from app.countries import countries


class CrudAnime:
    def __init__(self, db):
        self.db = db
        self.id = None
        self.animes = None

    def create_anime(self, 
        titol: str,
        sinopsi: str,
        primer_episodi: str,
        film: str,
        tipus: str,
    ) -> Anime:
        anime_data = Anime(
            titol=titol,
            sinopsi=sinopsi,
            primer_episodi=primer_episodi,
            film=film,
            tipus=tipus
        )
        self.db.add(anime_data)
        self.db.commit()
        self.db.refresh(anime_data)

        self.id = anime_data.id
        

        anime_data_dev = self.db.query(Anime).filter(Anime.id == self.id).first()
        self.animes = anime_data_dev
        if anime_data_dev is None:
            raise HTTPException(status_code=404, detail="Anime not found")

        return anime_data_dev

    def create_pais(self,pais: str):

        pais_data_list = []

        if pais == "":
            return pais_data_list
        

        for pais in pais.split(","):

            pais_dev = ' '.join(pais.split())
            
            for i in countries:
                if pais_dev == i[1]:
                    break
            else:
                raise HTTPException(status_code=404, detail="Pais not found") 

            pais_data = Pais(
                anime_id=self.id,
                pais=pais_dev
            )
            pais_data_list.append(pais_dev)
            self.db.add(pais_data)
            self.db.commit()
            self.db.refresh(pais_data)

        pais_data_dev = self.db.query(Pais).filter(Pais.anime_id == self.id).all()
        
        pais_data_dev_list = [pais.pais for pais in pais_data_dev]
        
        return pais_data_dev_list

    def create_director(self,director: str):
        director_data_list = []
        if director == "":
            return director_data_list
            
        for director in director.split(","):
            director_dev = ' '.join(director.split())
            director_data_dev = self.db.query(Director).filter(Director.nom == director_dev).first()
            if director_data_dev is None:
                director_data = Director(
                    nom=director_dev
                )
                self.db.add(director_data)
                self.db.commit()
                self.db.refresh(director_data)

                director_data_dev = self.db.query(Director).filter(Director.nom == director_dev).first()
            
            anime_director_data = AnimeDirector(
                anime_id=self.id,
                director_id=director_data_dev.id
            )
            self.db.add(anime_director_data)
            self.db.commit()
            self.db.refresh(anime_director_data)
            director_data_list.append(director_data_dev.nom)
        
        return director_data_list

    def create_date(self,date: str):
        date_data_list = []
        if date == "":
            return date_data_list
        
        for date in date.split(","):
            date_dev = ' '.join(date.split())
            anime_date_data = AnimeDate(
                anime_id=self.id,
                date=date_dev
            )
            self.db.add(anime_date_data)
            self.db.commit()
            self.db.refresh(anime_date_data)
            date_data_list.append(date_dev)
        
        return date_data_list
    
    def create_generes(self,generes: str):
        generes_data_list = []
        
        for generes in generes.split(","):
            generes_dev = ' '.join(generes.split())
            generes_data_dev = self.db.query(Generes).filter(Generes.generes == generes_dev).first()
            if generes_data_dev is None:
                generes_data = Generes(
                    generes=generes_dev
                )
                self.db.add(generes_data)
                self.db.commit()
                self.db.refresh(generes_data)

                generes_data_dev = self.db.query(Generes).filter(Generes.generes == generes_dev).first()
            
            anime_generes_data = AnimeGeneres(
                anime_id=self.id,
                genre_id=generes_data_dev.id
            )
            self.db.add(anime_generes_data)
            self.db.commit()
            self.db.refresh(anime_generes_data)
            generes_data_list.append(generes_data_dev.generes)
        
        return generes_data_list

    def create_paraula(self,paraula: str):
        paraula_data_list = []
        if paraula == "":
            return paraula_data_list
        
        for paraula in paraula.split(","):
            paraula_dev = ' '.join(paraula.split())
            paraula_data_dev = self.db.query(Paraula).filter(Paraula.paraula == paraula_dev).first()
            if paraula_data_dev is None:
                paraula_data = Paraula(
                    paraula=paraula_dev,
                    volumes=0
                )
                self.db.add(paraula_data)
                self.db.commit()
                self.db.refresh(paraula_data)

                paraula_data_dev = self.db.query(Paraula).filter(Paraula.paraula == paraula_dev).first()
            
            anime_paraula_data = AnimeParaula(
                anime_id=self.id,
                paraula_id=paraula_data_dev.id
            )
            self.db.add(anime_paraula_data)
            self.db.commit()
            self.db.refresh(anime_paraula_data)
            paraula_data_list.append(paraula_data_dev.paraula)
        
        return paraula_data_list

    def create_musica(self,musica: str):
        musica_data_list = []
        
        for musica in musica.split(","):
            musica_dev = ' '.join(musica.split())
            
            musica_data = Musica(
                anime_id=self.id,
                musica=musica_dev
            )
            self.db.add(musica_data)
            self.db.commit()
            self.db.refresh(musica_data)
        
        musica_data_dev = self.db.query(Musica).filter(Musica.anime_id == self.id).all()
        musica_data_dev_list = [musica.musica for musica in musica_data_dev]
        
        return musica_data_dev_list

    def create_musica_wiki(self,musica_wiki: str):
        musica_wiki_data_list = []
        
        for musica_wiki in musica_wiki.split(","):
            musica_wiki_dev = ' '.join(musica_wiki.split())
            
            musica_wiki_data = MusicaWiki(
                anime_id=self.id,
                musica_wiki=musica_wiki_dev
            )
            self.db.add(musica_wiki_data)
            self.db.commit()
            self.db.refresh(musica_wiki_data)
        
        musica_wiki_data_dev = self.db.query(MusicaWiki).filter(MusicaWiki.anime_id == self.id).all()
        musica_wiki_data_dev_list = [musica_wiki.musica_wiki for musica_wiki in musica_wiki_data_dev]
        
        return musica_wiki_data_dev_list

    def create_wiki(self,wiki: str):

        wiki_dev = ' '.join(wiki.split())   

        for wiki in wiki.split(","):
            wiki_dev = ' '.join(wiki.split())
            
            wiki_data = Wiki(
                anime_id=self.id,
                wiki=wiki_dev
            )
            self.db.add(wiki_data)
            self.db.commit()
            self.db.refresh(wiki_data)
            
        wiki_data_dev = self.db.query(Wiki).filter(Wiki.anime_id ==  self.id).all()
        wiki_data_dev_list = [wiki.wiki for wiki in wiki_data_dev]
        
        return wiki_data_dev_list


def update_anime_dict(db, id: int):
    anime_data = UpdateAnime(db, id)
    anime_dev = anime_data.update_anime()

    if anime_data.error_run():
        return {"error": "No existeix"}

    pais_dev = anime_data.update_pais()
    director_dev = anime_data.update_director()
    date_dev = anime_data.update_date()
    generes_dev = anime_data.update_generes()
    musica_dev = anime_data.update_musica()
    paraula_dev = anime_data.update_paraula()
    musica_wiki_dev = anime_data.update_musica_wiki()
    
    wiki_dev = anime_data.update_wiki()

    

    anime_dict = {
        "id": anime_dev.id,
        "titol": anime_dev.titol,
        "sinopsi": anime_dev.sinopsi,
        "primer_episodi": anime_dev.primer_episodi,
        "film": anime_dev.film,
        "tipus": anime_dev.tipus,
        "pais": pais_dev,
        "director": director_dev,
        "date": date_dev,
        "generes": generes_dev,
        "musica": musica_dev,
        "musica_wiki" : musica_wiki_dev,
        "paraula" : paraula_dev,
        "wiki" : wiki_dev
    }

    if anime_dev.tipus in ["Series", "OVA"]:
        serie_dev = anime_data.update_serie()
        anime_dict["serie"] = serie_dev
    
    return anime_dict






class UpdateAnime:
    def __init__(self, db, id: int):
        self.db = db
        self.id = id
        self._error = False

    def error_run(self):
        return self._error


    def update_anime(self) -> Anime:
        anime_data = self.db.query(Anime).filter(Anime.id == self.id).first()
        if anime_data is None:
            self._error = True
            return None
            #raise HTTPException(status_code=404, detail="Anime not found")
        
        return anime_data

    def update_pais(self) -> Anime:
        pais_data = self.db.query(Pais).filter(Pais.anime_id == self.id).all()
        if pais_data is None:
            raise HTTPException(status_code=404, detail="Anime not found")
        
        pais_data_list = [pais.pais for pais in pais_data]

        return pais_data_list   

    def update_director(self) -> Anime:
        anime_director_data = self.db.query(AnimeDirector).filter(AnimeDirector.anime_id == self.id).all()

        anime_director_data_list = []

        for anime_director_data in anime_director_data:

            director_data = self.db.query(Director).filter(Director.id == anime_director_data.director_id).first()
            anime_director_data_list.append(director_data.nom)
        
        return anime_director_data_list

    def update_date(self) -> Anime:
        anime_date_data = self.db.query(AnimeDate).filter(AnimeDate.anime_id == self.id).all()

        anime_date_data_list = [anime_date_data.date for anime_date_data in anime_date_data]

        return anime_date_data_list

    def update_generes(self) -> Anime:
        anime_generes_data = self.db.query(AnimeGeneres).filter(AnimeGeneres.anime_id == self.id).all()

        anime_generes_data_list = []

        for anime_generes_data in anime_generes_data:

            generes_data = self.db.query(Generes).filter(Generes.id == anime_generes_data.genre_id).first()
            anime_generes_data_list.append(generes_data.generes)
        
        return anime_generes_data_list
    
    def update_paraula(self) -> Anime:
        anime_paraula_data = self.db.query(AnimeParaula).filter(AnimeParaula.anime_id == self.id).all()

        anime_paraula_data_list = []

        for anime_paraula_data in anime_paraula_data:

            paraula_data = self.db.query(Paraula).filter(Paraula.id == anime_paraula_data.paraula_id).first()
            anime_paraula_data_list.append(paraula_data.paraula)
        
        return anime_paraula_data_list
    
    def update_musica(self) -> Anime:
        
        anime_musica_data = self.db.query(Musica).filter(Musica.anime_id == self.id).all()

        anime_musica_data_list = [anime_musica_data.musica for anime_musica_data in anime_musica_data]
        
        return anime_musica_data_list

    def update_musica_wiki(self) -> Anime:
        anime_musica_wiki_data = self.db.query(MusicaWiki).filter(MusicaWiki.anime_id == self.id).all()

        anime_musica_wiki_data_list = [anime_musica_wiki_data.musica_wiki for anime_musica_wiki_data in anime_musica_wiki_data]
        
        return anime_musica_wiki_data_list

    def update_serie(self) -> Anime:
        anime_serie_data = self.db.query(AnimeSerie).filter(AnimeSerie.anime_id == self.id).first()
        
        if anime_serie_data is None:
            anime_serie_data_list = {
                "durada_dels_capitols": "",
                "ultim_episodis": "",
                "temporades": 0,
                "episodis": 0
            }
        else:
            anime_serie_data_list = {
                "durada_dels_capitols": anime_serie_data.durada_dels_capitols,
                "ultim_episodis": anime_serie_data.ultim_episodis,
                "temporades": anime_serie_data.temporades,
                "episodis": anime_serie_data.episodis
            }
        
        return anime_serie_data_list

    def update_wiki(self) -> Anime:
        anime_wiki_data = self.db.query(Wiki).filter(Wiki.anime_id == self.id).all()
        anime_wiki_data_list = [anime_wiki_data.wiki for anime_wiki_data in anime_wiki_data]
        
        return anime_wiki_data_list
        

class ASeries:
    def __init__(self, db, id: int):
        self.db = db
        self.id = id
        
    def series(self, 
        durada_dels_capitols: str, 
        ultim_episodis: str, 
        temporades: int, 
        episodis: int
    ):
        anime_data = self.db.query(AnimeSerie).filter(AnimeSerie.anime_id == self.id).first()
        
        if anime_data == None:
            anime_data = AnimeSerie(
                durada_dels_capitols=durada_dels_capitols,
                ultim_episodis=ultim_episodis,
                temporades=temporades,
                episodis=episodis,
                anime_id=self.id
            )
        else:
            anime_data.durada_dels_capitols = durada_dels_capitols
            anime_data.ultim_episodis = ultim_episodis
            anime_data.temporades = temporades
            anime_data.episodis = episodis

        self.db.add(anime_data)
        self.db.commit()
        self.db.refresh(anime_data)

    
    def update_serie(self):
        anime_data = self.db.query(AnimeSerie).filter(AnimeSerie.anime_id == self.id).first()

        return anime_data

        
        