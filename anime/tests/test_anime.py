



#def test_get_anime(test_client):
#    response = test_client.get("/api/animes")
#    assert response.status_code == 200

def test_get_anime_id(test_client):
    response = test_client.get("/api/animes/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["titol"] == "L'abella Maia"
    assert data["sinopsi"] == ""
    assert data["primer_episodi"] == "1r-04-1975"
    assert data["film"] == "Manga"
    assert data["tipus"] == "Series"
    assert data["pais"] == ["Japo"]
    assert data["director"] == ["Hiroshi Saito"]
    assert data["date"] == ["05-02-2004"]
    assert data["generes"] == [""]
    assert data["musica"] == ["https://www.youtube.com/watch?v=CNZ-vyQaGAg"]
    assert data["paraula"] == []
    assert data["wiki"] == ["https://ca.wikipedia.org/wiki/L%27abella_Maia"]
    assert data["serie"] == {
        "durada_dels_capitols": "25 min",
        "ultim_episodis": "20-04-1976",
        "temporades": 2,
        "episodis": 52
    }

    
