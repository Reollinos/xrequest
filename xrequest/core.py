# Bibliotecas
import asyncio
import httpx
from .module import get_engine
from .box.var_box import SCRIPT_NAME as label
from .box.preferences import ResponseWrapper

'''
version 0.0.1;
'''

class Session:
    def __init__(self, timeout=5, headers=None, follow_redirects=True):
        self.client = httpx.AsyncClient(timeout=timeout, headers=headers, follow_redirects=follow_redirects)
    
    async def get(self, url: str | list):
        return await get(url, session=self.client)
    
    async def close(self):
        await self.client.aclose()





async def get(url: str | list, timeout=5, headers=None, follow_redirects=True, session=None):
    # Inicialização de requisição

    
    if not url:
        raise ValueError('URL is none')
    
    else:
        if isinstance(url, (str, list)):
            result = await get_engine.get_process(url, timeout, headers, follow_redirects, session)
            
        
        else:
            raise ValueError('A URL can only be a list or a str.')


    # checagem de preferencia
    final = ResponseWrapper(url, result)

    # resposta final
    return final
    


async def post():
    pass