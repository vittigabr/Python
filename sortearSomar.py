# Importação e criação das listas e bibliotecas
from random import randint
listaValores = []
pares = []

# Funções estabelecidas
def line(x):
    print('='*x)
    
def sortear(a, b):
    for c in range(0, 5):
        listaValores.append(randint(a, b))
    print(f'Os números sortados foram: {listaValores}')

def somaPar():
    soma = 0
    for c in listaValores:
        if c%2==0:
            pares.append(c)
            soma+=c
    print(f'A soma dos {pares} tem o valor de {soma}')

# Entrada de dados e resultado
a = int(input('Digite a margem de começo do sorteio: '))
b = int(input('Digite a margem final do sorteio: '))
line(40)
print(f'O sorteio vai ser de 5 números de {a} até {b}.')
sortear(a, b)
line(40)
somaPar()