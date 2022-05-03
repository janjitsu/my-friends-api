import pytest
from http import HTTPStatus
from app.main import app
from fastapi.testclient import TestClient
from app.tests.test_data import get_test_data
from app.routes.get_data import get_data

client = TestClient(app)
app.dependency_overrides[get_data] = get_test_data

def test_get_friends_of_list():
    """Should return List of friends known by a friend."""
    response = client.get("/friends/Ana")
    assert response.json() == ["Carlos"]

def test_get_friends_of_list_error():
    """Should return Error if friend not found."""
    response = client.get("/friends/Bogus")
    assert response.status_code == HTTPStatus.BAD_REQUEST
