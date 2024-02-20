
import pandas as pd
names_mas = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-mas-10000.csv")
names_fem = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-fem-10000.csv")

listinha = names_mas['nome']
l = len(listinha)
dic = {}
for nome in listinha:
    dic[nome] = nome

listinha = names_fem['nome']
l = len(listinha)
for nome in listinha:
    dic[nome] = nome




def names(palavra):
    if palavra.upper() in dic:
        return False
    return True