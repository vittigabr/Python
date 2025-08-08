preco = float(input('Digite o valor do produto: R$'))
print("""FORMA DE PAGAMENTO:
[1] À vista(dinheiro/cheque): 10% de desconto
[2] À vista(cartão): 5% de desconto
[3] Em 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros""")
modo = int(input('Escolha sua forma de pagamento: '))

if modo==1:
    desconto = preco - preco*0.10
    print(f'O valor a ser pago é de R${desconto:.2f}')
elif modo==2:
    desconto = preco - preco*0.05
    print(f'O valor a ser pago é de R${desconto:.2f}')
elif modo==3:
    parcela = preco/2
    print(f'O valor da parcela vai ser de R${parcela:.2f}')
else:
    parcela = int(input('Quantidade de parcelas: '))
    juros = (preco*0.2 + preco)/parcela
    print(f'O valor por parcela será de R${juros}')