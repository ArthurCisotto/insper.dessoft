import json

with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

# Criando um dicionário a partir das informações no texto
dic_produtos = json.loads(texto)
lista_valores = []

for info in dic_produtos.values():
    for produto in info:
        qtd = produto.get('quantidade')
        valor = produto.get('valor')
        lista_valores.append(qtd*valor)

print(sum(lista_valores))
