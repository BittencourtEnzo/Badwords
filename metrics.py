import pandas as pd
from badwords2 import main

lista_teste1 = ["acefalo", "arrombada", "arrombado", "asno", "babaca", "babuino", "baitola", "biba", "bicha", "bixa", "bixinha", "bobo", "boceta", "boceta", "boquete", "borra", "bosta", "buceta", "bundao", "burro", "cacete", "cadela", "cagar", "cala", "cale", "caralho", "caralio", "chupe", "come", "corno", "cu", "cusao", "cuzao", "desgracado", "disgracado", "egua", "enraba", "fdp", "fiderapariga", "fidumaegua", "filhodaputa", "filhodeumaputa", "foda", "fodase", "foder", "fuder", "fudeu", "fudido", "gay", "grelo", "idiota", "inferno", "jegue", "louco", "macaco", "mamar", "marica", "merda", "mijao", "otario", "pariu", "pau", "peidar", "pica", "pinto", "piriguete", "piroca", "piru", "porra", "puta", "quinto", "rapariga", "retardado", "rola", "siririca", "tesuda", "tomar", "vagabundo", "vaite", "veado", "velha", "viado", "xereca", "filhodaputa", "filhodaégua", "filhodeumaputa", "filhodeumaégua", "filhodumaputa", "filhodumaégua", "fodase", "vaidarocu", "vaidarorabo", "vaisefoder", "vaitefoder", "vaitomanocu", "vaitomanorabo", "vaitomarnocu", "vaitomarnorabo"]
lista_teste2 = ["anal", "anus", "arse", "ass", "assfuck", "assmonkey", "assmuncher", "asswhore", "balls", "ballsack", "biatch", "bitch", "blowjob", "bollock", "badfuck", "beatoff", "bigass", "boner", "boob", "bugger", "butt", "buttplug", "clitoris", "cock", "coon", "crap", "cunt", "damn", "dick", "dickless", "dike", "dildo", "dyke", "dong", "drug", "drunk", "eatballs", "eatme", "excrement", "fag", "felching", "fellatio", "flange", "fuc", "fuck", "fucka", "fucked", "fucker", "fudgepacker", "hell", "homo", "jizz", "muff", "mothafucker", "nigga", "nigger", "penis", "piss", "poop", "prick", "pube", "pussy", "queer", "scrotum", "sex", "shit", "slut", "spunk", "tit", "tosser", "turd", "twat", "vomit", "vagina", "wank", "whore", "wtf", "wuss", "yellowman", "zipperhead"]

names_mas = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-mas-10000.csv")
names_fem = pd.read_csv("/home/enzo.bittencourt/Badwords/Badwords/ibge-fem-10000.csv")

lista_teste3 = names_mas['nome']
lista_teste4 = names_fem['nome']

def metricas():
    false_p=0
    false_n=0
    true_p=0
    true_n=0
    
    for word in lista_teste1:
        if main(word):
            true_p +=1
        else:
            false_n +=1
            print(word)
    
    for word in lista_teste2:
        if main(word):
            true_p +=1
        else:
            false_n +=1
            print(word)

    for word in lista_teste3:
        if main(word):
            false_p +=1
            #print(word)
        else:
            true_n +=1

            
    for word in lista_teste4:
        if main(word):
            false_p +=1
            #print(word)
        else:
            true_n +=1


    cm = [[true_p, false_n],[false_p,true_n]]
    print(true_p)
    print(true_n)
    print(false_p)
    print(false_n)
    accuracy = (true_p + true_n)/(true_p + true_n + false_p + false_n)
    precision = true_p/(true_p + false_p)
    recall = true_p/(true_p + false_n)
    f1 = 2*(precision*recall)/(precision+recall)
    
    return cm, accuracy, precision, recall, f1


cm, accuracy, precision, recall, f1 = metricas()
print("CM:",cm)
print("Accuracy:", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1: ", f1)