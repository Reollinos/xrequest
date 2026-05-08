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
response = await session.get("https://api.example.com")
finally:
await session.close()
```

## License

MIT
 