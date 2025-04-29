from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NotasAluno(BaseModel):
    nota1: float
    nota2: float
    nota3: float

@app.post("/avaliar")
async def avaliar_aluno(notas: NotasAluno):
    media = (notas.nota1 + notas.nota2 + notas.nota3) / 3
    if media >= 7.0:
        return {"media": media, "status": "Aprovado"}
    else:
        return {"media": media, "status": "Reprovado"}