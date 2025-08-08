escolha = ''
maior = menor = soma = cont = 0
while escolha!='N':
    num = int(input('Digite um número: '))
    escolha = input('Deseja continuar? [S/N]: ').upper()
    soma += num
    cont += 1

    if cont==1:
        maior = num
        menor = num
    else:
        if num>maior:
            maior = num
        if num<menor:
            menor = num

media = soma/cont

print(f'O maior valor é {maior} e o menor valor é {menor}.')
print(f'E a média entre eles é {media}.')