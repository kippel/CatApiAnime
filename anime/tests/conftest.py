from fastapi.testclient import TestClient
import pytest
from app.main import app    

@pytest.fixture
def test_client():
    print("Setting up Test Client")
    with TestClient(app) as client:
        yield client

