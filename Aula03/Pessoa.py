from Cidade import Cidade
class Pessoa:

    def __init__(self, nome = None, altura = 0.0, city= Cidade() ):
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = city

    def __str__(self):
        texto = "Nome: " + self.nome + "\n"
        texto += "Altura: " + str( self.altura) + "\n"
        texto += "Cidade: " + self.cidade.nome + "\n"
        texto += "Estado: " + self.cidade.uf + "\n"
        return texto

    def imprimir(self):
        print("Nome: " , self.nome)
        print("Altura: " , self.altura)
        self.cidade.imprimir()

    def getIMC(self, peso):
        return peso / (self.altura * self.altura)
