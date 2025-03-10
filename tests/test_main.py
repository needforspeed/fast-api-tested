from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post(
        "/items/",
        json={"id": 1, "name": "Test Item"}
    )
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item_name": "Test Item"}
