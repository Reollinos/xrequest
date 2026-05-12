import httpx

async def put_process(url, json):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(url, json=json)
        return response
    except:
        raise Exception("PUT request failed")
