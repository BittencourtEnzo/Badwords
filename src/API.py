from fastapi import FastAPI
from .badwords2 import main

app = FastAPI()

@app.get("/")
def home():
    return "No URL, depois da barra (/), digite o nome que deseja classificar."
    

@app.get("/{nome}")
def classificador(nome: str):
    
    if main(nome):
        return "true"
    else:
        return "false"