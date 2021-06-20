def encontra_maximo(matriz):
    lista_absoluta = []
    c= 0 
    #Transforma os valores da lista em valores absolutos e junta em uma única lista#
    while c <= 2:
        for e in matriz[c]:
            lista_absoluta.append(abs(e)) 
        c += 1
    #Função max retorna o maior valor da lista#
    return max(lista_absoluta)
     