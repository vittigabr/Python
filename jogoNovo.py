# Bibliotecas
import random
import time

#Entrada de dados
computador = random.randint(0, 10)
player = int(input('Digite um número qualquer de 0 até 10: '))

#Analisando
print('Processando...')
time.sleep(2)

#Verificando se é True or False
if player == computador:
    print('Você GANHOU!!!')
else:
    print('Eu escolhi {}, PERDEDOR!!!'.format(computador))