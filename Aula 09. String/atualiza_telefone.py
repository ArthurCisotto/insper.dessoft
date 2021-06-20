def atualiza_telefone(numero):
    if '-' in numero:
        if len(numero) == 10:
            return numero
        else:
            return '9'+numero
    else:
        if len(numero) == 9:
            return numero
        else:
            return '9'+numero
    