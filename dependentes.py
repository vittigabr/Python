print('='*50)
print(f'{'SOLICITAÇÃO':^50}')
print('='*50)

# Entrada de dados
salarioAtual = float(input('Digite seu salário atual: '))
quantidadeDependentes = int(input('Digite a quantidade de dependentes: '))

# Condições para aumento de salário
if quantidadeDependentes==0:
    porcentagem = 0.05
    salarioNovo = salarioAtual*porcentagem + salarioAtual
elif quantidadeDependentes==1 or quantidadeDependentes==2:
    porcentagem = 0.10
    salarioNovo = salarioAtual*porcentagem + salarioAtual
elif quantidadeDependentes==3 or quantidadeDependentes==4:
    porcentagem = 0.15
    salarioNovo = salarioAtual*porcentagem + salarioAtual
else:
    porcentagem = 0.20
    salarioNovo = salarioAtual*porcentagem + salarioAtual

print('-*'*25)
print(f'{'EXIBIÇÃO DOS DADOS':^50}')    
print('-*'*25)
print(f'{'Quantidade de Dependentes':<30}: {quantidadeDependentes}')
print(f'{'Porcentagem de Aumento':<30}: {porcentagem*100}%')
print(f'{'Novo Salário':<30}: R${salarioNovo:.2f}')