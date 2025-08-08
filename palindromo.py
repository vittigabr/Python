#palavra= 'Python'
#for letra in palavra:
#    print(letra)
# Curso em video

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto==inverso:
    print(f'{junto} e {inverso} são palindromos pois são iguais.')
else:
    print(f'{junto} e {inverso} não são palindromos')