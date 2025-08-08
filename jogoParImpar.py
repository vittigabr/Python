from random import randint
vitorias = 0

while True:
    print('-'*10)
    print('Escolha qual seu time como no jogo Par ou Impar!')
    print("""Impar [1]
Par [2]""")
    print('-'*10)
    escolha = int(input('Escolha par ou impar: '))

    jogador = int(input('Digite um número de 0 a 10: '))
    computador = randint(0, 10)

    soma = jogador + computador

    if escolha==1:
        if soma%2==0:
            print(f'A soma foi {soma}, vc perdeu.')
            print(f'Acabou o jogo. Vc obteve {vitorias} vitórias.')
            break
        else:
            print(f'A soma foi {soma}, vc ganhou.')
            vitorias += 1
            print('Mais uma rodada.')
    else:
        if soma%2==0:
            print(f'A soma foi {soma}, vc ganhou.')
            vitorias += 1
            print('Mais uma rodada.')
        else:
            print(f'A soma foi {soma}, vc perdeu.')
            print(f'Acabou o jogo. Vc obteve {vitorias} vitórias.')
            break