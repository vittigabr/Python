numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))

print('=-='*20)
print(f'Você digitou os valores {numeros}')
print('=-='*20)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
print('=-='*20)
if numeros.count(3)>= 1:
    print(f'O número 3 está na {numeros.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('=-='*20)
print('Os valores pares digitados foram ', end=' ')
for n in numeros:
    if n%2==0:
        print(n, end=' ')