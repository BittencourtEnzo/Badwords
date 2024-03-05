#talvez seja necessário dar uma filtrada nas palavras, porque tem "aranha", por exemplo

#montar a lista
lista = []

f = open('./data/bagofwords.txt','r')
for i in range(1,1266):
    linha = f.readline()    
    linha = linha[0:len(linha)-1]
    linha = linha.lower()
    lista.append(linha)
f.close()

#funcao do filtro
def filtro(palavra):
    if palavra == ["pinto"]:
        return False
    if palavra in lista:
        return True
    else:
        return False
    

#agora testar

def match(palavras):
    if palavras[0] == "pinto":
        return False

    teste = list(filter(filtro,palavras))
    return len(teste) != 0

def word_in_string(palavra):
    for palavrao in lista:
        
        whitelist = ["cu","ass","pau","pinto","anal","hell","anta","anus","rola","anus","ku","imundo","fag"] 
        if palavrao not in whitelist and palavra.__contains__(palavrao):
            
            return True
    return False