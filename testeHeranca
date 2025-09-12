class Animal:
  def __init__ (self, nome, especie):
    self.nome = nome
    self.especie = especie
  
  def exibirInformacoes(self):
    print(f'O nome dele é {self.nome}, sendo da espécie {self.especie}.')

class Local(Animal):
  def __init__(self, nome, especie, terreno):
    super().__init__(nome, especie)
    self.terreno = terreno

  def exibirInformacoes(self):
    super().exibirInformacoes()
    print(f'Ele é {self.terreno}')

animal1 = Local('Auau', 'Cachorro', 'Terrestre')
animal1.exibirInformacoes()
