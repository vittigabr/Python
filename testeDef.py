# Soma os números dado pelo dev
def soma(*num):
    somar = sum(num)
    print(f'A soma dos números {num} é {somar}')
    
soma(2, 3)
soma(3, 4, 5)
soma(5, 29, 1)


# Faz uma tabela
def tabela(msg):
    print('='*50)
    print(f'{msg:^50}')
    print('='*50)
    
tabela('Tabela de jogadores')


# Dobra os valores de uma lista
def dobrar(lista):
    pos = 0
    while pos<len(lista):
        lista[pos]*=2
        pos+=1
    print(lista)
    
valores = [2, 3, 4, 5, 6]
print(valores)
dobrar(valores)


# Usa o soma() para somar valores dado pelo usuário
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma(num1, num2)


# Dá ao usuário a escolha dos números e multiplica
def multiplicar():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    vezes = n1*n2
    print(f'O produto de {n1} e {n2} é {vezes}')
    
multiplicar()


# Conta quantos números foram dados a função
def contador(*num):
    cont = len(num)
    print(f'Vc me passou {cont} números')
    
contador(2, 5, 6, 3, 2, 6, 7)