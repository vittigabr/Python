# Tela de entrada
print('='*40)
print(f'{'SISTEMA DE CONTROLE DE HORAS':^40}')
print('='*40)

# Entrada de informações
nome = input('Digite seu nome: ').strip().capitalize()
numeroID = int(input('Digite seu código de verificação: '))
salario = float(input('Digite seu salário por hora(R$): '))
hora = int(input('Digite quantas horas trabalhou hoje: '))

# Cálculo salário
salarioTotal = salario*hora

# Tela de saída
print('=-'*20)
print(f'{'FOLHA DE PAGAMENTO DIÁRIA':^40}')
print('=-'*20)
print(f'{'Nome':<20}: {nome}')
print(f'{'Identificação':<20}: {numeroID}')
print(f'{'Horas Trabalhadas':<20}: {hora}')
print(f'{'Salário por Hora':<20}: {salario}')
print(f'{'Salário do Dia':<20}: {salarioTotal}')
print('=-'*20)