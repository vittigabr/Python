somaI = 0
maioridadehomem = 0
nomevelho = ''
cont = 0

for c in range(1, 5):
    print(f'---------{c}ª PESSOA---------')
    nome = input('Nome: ').capitalize().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo(Homem/Mulher): ').capitalize()

    somaI += idade
    
    if idade<20 and sexo=='Mulher':
        cont+=1

    if c==1 and sexo=='Homem':
        maioridadehomem = idade
        nomevelho = nome
    if sexo=='Homem' and idade>maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

media = somaI/4
print(f'A média de idade é {media} anos;')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho.capitalize()}')
print(f'e tem {cont} mulheres com menos de 20 anos.')