def login_disponivel(login_novo, lista_logins):
    indice_nome = 1
    termo = login_novo
    for e in lista_logins:
        if termo == e:
            termo = f'{login_novo}{indice_nome}'
            indice_nome += 1
    return termo