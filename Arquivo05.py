n1 = float(input("digite sua nota: "))
n2 = float(input("digite sua nota: "))
n3 = float(input("digite sua nota: "))

media = (n1+n2+n3)/3

if media >= 7:
    print(f"ALUNO APROVADO APROVADO MEDIA {media:.2f}")
else:
    if media >= 4:
    print(f"ALUNO REPROVADO MEDIA {media:.2f}")
    else:
    print(f"ALUNO DE RECUPERAÇÃO MEDIA {media:.2f}")
