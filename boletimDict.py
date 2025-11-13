import os
boletim = {}

def limpaTela():
    os.system('cls' if os.name=='nt' else 'clear')

def exibirBoletim():
    limpaTela()
    print('='*80)
    print(f'{' BOLETIM DOS ESTUDANTES ':-^80}')
    print('='*80)
    for k, v in boletim.items():
        print(f'{f'|Nome: {k}':<20}{f'|Notas: {v[0]}':<35}{f'|Média: {v[1]}'}')
    
while True:
    limpaTela()
    nome = input('Digite o nome do aluno: ').capitalize().strip()
    notas = []
    for c in range(1, 5):
        notas.append(float(input(f'Digite a {c}ª nota: ')))
    media = (sum(notas))/4
    boletim[nome] = [notas, media]
    opcao = input('Deseja continuar? [S/N]: ').upper().strip()
    if opcao in 'N':
        break
    
exibirBoletim()