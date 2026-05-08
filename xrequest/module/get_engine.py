import httpx
import asyncio

async def get_process(url, timeout, headers, follow_redirects, session):
    url = [url] if isinstance(url, str) else url

    try:
        if session is None:
            async with httpx.AsyncClient(timeout=timeout, headers=headers, follow_redirects=follow_redirects) as client:
                responses = await asyncio.gather(
                    *[client.get(urlu) for urlu in url]
                )
        
        else:
            responses = await asyncio.gather(
                *[session.get(urlu) for urlu in url]
            )
    
    except:
        raise Exception('httpx error. please, try again later.')

    return responses