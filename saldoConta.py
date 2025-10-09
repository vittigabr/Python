import os

def limpar_tela():
    #Tenta limpar a tela de forma cross-platform; se falhar, imprime muitas linhas.
    comando = 'cls' if os.name == 'nt' else 'clear'
    # se o comando retornar diferente de 0, usa fallback
    if os.system(comando) != 0:
        print("\n" * 120)

saldo = 1000

while True: 
    limpar_tela()
    print('='*60)
    print(f'{' Bem-vindo ao Seu Banco ':^60}')
    print('='*60)
    print('''Escolha uma opção: 
[1] - Consultar saldo
[2] - Saque
[3] - Sair''')
    
    try:
        opcao = int(input('Digite o número da opção desejada: '))
    except ValueError:
        print('Opção inválida... Digite uma opção válida.')
        
    if opcao == 1:
        print(f'Seu saldo atual é: R${saldo:.2f}')
    elif opcao == 2:
        saque = float(input('Digite o valor que deseja sacar: R$'))
        saldo -= saque
    elif opcao == 3:
        print('\n')
        print('='*60)
        print(f'{' Encerrando programa ':^60}')
        print('='*60)
        break
    
    input('\nPressione ENTER para continuar...')