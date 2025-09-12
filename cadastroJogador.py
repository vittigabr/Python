# Criação do dict
dadosJogador = {}

# Entrada de dados
dadosJogador['Nome'] = input('Digite o nome do jogador: ').capitalize()
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

# Tabela dos dados gerais
print('='*50)
print(f'{'Dados do Campeonato por Jogador':^50}')
print('='*50)
for k, v in dadosJogador.items():
    print(f'{k:.<20}: {v}')

# Tabela dos gols marcados por partida
print('='*50)
print(f'{'Quantidade de Gols por Partida':^50}')
print('='*50)
for i, v in enumerate(dadosJogador['Gols por Partida']):
    print(f'{i+1}ª partida foram feitos {v} gols.')
    print('-'*50)