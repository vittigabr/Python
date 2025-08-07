#Verificar tempo de empresa e seu reajuste salarial(5%)
nome = input('Digite seu nome: ')
anos = int(input('Digite seu tempo de empresa(anos): '))
salario = float(input('Digite seu salario: '))
atual = salario+salario*0.05

#Verificar se haverá reajuste e mostrar a mensagem na tela
if anos>=3:
    print('Seu nome é {} e tem tempo suficiente para receber o reajuste de 5%, tendo salário atual de R${:.2f}.'.format(nome,atual))
else:
    print('Seu nome é {} e não tem tempo suficiente para receber o reajuste, continuando com salário de R${:.2f}'.format(nome, salario))