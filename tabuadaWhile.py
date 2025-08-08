while True:
    n = int(input('Digite um número para tabuada: '))
    print('-'*15)
    for t in range(0, 11):
        produto = n*t
        print(f'{n}x{t} = {produto}')
        t += 1
    print('-'*15)
    if n<0:
        print('TABUADA ENCERRADA, volte sempre!')
        break
