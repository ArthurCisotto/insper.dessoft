def transpor_matriz(matriz):
    transposta = [None]*len(matriz[0])
    for t in range(len(matriz)):
        transposta[t] = [None]*len(matriz)
        for tt in range(len(matriz[t])):
            transposta[t][tt] = matriz[tt][t]
    return transposta


def quadrado_magico(matriz):
    referencia = sum(matriz[0])
    check = 0
    #Check das linhas#
    for l in matriz:
        if sum(l) == referencia:
            check+=1
    #Check das colunas#
    for c in transpor_matriz(matriz):
        if sum(c) == referencia:
            check+=1
    #Check das diagonais#
    diag1 = [None]*len(matriz)
    diag2 = [None]*len(matriz)
    for t in range(len(matriz)):
        diag1[t] = matriz[t][t]

    i = len(matriz)-1
    for t in range(len(matriz)):
        diag2[t] = matriz[t][i]
        i -= 1
    
    if sum(diag1) == referencia and sum(diag2) == referencia:
        check += 1
    
    if check == 2*len(matriz) + 1:
        return True
    else: 
        return False