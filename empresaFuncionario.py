# Cabeçalho
print('=-'*25)
print(f'{' EMPRESA NOVATECH ':*^50}')
print('=-'*25)

# Entrada de valores
dados = {'nome': '', 'código': 0, 'horas trabalhadas': 0, 'valor por hora trabalhada': 0.0, 'salário por hora trabalhada': 0}
dados['nome'] = input('Digite o nome do funcionário: ').strip().capitalize()
dados['código'] = int(input('Digite o código do funcionário: '))
dados['horas trabalhadas'] = int(input('Digite as horas trabalhadas: '))
dados['valor por hora trabalhada'] = float(input('Digite o valor que recebe por hora: '))

# Cálculo do salário 
dados['salário por hora trabalhada'] = dados['horas trabalhadas']*dados['valor por hora trabalhada']

# Saída dos valores
print('=-'*25)
print(f'{' INFORMAÇÕES ':-^50}')
print('=-'*25)
for k, v in dados.items():
    print(f'{k.capitalize():_<38}{v:>8}')