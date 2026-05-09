# Bibliotecas
import asyncio
import httpx
from .module import get_engine, post_engine
from .box.var_box import SCRIPT_NAME as label
from .box.preferences import ResponseWrapper

'''
version 0.0.3;
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
    session: bool | None = None):
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
    
    if url:
        if not isinstance(url, (str, list)):
            raise ValueError('A URL can only be a list or a str.')
        
        else:
            result = await get_engine.get_process(
                url,
                timeout,
                headers,
                follow_redirects,
                retries,
                session=session,
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
        raise ValueError('URL is none.')
    
    else:
        if isinstance(url, (str, list)):
            result = await post_engine.post_process(url, json)
        
        return result