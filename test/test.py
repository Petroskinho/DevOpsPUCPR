import pytest
from src.main import avaliar_aluno, NotasAluno

@pytest.mark.asyncio
async def test_avaliar_aprovado():
    notas = NotasAluno(nota1=8.0, nota2=7.5, nota3=9.0)
    resultado = await avaliar_aluno(notas)
    assert resultado["status"] == "Aprovado"
    assert round(resultado["media"], 2) == 8.17

@pytest.mark.asyncio
async def test_avaliar_reprovado():
    notas = NotasAluno(nota1=5.0, nota2=6.0, nota3=5.5)
    resultado = await avaliar_aluno(notas)
    assert resultado["status"] == "Reprovado"
    assert round(resultado["media"], 2) == 5.5

@pytest.mark.asyncio
async def test_avaliar_na_trave():
    notas = NotasAluno(nota1=7.0, nota2=7.0, nota3=7.0)
    resultado = await avaliar_aluno(notas)
    assert resultado["status"] == "Aprovado"
    assert resultado["media"] == 7.0