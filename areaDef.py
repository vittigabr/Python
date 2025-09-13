# Definição da def para cálculo
def area(c, l):
    areaR = c*l
    print(f'O terreno de comprimento {c}m e largura {l}m tem {areaR}m².')

# Cabeçalho
print('='*40)
print(f'{'Controle da Área':^40}')
print('='*40)

# Programa principal
comprimento = float(input('Digite o comprimento do terreno(m): '))
largura = float(input('Digite a largura do terreno(m): '))  
area(comprimento, largura)