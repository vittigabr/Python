print('=--='*20)
print("""Opções de escolha de base para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal""")
print('=--='*20)

escolha = int(input('Em qual base deseja converter um número? '))
numero = int(input('Escreva qualquer número: '))

if escolha == 1:
    print(f'O número {numero} convertido para Binário é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} convertido para Octal é igual a {oct(numero)[2:]}')
elif escolha == 3: 
    print(f'O número {numero} converido para Hexadecimal é igual a {hex(numero)[2:]}')
else: 
    print('Esta opção é inválida')