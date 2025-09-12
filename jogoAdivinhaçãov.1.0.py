from random import choice
from time import sleep

print('=--='*20)
print('Olá, você terá que adivinhar qual número o computador vai escolher entre 0 e 5.')
print('=--='*20)

n1 = int(input('Digite o número: ')) # Jogador tenta adivinhar o número
lista = [0, 1, 2, 3, 4, 5] # Lista dos números do cumputador
lista = choice(lista)

print('Pensando...')
sleep(2)

if n1 == lista:
    print('Parabéns, você acertou!!!')
else:
    print(f'O número escolhido pelo computador foi {lista}.')
    print('Você perdeu :(')
