pergunta1 = str(input('Já assistiu todos os filmes?'))
pergunta2 = str(input('Tem camiseta temática?'))
pergunta3 = str(input('Já se fantasiou de algum personagem?'))
pergunta4 = str(input('Tem algum action figure/nave/etc?'))
pergunta5 = str(input('Já foi no Galaxys Edge, o parque temático da franquia?'))
counter = int(0)
if pergunta1 == 'sim':
    counter += 1
if pergunta2 == 'sim':
    counter += 1
if pergunta3 == 'sim':
    counter += 1  
if pergunta4 == 'sim':
    counter += 1  
if pergunta5 == 'sim':
    counter += 1    

if counter == 5: 
    print('One with the Force')
else:
    if counter == 3 or counter == 4:
        print('Jedi')
    else:
        if counter == 2:
            print('Padawan')
        else:
            print('Inocente')

