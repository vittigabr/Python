#anoAtual = int(input('Digite o ano atual: '))
import datetime
anoAtual = datetime.date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNasc
genero = int(input('Masculino[1] ou Feminino[2]: '))

if genero==1:
    if idade<18:
        print(f'Você ainda não tem idade para se alistar, faltam {18-idade} anos.')
    elif idade==18:
        print(f'Está na hora certa de se alistar.')
    else:
        print(f'Você ja passou {idade-18} anos da idade de se alistar.')
else:
    print('Você não precisa se alistar.')