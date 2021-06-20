def remove_vogais(string):
    vogais = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
    string_final = ''
    for e in string:
        if e not in vogais:
            string_final += e
    return string_final
    