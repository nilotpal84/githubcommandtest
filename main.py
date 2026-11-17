from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My Azure FastAPI App")


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"status": "healthy", "message": "FastAPI is running on Azure!!"}


@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}


@app.post("/items/")
def create_item(item: Item):
    return {"received": item.name, "total_with_tax": round(item.price * 1.18, 2)}
