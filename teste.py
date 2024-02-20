""" 
import pandas as pd
names_mas = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-mas-10000.csv")
names_fem = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-fem-10000.csv")

listinha = names_mas['nome']
print(listinha[0])
#def comparar_nomes(nome):
#    nome = nome.upper()
#    no_mas = names_mas[names_mas.nome == nome]
#    #print(no_mas)
#    no_fem = names_fem[names_fem.nome == nome]
#    if (len(no_mas) >0) or (len(no_fem) > 0):
#        return True
#    return False

palavra = "putamerda"
lista = ["puta", "merda", "lixo", "droga"]

for palavrao in lista:
    if palavra.__contains__(palavrao):
        print("Funcionou")
"""

dic = {"a":1,"b":2}

var = "a"

print(dic[var])