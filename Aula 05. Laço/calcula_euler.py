import math
def calcula_euler(x, n):
    soma = 0
    i = 0
    while i < n: 
            termo = x**i/math.factorial(i)
            soma += termo
            i += 1
           
    return soma
    