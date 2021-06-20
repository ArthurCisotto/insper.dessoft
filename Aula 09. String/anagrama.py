def anagrama(string1, string2):
    lista1 = []
    lista2 = []
    for e in string1:
        lista1.append(e)
    for c in string2:
        lista2.append(c)
    
    check1 = 0
    for i in lista1:
        if i in lista2:
            check1 += 1

    check2 = 0
    for j in lista2:
        if j in lista1:
            check2 += 1

    if check1 == len(lista1) or check2 == len(lista2):
        return True
    else:
        return False
