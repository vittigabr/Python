# Importação de biblioteca e criação do dicionário
import datetime
dados = {}

# Tela de entrada
print('=-'*30)
print(f'{'TABELA DE INFORMAÇÕES':^60}')
print('=-'*30)

# Keys do dict e entrada de dados
dados['Nome'] = input('Nome do funcionário: ').strip().capitalize()
anoNascimento = int(input('Ano de nascimento: '))
anoAtual = datetime.datetime.today().year
dados['Idade'] = anoAtual - anoNascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# Condições de conclusão da tabela
if dados['CTPS']!=0:
    dados['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados['Tempo de Empresa'] = anoAtual - dados['Ano de Contratação']
    dados['Salário'] = float(input('Salário: '))
    dados['Idade para Aposentar'] = (dados['Ano de Contratação'] + 35) - anoAtual
    
    # Tabela de dados coletados
    print('=-'*30)
    print(f'{'DADOS DO FUNCIONÁRIO':^60}')
    print('=-'*30)
    for k, v in dados.items():
        print(f'{k:_<30}: {v}')
else:
    # Tabela de dados coletados
    print('=-'*30)
    print(f'{'DADOS DO FUNCIONÁRIO':^60}')
    print('=-'*30)
    for k, v in dados.items():
        print(f'{k:_<30}: {v}')