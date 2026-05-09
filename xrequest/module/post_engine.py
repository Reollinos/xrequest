import asyncio
import httpx

async def post_process(url, json):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=json)
        return response
    except:
        pass