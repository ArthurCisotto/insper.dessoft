def pa(lista):
    i = 1
    check = 0
    const_PA = lista[1] - lista[0]
    while i<len(lista):
        if lista[i] - lista[i-1] == const_PA:
            check += 0
        else:
            check += 1
        i+= 1
    if check == 0:
        return True
    else:
        return False

    
def pg(lista):
    i = 1
    check = 0
    if lista[0] == 0:
        return False
    const_PG = lista[1]/lista[0]
    while i<len(lista):
        if lista[i]/lista[i-1] == const_PG:
            check += 0
        else:
            check += 1
        i+= 1
    if check == 0:
        return True
    else:
        return False

def verifica_progressao(lista):
    if pa(lista) and pg(lista):
        return 'AG'
    if pa(lista):
        return 'PA'
    if pg(lista):
        return 'PG'
    else:
        return 'NA'
    

        