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

def primos_entre(a,b):
    lista_primos = []
    n = a
    while n <= b:
        if eh_primo(n):
            lista_primos.append(n)
        n += 1
    return lista_primos