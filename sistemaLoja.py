class Loja:
    def __init__(self, preco, codigo):
        self.preco = preco
        self.codigo = codigo
        
    def descricao(self):
        return f'{self.codigo} custa {self.preco}'
    
class Livro(Loja):
    def __init__(self, preco, codigo, pagina):
        super().__init__(preco, codigo)
        self.pagina = pagina
        
    def descricao(self):
        return f'O livro {self.codigo} tem {self.pagina} páginas'
        
class Eletronicos(Loja):
    def __init__(self, preco, codigo, voltagem):
        super().__init__(preco, codigo)
        self.voltagem = voltagem
        
    def descricao(self):
        return f'O eletronico {self.codigo} e tem {self.voltagem}V'
    
class Alimento(Loja):
    def __init__(self, preco, codigo, nome):
        super().__init__(preco, codigo)
        self.nome = nome
        
    def descricao(self):
        return f'O alimento {self.nome} tem {self.codigo}'
    
livro1 = Livro('59,90', 'cod.5489', '236')
eletronicos1 = Eletronicos('6000', 'cod.25476', '220')
alimento1 = Alimento('6,79', 'cod.345', 'maçã')
print(livro1.descricao())
print(eletronicos1.descricao())
print(alimento1.descricao())