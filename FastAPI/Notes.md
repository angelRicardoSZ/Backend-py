# FastAPI

Installation 

```bash
pip install fastapi uvicorn 
```

Example

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

run 

```bash
uvicorn main:app --reload
```

Test

```
http://127.0.0.1:8000/items/5?q=somequery
```

Output

```
{"item_id": 5, "q": "somequery"}
```

Docs

```
http://127.0.0.1:8000/docs
```



## Dependences

- [Uvicorn](https://www.uvicorn.org/) is an ASGI web server implementation for Python.

  ```python
  pip install uvicorn
  ```

  example:

  ```python
  async def app(scope, receive, send):
      assert scope['type'] == 'http'
  
      await send({
          'type': 'http.response.start',
          'status': 200,
          'headers': [
              [b'content-type', b'text/plain'],
          ],
      })
      await send({
          'type': 'http.response.body',
          'body': b'Hello, world!',
      })
  ```

  run the server

  ```python
  uvicorn example:app
  ```

- [Starlette](https://www.starlette.io/): a lightweight [ASGI](https://asgi.readthedocs.io/en/latest/) framework/toolkit

  ```python
  pip3 install starlette
  pip3 install uvicorn
  ```

  Example

  ```python
  from starlette.applications import Starlette
  from starlette.responses import JSONResponse
  from starlette.routing import Route
  
  
  async def homepage(request):
      return JSONResponse({'hello': 'world'})
  
  
  app = Starlette(debug=True, routes=[
      Route('/', homepage),
  ])
  ```

  run

  ```python
  uvicorn example:app
  ```

- [Pydantic](https://pydantic-docs.helpmanual.io/) Data validation and settings management

​	  Example

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'  # default value
    signup_ts: Optional[datetime] = None # optional value
    friends: List[int] = [] 

# Input
external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
# instance
user = User(**external_data)
print(user.id)
#> 123
print(repr(user.signup_ts))
#> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
#> [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
```

Validation

```python
from pydantic import ValidationError
try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())
```

