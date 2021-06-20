with open('texto.txt', 'r') as arquivo:
    lista_palavras = arquivo.read().strip().split()
print(len(lista_palavras))
