from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, ano, cat, qtdPortas):
        super().__init__(marca, ano, cat)
        self.qtdPortas = qtdPortas

    def imprimir(self):
        super().imprimir()
        print( "Portas: " + str( self.qtdPortas) )

    def __str__(self):
        text = super().__str__()
        text += "Portas_: " + str( self.qtdPortas)
        return text
    