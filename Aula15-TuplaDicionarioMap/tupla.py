carros = "Uno", "Doblo", "Renagade", "Toro"

print( carros )

print( carros[2] )
print( carros[1:3] )
print( carros[1:-1] )
print( carros[1:] )

itens = carros[2:] , carros[0]
print("Itens: ", itens)

def calcular(x, y):
    return x+y , x-y , x*y , x/y

print( calcular(10, 2) )
resultados = calcular(9, 3)
a, b, c, d = calcular(9, 3)
print("Soma: ", a)
print("Subtração: ", b)
print("Multiplicação: ", c)
print("Divisão: ", d)

