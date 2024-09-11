# Verificação para ver um eclipse...
print ("Vamos ver se você consegue ver o eclipse!")
print ("Qual e a sua localização? 1. Rio de Janeiro / 2. Espirito Santo / 3. São Paulo / 4. Minas Gerais / 5. Outras Localizações ")
Loc = int(input())
print ("Qual e o Clima? 1. Dia ensolarado / 2. Dia nublado / 3. Tempo chuvoso")
Clima = int (input())

if Loc == 1 and Clima == 1:
    print ("Você podera ver um eclipse total as 15:25h ")
elif Loc == 1 and Clima == 2:
    print ("Você não consiguira ver o eclipse!") 
elif Loc == 1 and Clima == 3:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 2 and Clima == 1:
    print ("Você podera ver um eclipse parcial por mais ou menos 5 minutos as 15:25h")
elif Loc == 2 and Clima == 2:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 2 and Clima == 3:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 3 and Clima == 1:
    print ("Você podera ver um eclipse parcial por mais ou menos 5 minutos as 15:25h")
elif Loc == 3 and Clima == 2:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 3 and Clima == 3:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 4 and Clima == 1:
    print ("Você podera ver um eclipse parcial por mais ou menos 5 minutos as 15:25h")
elif Loc == 4 and Clima == 2:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 4 and Clima == 3:
    print ("Você não consiguira ver o eclipse!")
elif Loc == 5:
    print ("Você não consiguira ver o eclipse!")                     