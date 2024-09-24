def Calculo (x,y):
    Val = Dist / ConsuL
    print (f"Foram gastos {Val}L de combustivel")
# Coletando dados
while True:
    try:
        while True:
            ConsuL = float(input("Digite o consumo medio de combustivel do seu veiculo em Litros: "))
            if ConsuL == 0 or ConsuL == "":
                print ("Não foi possivel fazer o calculo! Tente novamente!")
            else:
                break
        while True:
            Dist = float(input("Digite a distancia  que foi percorrida pelo veiculo em KM: "))
            if Dist == "" or Dist == 0:
                print ("Não foi possivel fazer o calculo! Tente novamente!")
            else:
                break
    except ValueError or NameError:
        print ("Valor digitado incorreto! ")
    else:
        Calculo (ConsuL,Dist)
        break
