class Pessoa:

    def __init__(self, name, idade):
        print("Objeto instanciado")
        self.nome = name
        self.idade = idade

    def imprimir(self):
        print("Nome: " , self.nome)
        print("Idade: " , self.idade)

        
        