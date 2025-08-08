sexo = input('Digite seu sexo[M/F]: ')
while sexo!='M' and sexo!='F':
    sexo = input('Dados inválidos, por favor, informe novamente: ')
print(f'Sexo {sexo} registrado com sucesso.')