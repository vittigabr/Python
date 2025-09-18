def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3

def notas(*num, situacao=False):
    """notas(*num, situacao=False)
    *num = adiciona quantos números necessário, separados por vírgula(ex: 5.8, 9.7)
    situacao = sempre deve escrita para entendimento do programa(ex: (5.8, 9.7, situacao=True), caso deseje ver a situação da turma)
    """    
    dados = {}
    soma = float(0)
    dados['Total de Notas'] = len(num)
    for c in num:
        soma += c 
    media = soma/len(num)
    if situacao==True:
        if 7>media>=5:
            sit = 'A turma está de RECUPERAÇÃO.'
        elif media>=7:
            sit = 'A turma está APROVADA.'
        else:
            sit = 'A turma está REPROVADA.'
    dados['Maior Nota'] = max(num)
    dados['Menor Nota'] = min(num)
    dados['Média dos Alunos'] = (f'{media:.2f}')
    dados['Situação da Turma'] = sit
    return dados