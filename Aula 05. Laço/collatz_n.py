def collatz_n(n):
    aux = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else: 
            n = (3 * n) + 1
        #print(n)
        aux += 1
    #print(aux)
    return aux

teto = 1
for i in range(1, 1001):
    #print(f"Numero {i}, tem {collatz_n(i)} passos")
    if collatz_n(i) > collatz_n(teto):
        teto = i
        #print(teto)
print(teto)