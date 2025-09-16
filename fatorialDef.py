from math import factorial
def fatorial(n, show=False):
    """fatorial: Faz somente o cálculo ou pode mostrar o caminho
    da conta dependendo do pedido
    n = número que deseja fatorial
    show=False = não mostra o caminho da conta
    show=True = mostra o caminho da conta 
    return = o resultado do fatorial de um número n
    """
    resultado = factorial(n)
    if show==True:
        for c in range(n, 0, -1):
            if c>1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {resultado}')
    else:
        return print(f'{resultado}')

num = int(input('Digite o número que deseja o fatorial: '))
opcao = input('Quer ver a conta? [S/N]: ').upper()
if opcao in 'S':
    opcao = True
print('-'*50)
print(f'{'RESULTADO':^50}')
print('-'*50)
fatorial(num, opcao)