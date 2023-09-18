def cont(*n,sit = True):
    """
    -> Cfunção para analisar notas e situaçãoes de vários alunos.
    :Param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    
    
    r = dict()
    r['TOTAL'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/ len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >= 5:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r

print(cont(5.5,4.5,6.1,1.5,sit=True))