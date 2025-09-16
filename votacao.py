import datetime
def voto(anoNasc):
    idade = datetime.date.today().year - anoNasc
    if idade<16:
        condicao = 'NEGADO'
    elif 15<idade<18 or idade>59:
        condicao = 'OPCIONAL'
    else:
        condicao = 'OBRIGATÓRIO'
    return condicao

anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - anoNascimento
print(f'Você nasceu em {anoNascimento}, tem {idade} anos de idade, seu voto é {voto(anoNascimento)}.')