# Pedra, Papel, Tesoura...

SN = input("Vamos brincar de pedra, papel ou tesoura? S/N: ")

if SN == "S":
    N1 = input ("Qual seu nome? ")
    N2 = input ("E qual e o nome do segundo jogador?")
    P1 = input ("Escolha Pedra, Papel ou Tesoura: ")
    P2 = input ("Escolha Pedra, Papel ou Tesoura: ")

    if P1 == "Pedra" and P2 == "Pedra":
        print ("Vocês empataram!")
    if P1 == "Pedra" and P2 == "Papel":
        print (f"{N2} ganhou pois papel ganha da pedra!")
    if P1 == "Pedra" and P2 == "Tesoura":
        print (f"{N1} ganhou pois tesoura ganha da pedra! ")
    if P1 == "Papel" and P2 == "Papel":
        print ("Vocês empataram!")
    if P1 == "Papel" and P2 == "Pedra":
        print (f"{N1} ganhou pois papel vence pedra! ")                
    if P1 == "Papel" and P2 == "Tesoura":
        print (f"{N2} ganhou pois tesoura vence papel! ")
    if P1 == "Tesoura" and P2 == "Tesoura":
        print ("Vocês empataram! ")
    if P1 == "Tesoura" and P2 == "Pedra":
        print (f"{N2} ganhou pois pedra vence tesoura! ")
    if P1 == "Tesoura" and P2 == "Papel":
        print (f"{N1} ganhou pois tesoura vence papel! ")
else: 
    print ("Então tchau!")                        