nome = input ("Digite seu nome:")
idade = int(input("Digite sua idade:"))
salario = float(input("Digite seu salario:"))
percentual = float(input("digite seu percentual:"))

porcentagem = (salario*percentual/100)


salarioatual = (porcentagem+salario)

print (f"Olá {nome},sua idade é {idade} anos, voce recebe {salario:.2f}, teve aumento de R${porcentagem:.2f} e seu salario atual é R${salarioatual:.2f} ")
