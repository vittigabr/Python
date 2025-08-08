import datetime

# Recolhendo dados
anoNasc = int(input('Digite seu ano de nascimento: ')) #Ano de nascimento
anoAtual = datetime.date.today().year #Ano registrado no computador
idade = anoAtual - anoNasc #Calculo da idade

# Condições
if idade<=9: # até 9 anos
    print(f'Você tem {idade} anos: mirim')
elif 9<idade<=14: # até 14 anos
    print(f'Você tem {idade} anos: infantil')
elif 14<idade<=19: # até 19 anos
    print(f'Você tem {idade} anos: junior')
elif 19<idade<=25: # até 25 anos
    print(f'Você tem {idade} anos: sênior')
else: # mais de 25 anos
    print(f'Você tem {idade} anos: master')