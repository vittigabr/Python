comp = int(input('Qual o comprimento da parede? '))
larg = int(input('Qual a largura da parede? '))
m2 = comp*larg
paint = m2/2
print('A parede tem {}m² e vai ser necessário {:.2f}L de tinta para pinta-lá'.format(m2, paint))