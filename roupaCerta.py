temperatura = float(input('Digite a temperatura atual(Cº): '))

if temperatura>=-50 and temperatura<=60:
    if temperatura<10:
        print('Roupas de inverno são necessárias(casaco, cachecol).')
    elif temperatura>=10 and temperatura<=20:
        print('Roupas de meia estação são necessárias(blusa de manga longa).')
    elif temperatura>=21 and temperatura<=30:
        print('Roupas leves são necessárias(camiseta).')
    else:
        print('Roupas bem leves são necessárias(regata, shorts).')
else:
    print('Temperatura inválida! Por favor insira um valor realista.')