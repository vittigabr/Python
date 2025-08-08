import random
computador = random.randint(0, 50)
resp1 = input('Vc deseja uma dica? ou chutar o número?(S/N) ')

if resp1 == 'S':
    if computador%2 == 0:
        print('O número é par.')
    else:
        print('O número é impar.')
else:
    resp2 = input('Qual seria o número? ')

if resp2 == computador:
    print('Vc ganhou')
else:
    resp3 = ('Quer mais uma dica? S/N ')

if resp3 == 'S':
    antecessor = computador-1
    sucessor = computador+1
    print(f'O antecessor do número {computador} é {antecessor}.')
    print(f'O antecessor do número {computador} é {sucessor}.')
else:
    resp4 = input('Qual o número? ')

if resp4 == computador:
    print('Vc ganhou!!')