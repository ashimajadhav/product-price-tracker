import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Product Price Tracker" in response.data


def test_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert b"Laptop" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}