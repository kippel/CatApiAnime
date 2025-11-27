from app.db.models import Anime, AnimeSerie

def test_create_anime(test_client, db):
    """Test create anime endpoint"""
    # Clean up before test
    db.query(Anime).filter(Anime.titol == "Test Anime").delete(synchronize_session=False)
    db.commit() 

    response = test_client.post(
        "/api/crud/create",
        data={
            "titol": "Test Bola de Drac",
            "tipus": "Series",
            "sinopsi": "",
            "primer_episodi": "26-02-1986",
            "film": "Manga",
            "pais": "Japan", 
            "director": "Akira Toriyama",
            "date": "26-02-1986",
            "generes": "Sci-Fi",
            "paraula": "Test Anime",
            "musica": "https://www.youtube.com/watch?v=L4auFrAK-mQ"
        }
    )
    assert response.status_code == 200
    data = response.json()

    assert data["titol"] == "Test Bola de Drac"
    assert data["tipus"] == "Series"
    assert data["sinopsi"] == ""
    assert data["primer_episodi"] == "26-02-1986"
    assert data["film"] == "Manga"   
    assert data["pais"] == ["Japan"]
    assert data["director"] == ["Akira Toriyama"]
    assert data["date"] == ["26-02-1986"]
    assert data["generes"] == ["Sci-Fi"]
    assert data["paraula"] == ["Test Anime"]
    assert data["musica"] == ["https://www.youtube.com/watch?v=L4auFrAK-mQ"]
    
    
    # Clean up after test
    db.query(Anime).filter(Anime.titol == "Test Anime").delete(synchronize_session=False)
    db.commit()

'''
durada_dels_capitols: Mapped[str]   = mapped_column(String) 
ultim_episodis: Mapped[str] = mapped_column(String)
temporades: Mapped[int] = mapped_column(Integer)
episodis: Mapped[int] = mapped_column(Integer)
'''

'''
def test_create_series_id(test_client, db):
    """Test create series endpoint"""   
    # Clean up before test
    db.query(AnimeSerie).filter(AnimeSerie.durada_dels_capitols == "25 min").delete()
    db.commit()

    response = test_client.post(
        "/api/crud/serie/1",
        data={
            "durada_dels_capitols": "25 min",
            "ultim_episodis": "19-05-1989",
            "temporades": 5,
            "episodis": 153,
        }
    )
    assert response.status_code == 200
    data = response.json()

    assert data["durada_dels_capitols"] == "25 min"
    assert data["ultim_episodis"] == "19-05-1989"
    assert data["temporades"] == 5
    assert data["episodis"] == 153
    
    # Clean up after test
    db.query(AnimeSerie).filter(AnimeSerie.durada_dels_capitols == "25 min").delete()
    db.commit() 
'''