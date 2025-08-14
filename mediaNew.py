soma = 0

# Entrada de notas
for c in range(0,4):
    notas = float(input('Digite sua nota: '))
    soma += notas

# Cálculo de média
media = soma/4

# Condicionais da média
if media<=4:
    print(f'Sua média foi {media:.2}, você está REPROVADO.')
elif 5>media>=7:
    print(f'Sua média foi {media:2f}, você está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi {media:.2f}, você está APROVADO.')