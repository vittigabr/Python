nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: R$'))
if salario > 1250:
    salarioa = salario * 0.10 + salario
else:
    salarioa = salario * 0.15 + salario
print(f'{nome}, seu salário agora é de R${salarioa}')