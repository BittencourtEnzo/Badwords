#vamos filhos altivos dos ares

from lista import afuncaola, funcaocontrario
from lista_sorted import afuncaola_sorted, funcaocontrario_sorted
#from names import comparar_nomes
#caso 0: se tiver caracteres especiais

#caso 1: tirar espaços e comparar tudo com a lista
def caso1(nome):
    nome = nome.lower()
    nome_splited = [*nome]
    temp = []
    for l in nome_splited:
        if l != ' ':
            temp.append(l)
    nome_splited =  "".join(temp)
    #print(nome_splited)
    aux = [nome_splited]
    resultado1 = afuncaola(aux)
    #resultado5 = funcaocontrario(nome_splited)
    #5 é igual ao 4, mas sem ser sorted
    
    #invocando o caso3:
    #print(type(temp))
    temp.sort()
    nome_sorted = temp
    #print(nome_sorted)
    nome_sorted = "".join(nome_sorted)
    aux = [nome_sorted]
    resultado3 = caso3(aux)
    #print(resultado1)
    #print(resultado3)
    #resultado4 = caso4(nome_sorted)
    return resultado1 #or resultado3 #or resultado5 #or resultado4

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
            #print(aux)
            resultado = afuncaola(aux)
            if resultado:
                #print("aaaaaaa")
                return True
            temp.sort()
            nome_sorted = temp
            nome_sorted = "".join(nome_sorted)
            aux = [nome_sorted]
            if caso3(aux):
                #print("aaaa")
                return True
            temp = []
    
    temp_joined = "".join(temp)
    aux = [temp_joined]
    #print(aux)
    resultado = afuncaola(aux)
    if resultado:
        print("aaaaaa")
        return True
    temp.sort()
    nome_sorted = temp
    nome_sorted = "".join(nome_sorted)
    aux = [nome_sorted]
    if caso3(aux):
        #print("a")
        return True
    temp = []
    
    return False

#caso 3: pegar UM nome ordenado e comparar
def caso3(nome_sorted):
    return afuncaola_sorted(nome_sorted)

#caso 4: verificar se alguem da lista_sorted ta na string sorted
def caso4(nome_sorted):
    #print(nome_sorted)
    return funcaocontrario_sorted(nome_sorted)

#função main:
def main(palavra):
    special_characters = "!@#$%^&*.()-+?_=,<>/1234567890"
    if any(c in special_characters for c in palavra):        
        print("Por favor, não use caracteres especiais. O seu nome certamente não tem esses caracteres!")
        return True
    
    
    #print(caso1(palavra))
    #print(caso2(palavra))
    
    return  caso1(palavra) #or caso2(palavra)

#nomes-teste:
#nome1 = "meu nome é Jorge da Silva caralho" #ok
#nome2 = "Jorge" #ok
#nome3 = "Jorge Sun-glass" #ok
#nome4 = "caralho" #ok
#nome5 = "caraleo" #ok
#nome6 = "cara!ho" #ok
#nome7 = "caralh*" #ok
#nome8 = "car alho" #ok
#nome9 = "ohlarac" #ok
#nome10 = "caralho alado" #ok
#nome11 = "alado caralho" #ok
#nome12 = "meu nome é vadia" #ok
#nome13 = "meu car alho" # ok
#nome14 = "zzzzzmerdazzzzz" #ok
#nome15 = "merd" #falso positivo

#casos faltantes: 1 letra faltando (augmentation)

final = main("marcia")
print(final)