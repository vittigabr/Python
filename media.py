#Inserir nome
nome = input('Digite seu nome: ')
soma = 0

#Inserir as notas
for c in range(0, 4):
    nota = float(input(f'Digite a {c+1}ª nota: '))
    soma += nota

#Cálculo da média
media = soma/4
print(f'Sua média é {media:.2f}')

#Condições de comparação
if media>=7:
    print(f'O aluno, {nome}, está APROVADO.')
elif 7>media>=5:  #media<7 and media>=5:
    print(f'O aluno, {nome}, está de RECUPERAÇÃO.')
else: 
    print(f'O aluno, {nome}, está REPROVADO.')