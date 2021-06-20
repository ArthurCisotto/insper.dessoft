def verifica_lista(lista):
    if len(lista) == 0:
        return 'misturado'
    else:
        i = 0
        check = 0
        while i < len(lista):
            if lista[i] % 2 == 1:
                check += 1
            if lista[i] % 2 == 0:
                check += 0
            i += 1
        if check == len(lista):
            return 'ímpar'
        if check == 0:
            return 'par'
        else:
            return 'misturado'