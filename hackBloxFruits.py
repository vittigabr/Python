import time

# Letra da música
letra_musica = "Primeira linha da música\nSegunda linha da música\nTerceira linha da música"

# Exibe a letra sequencialmente
for char in letra_musica:
    print(char, end='', flush=True)  # Imprime o caractere sem pular linha
    time.sleep(0.1)  # Espera 0.1 segundos entre cada letra

