def  leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = input(msg)
        if n.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('*'*40)
            print('ERRO! Digite um número inteiro válido.')
            print('*'*40)
        if ok:
            break
    return valor
    
# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')