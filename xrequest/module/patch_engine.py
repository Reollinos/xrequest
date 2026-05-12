async def patch_process(url, json):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.patch(url, json=json)
        return response
    except:
        raise Exception("patch request failed")
