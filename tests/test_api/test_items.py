from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_item():
    item_data = {"name": "Test Item", "price": 10.5, "is_offer": True}
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert data["is_offer"] == item_data["is_offer"]
    assert "id" in data


def test_read_item():
    # First create an item
    item_data = {"name": "Test Item", "price": 10.5, "is_offer": True}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]

    # Then read it
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]


def test_read_nonexistent_item():
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404 
