import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def test_client():
    print("Setting up Test Client")
    with TestClient(app) as client:
        yield client