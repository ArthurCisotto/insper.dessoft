with open('criptografado.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
lista_linhas = []
dic = {'s': 'z', 'a': 'e', 'r': 'b','b': 'r', 'e': 'a', 'z': 's'}
for linha in conteudo:
    nova_linha = ''
    for letra in linha:
        if letra in dic.keys():
            nova_linha += dic[letra]
        else: 
            nova_linha += letra
    lista_linhas.append(nova_linha)
print(lista_linhas)
