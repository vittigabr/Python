matriz = [[], [], [],
          [], [], [],
          [], [], []]

cont = 0
for c in range(0, 9):
    n = int(input('Digite um número: '))
    matriz[c].append(n)
    cont += 1
    
print(matriz[:3])
print(matriz[3:6])
print(matriz[6:])