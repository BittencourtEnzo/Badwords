from lista import match, palavrao_na_string
from lista_sorted import match_sorted, palavrao_na_string_sorted
from names import names
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
    return resultado1 #or resultado2 #or resultado4 #or resultado3


#caso 2: separar por espaços e comparar as partes com a lista
def caso2(nome):
    nome = nome.lower()
    nome_splited = [*nome]
    temp = []
    resultado = False
    for l in nome_splited:
        if l != ' ':
            temp.append(l)
        else:
            temp_joined = "".join(temp)
            aux = [temp_joined]
            resultado = match(aux)
            if resultado:
                return True
            temp.sort()
            nome_sorted = temp
            nome_sorted = "".join(nome_sorted)
            aux = [nome_sorted]
            if match_sorted(aux):
                return True
            temp = []
    
    temp_joined = "".join(temp)
    aux = [temp_joined]
    #print(aux)
    resultado = match(aux)
    if resultado:
        return True
    temp.sort()
    nome_sorted = temp
    nome_sorted = "".join(nome_sorted)
    aux = [nome_sorted]
    if match_sorted(aux):
        return True
    temp = []
    
    return False

#função main:
def main(palavra):
    special_characters = "!@#$%^&*.()-+?_=,<>/1234567890"
    if any(c in special_characters for c in palavra):        
        print("Por favor, não use caracteres especiais. O seu nome certamente não tem esses caracteres!")
        return True
    
    if not names(palavra):
        #print("Estava no dicionário de nome do IBGE!!!")
        return False
    
    #print(caso1(palavra))
    #print(caso2(palavra))
    return  caso1(palavra) #or caso2(palavra)

print(main("putamerda"))