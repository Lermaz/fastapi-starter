import pytest

@pytest.mark.asyncio
async def test_auth_ping(client):
    resp = await client.get("/auth/ping")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "pong"} 