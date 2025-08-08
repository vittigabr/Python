from random import randint
"""a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)

numeros = (a, b, c, d, e)
print(f'Os números sorteados foram: {numeros}')"""

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior valor sortado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')