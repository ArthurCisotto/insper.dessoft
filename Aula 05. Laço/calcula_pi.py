import math
def calcula_pi(n):
    i = 1
    soma = 0
    while i <= n:
        x = 6 * (i**(-2))
        soma += x
        pi = math.sqrt(soma)
        i = i + 1
    return pi