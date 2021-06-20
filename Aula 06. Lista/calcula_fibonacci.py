def calcula_fibonacci(n):
    fib = [0]*n
    i = 2
    if n == 1:
        fib[0] = 1
        return fib
    else:
        fib[0] = 1
        fib[1] = 1
        while i < n:
            fib[i] = fib[i-1] + fib[i-2]
            i += 1
        return fib