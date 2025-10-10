import os
import time

def pausa():
    input('\nPressione ENTER para continuar...')
    
def limpar_tela():
    #Tenta limpar a tela de forma cross-platform; se falhar, imprime muitas linhas.
    comando = 'cls' if os.name == 'nt' else 'clear'
    # se o comando retornar diferente de 0, usa fallback
    if os.system(comando) != 0:
        print("\n" * 120)
        
def exibir_menu():
    print('='*60)
    print(f'{' Bem-vindo ao Seu Banco ':^60}')
    print('='*60)
    print('''Escolha uma opção: 
[1] - Consultar saldo
[2] - Saque
[3] - Depósito
[4] - Sair''')

def exibir_saldo(saldo):
    print(f'Seu saldo atual é: R${saldo:.2f}')
    
def realizar_saque():
    global saldo
    try:
        while True:
            saque = float(input('Digite o valor que deseja sacar: R$'))
            if saque>saldo:
                print(f'Saldo insuficiente para sacar R${saque}.')
                break
            elif saque==0:
                print('O valor do saque deve ser positivo. Tente novamente...')
            else:
                saldo-=saque
                print('Valor sacado com sucesso...')
                print(f'Novo saldo: {saldo:.2f}')
                break
    except ValueError:
        print('ERRO! Digite um valor monetário.')

def realizar_deposito():
    global saldo
    try:
        while True:
            deposito = float(input('Digite o valor que deseja depositar: R$')) 
            if deposito>0:
                saldo+= deposito
                print(f'Depósito de R${deposito:.2f} executado com sucesso.')
                print(f'Novo saldo: R${saldo:.2f}')
                break
            else:
                print('Você não informou o valor do depósito. Tente novamente...')
    except ValueError:
        print('ERRO! Digite um valor monetário.')
        
def main():
    global saldo
    saldo = 1000
    while True: 
        limpar_tela()
        
        #Mostra a data e hora atual
        dataHoraAtual = time.strftime('%d/%m/%Y %H:%M:%S')
        print(f'Data e Hora Atual: {dataHoraAtual}')
        
        exibir_menu()
        opcao = int(input('Digite o número da opção desejada: '))
        if opcao == 1:
            exibir_saldo(saldo)
            pausa()
        elif opcao == 2:
            realizar_saque()
            pausa()
        elif opcao == 3:
            realizar_deposito()
            pausa()
        elif opcao == 4:
            print('\n')
            print('='*60)
            print(f'{' Encerrando programa ':^60}')
            print('='*60)
            fim = 'Saindo do Programa...'
            for c in fim:
                print(c, end='', flush=True)
                time.sleep(0.1)
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            pausa()

if __name__ == '__main__':
    main()