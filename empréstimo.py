# Recolhendo informações
valorCasa = float(input('Qual o valor da propriedade que deseja? R$'))
salario = float(input('Qual o seu salário? R$'))
parcela = int(input('Quantas parcelas vai pagar? '))

# Calculos
valorParcela = valorCasa/parcela
porcSalario = salario*0.3

print(f'O valor da parcela ficou R${valorParcela:.2f} e 30% do seu salário é R${porcSalario:.2f}')

# Condicionais
if valorParcela>porcSalario:
    print('Seu empréstimo foi reprovado. Sinto muito.')
elif valorParcela==porcSalario:
    print('Pode não ser uma boa ideia comprar esta casa.')
else: 
    print('Ótimo, seu empréstimo foi aprovado.')