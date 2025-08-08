#Crie um programa que leia o nome, peso e idade de 5 pessoas e mostre no final todos os dados do que possui maior e menor peso.

maior = 0
menor = 0
nomeMaior = ''
nomeMenor = ''
idadeMaior = 0
idadeMenor = 0

for c in range(1, 6):
    print(f'------ {c}ª PESSOA ------')
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    peso = float(input('Peso(kg): '))

    if c==1:
        maior = peso
        menor = peso
    else: 
        if peso>maior:
            maior = peso
            nomeMaior = nome
            idadeMaior = idade
        if peso<menor:
            menor = peso
            nomeMenor = nome
            idadeMenor = idade

print(f'A pessoa com maior peso tem {maior}kg, chama {nomeMaior} e tem {idadeMaior} anos.')
print(f'A pessoa com menor peso tem {menor}kg, chama {nomeMenor} e tem {idadeMenor} anos.')