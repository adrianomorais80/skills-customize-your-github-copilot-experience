"""Starter code for the 'Building REST APIs with FastAPI' assignment.

Run locally:
  pip install fastapi uvicorn
  uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment API")


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


# In-memory storage for assignment practice
items_db: dict[int, Item] = {}


@app.get("/")
def read_root():
    # TODO: return a welcome JSON message
    return {"message": "TODO"}


@app.get("/health")
def health_check():
    # TODO: return health status JSON
    return {"status": "TODO"}


@app.post("/items")
def create_item(item: Item):
    # TODO: prevent duplicate IDs and save item in items_db
    # Raise HTTPException(status_code=400, detail="...") when needed.
    return item


@app.get("/items")
def list_items():
    # TODO: return all items as a list
    return []


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: return item if found, otherwise raise 404
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: update existing item, otherwise raise 404
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: delete existing item and return a confirmation message
    # Raise 404 if item does not exist.
    raise HTTPException(status_code=404, detail="Item not found")
