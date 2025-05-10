# Correction Flake8 E402/W291 pour GitHub Actions
import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
