# Formação da matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# Formatação da matriz
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    
print('=-'*30)
print(f'{'Soma dos Pares':-^60}')    
# Soma dos pares
somaPares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c]%2==0:
            somaPares += matriz[l][c]
print(f'A soma dos pares é: {somaPares}')

# Soma dos valores da terceira coluna
print('=-'*30)
print(f'{'Soma dos valores da terceira coluna':-^60}')
somaTerceira = 0
for l in range(0, 3):
    somaTerceira += matriz[l][2] 
print(f'A soma dos valores da terceira coluna é: {somaTerceira}')

# Maior valor da segunda linha
print('=-'*30)
print(f'{'Maior valor da segunda linha':-^60}')
maior = 0
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c]>maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda coluna é: {maior}')
print('=-'*30)