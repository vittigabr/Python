print('Vc quer fazer uma viagem')
viagem = float(input('Me diga qual a distância da viagem: ')) # Lê a distância da viagem
if viagem <= 200: # Calcula o valor se for até 200km
    preco = viagem * 0.5
    print('O custo do transporte vai ser de R${:.2f}'.format(preco))
else: # Calcula o valor da viagem se for maior que 200km
    preco = viagem * 0.45
    print('O custo do transporte vai ser de R${:.2f}'.format(preco))