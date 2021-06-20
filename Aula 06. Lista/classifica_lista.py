def classifica_lista(lista):
    i = 1
    check = 0
    if len(lista) < 2:
        return 'nenhum'
    while i < len(lista):
        if lista[i-1] < lista[i]:
            check+=0
        if lista[i-1] > lista[i]:
            check+=1
        i+=1

    if check == 0:
        return 'crescente'
    if check == (len(lista)-1):
        return 'decrescente'
    else: 
        return 'nenhum'


