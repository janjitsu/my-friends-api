import pytest
from http import HTTPStatus
from app.main import app
from fastapi.testclient import TestClient
from app.tests.test_data import get_test_data
from app.routes.get_data import get_data

client = TestClient(app)
app.dependency_overrides[get_data] = get_test_data

def test_get_friends():
    """Should return 200."""
    response = client.get("/friends")
    assert response.status_code == HTTPStatus.OK

def test_get_friend_list():
    """Should return List of friends."""
    response = client.get("/friends")
    assert "Ana" in response.json()
    assert "Carlos" in response.json()
    assert "Julia" in response.json()

