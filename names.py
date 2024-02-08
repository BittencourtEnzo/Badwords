
import pandas as pd
names_mas = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-mas-10000.csv")
names_fem = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-fem-10000.csv")

def comparar_nomes(nome):
    nome = nome.upper()
    no_mas = names_mas[names_mas.nome == nome]
    #print(no_mas)
    no_fem = names_fem[names_fem.nome == nome]
    if (len(no_mas) >0) or (len(no_fem) > 0):
        return True
    return False