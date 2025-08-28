# Listas
lista = []
boletim = []

# Entrada de dados e organização das listas
while True:
    nome = input('Digite um nome: ').capitalize().strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    escolha = input('Quer continuar? [S/N]: ').strip().upper()
    
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    boletim.append(lista[:])
    lista.clear()
    if escolha in 'N':
        break

# Exposição em forma de tabela dos dados
print('='*30)
print(f'{'BOLETIM':^30}')
print('='*30)
tot = b = num = 0
print(f'{'Dados dos Alunos':^30}')
print('-'*30)
while tot<=len(boletim):
    if tot>=len(boletim):
        break
    for n in range(0, 3):
        if n==0:
            print(f'nº{num}')
            num+=1
            print(f'Nome: {boletim[b][n]}')
    media = (boletim[b][1]+boletim[b][2])/2
    print(f'Média: {media}')
    print('-'*30)
    tot+=1 
    b+=1

# Mostrar as notas individuais de cada aluno
while True:
    num = int(input('Qual aluno você quer ver as notas? (999 interrompe): '))
    if num==999:
        break
    elif num>len(boletim):
        print('Número inválido, tente novamente...')
        num = int(input('Qual aluno você quer ver as notas? (999 interrompe): '))
    print('='*30)
    print(f'{'NOTAS INDIVIDUAIS':^30}')
    print('='*30)
    print(f'Nome: {boletim[num][0]}')
    print(f'Nota 1: {boletim[num][1]}')
    print(f'Nota 2: {boletim[num][2]}')
    print('-'*30)