'''nums = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))

    if c==0:
        nums.append(num)
        print('O número foi adicionado ao final da lista...')
    elif num<nums[0]:
        nums.insert(num, 0)
        print('O número foi adiciona na posição 0...')
    elif nums[0]<num<nums[1]:
        nums.insert(num, 1)
        print('O número foi adicionado na posição 1...')
    elif num>nums[1] or num>nums[2]:
        nums.append(num)
        print('O número foi adicionado ao final da lista...')
    elif nums[1]<num<nums[2]:
        nums.insert(num, 2)
        print('O número foi adicionado na posição 2...')
    elif nums[2]<num<nums[3]:
        nums.insert(num, 3)
        print('O número foi adicionado na posição 3...')
    else:
        nums.append(num)

print('=-=' *30)
print(f'A lista ficou assim: {nums}.')
print('=-=' *30)'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c==0 or n>lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos<len(lista):
            if n<=lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('=-=' *30)
print(f'Os valores digitados em ordem foram: {lista}.')