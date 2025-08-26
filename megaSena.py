# Biblioteca
from random import randint
from time import sleep

# Cabeçário
print('='*40)
print(f'{'JOGA NA  MEGA SENA':^40}')
print('='*40)

# variáveis
jogos = []
lista = []
tot = 1
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot<=quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('='*40)
print(f'{f'SORTEANDO {quant} JOGOS':^40}')
print('='*40)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)