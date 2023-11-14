carro = {
    "marca" : "Jeep" ,
    "ano" : 2021 ,
    "motor" : 1.8
}

print( carro )
print( "Marca" , carro["marca"])
print( carro.keys() )
print( "------------------------" )

for chave, valor in carro.items():
    print( chave , " - ", valor )
print( "------------------------" )
for chave in carro.keys():
    print( chave , " - ", carro[ chave ] )


filho1 = { "nome":"Júlia" , "idade" : 15 }
filho2 = { "nome":"Pedro" , "idade" : 5 }
filho3 = { "nome":"Laura" , "idade" : 1 }

filhos = filho1, filho2
print( filhos )
#filhos[1] = filho3
filho2["nome"] = "Laura" 
print( filhos )
del filho1["nome"]
filho1["apelido"] = "Juju"
print( filhos )
