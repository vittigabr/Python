from datetime import datetime
import os

# Mostrar data e hora
dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Função para limpar tela
def limpar_Tela():
    comando = 'cls' if os.name=='nt' else 'clear'
    
    if os.system(comando)!=0:
        print('\n'*120)
        
# Dict dos produtos
produtos = {}
totalGeral = 0
# Adicionando items ao dict
while True:
    limpar_Tela()
    produto = input('Digite o nome do produto (ou sair para encerrar o sistema): ').lower()
    if produto in 'sair':
        break
    preco = float(input('Digite o preço do produto: R$'))
    quantidade = int(input('Digite a quantidade de produto: '))
    subtotal = preco*quantidade
    produtos[produto] = [preco, quantidade, subtotal]

# Exibição do cupom fiscal
limpar_Tela()
print('='*60)
print(f'{' CUPOM FISCAL SIMPLIFICADO ':-^60}')
print('='*60)
print(f'Data e hora: {dataHora}')
print('-'*60)
print(f'{'Produto':<20}|{'Preço(R$)':<14}|{'Quantidade':<15}|{'Subtotal'}')
print('-'*60)
for chave, valor in produtos.items():
    print(f'{chave.capitalize():<20}|{valor[0]:<14}|{valor[1]:<15}|R${valor[2]}')
    totalGeral+=valor[2]
print('-'*60)
print(f'{'Total'}{f'R${totalGeral:.2f}':>54}')