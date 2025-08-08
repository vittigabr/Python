cont = num = soma =  0
while num!=999:
    num = int(input('Digite um número[999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'A soma dos números foi de {soma}.')
print(f'Foram feitas {cont} tentativas.')