import os
listaCompras = []
opcao = 0
# Função que mostra a lista na tela
def Mostar_Lista():
    print('Lista: ')
    if listaCompras:
        for i, p in enumerate(listaCompras, start=1): # enumerate(listaCompras, start=x) - o i começa no x
            print(f'{i}º - {p}')
    else:
        print(' (Lista vazia) ')

# Função que limpa a tela
def Limpar_Tela():
    os.system('cls' if os.name=='nt' else 'clear')

# Tela de opções
while opcao!=4:
    Limpar_Tela()
    print('='*50)
    print(f'{'LISTA DE COMPRAS':^50}')
    print('='*50)
    print('''[1] Adicionar na lista
[2] Ver a lista
[3] Remover produto
[4] Sair''')
    
    # Escolha da opção e tratamento de erro
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        # Vai dizer ao usuário escolher uma opção válida
        print('Opção inválida... Tente novamente.')
        print('Escolha uma opção de 1 a 4.')
        continue
    
    # Condições
    if opcao == 1:
        # Se produto ainda não estiver cadastrado, vai ser adicionado a lista
        produto = input('Digite o nome do produto: ').capitalize().strip()
        if produto in listaCompras:
            print('O produto já está cadastrado.')
        else:
            listaCompras.append(produto)
            print(f'{produto} adicionado...')
    elif opcao == 2:
        # Vai mostrar a Lista
        Mostar_Lista()
    elif opcao == 3:
        # Vai pedir nome do produto que será removido
        Mostar_Lista()
        produto = int(input('Digite o número do produto para remover: '))
        print(f'{listaCompras[produto - 1]} foi removido...')
        listaCompras.pop(produto - 1)
    elif opcao<4:
        input('\nPressione qualquer tecla para continuar...')

# Vai encerrar o programa e mostrar a lista
print('Encerrando a lista...')
Mostar_Lista()
print('\nAdeus!')
        