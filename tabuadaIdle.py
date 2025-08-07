tab = int(input('Qual tabuada faremos? '))
quant = int(input('Qauntas vezes vamos repetir? '))
for i in range(quant+1):
    print('{} X {} = {}'.format(tab, i, tab*i))
