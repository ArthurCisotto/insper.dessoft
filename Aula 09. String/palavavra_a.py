palavra = input('Digite uma palavra: ')
lista = []
while palavra != 'fim':
    lista.append(palavra)
    palavra = input('Digite uma palavra: ')
i = 0
while i < len(lista):
        primeira_letra= lista[i][0]
        if primeira_letra == 'a':
            print(lista[i])        
        i += 1
    
