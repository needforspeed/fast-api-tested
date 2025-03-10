from fastapi import FastAPI
import uvicorn

from .models import Item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return {"item_id": item.id, "item_name": item.name}

def run():
    """Entry point for starting the application."""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
