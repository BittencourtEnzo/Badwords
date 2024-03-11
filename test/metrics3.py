import sys
sys.path.append('../')

from src.badwords2 import main
import pandas as pd
from src.names import hashmap

mapa = hashmap()

validacao = pd.read_csv("./validacao.csv")

nomes_validacao = validacao['Nome']
palavroes_validacao = validacao['palavrao']

true_p = 0
true_n = 0
false_p = 0
false_n = 0

for nome in nomes_validacao:
    if main(nome, mapa):
        print(nome)
        false_p += 1
    else:
        true_n +=1
        

for palavrao in palavroes_validacao:
    if main(palavrao,mapa):
        true_p +=1
    else:
        print("\n",palavrao)
        false_n += 1
        

cm = [[true_p, false_n],[false_p,true_n]]
accuracy = (true_p + true_n)/(true_p + true_n + false_p + false_n)
precision = true_p/(true_p + false_p)
recall = true_p/(true_p + false_n)
f1 = 2*(precision*recall)/(precision+recall)

print("True positives:",true_p)
print("True negatives:",true_n)
print("False positives:",false_p)
print("False negatives:",false_n)


print("CM:",cm)
print("Accuracy:", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1: ", f1)
