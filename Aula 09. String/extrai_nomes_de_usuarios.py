def extrai_nomes_de_usuarios(lista_emails):
    lista_nomes = []
    for email in lista_emails:
        email_separado = email.split('@')
        lista_nomes.append(email_separado[0])
    return lista_nomes
