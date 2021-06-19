def pedra_papel_tesoura(um, dois):
    if ((um != 'pedra') and (um != 'papel') and (um != 'tesoura')) or (dois != 'pedra') and (dois != 'papel') and (dois != 'tesoura') :
        return 'Escolha pedra, papel ou tesoura para jogar'
    else:
        if um == dois:
            return 'empate'
        else:
            if (um == 'pedra' and dois == 'tesoura') or (um == 'tesoura' and dois == 'papel') or (um == 'papel' and dois == 'pedra'):
                return 'um'
            else:
                return 'dois'
                

