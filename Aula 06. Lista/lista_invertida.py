numeros = []
x = int(input('Digite números inteiros positivos. Para parar digite um número negativo ou zero'))
while x > 0:
    numeros.append(x)
    x = int(input('Digite números inteiros positivos. Para parar digite um número negativo ou zero'))
print(numeros[::-1])