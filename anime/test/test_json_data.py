
'''
def test_write_json_data(test_client):
    response = test_client.get("/api/json_data/write")
    assert response.status_code == 200
    assert response.json() == {"message": "Animes saved to file"}


def test_read_json_data(test_client):
    response = test_client.get("/api/json_data/read")
    assert response.status_code == 200
    assert response.json() == {"message": "Animes read from file"}
'''