with open('macacos-me-mordam.txt', 'r') as arquivo:
    qntd_bananas = arquivo.read().lower().strip().count('banana')
print(qntd_bananas)
