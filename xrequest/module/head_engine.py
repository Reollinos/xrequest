async def head_process(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.head(url)
        return response
    except:
        raise Exception("head request failed")
