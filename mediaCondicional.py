#Cálculo da média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

#Calculando a média
M = (n1+n2+n3+n4)/4

#Mostrando o resultado
print('A média das notas {:.2f}, {:.2f}, {:.2f}, {:.2f} é igual a {:.2f}'.format(n1, n2, n3, n4, M))

#Situação do  aluno
if M>=6:
    print('Parabéns, você foi APROVADO!!')
elif M<=4.9:
    print('Você não passou, estude mais, está REPROVADO:(')
else:
    print('Você está de recuperação')