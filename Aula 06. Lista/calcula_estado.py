def calcula_estado(lista):
    #definição da lista de quizzes com a menor nota removida#
    quizzes = []
    for e in range(len(lista)):
        quizzes.append(lista[e][1])
    for e in range(len(quizzes)):
            quizzes[e].remove(min(quizzes[e]))
    
    #definição da lista com as medias dos quizzes#
    media_quiz = []
    for c in range(len(quizzes)):
        media = sum(quizzes[c])/len(quizzes[c])
        media_quiz.append(media)
       
    #definição das listas com as notas da AI e da AF#
    notas_AI = []
    notas_AF = []
    for s in range(len(lista)):
        notas_AI.append(lista[s][2][0])
        notas_AF.append(lista[s][2][1])
    
    #definição da lista com as medias finais#
    media_final = []
    for m in range(len(lista)):
        media_f = 0.1*media_quiz[m] + 0.4*notas_AI[m] + 0.5*notas_AF[m]
        media_final.append(media_f)
    
    #checa se o aluno foi aprovado e define a lista final#
    lista_final = []
    for t in range(len(lista)):
        if media_final[t] >= 5:
           resultado = [lista[t][0], 'A'] 
        else:
            resultado = [lista[t][0], 'R']
        lista_final.append(resultado) 
    return lista_final

