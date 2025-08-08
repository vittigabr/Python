n = int(input('Digite um número para realizar seu fatorial: '))
c = n
fatorial = 1
print(f'Calculando: {n}! =', end='')
while c>0:
    print(f'{c}', end= ' ')
    print('x' if c>1 else '=', end=' ')
    fatorial *= c
    c -= 1
print(fatorial)