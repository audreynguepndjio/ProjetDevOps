from fastapi import FastAPI, HTTPException
from typing import List
from models import Item
from schemas import ItemCreate
from crud import get_items, get_item, create_item, update_item, delete_item

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API en ligne"}


@app.get("/items", response_model=List[Item])
def read_items():
    return get_items()


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return item


@app.post("/items", response_model=Item)
def create_new_item(item: ItemCreate):
    return create_item(item)


@app.put("/items/{item_id}", response_model=Item)
def update_existing_item(item_id: int, item: ItemCreate):
    updated = update_item(item_id, item)
    if updated is None:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return updated


@app.delete("/items/{item_id}")
def delete_existing_item(item_id: int):
    result, status_code = delete_item(item_id)
    if status_code == 404:
        raise HTTPException(status_code=404, detail=result["detail"])
    return result
