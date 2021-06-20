def esconde_senha(senha):
    my_str = ''
    for i in range(0,len(senha)):
        my_str = senha.replace(my_str,senha[i],'*')
    return my_str
    
