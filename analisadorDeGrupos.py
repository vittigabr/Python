continuar = ''
cont18 = contHomem = contMulher20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    if continuar in 'S':
        idade = int(input('Digite sua idade: '))
        sexo = input('Digite seu sexo[H/M]: ').strip().upper()[0]
        continuar = input('Quer continuar[S/N]: ').strip().upper()[0]
    else:
        break

    if idade>18:
        cont18 += 1
    if sexo in 'H':
        contHomem += 1
    if idade<18 and sexo in 'M':
        contMulher20 += 1

print(f'Foram cadastrados {cont18} pessoas maiores de idade.')
print(f'Foram cadastrados {contHomem} homens.')
print(f'E {contMulher20} mulheres menor de idade.')