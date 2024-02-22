from lista import match, palavrao_na_string
from lista_sorted import match_sorted, palavrao_na_string_sorted
from names import names
import time
#caso 0: se tiver caracteres especiais

#caso 1: tirar espaços e comparar tudo com a lista
def caso1(nome):
    nome = nome.lower()
    nome_splited = [*nome]
    temp = []
    for l in nome_splited:
        if l != ' ':
            temp.append(l)
    nome_s_espacos =  "".join(temp)
    
    aux = [nome_s_espacos]
    resultado1 = match(aux)
    resultado2 = palavrao_na_string(nome_s_espacos)
    
    temp.sort()
    nome_sorted = temp
    aux = [nome_sorted]
    resultado3 = match_sorted(aux)
    resultado4 = palavrao_na_string_sorted(nome_sorted)
    
    if resultado1:
        print("1.1")
    elif resultado2:
        print("1.2")
    elif resultado3:
        print("1.3")
    elif resultado4:
        print("1.4")
    
    return resultado1 or resultado2 #or resultado4 or resultado3


#caso 2: separar por espaços e comparar as partes com a lista
def caso2(palavra):
    palavra = palavra.lower()
    lista = list(palavra)
    aux = [palavra]
    resultado = match(aux)
    if resultado:
        return True
    lista.sort()
    palavra_sorted = lista
    palavra_sorted = "".join(palavra_sorted)
    aux = [palavra_sorted]
    if match_sorted(aux):
        return True
    return False

#função main:
def main(nome):
    special_characters = "!@#$%^&*()-+?_=,<>/1234567890"
    if any(c in special_characters for c in nome):        
        #print("Por favor, não use caracteres especiais. O seu nome certamente não tem esses caracteres!")
        return True
    
    #verificar se esta na lista de nomes
    palavras = nome.split()
    for palavra in palavras:
        if not names(palavra):
            #print("Estava no dicionário de nome do IBGE!!!")
            palavras.remove(palavra)
    
    #print(caso1(nome))
    #print(caso2(nome))
    if caso1(nome):
        print("1")
        return True
    for palavra in palavras:
        if caso2(palavra):
            print("2")
            return True
    return False


#t0 = time.time()
print(main("karia"))
#tf = time.time()
#print("Tempo de execução: ",tf-t0)

#por enquanto tirei do código o "."

#arrumar a palavra pinto, anta, anus, rola, cu, imundo, ku, fag
#melhorar a parte do match com nomes

