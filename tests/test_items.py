import sys
import os
from fastapi.testclient import TestClient
from main import app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
