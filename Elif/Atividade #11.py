# Tabela do brasileirão...

Time = input ("Digite o nome do time do campeonato brasileiro: ")
Class = int(input ("Agora digite a classificação desse time: "))

if Class == 1:
    print ("---------------------------------------")
    print (f"O {Time} é campeão")
    print ("---------------------------------------")
elif Class > 1 and  Class <= 6:
    print ("-------------------------------------------------")
    print (f"O {Time} está classificado para a Libertadores!")
    print ("-------------------------------------------------")
elif Class >= 7 and Class <= 12:
    print ("--------------------------------------------------")
    print (f"O {Time} está classificado para a Sul-Americana!")
    print ("--------------------------------------------------") 
elif Class >= 13 and Class <=20:
    print ("---------------------------------------")
    print (f"O {Time} está  Rebaixado")
    print ("---------------------------------------")