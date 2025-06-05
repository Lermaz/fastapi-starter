import pytest

@pytest.mark.asyncio
async def test_posts_ping(client):
    resp = await client.get("/posts/ping")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "pong"} 