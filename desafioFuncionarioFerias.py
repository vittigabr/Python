import os
from datetime import datetime

setores = {}
mesAlta = ['janeiro', 'julho', 'dezembro']
dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def limpaTela():
    os.system('cls' if os.name=='nt' else 'clear')
    
def pausa():
    input('\nAperte qualquer tecla para continuar...')
    
def exibirMenu():
    print('='*60)
    print(f'{' MENU DE OPÇÕES ':-^60}')
    print('='*60)
    print(f'Data e Hora: {dataHora}')
    print('-'*60)
    print('''1 - Solicitar Férias
2 - Visuaizar setores e quantidadesde funcionários
3 - Sair''')
    
def analiseFerias():
    setorFuncionario = input('Digite seu setor de trabalho: ').upper().strip()
    setores[setorFuncionario] = 0
    tempoTrabalho = int(input('Digite seu tempo de empresa em anos: '))
        if tempoTrabalho>=3:
            print('Pode escolher qualquer mês...')
            mesFerias = input('Digite o mês que deseja tirar férias: ').lower().strip()
    
while True:
    limpaTela()
    exibirMenu()
    opcao = int(input('Digite o número da opção que deseja: '))
    
    if opcao==1:
    elif opcao==2:
    elif opcao==3:
    else: