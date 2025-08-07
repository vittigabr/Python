while True:
    sacar = float(input('Digite o valor que deseja sacar: R$'))

    ced50 = sacar//50
    rvalor = sacar - ced50*50
    print(f'{ced50} cédulas são de R$50.')

    if rvalor//20!=0:
        ced20 = rvalor//20
        rvalor -= ced20*20
        print(f'{ced20} cédulas são de R$20.')
    else:
        if rvalor//10!=0:
            ced10 = rvalor//10
            rvalor -= ced10*10
            print(f'{ced10} cédulas são de R$10.')

        if rvalor//1!=0:
            ced1 = rvalor//1
            print(f'{ced1} cédulas são de R$1.')

    escolha = input('Deseja retirar mais algum valor?[S/N]: ').strip()

    if escolha in 'Nn':
        print('Volte sempre!!')
        break