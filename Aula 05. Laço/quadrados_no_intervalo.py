def verifica_quadrado_perfeito(num):
    raiz = int(num**(1/2))
    if raiz**2 == num:
        return True
    else:
        return False

def quadrados_no_intervalo(a,b):
    quadrados = 0
    for n in range(a, b+1):
        if verifica_quadrado_perfeito(n):
            quadrados+=1
    return quadrados
