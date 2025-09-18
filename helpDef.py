def ajuda(cod):
    resp = help(cod)
    return resp

while True:
    comando = input('Digite o comando que precisa de ajuda(digite "fim" para encerrar): ').strip()
    if comando in '':
        print('Tente Novamente...')
    elif comando in 'fim':
        print('Encerrando...')
        break
    else:
        print('='*60)
        print(f'{' MANUAL DO CÓDIGO ':-^60}')
        print('='*60)
        ajuda(comando)