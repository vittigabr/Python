#Script para permitir o acesso 

# Solicita o cargo e dia
cargo = input('Digite seu cargo [Gerente/Analista/Estagiário]: ').strip().capitalize()
dia = input('Digite o dia da semana [Segunda,Terça...]: ').strip().capitalize()

# Condições de acesso
# Caso seja Gerente
if cargo in 'Gerente':
    if dia in 'Domingo':
        print(f'{cargo}, você não tem acesso hoje.')
    else: 
        print(f'{cargo}, seu acesso está permitido.')
# Caso seja Analista
elif cargo in 'Analista':
    if dia in 'SegundaTerçaQuartaQuintaSexta':
        print(f'{cargo}, seu acesso está permitido.')
    else:
        print(f'{cargo}, você não tem acesso hoje.')
# Caso seja Estagiário
elif cargo in 'Estagiário':
    if dia in 'SegundaQuartaSexta':
        print(f'{cargo}, seu acesso está permitido.')
    else:
        print(f'{cargo}, você não tem acesso hoje.')
# Caso não tenha Cargo Registrado
else:
    print('Você não tem cargo que permite o acesso.')