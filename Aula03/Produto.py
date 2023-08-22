class Produto:
    def __init__(self, nome = None, preco = 0.0, cat = Categoria() ):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.cat = cat
    def __str__(self):
        texto = "Produto: " + self.nome + "\n"
        texto += "Preço: " + str( self.preco ) + "\n"
    #    texto += "Categoria: " + self.cat.nome
        texto += self.cat.__str__()
        return texto
    