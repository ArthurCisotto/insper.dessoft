def aproxima_raiz(n):
    i = 1 
    while (i**2) < n: 
        i = i + 1
    if abs((n - (i**2))) < abs((n - ((i-1)**2))):
        return i         
    else:
        return (i-1)