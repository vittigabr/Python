lista = []
boletim = []
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

print('='*30)
print(f'{'BOLETIM':^30}')
print('='*30)
tot = b = 0
print(f'{'Dados dos Alunos':^30}')
while tot<=len(boletim):
    if tot>=len(boletim):
        break
    for n in range(0, 3):
        if n==0:
            print(f'Nome: {boletim[b][n]}')
        else:
            print(f'Nota {n}: {boletim[b][n]}')
    media = (boletim[b][1]+boletim[b][2])/2
    print(f'Média: {media}')
    print('-'*30)
    tot+=1 
    b+=1