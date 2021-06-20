def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i < n:
        if n%i == 0:
            return False
        i += 2
    return True

def verifica_primos(lista_n):
    dic = {}
    for n in lista_n:
        dic[n] = eh_primo(n)
    return dic