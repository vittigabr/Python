tabelaB = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Bahia',
         'Palmeiras', 'Botafogo', 'Fluminense', 'Atlético-MG', 
         'Ceará SC', 'Mirassol', 'Corinthians', 'Grêmio', 
         'Internacional', 'Vasco da Gama', 'São Paulo', 'Santos', 
         'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')
a = (tabelaB[0:5])
b = (tabelaB[16:]) #[-4:]
c = (sorted(tabelaB))
d = (tabelaB.index('Palmeiras') + 1)

print('=-=' * 30)
print(f'Lista de times do Brasileirão: {tabelaB}')
print('=-=' * 30)
print(f'Os 5 primeiros são: {a}')
print('=-=' * 30)
print(f'Os 4 últimos são: {b}')
print('=-=' * 30)
print(f'Times em ordem alfabética: {c}')
print('=-=' * 30)
print(f'O Palmeiras está em {d}ª posição')