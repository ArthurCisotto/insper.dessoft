idade = int(input('Qual é a sua idade?'))
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0


if idade < 0:
    print('0-11 anos: 0.00 %')
    print ('12-17 anos: 0.00 %')
    print('18-25 anos: 0.00 %')
    print('26-35 anos: 0.00 %')
    print('36-59 anos: 0.00 %')
    print('Acima de 60 anos: 0.00 %')
if idade >= 60:
    f += 1
elif idade >= 36 and idade <= 59:
    e += 1 
elif idade >= 26 and idade <= 35:
    d += 1 
elif idade >= 18 and idade <= 25:
    c += 1 
elif idade >= 12 and idade <= 17:
    b += 1 
elif idade >= 0 and idade <= 11:
    a += 1 
while idade >= 0:
    idade = int(input('Qual é a sua idade?'))
    if idade >= 60:
        f += 1
    elif idade >= 36 and idade <= 59:
        e += 1 
    elif idade >= 26 and idade <= 35:
        d += 1 
    elif idade >= 18 and idade <= 25:
        c += 1 
    elif idade >= 12 and idade <= 17:
        b += 1 
    elif idade >= 0 and idade <= 11:
        a += 1 
total = a + b + c + d + e + f
porc_a = a/total * 100
porc_b = b/total * 100
porc_c = c/total * 100
porc_d = d/total * 100
porc_e = e/total * 100
porc_f = f/total * 100

print('0-11 anos: {:.2f} %'.format(porc_a))
print ('12-17 anos: {:.2f} %'.format(porc_b))
print('18-25 anos: {:.2f} %'.format(porc_c))
print('26-35 anos: {:.2f} %'.format(porc_d))
print('36-59 anos:{:.2f} %'.format(porc_e))
print('Acima de 60 anos: {:.2f} %'.format(porc_f))