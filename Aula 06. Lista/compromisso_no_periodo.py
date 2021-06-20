def compromisso_no_periodo(grade, dia, periodo):
    compromisso = grade[periodo][dia]
    if compromisso == '':
        return 'Livre'
    else:
        return compromisso

