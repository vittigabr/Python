while True:
    num = int(input('DIigte o número que deseja a tabuada: '))
    cont = 0
    while cont<=10:
        print(f'{num} X {cont} = {num * cont}')
        cont += 1

    escolha = input('Deseja digitar outro número? [S/N]: ')
    if escolha in 'Nn':
        print('Obrigado, volte sempre!')
        break