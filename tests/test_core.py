import xrequest
import asyncio
from xrequest.utils import show
from xrequest.utils.base_headers import HEADERS 


async def test():
    '''
    test = await xrequest.get("https://google.com", session=True)
    '''
    l = await xrequest.get(url='https://google.com', headers=HEADERS['human'])
    f = l.status_code

    print(f"Direct get: {f}")

    # Test with session
    session = xrequest.Session()
    try:
        l2 = await session.get(url='https://google.com')
        f2 = l2.status_code
        print(f"Session get: {f2}")
    finally:
        await session.close()


asyncio.run(test())