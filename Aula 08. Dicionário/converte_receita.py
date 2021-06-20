def converte_receita(receita):
    dic_convertido = {}
    for ingrediente, qtd in receita.items():
        quantidade = int(qtd[0])
        if "xícara" in qtd:
            dic_convertido[ingrediente] = f'{quantidade*250} ml'
        elif "sopa" in qtd:
            dic_convertido[ingrediente] = f'{quantidade*15} ml'
        elif "chá" in qtd:
            dic_convertido[ingrediente] = f'{quantidade*5} ml'
        else:
            dic_convertido[ingrediente] = qtd          
    return dic_convertido
