def maximo_divisor_comum(a, b):
    if b == 0:
        return a
    else:
        return maximo_divisor_comum(b, a % b)

