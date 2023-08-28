class Pedido:
    def __init__(self, end, cli):
        self.id = None
        self.end = end
        self.cliente = cli
        self.produtos = []

    # método addProd receberá um objeto do tipo Produto
    # e o adicionará na lista de produtos existente no atributo
    # produtos da classe Pedido, retornando o total do Pedido
    def addProd( self, produto):
        self.produtos.append( produto )
        total = 0.0
        for prod in self.produtos:
            total += prod.preco
        return total

    def __str__(self):
        texto = "Endereço do Pedido: " + self.end + "\n"
        texto += "Cliente: " + self.cliente.nome + "\n"
        if len( self.produtos ) == 0:
            texto += "Pedido vazio"
        else:
            texto += "Produtos: \n"
            for prod in self.produtos:
            #    texto += prod.__str__()
                texto += str( prod ) + "\n"
        return texto


