from models import Item
from schemas import ItemCreate

items = []


def get_items():
    return items


def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return None


def create_item(item: ItemCreate):
    item_id = len(items) + 1
    # Créer un nouvel item à partir des données de ItemCreate
    new_item = Item(
        id=item_id, name=item.name, price=item.price, in_stock=item.in_stock
    )
    items.append(new_item)
    return new_item


def update_item(item_id: int, item: ItemCreate):
    for i, existing_item in enumerate(items):
        if existing_item.id == item_id:
            updated_item = Item(
                id=item_id, name=item.name, price=item.price, in_stock=item.in_stock
            )
            items[i] = updated_item
            return updated_item
    return None


def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"message": "Item deleted"}, 200
    return {"detail": "Item non trouvé"}, 404
