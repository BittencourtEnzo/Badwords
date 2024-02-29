lista = []

f = open('./Badwords/pt.txt','r')
for i in range(1,844):
    linha=f.readline()
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
    linha = [*linha]
    linha.sort()
    linha = "".join(linha)
    lista.append(linha)
f.close()

f = open('./Badwords/en.txt','r')
for i in range(1,423):
    linha = f.readline()
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
    linha = [*linha]
    linha.sort()
    linha = "".join(linha)
    lista.append(linha)
f.close()

#print(lista[0:4])

#funcao do filtro
def filtro(palavra):
    if palavra in lista:
        return True
    else:
        return False

#agora testar

#palavras = ['aborto','aranha','morte']

def match_sorted(palavras):
    if palavras[0] == "inopt":
        return False
    #print(palavras)
    teste = list(filter(filtro,palavras))
    return len(teste) != 0

def word_in_string_sorted(palavra):
    for palavrao in lista:
        #print(palavrao)
        if palavra.__contains__(palavrao):
            #print("Funcionou")
            return True
    return False