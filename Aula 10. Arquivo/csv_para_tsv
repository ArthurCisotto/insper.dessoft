with open('dados.csv', 'r') as arquivo:
    lista_valores = arquivo.read()

csv2tsv = lista_valores.replace(',', '\t')

with open('dados.tsv', 'w') as arquivo2:
    arquivo2.write(csv2tsv)
