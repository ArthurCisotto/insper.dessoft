with open('churras.txt', 'r') as arquivo:
    itens = arquivo.readlines()
qnt_e_custos = {}
for i in itens:
    i = i.strip().split(',')
    qnt_e_custos[i[0]] = int(i[1])*float(i[2])

print(sum(qnt_e_custos.values()))
