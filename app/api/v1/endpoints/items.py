from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

# In-memory storage for demo purposes
items_db = {}


@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100):
    return list(items_db.values())[skip : skip + limit]


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    item_id = len(items_db) + 1
    item_dict = item.model_dump()
    item_dict["id"] = item_id
    items_db[item_id] = item_dict
    return item_dict


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item_dict = item.model_dump()
    item_dict["id"] = item_id
    items_db[item_id] = item_dict
    return item_dict


@router.delete("/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"ok": True} 