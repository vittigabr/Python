import random
import time

print("""O computador vai pensar num número qualquer entre 1 e 10.
Seu objetivo é adivinhar este número.""")

computador = random.randint(1, 10)
player = int(input('Escolha o número: '))
cont = 1

while player!=computador:
    player = int(input('Vc errou, tente novamente: '))
    cont += 1
    print('Verificando...')
    time.sleep(2)

print(f'Parabéns, vc acertou em {cont} tentativas.')