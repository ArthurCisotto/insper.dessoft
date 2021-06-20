def eh_crescente(lista):
    i = 1
    check = 0
    while i < len(lista):
        if lista[i-1] < lista[i]:
            check+=0
        else:
            check+=1
        i+=1

    if check == 0:
        return True
    else:
        return False


