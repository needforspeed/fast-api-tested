from fastapi import FastAPI
from .models import Item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return {"item_id": item.id, "item_name": item.name}
