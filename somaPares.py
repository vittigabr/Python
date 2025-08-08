cont = 0
soma = 0
for c in range(1, 7):
    numero = int(input(f'Digite {c}º número: '))
    if numero%2==0:
        soma+=numero
        cont+= 1
print(f'A somas dos {cont} valores pares é {soma}.')