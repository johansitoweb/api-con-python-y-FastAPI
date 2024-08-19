from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Almacenamiento en memoria
items: Dict[int, Item] = {}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items[item.id] = item
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return items.get(item_id)

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item eliminado"}
    return {"message": "Item no encontrado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
