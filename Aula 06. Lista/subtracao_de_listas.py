
def subtracao_de_listas(lista1, lista2):
	lista_dif = [i for i in lista1 + lista2 if i not in lista2]
	return lista_dif
