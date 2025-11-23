import uuid
from app.db.models import Anime

def test_create_anime(test_client, db):
    """Test create anime endpoint"""
    # Clean up before test
    db.query(Anime).filter(Anime.titol == "Test Anime").delete(synchronize_session=False)
    db.commit()

    response = test_client.post(
        "/api/crud/create",
        data={
            "titol": "Test Anime",
            "tipus": "Series",
            "sinopsi": "A test anime synopsis",
            "episodis": 12,
            "sortida_date": "2023-01-01",
            "final_date": "2023-03-31",
            "film": "..."
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "msg" in data
    assert data["msg"]["titol"] == "Test Anime"
    assert data["msg"]["tipus"] == "Series"


    # Clean up after test
    db.query(Anime).filter(Anime.titol == "Test Anime").delete(synchronize_session=False)
    db.commit()