n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1+n2
subt = n1-n2
mult = n1*n2
divi = n1/n2
divii = n1//n2
potn = n1**n2
print('A soma é {}, a subtração é {}, a multiplicação é {} e a divisão é {:.2f}'.format(soma, subt, mult, divi))
print('A divisão inteira é {} e a potência é {}'.format(divii, potn))
