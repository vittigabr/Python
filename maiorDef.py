# Definição da função
def maior(*num):
    for c in range(0, len(nums)):
        if c==0:
            maiorV = nums[0]
        else:
            if nums[c]>maiorV:
                maiorV = nums[c]
    print(f'Você digitou os valores {num}, ao todo foram {len(nums)} valores.')
    print(f'O maior valor entre eles é {maiorV}.')

# Adicionando os valores a lista
nums = []
while True:
    nums.append(int(input('Digite qualquer número: ')))
    opcao = input('Deseja adicionar mais números? [S/N] ').upper()
    if opcao in 'N':
        break

# Colocando a função para funcionar
print('='*60)
maior(nums)
print('='*60)