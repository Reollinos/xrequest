async def options_process(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.options(url)
        return response
    except:
        raise Exception("options request failed")
