#talvez seja necessário dar uma filtrada nas palavras, porque tem "aranha", por exemplo

#montar a lista
lista = []

f = open('/home/enzo.bittencourt/Badwords/Badwords/pt.txt','r')
for i in range(1,844):
    linha=f.readline()
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
    lista.append(linha)
f.close()

f = open('/home/enzo.bittencourt/Badwords/Badwords/en.txt','r')
for i in range(1,423):
    linha = f.readline()    
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
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

def match(palavras):
    #print(palavras)
    teste = list(filter(filtro,palavras))
    #print(teste)
    #print(len(teste))
    #se for true é porque tinha palavrao
    #print("Tinha palavrao =",teste != [])
    return len(teste) != 0

def palavrao_na_string(palavra):
    for palavrao in lista:
        #print(palavrao)
        if palavrao != "cu":
            if palavra.__contains__(palavrao):
                #print("Funcionou")
                return True
    return False

