import httpx
import asyncio

async def get_process(url, timeout, headers, follow_redirects,retries, session=None):
    url = [url] if isinstance(url, str) else url

    num = 0

    while num <= retries:
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

            return responses
        
        except Exception as exc:
            num += 1
            if num > retries:
                raise Exception(f'The connection was attempted {num} times, but there was no response.') from exc
            # Continue to next retry
