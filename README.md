# xrequest

Biblioteca simples para requisições HTTP assíncronas.

## Instalação

```bash
pip install xrequest
```

## Uso

### Sem Session
```python
import xrequest

response = await xrequest.get("https://api.example.com")
```

### Com Session (reutilizar conexão)
```python
import xrequest

session = xrequest.Session()
try:
    response = await session.get("https://api.example.com")
finally:
    await session.close()
```

## Licença

MIT
