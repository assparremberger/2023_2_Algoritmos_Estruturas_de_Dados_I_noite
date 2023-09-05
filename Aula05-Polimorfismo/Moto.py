from Veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, ano, cat, cilindradas):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilindradas
    def imprimir(self):
        print( "Moto: \n " , self )
        
    def __str__(self):
        text = super().__str__()
        text += "Cilindradas: " + str( self.cilindradas)
        return text
    