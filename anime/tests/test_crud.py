from app.db.models import Anime, AnimeSerie

def test_create_anime(test_client, db):
    """Test create anime endpoint"""
    # Clean up before test
    db.query(Anime).filter(Anime.titol == "Test Anime").delete()
    db.commit()

    response = test_client.post(
        "/api/crud/create",
        data={
            "titol": "Test Anime",
            "tipus": "Series",
            "sinopsi": "",
            "primer_episodi": "2023-01-01",
            "film": "Manga",
            "pais": "",
            "director": ""
        }
    )
    assert response.status_code == 200
    data = response.json()

    assert data["titol"] == "Test Anime"
    assert data["tipus"] == "Series"
    assert data["sinopsi"] == ""
    assert data["primer_episodi"] == "2023-01-01"
    assert data["film"] == "Manga"   
    assert data["pais"] == []
    assert data["director"] == []
    
    # Clean up after test
    db.query(Anime).filter(Anime.titol == "Test Anime").delete()
    db.commit()


