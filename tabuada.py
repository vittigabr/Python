tab = int(input('Qual tabuada vamos fazer? '))
quant = int(input('Quantas vezes vamos repetir? '))
for i in range(quant+1):
    print('{} X {}= {}'.format(tab, i, tab*i))