num = []
maior = menor = 0
for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
               
    if cont==0:
        maior = num[cont]
        menor = num[cont]
    else:
        if num[cont]>maior:
            maior = num[cont]
        if num[cont]<menor:
            menor = num[cont]
    
    #maior = max(num)
    #menor = min(num)

print(f'Foram digitados os números {num}.')
print(f'O maior número foi {maior} e estão nas posições ', end='')
for pos, n in enumerate(num):
    if n == maior:
        print(f'{pos + 1}...', end='')
print()
print(f'O menor número foi {menor} e estão nas posições ', end='')
for pos, n in enumerate(num):
    if n == menor:
        print(f'{pos + 1}...', end='')