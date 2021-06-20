def calcula_extensao(listax, listay):
    i = 1
    soma = 0
    while i < len(listax):
        termo = (listax[i] - listax[i-1])**2 + (listay[i] - listay[i-1])**2
        termo_final = termo**(1/2)
        soma += termo_final
        i += 1
    return soma