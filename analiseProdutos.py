continuar = nomeBarato = ''
gastoTotal = preco1000 = c = menor = 0
while True:
    if continuar in 'S':
        produto = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        continuar = input('Quer continuar?[S/N] ').strip().upper()[0]
    else:
        break

    c += 1
    gastoTotal += preco

    if preco>1000:
        preco1000 += 1

    if c==1:
        menor = preco
        nomeBarato = produto
    else:
        if preco<menor:
            menor = preco
            nomeBarato = produto

print(f'O gasto total da compra foi de R${gastoTotal:.2f}.')
print(f'{preco1000} produtos tem um valor acima de R$1000,00')
print(f'O produto {nomeBarato} é o mais barato e custa R${menor:.2f}')