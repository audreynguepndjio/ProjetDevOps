import sys
import os

# Ajouter le chemin du projet avant les imports locaux
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API en ligne"}


def test_create_item():
    item = {"name": "stylo", "price": 1.99, "in_stock": True, "description": "Un stylo bleu"}
    response = client.post("/items", json=item)
    assert response.status_code == 200
    assert response.json()["name"] == "stylo"
