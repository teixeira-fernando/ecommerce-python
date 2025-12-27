from fastapi.testclient import TestClient

from ecommerce.app.api.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders", json={"user": "alice", "products": ["Book", "Pen"]})
    assert response.status_code == 200
    data = response.json()
    assert data["user"] == "alice"
    assert data["products"] == ["Book", "Pen"]
    assert "id" in data
