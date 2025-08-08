a1 = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão: '))
t = 0
af = 0
escolha = 0
while t<10:
    af = a1 + t*razao
    print(af, end=' --> ')
    t += 1

termos = 20

while escolha!=2:    
    print("""\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[1] Deseja mostra mais termos
[2] Encerrar códgo""")
    escolha = int(input('Faça sua escolha: '))

    if escolha==1:
        while t<termos:
            af = a1 + t*razao
            print(af, end=' --> ')
            t += 1
        termos += 10
    else:
        print('Acabou')
