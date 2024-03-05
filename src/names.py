import pandas as pd
nomes_ibge = pd.read_csv("../data/nomes.csv")

names_list = nomes_ibge['nome']
l = len(names_list)
dic = {}
for nome in names_list:
    dic[nome] = nome

def names(palavra):
    if palavra.upper() in dic:
        return False
    return True
