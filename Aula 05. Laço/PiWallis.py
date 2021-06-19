def PiWallis(n):
    produto = 1
    par = 0
    impar = 1
    for i in range(n):
        if i % 2 == 0:
            par += 2
        else:
            impar += 2
        produto *= par/impar

    return 2*produto

