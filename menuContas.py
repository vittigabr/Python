escolha = 0 
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

while escolha!=6:
    print("""------ MENU DE AÇÕES ------
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Novos valores
[6] Sair do programa""")
    escolha = int(input('Sua escolha: '))

    if escolha==1:
        soma = numero1 + numero2
        print(f'A soma dos números é {soma}')
    elif escolha==2:
        subtrair = numero1 - numero2
        print(f'A subtração dos números é {subtrair}')
    elif escolha==3:
        multiplicar = numero1 * numero2
        print(f'O produto dos números é {multiplicar}')
    elif escolha==4:
        dividir = numero1/numero2
        print(f'O quociente dos números é {dividir}')
    elif escolha==5:
        print('Vamos recomeçar.')
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
    else:
        print('Adeus!!')