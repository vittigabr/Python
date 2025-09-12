# Entrada de dados e criação do dict
dadosPessoas = {}
listaPessoas = []
while True:
    dadosPessoas['Nome'] = input('Digite o nome: ').capitalize().strip()
    dadosPessoas['Idade'] = int(input('Digite a idade: '))
    dadosPessoas['Sexo'] = input('Homem[H] ou Mulher[M]: ').upper()
    opcao = input('Cadastrar outra pessoa[S/N]: ').upper()
    listaPessoas.append(dadosPessoas.copy())
    if opcao in 'N':
        break

# Telas que mostram resultados específicos
print('='*50)
print(f'{'Pessoas Cadastradas':^50}')
print('='*50)
print(f'Foram cadastradas {len(listaPessoas)} pessoas.')

print('='*50)
print(f'{'Média de Idade':^50}')
print('='*50)
idade = []
for c in range(0, len(listaPessoas)):
    idade.append(listaPessoas[c]['Idade'])
somaIdade = sum(idade) # Comando que soma (sum(***))
media = somaIdade/len(listaPessoas)
print(f'A média de idade é de {media}')

print('='*50)
print(f'{'Somente Mulheres':^50}')
print('='*50)
for c in range(0, len(listaPessoas)):
    if listaPessoas[c]['Sexo'] in 'M':
        print(f'{'Nome':_<30}: {listaPessoas[c]['Nome']}')
        print(f'{'Idade':_<30}: {listaPessoas[c]['Idade']}')
        print(f'{'Sexo':_<30}: {listaPessoas[c]['Sexo']}')
        print('-'*50)

print('='*50)
print(f'{'Pessoas com Idade Acima da Média':^50}')
print('='*50)     
for c in range(0, len(listaPessoas)):
    if listaPessoas[c]['Idade']>media:
        print(f'{'Nome':_<30}: {listaPessoas[c]['Nome']}')
        print(f'{'Idade':_<30}: {listaPessoas[c]['Idade']}')
        print(f'{'Sexo':_<30}: {listaPessoas[c]['Sexo']}')
        print('-'*50)