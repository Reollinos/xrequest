import xrequest
import asyncio
from xrequest.utils import show
from xrequest.utils.base_headers import HEADERS


async def test():

    sites = await xrequest.get(['https://httpbin.org/','https://httpbin.org/','https://httpbin.org/'])
    s = sites.text
    print(s)


asyncio.run(test())
