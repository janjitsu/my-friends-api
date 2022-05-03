import pytest
from http import HTTPStatus
from app.main import app
from fastapi.testclient import TestClient
from app.tests.test_data import get_test_data
from app.routes.get_data import get_data

client = TestClient(app)
app.dependency_overrides[get_data] = get_test_data

def test_get_related_friends_list():
    """Should return List of related friends."""
    response = client.get("/friends/Ana/related")
    assert response.json() == ["Julia", "Peter"]

def test_get_related_friends_error():
    """Should return error when friend does not exist."""
    response = client.get("/friends/Bogus/related")
    assert response.status_code == HTTPStatus.BAD_REQUEST


