#talvez seja necessário dar uma filtrada nas palavras, porque tem "aranha", por exemplo

#montar a lista
lista = []

f = open('/home/enzo.bittencourt/Badwords/Badwords/pt.txt','r')
for i in range(1,790):
    linha=f.readline()
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
    lista.append(linha)
f.close()

f = open('/home/enzo.bittencourt/Badwords/Badwords/en.txt','r')
for i in range(1,403):
    linha = f.readline()
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

def afuncaola(palavras):
    #print(palavras)
    teste = list(filter(filtro,palavras))
    #print(teste)
    #print(len(teste))
    #se for true é porque tinha palavrao
    #print("Tinha palavrao =",teste != [])
    return len(teste) != 0

