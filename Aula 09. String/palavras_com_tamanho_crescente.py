def palavras_com_tamanho_crescente(lista):
    check = 1
    i = 0
    while i < len(lista)-1:
        if len(lista[i+1]) > len(lista[i]):
            check+=1
        i+=1
    if check == len(lista):
        return True
    else:
        return False
