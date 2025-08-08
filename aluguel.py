km = float(input('Quantos km foram percorridos? '))
d = int(input('Quantos dias ele foi alugado? '))
total = km * 0.15 + d * 60
print('O total a pagar é de R${:.2f}'.format(total))