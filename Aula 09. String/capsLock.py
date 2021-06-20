def capsLock(string):
    alf_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alf_max = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    string_invertida = ''
    for e in string:
        if e in alf_min:
            posicao =alf_min.index(e)
            string_invertida += (alf_max[posicao]) 
        if e in alf_max:
            posicao =alf_max.index(e)
            string_invertida += (alf_min[posicao])
        if e == ' ':
            string_invertida += ' '
    return string_invertida
