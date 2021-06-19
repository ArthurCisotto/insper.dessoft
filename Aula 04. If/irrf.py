salario_bruto = float(input('Qual é o seu salário bruto?'))
num_dependentes = float(input('Qual é o seu  o número de dependentes?'))

if salario_bruto <= 1045:
    contribuicao = salario_bruto * 0.075
else:
    if salario_bruto > 1045 and salario_bruto <= 2089.60:
        contribuicao = salario_bruto * 0.09
    else:
        if salario_bruto > 2089.60 and salario_bruto <= 3134.40:
            contribuicao = salario_bruto * 0.12
        else:
            if salario_bruto > 3134.40 and salario_bruto <= 6101.06:
                contribuicao = salario_bruto * 0.14
            else:
                contribuicao = 671.12

base = salario_bruto - contribuicao - (num_dependentes*189.59)

if base <= 1903.98:
    aliquota = 0
    deducao = 0
else:
    if base > 1903.98 and base <= 2826.65:
        aliquota = 0.075
        deducao = 142.80
    else:
        if base > 2826.65 and base <= 3751.05:
            aliquota = 0.15
            deducao = 354.80
        else:
            if base > 3751.05 and base <= 4664.68:
                aliquota = 0.225
                deducao = 636.13
            else:
                aliquota = 0.275
                deducao = 869.36

irrf = base * aliquota - deducao

print(irrf)