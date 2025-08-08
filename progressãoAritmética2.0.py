a1 = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão: '))
t = 0
af = 0
while t<10:
    af = a1 + t*razao
    print(af, end=' --> ')
    t += 1
print('Acabou')