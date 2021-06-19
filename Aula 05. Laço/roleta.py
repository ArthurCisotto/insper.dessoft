import random

carteira = 100
continua_apostando= True

while continua_apostando:
    print(f'Valor na carteira: {carteira}') 
    aposta = int(input('Quanto você deseja apostar?'))
    if aposta > 0:
        tipo_aposta = input('A aposta é em número ou paridade[n/p]? ')
        num_sorteado = random.randint(0,36)
        if tipo_aposta == 'n':
            numero_escolhido = int(input('Digite o número[1;36]: '))
            if numero_escolhido == num_sorteado:
                recompensa = 35*aposta
                carteira += recompensa
            else:
                carteira -= aposta    
        elif tipo_aposta == 'p':
            paridade_escolhida = input('A aposta é em par ou ímpar[p/i]?')
            if (paridade_escolhida == 'p' and num_sorteado % 2 == 0) or (paridade_escolhida == 'i' and num_sorteado % 2 == 1):
                carteira += aposta
            else:
                carteira -= aposta
    else:
        continua_apostando = False
    if carteira == 0:
        continua_apostando = False         