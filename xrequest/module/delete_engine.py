
import httpx

async def delete_process(url):
    if not url:
        raise ValueError('A URL can only be a list or a str.')

    else:
        if isinstance(url, str):
            url = [url]

        for u in url:
            async with httpx.AsyncClient() as client:
                response = await client.delete(u)
