import pytest
from http import HTTPStatus
from app.main import app
from fastapi.testclient import TestClient
from app.tests.test_data import get_test_data
from app.routes.get_data import get_data

client = TestClient(app)
app.dependency_overrides[get_data] = get_test_data

def test_add_friends():
    """Should add friend."""

    response = client.post(
        "/friends",
        headers={"Content-Type": "application/json"},
        json={
            "name": "Test Name",
            "friends": ["Peter"]
        },
    )
    assert response.status_code == HTTPStatus.CREATED

def test_add_friends_error_when_friend_not_exists():
    """Should return error when friends list invalid."""

    response = client.post(
        "/friends",
        headers={"Content-Type": "application/json"},
        json={
            "name": "Test Name",
            "friends": ["Bogus"]
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_add_friends():
    """Should list new friend on known friends list."""

    client.post(
        "/friends",
        headers={"Content-Type": "application/json"},
        json={
            "name": "Test Name",
            "friends": ["Peter"]
        },
    )
    response = client.get("/friends/Peter")
    assert "Test Name" in response.json()


