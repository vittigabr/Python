# Entrando com os valores
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Testando qual o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor é {}'.format(menor))

# Testando o maior

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
        maior = c
print('O maior valor é {}'.format(maior))