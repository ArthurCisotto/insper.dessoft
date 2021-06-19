def maior_produto3(lista):
    lista_termos = []
    produtos = []
    if len(lista) == 3:
        return lista[0]*lista[1]*lista[2]    
    min1 = min(lista)
    lista.remove(min1)
    min2 = min(lista)
    x = max(lista)
    lista.remove(x)
    y = max(lista)
    lista.remove(y)
    z = max(lista)
    produtos.append(x*y*z)
    produtos.append(x*min1*min2)

    return max(produtos)