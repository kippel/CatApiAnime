    
def test_read_root(test_client):
    """Test root endpoint - should return user list"""
    response = test_client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert "user" in response.json()