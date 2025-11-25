from app.db.models import Anime, Pais


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
        for pais in pais.split(","):

            pais_dev = ' '.join(pais.split())

            pais_data = Pais(
                anime_id=self.id,
                pais=pais_dev
            )
            pais_data_list.append(pais)
            self.db.add(pais_data)
            self.db.commit()
            self.db.refresh(pais_data)

        pais_data_dev = self.db.query(Pais).filter(Pais.anime_id == self.id).all()
        
        pais_data_dev_list = []
        for pais in pais_data_dev:
            pais_data_dev_list.append(pais.pais)
        
        return pais_data_dev_list
        

class UpdateAnime:
    def __init__(self, db, id: int):
        self.db = db
        self.id = id
        

    def update_anime(self) -> Anime:
        anime_data = self.db.query(Anime).filter(Anime.id == self.id).first()
        if anime_data is None:
            raise HTTPException(status_code=404, detail="Anime not found")
        
        return anime_data

    def update_pais(self) -> Anime:
        pais_data = self.db.query(Pais).filter(Pais.anime_id == self.id).all()
        if pais_data is None:
            raise HTTPException(status_code=404, detail="Anime not found")
        
        pais_data_list = []
        for pais in pais_data:
            pais_data_list.append(pais.pais)

        return pais_data_list   