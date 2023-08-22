class Cidade:
    def __init__(self, nome = None, estado = None):
        self.id = None
        self.nome = nome
        self.uf = estado

    def imprimir(self):
        print("Cidade: " , self.nome)
        print("Estado: ", self.uf )

    