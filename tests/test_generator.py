#!/usr/bin/env python3

async def test_ping(iu9lab_client):
    response = await iu9lab_client.get(
        '/ping',
    )
    assert response.status_code == 200
