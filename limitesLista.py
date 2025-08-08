nums = []
c = 0
while True:
    num = int(input('Digite um valor: '))
    
    if num not in nums:
        nums.append(num)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar.')
    
    escolha = input('Quer continuar? [S/N] ').strip().upper() #decide se continua ou nao
    if escolha in 'N':
        break #quebra o laço

nums.sort() #ordem crescente
print(f'Vc digitou os valores: {nums}') #mostra valores