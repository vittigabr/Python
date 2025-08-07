import random
import time

w = 10
print('=--='*w)
print("""Escolha sua jogada:
[1] Pedra
[2] Papel
[3] Tesoura """)
print('=--='*w)

# Usando a mesma ordem do usuário para o computador decidir qual a jogada.
computador = random.randint(1, 3)
jogador = int(input('Qual vai ser sua jogada? '))

print('Verificando a partida...')
time.sleep(3)

if jogador==1 and computador==3:
    print('Computador escolheu Tesoura.')
    print('Você ganhou!!')
elif jogador==2 and computador==1:
    print('Computador escolheu Pedra.')
    print('Você ganhou!!')
elif jogador==3 and computador==2:
    print('Computador escolheu Papel.')
    print('Você ganhou!!')
elif jogador==1 and computador==2:
    print('Computador escolheu Papel.')
    print('Você perdeu!!')
elif jogador==2 and computador==3:
    print('Computador escolheu Tesoura.')
    print('Você perdeu!!')
elif jogador==3 and computador==1:
    print('Computador escolheu Pedra.')
    print('Você perdeu!!')
else:
    print('Temos um empate')