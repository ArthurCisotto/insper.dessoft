def valida_senha(senha):
    caracteres_especiais = ['?', '!', '@', '#', '$', '%', '&', '*']
    char_esp_usados = []
    for char in caracteres_especiais:
        if char in senha:
            char_esp_usados.append(char)
    if len(char_esp_usados) < 2:
        return False
    if len(senha) < 8:
        return False
    i = 1 
    while i < len(senha)-1:
        if senha[i] == senha[i-1]:
            return False
        i+=1
    else:
        return True