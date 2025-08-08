while True:
    valor = int(input('Qual valor deseja sacar? R$'))
    c50 = valor//50
    rvalor = valor - c50*50
    print(f'{c50} cédulas são de R$50.')

    if rvalor//20>0:
        c20 = rvalor//20
        rvalor -= c20*20
        print(f'{c20} cédulas são de R$20.')

    if rvalor//10>0:
        c10 = rvalor//10
        rvalor -= c10*10
        print(f'{c10} cédulas são de R$10.')

    if rvalor//1>0:
        c1 = rvalor//1
        print(f'{c1} cédulas são de R$1.')

    escolha = input('Deseja sacar mais algum valor? [S/N] ').strip().upper()[0]
    if escolha in 'N':
        print('Volte sempre. Obrigado!')
        break