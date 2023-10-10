from No import No

class Lista:

    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def addNoInicio(self, valor):
        no = No( valor )
        if self.primeiro == None:
            self.primeiro = no
        else:
            no.proximo = self.primeiro
            self.primeiro = no
        self.tamanho += 1
        self.imprimir()

    # def addNoInicio(self, valor):
    #     no = No( valor )
    #     if self.primeiro != None:
    #         no.proximo = self.primeiro
    #     self.primeiro = no
    #     self.tamanho += 1
    #     self.imprimir() 
    

    def imprimir(self):
        aux = self.primeiro
        while( aux ):
           print( aux.dado ) 
           aux = aux.proximo
        print( "Total: " , self.tamanho )

    def addNoFim(self, valor):
        no = No( valor )
        if self.primeiro == None:
            self.primeiro = no
        else:
            aux = self.primeiro
            while( aux ):
                if aux.proximo == None:
                    aux.proximo = no
                    break
                aux = aux.proximo
        self.tamanho += 1
        self.imprimir()

    # def addNoFim(self, valor):
    #     no = No( valor )
    #     if self.primeiro != None:
    #         aux = self.primeiro
    #         while aux.proximo :
    #             aux = aux.proximo
    #         aux.proximo = no
    #     else:
    #         self.primeiro = no
    #     self.tamanho += 1
    #     self.imprimir()

    def removerDoInicio(self):
        if self.primeiro == None:
            print("Lista Vazia!")
        elif self.primeiro.proximo == None :
            self.primeiro = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()

    # def removerDoInicio(self):
    #     if self.primeiro == None:
    #         print("Lista Vazia!")
    #     else:
    #         self.primeiro = self.primeiro.proximo
    #         self.tamanho -= 1
    #     self.imprimir()


    def removerDoFim(self):
        if self.primeiro == None:
            print("Lista Vazia!")
        elif self.primeiro.proximo == None:
            self.primeiro =  None
            self.tamanho = 0
        else:
            anterior = self.primeiro
            aux = self.primeiro.proximo
            while aux.proximo :
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None
            self.tamanho -= 1
        self.imprimir()
        