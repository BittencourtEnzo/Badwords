#montar a lista
f = open('pt.txt','r')
linha=f.readline()
print(linha)

lista = []


#funcao do filtro
def filtro(palavra):
    if palavra in lista:
        return True
    else:
        return False
    

#agora testar

#palavras = ['falecimento','muerte','morte']

#teste = list(filter(filtro,palavras))

#print(teste)