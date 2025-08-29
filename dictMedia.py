soma = 0
cont = 1
dados = {'Nome': 0, 'Media': 0, 'Condicao': 0}
dados['Nome'] = input('Digite seu nome: ').strip().capitalize()

# Entrada de notas
while cont<=4:
    notas = float(input(f'Digite sua {cont}º nota: '))
    soma += notas
    cont += 1

# Cálculo de média
dados['Media'] = soma/4

# Tabela
print('='*55)
print(f'{'MÉDIA E CONDIÇÃO':^55}')
print('='*55)

# Condicionais da média
if dados['Media']<=4:
    dados['Condicao'] = 'Você está REPROVADO'
elif 5<=dados['Media']<7:
    dados['Condicao'] = 'Você está de RECUPERAÇÃO'
else:
    dados['Condicao'] = 'Você está APROVADO'
for k, v in dados.items():
    print(f'{k:.<30}', end='')
    print(f'{v:>25}')
print('-'*55)