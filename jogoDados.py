from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = []
print('='*30)
print(f'{'Valores Sorteados':^30}')
print('='*30)
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    print('-'*30)
    sleep(0.75)
print('=-'*15)
print(f'{'COLOCAÇÃO DOS RANKS':*^30}')
print('=-'*15)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')
    print('-'*30)
    sleep(0.75)