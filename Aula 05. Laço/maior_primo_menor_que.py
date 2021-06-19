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

def maior_primo_menor_que(n):
    if n < 2:
        return -1
    x = 0
    primo = 0
    while x <=n:
        if eh_primo(x):
            primo = x
        x += 1
    return primo

