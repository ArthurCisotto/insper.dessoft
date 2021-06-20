def converteHora(horario):
    if int(horario[:2]) < 12:
        return horario + ' AM'
    elif int(horario[:2]) == 12:
        return horario + ' PM'
    else:
        mudanca = int(horario[:2]) - 12
        if mudanca < 10: 
            return f'0{mudanca}' + horario[2:] + ' PM'
        else:
            return f'{mudanca}' + horario[2:] + ' PM'  