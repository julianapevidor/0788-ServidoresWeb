# Gravar como 'hello_fastapi.py'
# Executar:
#       $ uvicorn hello_fastapi:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World!"}
#:

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"2xitem_id": item_id * 2, "q": q}
#:

# Por omissão FastAPI gera JSON

# Protocolo HTTP possui um conjunto de métodos (isto é, de mensagens):
#   - GET: obter um recurso (ler)
#   - POST: enviar dados para o servidor / criar um registo no servidor
#   - PUT: semelhante a POST mas dados são enviados como um upload
#   - DELETE: apagar recursos no lado do servidor
#   - HEAD
#   - etc.