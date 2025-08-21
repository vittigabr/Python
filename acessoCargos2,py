#Script para permitir o acesso 

# Solicita o cargo e dia
cargo = input('Digite seu cargo [Gerente/Analista/Estagiário]: ').strip().capitalize()
dia = input('Digite o dia da semana [Segunda,Terça...]: ').strip().capitalize()
semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

# Condições de acesso
# Caso seja Gerente
if cargo in 'Gerente':
    if dia == semana[0]:
        print(f'{cargo}, você não tem acesso hoje.')
    else: 
        print(f'{cargo}, seu acesso está permitido.')
# Caso seja Analista
elif cargo in 'Analista':
    if dia == semana[1:6]:
        print(f'{cargo}, seu acesso está permitido.')
    else:
        print(f'{cargo}, você não tem acesso hoje.')
# Caso seja Estagiário
elif cargo in 'Estagiário':
    if dia == semana[1:6:2]:
        print(f'{cargo}, seu acesso está permitido.')
    else:
        print(f'{cargo}, você não tem acesso hoje.')
# Caso não tenha Cargo Registrado
else:
    print('Você não tem cargo que permite o acesso.')