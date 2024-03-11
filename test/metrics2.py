import sys
sys.path.append('../')

from src.badwords2 import main
from src.names import hashmap
import pandas as pd
import time

names_jae = pd.read_csv("../data/nomes_jae.csv")
names_sky = pd.read_csv("../data/nomes_sky.csv")
ti = time.time()
positives = 0
negatives = 0
lista_positives = []

mapa = hashmap()

lista1 = names_jae['name']
for i in range(0,len(lista1)):
    if main(lista1[i],mapa):
        positives += 1
        lista_positives.append(lista1[i])
    else:
        negatives += 1

lista2 = names_sky['name']
for i in range(0,len(lista2)):
    if main(lista2[i],mapa):
        positives += 1
        lista_positives.append(lista2[i])
    else:
        negatives += 1
        
print("Positivos: ",positives)
print("Negativos: ",negatives)

#for palavra in lista_positives:
#    print(palavra)
#tf = time.time()

#print(tf-ti)
