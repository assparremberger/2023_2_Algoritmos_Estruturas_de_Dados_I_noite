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

print("------ 28/08/2023 -------")
from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido

beb = Categoria("Bebidas")
ali = Categoria("Alimentos")

pro01 = Produto("Coca-Cola 355ml", 4.99 , beb )
pro02 = Produto("Coca-Cola 2L", 7.49 , beb )
pro03 = Produto("Trakinas", 3.95 , ali )

ped = Pedido("Rua A", p1)
ped.addProd( pro02 )
ped.addProd( pro01 )
print( ped )




