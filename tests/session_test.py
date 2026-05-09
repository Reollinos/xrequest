import asyncio
import xrequest

async def test():
    # Test with session
    session = xrequest.Session()
    try:
        l2 = await session.get(url='https://google.com')
        f2 = l2.status_code
        print(f"Session get: {f2}")
    finally:
        await session.close()


asyncio.run(test())