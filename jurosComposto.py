C = float(input('Qual a capital(R$)? '))
i = float(input('Qual a taxa? '))
t = int(input('Quanto tempo vai ficar(meses)? '))
M = C*(1 + i/100)**t
print(f'Seu capital inicial é de R${C}, sendo investido por {t} meses a uma taxa de {i}%, você obtem R${M:.2f}.')