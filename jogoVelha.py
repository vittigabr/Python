import os
def adicionarPontos():
    global vitoriasO, vitoriasX
    if velha[linha][coluna] in 'X':
        vitoriasX+=1
    else:
        vitoriasO+=1
        
def limpaTela():
    comando = 'cls' if os.name=='nt' else 'clear'
    
    if os.system(comando)!=0:
        print('\n'*120)

def exibirTabuleiro():
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{velha[l][c]:^3}]' , end='')
        print()
        
print('''        JOGO DA VELHA
      0  [ ] [ ] [ ]
      1  [ ] [ ] [ ]
      2  [ ] [ ] [ ]
          0   1   2''')
velha = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
vitoriasX = 0
vitoriasO = 0
while True:
    cont = 1
    while cont<=9:
        linha = int(input('Escolha a linha que vai jogar(número ao lado esquerdo): '))
        coluna = int(input('Escolha a coluna que vai jogar(número na parte debaixo): '))
        velha[linha][coluna] = input('Você quer o X ou O? ').upper().strip()
        exibirTabuleiro()
        input('Pressione qualquer tecla para continuar...')
        if cont>=3:
            if velha[0][0] and velha[1][1] and velha[2][2] or velha[2][0] and velha[1][1] and velha[0][2] in 'XO': #diagonais
                print(f'{velha[linha][coluna]} ganhou')
                adicionarPontos()
                break
            elif velha[0][0] and velha[1][0] and velha[2][0] or velha[0][1] and velha[1][1] and velha[2][1] or velha[0][2] and velha[1][2] and velha[2][2] in 'XO': #verticais
                print(f'{velha[linha][coluna]} ganhou')
                adicionarPontos()
                break
            elif velha[0][0] and velha[0][1] and velha[0][2] or velha[1][0] and velha[1][1] and velha[1][2] or velha[2][0] and velha[2][1] and velha[2][2] in 'XO': #verticais
                print(f'{velha[linha][coluna]} ganhou')
                adicionarPontos()
                break
            else:
                print('Deu empate')
        cont+=1
        limpaTela()
        exibirTabuleiro()
        
    resposta = input('Deseja jogar mais uma partida? [S/N]: ').upper().strip()
    if resposta in 'N':
        print('Encerrando...')
        break

print('='*60)
print(f'{' PLACAR DE VITÓRIAS ':^60}')
print('='*60)
print(f'Vitórias do X: {vitoriasX}')
print(f'Vitórias do O: {vitoriasO}')