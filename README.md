# xrequest

Simple library for asynchronous HTTP requests.

## Installation

```bash
pip install xrequest

```

## Usage

### Without Session
```python
import xrequest

response = await xrequest.get("https://api.example.com")
```

### With Session (reuse connection)
```python
import xrequest

session = xrequest.Session()
try:
    response = await.session.get("https://api.example.com")
finally:
    await session.close()
```
For now, request is a library that only works for async functions.

´´´python
async def get(
    url: str | list,
    timeout: int = 5,
    headers: dict | None = None,
    follow_redirects: bool = True,
    retries: int = 0,
    session: bool | None = None):
´´´


## License

MIT
 
