import pytest
from app.core.friends import Friends
from app.tests.test_data import data

friends = Friends(data)

def test_all():
    result = friends.all()

    assert "Ana" in result
    assert "Carlos" in result
    assert "Julia" in result

def test_of():
    result = friends.of("Ana")

    assert "Carlos" in result

def test_add():
    friends.add("Test Name", ["Peter"])

    result = friends.of("Peter")

    assert "Test Name" in result

def test_related():
    result = friends.related("Ana")

    assert "Julia" in result
    assert "Peter" in result
