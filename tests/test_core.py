import xrequest
import asyncio
from xrequest.utils import show
from xrequest.utils.base_headers import HEADERS


async def test():
    j = {
      "title": "Meu post",
      "body": "Olá mundo",
      "userId": 1
    }
    sites = await xrequest.get('https://httpbin.org/')
    s = sites.status_code
    print(s)


asyncio.run(test())
