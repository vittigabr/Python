# inserir as notas e nome
nome = input('Digite seu nome: ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))

#Verificando a média
media = (n1+n2+n3+n4)/4
print(f'Sua média é {media:.2f}')

#condição do aluno
if media>=7:
    print(f'O aluno, {nome}, está APROVADO.')
elif 5>=media<7:
    print(f'O aluno, {nome}, está de RECUPERAÇÃO.')
else: 
    print(f'O aluno, {nome}, está REPROVADO.')
    
