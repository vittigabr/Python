lista = []
contador = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    contador += 1

    escolha = input('Quer continuar? [S/N]: ')
    if escolha in 'Nn':
        break 

print('=-='*30)
a = print(f'Foram digitados {contador} elementos.')
print('=-='*30)
lista.sort(reverse=True)
b = print(f'A lista em ordem decrescente: {lista}')
print('=-='*30)
if 5 in lista:
    print('O 5 faz parte da lista.')
else:
    print('O 5 não faz parte da lista.')