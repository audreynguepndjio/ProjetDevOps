from models import Item
from schemas import ItemCreate

db = []
counter = 1


def get_items():
    return db


def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    return None


def create_item(item: ItemCreate):
    global counter
    new_item = Item(id=counter, **item.dict())
    db.append(new_item)
    counter += 1
    return new_item


def update_item(item_id: int, item: ItemCreate):
    for i, old_item in enumerate(db):
        if old_item.id == item_id:
            updated = Item(id=item_id, **item.dict())
            db[i] = updated
            return updated
    return None


def delete_item(item_id: int):
    global db
    db = [item for item in db if item.id != item_id]
    return {"message": f"Item {item_id} supprimé"}
