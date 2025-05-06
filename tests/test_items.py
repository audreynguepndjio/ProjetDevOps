from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


client = TestClient(app)


def test_create_item():
    response = client.post(
        "/items", json={"name": "Stylo", "price": 2.5, "in_stock": True}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Stylo"


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
