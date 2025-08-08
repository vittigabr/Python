kg = float(input('Digite seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = kg/(altura**2)

print(f'Seu IMC é de {imc:.2f}')
print('Sua condição é de: ', end= '')

if(imc <=18.4):
    print('Abaixo do peso')
elif(imc>=18.5) and (imc<=24.9):
    print('Peso normal (saudável)')
elif(imc>=25.0) and (imc<=29.9):
    print('Sobrepeso')
elif(imc>=30.0) and (imc<=34.9):
    print('Obesidade grau I')
elif(imc>=35.0) and (imc<=39.9):
    print('Obesidade grau II (severa)')
else:
    print('Obesidade grau III (mórbida)')