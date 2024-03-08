from fastapi import FastAPI
from .badwords2 import main
from .names import hashmap
import pandas as pd


app = FastAPI()
mapa = hashmap()

@app.get("/")
def home():
    return "No URL, depois da barra (/), digite o nome que deseja classificar."
    

@app.get("/{nome}")
def classificador(nome: str):
    
    if main(nome, mapa):
        return "true"
    else:
        return "false"
    