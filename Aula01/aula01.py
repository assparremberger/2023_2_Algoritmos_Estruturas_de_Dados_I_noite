# método que não recebe parâmetro e
# possui retorno
def getPI():
    return 3.14

def getDobroDoPI():
    return getPI() * 2

# método que não recebe parâmetro e
# não possui retorno
def imprimirPI():
    print( getPI()  )



# método que recebe parâmetro e
# possui retorno
def getAreaCirculo( raio ):
    return getPI() * ( raio * raio)


# método que recebe parâmetro e
# não possui retorno
def imprimirAreaCirculo( raio ):
    print( getAreaCirculo( raio ) )


# execusão

imprimirPI()
#print( getAreaCirculo( 6 * 2 ) )
imprimirAreaCirculo( 10 )


