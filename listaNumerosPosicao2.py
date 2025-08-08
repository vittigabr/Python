nums = []
maior = menor = 0
for c in range(0, 5):
    nums.append(int(input(f'Digite o {c + 1}º valor: ')))
    if c==0:
        maior = menor = nums[c]
    else:
        if nums[c]>maior:
            maior = nums[c]
        if nums[c]<menor:
            menor = nums[c]

print(f'Os valores digitados foram: {nums}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for p, v in enumerate(nums):
    if v==maior:
        print(f'{p + 1}...', end= '')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for p, v in enumerate(nums):
    if v==menor:
        print(f'{p + 1}...', end='')