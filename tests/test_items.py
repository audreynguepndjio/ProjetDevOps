import sys
import os

# Ajouter le chemin du projet avant les imports locaux
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API en ligne"}


def test_create_item():
    item = {"name": "stylo", "price": 1.99, "in_stock": True}
    response = client.post("/items", json=item)
    assert response.status_code == 200
    assert response.json()["name"] == "stylo"
    assert response.json()["id"] == 1


def test_read_item():
    item = {"name": "crayon", "price": 0.99, "in_stock": True}
    client.post("/items", json=item)
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "stylo"
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item non trouvé"


def test_update_item():
    item = {"name": "stylo", "price": 1.99, "in_stock": True}
    client.post("/items", json=item)
    updated_item = {"name": "stylo rouge", "price": 2.49, "in_stock": False}
    response = client.put("/items/1", json=updated_item)
    assert response.status_code == 200
    assert response.json()["name"] == "stylo rouge"
    assert response.json()["price"] == 2.49
    assert response.json()["in_stock"] == False
    response = client.put("/items/999", json=updated_item)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item non trouvé"


def test_delete_item():
    item = {"name": "crayon", "price": 0.99, "in_stock": True}
    client.post("/items", json=item)
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
    response = client.get("/items/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item non trouvé"
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item non trouvé"
