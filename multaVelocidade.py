velocidade = float(input('Qual a velocidade do carro: km '))
multa = (velocidade - 80) * 7
if velocidade <=80:
    print('Pode prosseguir, você não foi multado')
else:
    print('Você foi multado e vai pagar R$7.00 por km aima do limite de 80km/h')
    print(f'Você vai pagar um total de R${multa:.2f}')