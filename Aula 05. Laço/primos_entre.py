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

def primos_entre(a, b):
    x = a
    primos = 0
    while x <=b:
        if eh_primo(x):
            primos += 1
        x += 1
    return primos