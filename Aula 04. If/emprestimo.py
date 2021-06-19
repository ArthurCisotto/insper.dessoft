valor_casa = float(input('Qual é o valor da casa a ser comprada?'))
salario = float(input('Qual é o valor do seu salário?'))
anos = int(input('Em quantos anos você quer pagar?'))

meses = anos * 12

if valor_casa/meses > salario*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')

