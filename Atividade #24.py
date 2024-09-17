# Posto de combustivel

# Declarando as variaveis
Resp = "S"
TL = 0
TLe = 0
TLGc = 0
TLGa = 0
TLD = 0
QLVE = 0
QLVGc = 0
QLVGa = 0
QLVD = 0

# Iniciandp bloco de repetição
print ("Olá seja bem vindo ao meu posto de combustivel! ")
while Resp == "S" or Resp == "s":
    # Coletando dados
    QLV = float(input("Quantos litros foi abastecido? "))
    TC = input ("Que tipo de combustivel foi inserido: E - Etanol/ Gc - Gasolina comum / Ga - Gasolina aditivada / D - Diesel: ")
    
    # Acumulando dados
    if TC == "E" or TC == "e":
        print (f"Valor do Etanol saiu a R${(QLV * 3.70):.2f}")
        TLe = TLe + QLV
        QLVE = QLV
    elif TC == "Gc" or TC == "gc":
        print (f"Valor da Gasolina Comum saiu a R${(QLV * 5.39):.2f}")
        TLGc = TLGc + QLV
        QLVGc = QLV
    elif TC == "Ga" or TC == "ga":
        print (f"Valor da Gasolina Aditivada saiu a R${(QLV * 5.75):.2f}")
        TLGa = TLGa + QLV
        QLVGa = QLV
    elif TC == "D" or TC == "d":
        print (f"Valor do Diesel saiu a R${(QLV * 4.90):.2f}")
        TLD = TLD + QLV
        QLVD = QLV
    else:
        print ("Erro! Não consigo indentificar o tipo de combustivel!!! ")
        print ("Repita novamente!")
        continue

    TL = TL + QLV
    
    # Loop
    Resp = input ("Deseja continuar? S/N: ")
#Final Bloco de repetição
# Fim do codigo
print ("---------------------------------------------------------------------------------")
print (f"Total de litros abastecidos foi de: {(TL):.1f}L")
print (f"O total arrecadado foi de: R${((QLVE*3.70)+(QLVGc*5.39)+(QLVGa*5.75)+(QLVD*4.90)):.2f}")
print ("")
print (f"Total de litros abastecidos com Etanol foi de: {(TLe):.1f}L")
print (f"Total de litros abastecidos com Gasolina Comum foi de: {(TLGc):.1f}L")
print (f"Total de litros abastecidos com Gasolina Aditivada foi de: {(TLGa):.1f}L")
print (f"Total de litros abastecidos com Diesel foi de: {(TLD):.1f}L")
print ("")
print (f"Total arrecadado abastecendo Etanol foi de: R${(QLVE * 3.70):.2f}")
print (f"Total arrecadado abastecendo Gasolina Comum foi de: R${(QLVGc * 5.39):.2f}")
print (f"Total arrecadado abastecendo Gasolina Aditivada foi de: R${(QLVGa * 5.75):.2f}")
print (f"Total arrecadado abastecendo Diesel foi de: R${(QLVD * 4.90):.2f}")
print ("---------------------------------------------------------------------------------")