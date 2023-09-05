from Categoria import Categoria
class Veiculo:
    def __init__(self, marca="Honda", ano=2014, cat=Categoria(None)):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.categoria = cat
    def __str__(self):
        text = "Marca: " + self.marca + "\n"
        text += "Ano: " + str( self.ano ) + "\n"
        text += "Categoria: " + str( self.categoria.nome ) + "\n"
        return text

    def imprimir(self):
        print( "Veículo: \n" , self )
        #print( "Veículo: \n" , self.__str__() )
        #print( "Veículo: \n" , str( self ) )