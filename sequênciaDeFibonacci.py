termo = int(input('Digite quantos termos  deseja: '))
cont = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
while cont<=termo:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')