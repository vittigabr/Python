nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade<=13:
    print('Você é uma criança.')
elif idade<=18:
    print('Você é adolescente.')
else:
    print('Você é adulto.')