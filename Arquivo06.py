time1 = input("digite o nome do time: ")
time2 = input("digite o nome do time: ")

placartime1 = int(input("digite placar: "))
placartime2 = int(input("digite placar: "))

if placartime1>placartime2:
    print(f"{time1} VENCEDOR")
else:
    if placartime1 == placartime2:
        print("EMPATE")
    else:
        print(f"{time2} VENCEDOR")
