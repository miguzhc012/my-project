Valor = float(input("Digite o valor do produto desejado: "))
Taxa = float (input("Digite o quanto de taxa: "))
Ot = int (input("Digite quantas parcelas?: "))
Parcelas = Valor / Ot
Pgto = Valor / Ot
Acumulado = 0
for X in range (0,Ot):
    print (f"Deseja pagar a {X + 1}ª parcela?")
    Pagar = input ()
    if Pagar =="Sim":
        Parcelas = Parcelas * (1+Taxa)
        Acumulado = Acumulado + Parcelas
        print (f"R${Acumulado} faltam R${Acumulado - Valor } ")
    elif Pagar == "Não":
        print ("Ok! Quando quiser me chame novamente!")
        break    