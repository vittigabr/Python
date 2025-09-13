from time import sleep
def contador(inicio, fim, passo):
    if inicio<fim:
        while inicio<=fim:
            print(inicio, end=' -> ', flush=True)
            sleep(0.5)
            inicio += passo
        print('FIM\n')
        print('='*50)
    else:
        while inicio>=fim:
            print(inicio, end=' -> ', flush=True)
            sleep(0.5)
            inicio -= passo
        print('FIM\n')
        print('='*50)

print('Contagem de 1 até 10, de 1 em 1')
contador(1, 10, 1)

print('Contagem de 10 até 0, de 2 em 2')
contador(10, 0, 2)

print('Agora é sua vez, de personalizar sua contagem!')
start = int(input('Início: '))
finish = int(input('Fim: '))
jump = int(input('De quanto em quanto: '))
contador(start, finish, jump)