print('Vamos descobrir se o númeor que você escolher vai ser Par ou Ímpar')
n1 = int(input('Digite um número: '))
parImpar = n1%2
if parImpar == 0:
    print(f'O número {n1} é par!!')
else:
    print(f'O número {n1} é ímpar')