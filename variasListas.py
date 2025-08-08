lista = []
listaPar = []
listaImpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    if n%2==0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break

print('=-='*30)
print(f'Lista geral: {lista}.')
print('=-='*30)
print(f'Lista de pares: {listaPar}')
print('=-='*30)
print(f'LIsta de ímpares: {listaImpar}')