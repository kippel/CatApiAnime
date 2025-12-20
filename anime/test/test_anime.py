

def test_get_titol(test_client):
    response = test_client.get("/api/animes/titol/Bola de drac")
    assert response.status_code == 200
    assert response.json()["titol"] == "Bola de drac"


def test_get_titol_not_found(test_client):
    response = test_client.get("/api/animes/titol/No existe")
    assert response.status_code == 404
