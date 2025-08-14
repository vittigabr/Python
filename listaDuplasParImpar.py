par = []
impar = []
numeros = []
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º número: '))
    
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
par.clear()
impar.clear()
print(numeros)

print(f'Lista completa: {numeros}')