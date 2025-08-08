num = int(input('Digite a tabuada que deseja: '))
c = int(input('Digite até qual número deverá ir: '))
for t in range(0, c+1):
    tabuada = num*t
    print(f'{num} X {t} = {tabuada}')