from exerciciosCursoVideo import moeda

while True:
    print('='*50)
    print(f'{' Menu de Opções ':-^50}')
    print('='*50)
    print('''[1] Aumento
[2] Desconto
[3] Dobrar
[4] Metade
[5] Sair''')
    opcao = int(input('Digite sua escolha: '))
    print('-*'*25)

    if opcao==1:
        dinheiro = float(input('Digite o valor a ser inserido: '))
        aumento = float(input('Digite a porcentagem de aumento: '))
        print(f'O valor {dinheiro}R$ com o aumento {aumento}% é de {moeda.aumentar(dinheiro, aumento)}R$')
    elif opcao==2:
        dinheiro = float(input('Digite o valor a ser inserido: '))
        desconto = float(input('Digite a porcentagem do desconto: '))
        print(f'O valor {dinheiro}R$ com o desconto de {desconto}% é de {moeda.diminuir(dinheiro, desconto)}R$')    
    elif opcao==3:
        dinheiro = float(input('Digite o valor a ser inserido: '))
        print(f'O valor {dinheiro}R$ dobrado é de {moeda.dobro(dinheiro)}R$')
    elif opcao==4:
        dinheiro = float(input('Digite o valor a ser inserido: '))
        print(f'O valor {dinheiro}R$ pela metade é de {moeda.metade(dinheiro)}R$')
    elif opcao==5:
        print('Adeus...Encerrando.')
        break
    else:
        print('Opção inválida, tente novamente...')