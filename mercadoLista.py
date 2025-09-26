listaCompras = []

# Tela de opções
while True:
    print('='*50)
    print(f'{'Menu de Opções':^50}')
    print('='*50)
    print('''[1] Adicionar na lista
[2] Ver a lista
[3] Sair''')
    
    # Escolha da opção
    opcao = int(input('Escolha uma opção: '))
    
    # Condições
    if opcao == 1:
        # Se produto ainda não estiver cadastrado, vai ser adicionado a lista
        produto = input('Digite o nome do produto: ').capitalize().strip()
        if produto in listaCompras:
            print('O produto já está cadastrado.')
        else:
            listaCompras.append(produto)
            print('Produto adicionado...')
    elif opcao == 2:
        # Vai mostrar a Lista
        print('Lista: ')
        for c in listaCompras:
            print(f'- {c}')
        print('\n')
    elif opcao == 3:
        # Vai encerrar o programa e mostrar a lista
        print('Encerrando a lista...')
        print('Lista: ')
        for c in listaCompras:
            print(f'- {c}')
        print('\n')
        print('Adeus!')
        break