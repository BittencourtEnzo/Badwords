from .lista import match, word_in_string
from .lista_sorted import match_sorted, word_in_string_sorted
from .names import names
import time
#caso 0: se tiver caracteres especiais

#caso 1: tirar espaços e comparar tudo com a lista
def case1(name):
    name = name.lower()
    name_splited = [*name]
    temp = []
    for l in name_splited:
        if l != ' ':
            temp.append(l)
    name_s_espacos =  "".join(temp)
    
    aux = [name_s_espacos]
    result1 = match(aux)
    result2 = word_in_string(name_s_espacos)
    
    temp.sort()
    name_sorted = temp
    aux = [name_sorted]
    result3 = match_sorted(aux)
    result4 = word_in_string_sorted(name_sorted)
    
    #if resultado1:
        #print("1.1")
    #elif resultado2:
        #print("1.2")
    #elif resultado3:
        #print("1.3")
    #elif resultado4:
        #print("1.4")
    
    return result1 or result2 #or result4 or result3


#caso 2: separar por espaços e comparar as partes com a lista


def case2(word):
    word = word.lower()
    list1 = list(word)
    aux = [word]
    result = match(aux)
    if result:
        return True
    list1.sort()
    word_sorted = list1
    word_sorted = "".join(word_sorted)
    aux = [word_sorted]
    if match_sorted(aux):
        return True
    return False

#função main:
def main(name):
    special_characters = "!@#$%^&*()-+?_=,<>/1234567890."
    if any(c in special_characters for c in name):        
        #print("Por favor, não use caracteres especiais. O seu nome certamente não tem esses caracteres!")
        return True
    
    #verificar se esta na lista de nomes
    words = name.split()
    for word in words:
        if not names(word):
            #print("Estava no dicionário de nome do IBGE!!!")
            words.remove(word)
    
    
    #print(caso1(nome))
    #print(caso2(nome))
    if case1(name):
        #print("1")
        return True
    for word in words:
        if case2(word):
            #print("2")
            return True
    return False


#t0 = time.time()
#print(main("Rolando"))
#tf = time.time()
#print("Tempo de execução: ",tf-t0)