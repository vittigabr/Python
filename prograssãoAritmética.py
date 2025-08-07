n = int(input('Qual o termo que você deseja conhecer? '))
a1 = int(input('Qual o primeiro termo da sequência? '))
r = int(input('Qual a razão da sequência? '))
an = a1 + (n - 1)*r
print(f'O termo {n}º tem o valor correspondente a {an}.')

sn = ((a1 + n)*n)/2
print(f'A soma dos termos é igual a {sn}.')