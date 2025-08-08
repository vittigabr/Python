num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num%c==0:
        cont+=1
print(f'O número {num} foi dividido {cont} vezes.')
if cont==2:
    print('Logo ele é PRIMO.')
else:
    print('Logo ele NÃO é PRIMO.')