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

resp = notas(9, 5, 9.7, 3, 2.4, situacao=True)
print('='*50)
print(f'{'TABELA DE RESULTADO':-^50}')
print('='*50)
for k, v in resp.items():
    print(f'{k:_<30} === {v}')