from datetime import datetime
import os

# Mostrar data e hora
dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Função para limpar tela
def limpar_Tela():
    comando = 'cls' if os.name=='nt' else 'clear'
    
    if os.system(comando)!=0:
        print('\n'*120)

def exibirMenu():
    print('='*60)
    print(f'{' MENU PRINCIPAL ':^60}')
    print('='*60)
    print('''[1] - Adicionar produto
[2] - Exibir produtos
[3] - Gerar cupom fiscal
[4] - Sair''')
    
def cupomFiscal():
    # Exibição do cupom fiscal e calculando total
    print('='*60)
    print(f'{' CUPOM FISCAL SIMPLIFICADO ':-^60}')
    print('='*60)
    print(f'Data e hora: {dataHora}')
    print('-'*60)
    print(f'{'Produto':<20}|{'Preço(R$)':<14}|{'Quantidade':<15}|{'Subtotal'}')
    print('-'*60)
    for chave, valor in produtos.items():
        print(f'{chave:<20}|{valor[0]:<14}|{valor[1]:<15}|R${valor[2]}')
        totalGeral+=valor[2]
    print('-'*60)
    print(f'{'Total'}{f'R${totalGeral:.2f}':>54}')
        
def adicionarProduto():
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    quantidade = int(input('Digite a quantidade de produto: '))
    subtotal = preco*quantidade
    produtos[produto] = [preco, quantidade, subtotal]
    
# Dict dos produtos
produtos = {}
totalGeral = 0
# Adicionando items ao dict
while True:
    limpar_Tela()
    exibirMenu()
    opcao = int(input('Escolha o número da opção: '))
    if opcao==1:
        adicionarProduto()
    elif opcao==3:
        cupomFiscal()
    elif opcao==4:
        break
        
        