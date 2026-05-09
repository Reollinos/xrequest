import xrequest
import asyncio
from xrequest.utils import show
from xrequest.utils.base_headers import HEADERS 


async def test():
    sites = await xrequest.get(['https://google.com'], timeout=6)
    s = sites.status_code
    print(s)

   
asyncio.run(test())