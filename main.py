import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}
  
@app.get("/teste1")
async def funcaoteste():
    return {"message": True, "num_aleatorio": random.randint(0, 1000)}

@app.get("/teste2")
async def funcaoteste2():
    return {"message": "Teste para o CI/CD"}

