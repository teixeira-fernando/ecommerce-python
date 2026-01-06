import pytest
import httpx
from ecommerce.app.api.main import app
from asgi_lifespan import LifespanManager

@pytest.mark.asyncio
async def test_create_order():
    async with LifespanManager(app):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/orders", json={"user": "alice", "products": ["Book", "Pen"]})
        assert response.status_code == 200
        data = response.json()
        assert data["user"] == "alice"
        assert data["products"] == ["Book", "Pen"]
        assert "id" in data
