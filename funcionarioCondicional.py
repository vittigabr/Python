# 04/06/25
#Pede os requisitos
nome = input('Digite seu nome: ')
sal = float(input('Digite seu salário: R$'))
aum = float(input('Digite o aumento do salário(%): '))

#Calcula o novo salário
newsal = sal*(aum/100) + sal

#Mostra a mensagem
print(f'Olá, {nome}, seu salário atual é R${sal:.2f}, você recebeu {aum:.1f}% de aumento, seu novo salário é R${newsal:.2f}')