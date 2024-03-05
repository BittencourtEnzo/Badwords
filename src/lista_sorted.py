lista = []

f = open('./data/bagofwords.txt','r')
for i in range(1,1266):
    linha = f.readline()
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
    linha = [*linha]
    linha.sort()
    linha = "".join(linha)
    lista.append(linha)
f.close()

#funcao do filtro
def filtro(palavra):
    if palavra in lista:
        return True
    else:
        return False


def match_sorted(palavras):
    if palavras[0] == "inopt":
        return False
    #print(palavras)
    teste = list(filter(filtro,palavras))
    return len(teste) != 0

def word_in_string_sorted(palavra):
    for palavrao in lista:
        
        if palavra.__contains__(palavrao):
            
            return True
    return False