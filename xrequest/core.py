# Bibliotecas
import asyncio
import httpx
from .module import get_engine, post_engine, put_engine, head_engine, patch_engine, options_engine
from .box.var_box import SCRIPT_NAME as label
from .box.preferences import ResponseWrapper

'''
version 0.2.0;
'''

# modulo de sessão
class Session:
    def __init__(self, timeout=5, headers=None, follow_redirects=True):
        self.client = httpx.AsyncClient(timeout=timeout, headers=headers, follow_redirects=follow_redirects)

    async def get(self, url: str | list):
        return await get(url, session=self.client)

    async def close(self):
        await self.client.aclose()




# get
async def get(
    url: str | list,
    timeout: int = 5,
    headers: dict | None = None,
    follow_redirects: bool = True,
    retries: int = 0,
    session: bool | None = None) -> list | str | int:
    # Inicialização de requisição

    # testadores de valores
    if not isinstance(timeout, int):
        raise ValueError("timeout can't be anything more than int")

    if not isinstance(headers, (dict, type(None))):
        raise ValueError('headers can only be dict or None')

    if not isinstance(follow_redirects, bool):
        raise ValueError('follow_redirects can only be a boolean')

    if not isinstance(retries, int):
        raise ValueError('retries can only be a int')

    if not isinstance(session, (bool, type(None))):
        raise ValueError('session can only be boolean and None')

    if not url:
        raise ValueError('URL is none.')


    # requisitor da resequiçao
    if not isinstance(url, (str, list)):
        raise ValueError('A URL can only be a list or a str.')

    else:
        result = await get_engine.get_process(
            url,
            timeout,
            headers,
            follow_redirects,
            retries,
            session,
        )

        # checagem de preferencia
        final = ResponseWrapper(url, result)

        # resposta final
        return final




# post
async def post(
    url: str,
    json: dict | None = None):

    if not url:
        raise ValueError('The URL is none.')

    else:
        if isinstance(url, (str, list)):
            result = await post_engine.post_process(url, json)

        return result



async def put(url: str, json: dict):
    if not url:
        raise ValueError('The URL is None')

    else:
        if isinstance(url, (str, list)):
            result = await put_engine.put_process(url, json)

        return result



async def delete(url: str):
    if not url:
        raise ValueError('The URL is None')

    else:
        if isinstance(url, (str, list)):
            result = await delete_engine.delete_process(url)

        return result



async def head(url: str):
    if not url:
        raise ValueError('The URL is None')

    else:
        if isinstance(url, (str, list)):
            result = await head_engine.head_process(url)

        return result



async def patch(url: str, json: dict = None):
    if not url:
        raise ValueError('The URL is None')

    if not json:
        raise ValueError('The JSON is None')

    else:
        if isinstance(url, (str, list)):
            result = await path_engine.patch_process(url)

        return result



async def options(url):
    if not url:
        raise ValueError('The URL is None')

    else:
        if isinstance(url, (str, list)):
            result = await options_engine.options_process(url)

        return result
