i = 0   
soma = 0
lista = []
while i <100:
    termo = 1/(2**i)
    lista.append(termo)
    i = i+1

for e in lista:
    soma += e 
print(soma)