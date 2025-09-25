print('='*50)
print(f'{' MENU DE OPÇÕES ':-^50}')
print('='*50)
print('''[1] Converter metros para quilômetros
[2] Converter quilômetros para metros
[3] Converter centímetros para metros
[4] Converter metros para centímetros
[5] Converter litros para mililitros
[6] Converter mililitros para litros
[7] Sair''')

while True:
    opcao = int(input('Digite o número da opção que você: '))
    print('+-'*25)

    if opcao==1:
        metros = float(input('Digite o valor a ser convertido: '))
        quilometros = metros/1000
        print(f'{metros}m convertido em quilômetros é {quilometros:.2f}km')
        print('+-'*25)
    elif opcao==2:
        quilometros = float(input('Digite o valor a ser convertido: '))
        metros = quilometros*1000
        print(f'{quilometros}km convertido em metros é {metros:.2f}m')
        print('+-'*25)
    elif opcao==3:
        centimetros = float(input('Digite o valor a ser convertido: '))
        metros = centimetros/100
        print(f'{centimetros}cm convertido em metros é {metros:.2f}m')
        print('+-'*25)
    elif opcao==4:
        metros = float(input('Digite o valor a ser convertido: '))
        centimetros = metros*100
        print(f'{metros}m convertido em centímetros é {centimetros:.2f}cm')
        print('+-'*25)
    elif opcao==5:
        litros = float(input('Digite o valor a ser convertido: '))
        mililitros = litros*1000
        print(f'{litros}L convertido em quilômetros é {mililitros:.2f}mL')
        print('+-'*25)
    elif opcao==6:
        mililitros = float(input('Digite o valor a ser convertido: '))
        litros = mililitros/1000
        print(f'{mililitros}mL convertido em quilômetros é {litros:.2f}L')
        print('+-'*25)
    elif opcao==7:
        print('Encerrando... Tchau!')
        break
    else:
        print('Tente novamente...')
        print('+-'*25)