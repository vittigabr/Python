lista = ('Arroz', 30,
         'Feijão', 13.90,
         'Café', 20, 
         'Açúcar', 9.90, 
         'Nescau', 13.50, 
         'Carne', 25.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos%2==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
print('-'*40)