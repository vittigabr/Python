import random
import time

print("""O computador vai pensar num número qualquer entre 0 e 30.
Seu objetivo é adivinhar este número.""")

computador = random.randint(0, 30)
player = int(input('Escolha o número: '))
cont = 1

while player!=computador:
    if player<computador:
        player = int(input('Mais... Tente novamente: '))
    else: 
        player = int(input('Menos... Tente novamente: '))
    cont += 1
    print('Verificando...')
    time.sleep(1)

print(f'Parabéns, vc acertou em {cont} tentativas.')
