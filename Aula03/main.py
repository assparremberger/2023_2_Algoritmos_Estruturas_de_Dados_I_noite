from Pessoa import Pessoa
from Cidade import Cidade

c1 = Cidade("Porto Alegre", "RS")

p1 = Pessoa("João", 1.75, c1)

p2 = Pessoa("Maria", 1.80,  c1 )

p3 = Pessoa("José", 1.65,  Cidade("Alvorada", "RS")  )

p1.imprimir()
p3.imprimir()

print( p2 )

print( "IMC de ", p1.nome , "= " , p1.getIMC( 75.640 )  )

