class ResponseWrapper:
        def __init__(self, url, result):
            self._result = result if isinstance(result, list) else [result]
            self._url = url

        def __getitem__(self, index):
            return self._result[index]

        def __len__(self):
            return len(self._result)


        # textos html
        @property
        def text(self):
            if isinstance(self._url, list) and len(self._url) > 1:
                return self._result.text
            
            elif isinstance(self._url, list) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].text

        # status do site
        @property
        def status_code(self):
            # return [r.status_code for r in self._result] if isinstance(self._result, (list)) else self._result[0].status_code

            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.status_code for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].status_code
            
        # json de sites apis
        @property
        def json(self):
            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.json() for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].json()
            
        # headers de sites
        @property
        def headers(self):
            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.headers for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].headers
            
        # contents dos sites
        @property
        def content(self):
            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.content for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].content
            
        # self._url final do site alvo
        @property
        def url(self):
            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.self._url for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].self._url
            
        #  cookies do site
        @property
        def cookies(self):
            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.cookies for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].cookies
            
        # historico
        @property
        def history(self):
            if isinstance(self._url, (list)) and len(self._url) > 1:
                return [r.history for r in self._result]
                
            elif isinstance(self._url, (list)) and len(self._url) == 1 or isinstance(self._url, str):
                return self._result[0].history
            


            
            