prod = int(input('Qual o preço do produto? '))
desc = int(input('Qual o desconto do produto? '))
pdesc = (prod/100)*desc
valorf = prod-pdesc
print('O produto teve desconto de {}% e sue valor final vai ser de {}R$'.format(desc, valorf))