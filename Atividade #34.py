# Calculo do gasto de combustivel de um veiculo
# Iniciando o codigo
# Declarando as Variaveis e Funções
def Calculo (x,y):
    try:
        Val = Dist / ConsuL
    except ZeroDivisionError:
        print ("Verifique o valor inserido!")
    else:
        print (f"Foram gastos {Val}L de combustivel")
# Fazendo a coleta de dados
# Iniciando Bloco de repetição
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
# Fim do Bloco de repetição
# Fim do codigo

