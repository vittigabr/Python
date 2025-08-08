while True:
    extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    num = int(input('Qual número de 0 a 20 vc deseja? '))
    
    if num>20 or num<0:
        while num>20 or num<0:
            num = int(input('Tente novamente. Digite um número de 0 a 20: '))

    print(f'Vc digitou o número {extenso[num]}')

    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha in 'N':
        print('Obrigado, volte sempre!')
        break