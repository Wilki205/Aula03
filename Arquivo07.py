tipo = input("digite G  para gasolina e E  para etanol: ")
G = 5.80
E = 4.90
litros = int(input("digite qtd de litros: "))
preco = 0
if tipo =="G" or tipo == "g":
     preco = litros*5.80
elif tipo == "E" or tipo == "e":
     preco = litros*4.90
else:
    print ( "tipo de combustivel invalido")
print (f"voce pagou R${preco:.2f} de combustivel")







