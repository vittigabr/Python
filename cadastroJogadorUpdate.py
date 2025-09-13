# Criação do dict
dadosJogador = {}
listaDados = []

# Entrada de dados
while True:
    dadosJogador['Nome'] = input('Digite o nome do jogador: ').capitalize().strip()
    dadosJogador['Partidas'] = int(input('Digite a quantida de partidas jogadas: '))
    i = 1
    soma = gol = 0
    gols = []
    while i<=dadosJogador['Partidas']:
        gol = int(input(f'Quantidade de gols feitos na {i}ª partida: '))
        i+= 1
        soma += gol
        gols.append(gol)
    dadosJogador['Gols por Partida'] = gols
    dadosJogador['Total de Gols'] = soma
    listaDados.append(dadosJogador.copy())
    opcao = input('Deseja cadastrar mais um jogador? [S/N]: ').strip().upper()
    if opcao in 'N':
        break

# Tabela dos dados gerais
print('='*50)
print(f'{'Dados do Campeonato por Jogador':^50}')
print('='*50)
for c in range(0, len(listaDados)):
    print(f'{'Nome':<30}: {listaDados[c]['Nome']}')
    print(f'{'Partidas':<30}: {listaDados[c]['Partidas']}')
    print(f'{'Gols por Partida':<30}: {listaDados[c]['Gols por Partida']}')
    print(f'{'Total de Gols':<30}: {listaDados[c]['Total de Gols']}')
    print('-'*50)

# Tabela dos gols marcados por partida
print('='*50)
print(f'{'Quantidade de Gols por Partida':^50}')
print('='*50)
escolha = input('Digite o nome do jogador que deseja visualizar os gols por partida: ').capitalize().strip()
for c in range(0, len(listaDados)):
    if listaDados[c]['Nome']==escolha:
        for i, v in enumerate(listaDados[c]['Gols por Partida']):
            print(f'{i+1}ª partida foram feitos {v} gols.')
            print('-'*50)