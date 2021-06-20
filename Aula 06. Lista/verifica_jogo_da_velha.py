def verifica_jogo_da_velha(matriz):
    i = 0
    #Definição das vitórias por linha e coluna#
        while i < 3:
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == 'X':
                return 'X'
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == 'O':
            return 'O'
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == 'X':
            return 'X'
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == 'O':
            return 'O'
        i += 1
    #Definição das vitórias por diagonais#
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == 'X':
        return 'X'
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == 'O':
        return 'O'
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == 'X':
        return 'X'
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == 'O':
        return 'O'
    else:
        return 'V'