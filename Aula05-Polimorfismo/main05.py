from Categoria import Categoria
from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto
cat01 = Categoria("Sedan")
cat02 = Categoria("SUV")
cat03 = Categoria("Esportiva")
v1 = Veiculo()
v1.imprimir()

car01 = Carro("Jeep", 2021, cat02, 4)
car01.imprimir()