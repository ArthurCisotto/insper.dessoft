def calcula_idade(d_nasc, m_nasc, a_nasc,d_atual, m_atual, a_atual):
    if m_atual > m_nasc:
        return (a_atual-a_nasc)
    if m_atual == m_nasc and d_atual >= d_nasc:
        return (a_atual-a_nasc)
    else:
        return (a_atual-a_nasc)-1
