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

# Adicionando items ao dict
while True:
    limpar_Tela()
    produto = input('Digite o nome do produto (ou sair para encerrar o sistema): ').lower()
    if produto in 'sair':
        break
    preco = float(input('Digite o preço do produto: R$'))
    quantidade = int(input('Digite a quantidade de produto: '))
    total = preco*quantidade
    produtos[produto] = [preco, quantidade, total]

limpar_Tela()
print('='*60)
print(f'{' CUPOM FISCAL SIMPLIFICADO ':-^60}')
print('='*60)
print(f'Data e hora: {dataHora}')
print('-'*60)
print(f'{'Produto':<20}|{'Preço(R$)':<14}|{'Quantidade':<15}|{'Total'}')
print('-'*60)
for k, v in produtos.items():
    print(f'{k.capitalize():<20}|{v[0]:<14}|{v[1]:<15}|{v[2]}')