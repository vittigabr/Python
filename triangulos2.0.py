r1 = int(input('Escreva a medida de um lado do triângulo: '))
r2 = int(input('Escreva a medida de outro lado do triângulo: '))
r3 = int(input('Escreva a medida de outro lado do triângulo: '))

# Dizendo a possibilidade de criação do triângulo
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('É possível formar um triângulo.')
    if r1!=r2!=r3:
        print('Este triângulo é isósceles.')
    elif r1==r2!=r3 or r1==r3!=r2 or r2==r3!=r1:
        print('Este triângulo é escaleno.')
    else:
        print('Este triângulo é equilátero.')
else:
    print('Não é possível formar um triângulo.')