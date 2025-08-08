a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(0, 11):
    c = a1 + c*razao
    print(c, end=' --> ')
print(' ACABOU')