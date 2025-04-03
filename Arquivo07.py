tipo = input("digite G para gasolina e E para etanol: ")
G = 5.80
E = 4.90
litros = int(input("digite qtd de litros: "))
preco = G*litros
preco2 = E*litros
if tipo =="G":
     preco = litros*5.80
else:
     preco2 = litros*4.90

print (f"voce pagou R${preco:.2f} de combustivel")







