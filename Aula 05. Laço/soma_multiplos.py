def soma_multiplos(a, b):
    if a > b:
        maximo = a*10
    else:
        maximo = b*10
    lista_a = []
    lista_b = []
    multiplos_a = 0
    multiplos_b = 0
    while multiplos_a <= maximo:
        if multiplos_a%a == 0:
            lista_a.append(multiplos_a)
        multiplos_a += 1
    while multiplos_b <= maximo:
        if multiplos_b%b == 0:
            lista_b.append(multiplos_b)
        multiplos_b += 1
    lista_final = lista_a
    for e in lista_b:
        if e not in lista_a:
            lista_final.append(e)
    return sum(lista_final)
