




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
    assert data["generes"] == ["Fantasia"]
    assert data["musica"] == ["https://www.youtube.com/watch?v=CNZ-vyQaGAg"]
    assert data["paraula"] == []
    assert data["wiki"] == ["https://ca.wikipedia.org/wiki/Abella_Maia"]

    assert data["serie"]["durada_dels_capitols"] == "25 min"
    assert data["serie"]["ultim_episodis"] == "20-04-1976"
    assert data["serie"]["temporades"] == 2
    assert data["serie"]["episodis"] == 52


def test_get_anime_id_dos(test_client):

    response = test_client.get("/api/animes/2")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 2
    assert data["titol"] == "Bola de drac"
    assert data["sinopsi"] == ""
    assert data["primer_episodi"] == "26-02-1986"
    assert data["film"] == "Manga"
    assert data["tipus"] == "Series"
    assert data["pais"] == ["Japo"]
    assert data["director"] == ["Minoru Okazaki", "Daisuke Nishio"]
    assert data["date"] == []
    assert data["generes"] == ["Action"]
    assert data["musica"] == ["Shunsuke Kikuchi", "https://www.youtube.com/watch?v=cENvh9nQjNc", "https://www.youtube.com/watch?v=puSHHK8LOlQ"]
    assert data["paraula"] == ["Bola de drac"]
    assert data["wiki"] == ["https://en.wikipedia.org/wiki/Bola_de_drac"]

    assert data["serie"]["durada_dels_capitols"] == ""
    assert data["serie"]["ultim_episodis"] == "19 de abril de 1989"
    assert data["serie"]["temporades"] == 0
    assert data["serie"]["episodis"] == 153

