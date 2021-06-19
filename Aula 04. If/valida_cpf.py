def valida_cpf(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11):
    check1 = False
    check2 = False
    if d1 == d2 == d3 == d4 == d5 == d6 == d7 == d8 == d9 == d10 == d11:
        return False
    prim_verificador = ((d1*10+d2*9+d3*8+d4*7+d5*6+d6*5+d7*4+d8*3+d9*2)*10)%11
    if prim_verificador == 10:
        prim_verificador = 0
    if prim_verificador == d10:
        check1 = True
    
    segund_verificador = ((d1*11+d2*10+d3*9+d4*8+d5*7+d6*6+d7*5+d8*4+d9*3+d10*2)*10)%11
    if segund_verificador == 10:
        prim_verificador = 0
    if segund_verificador == d11:
        check2 = True

    if check1 and check2:
        return True
    else: 
        return False
        
    