from fastapi import FastAPI
from .badwords2 import main

app = FastAPI()

@app.get("/")
def home():
    return "No URL, depois da barra (/), digite o nome que deseja classificar."
    

@app.get("/{nome}")
def classificador(nome: str):
    
    if main(nome):
        return "Desculpe, é um palavrão. Poderia tentar de novo? Nome: ", nome
    else:
        return "Não é um palavrão. Nome: ", nome