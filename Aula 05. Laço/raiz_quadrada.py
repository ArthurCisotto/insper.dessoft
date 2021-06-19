def raiz_quadrada(n):
    impar = 1
    raiz = 0
    while n != 0:
        n = n - impar
        impar += 2
        raiz += 1
        
    return raiz
        