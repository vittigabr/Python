class Acougue:
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        
    def exibir_detalhes(self):
        return print(f'O nome da carne é {self.nome}, com o código {self.codigo}, no preço R${self.preco}.')
    
class Peixe(Acougue):
    def __init__(self, nome, codigo, preco, tipo, tempo):
        super().__init__(nome, codigo, preco)
        self.tipo = tipo
        self.tempo = tempo
        
    def exibir_detalhes(self):
        return print(f'É carne de {self.nome}, com o código {self.codigo}, no preço R${self.preco}, sendo um peixe de água {self.tipo} e está {self.tempo}.')
    
class Boi(Acougue):
    def __init__(self, nome, codigo, preco, corte):
        super().__init__(nome, codigo, preco)
        self.corte = corte
        
    def exibir_detalhes(self):
        return print(f'É carne de {self.nome}, com o código {self.codigo}, no preço R${self.preco}, tem o corte {self.corte}.')
    
peixe = Peixe('peixe', 556, 70.99, 'salgada', 'fresco')
carne = Boi('boi', 555, 69.99, 'picanha')

peixe.exibir_detalhes()
carne.exibir_detalhes()