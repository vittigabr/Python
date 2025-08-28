print('''        JOGO DA VELHA
      0  [ ] [ ] [ ]
      1  [ ] [ ] [ ]
      2  [ ] [ ] [ ]
          0   1   2''')
velha = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 1
while cont<=9:
    coluna = int(input('Escolha a coluna que vai jogar(número na parte debaixo): '))
    linha = int(input('Escolha a linha que vai jogar(número ao lado esquerdo): '))
    velha[linha][coluna] = input('Você quer o X ou O? ').upper().strip()
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{velha[l][c]:^3}]' , end='')
        print()
    cont+=1