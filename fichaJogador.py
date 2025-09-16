def ficha(nome, points):
    if nome=='':
        nome = '<desconhecido>'
    if points=='':
        points = '0'
    return print(f'O jogador {nome} fez {points} ponto(s) no campeonato.')

nome = input('Digite seu nome: ').strip().capitalize()
pontos = input('Digite quantos gols foram marcados: ')
ficha(nome, pontos)