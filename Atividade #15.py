# Avaliação de um pedido...

print ("Ola! Por acaso o(a) senhor(a) recebeu seu pedido?")
Ped = input ("Se sim por favor diga: S para não digite: N: ")

if Ped == "S":
    Av = input ("Gostaria de avaliar nossa entrega? se sim digite: S se não digite: N: ")
    if Av == "S":
        Ava = input ("De 1 a 5 qual foi seu nivel de satisfação com a entrega? 1= péssimo / 2 para ruim / 3 para razoavel / 4 para bom e 5 para otimo: ")
        if Ava == 1:
            print ("Sinto muito! Poderia nos dizer o motivo de tal nota?")
            Desc = input ()
        if Ava == 2:
            print ("Sinto muito! O que poderiamos fazer para aumentar a sua nota?")
            Desc = input ()
        if Ava ==3:
            print ("Ok! E oque poderiamos fazer para aumentar a sua nota?")
            Desc = input ()
        if Ava == 4:
            print ("Que bom que gostou! Espero podermos fazer melhor na proxima vez!")
        if Ava == 5:
                print ("Perfeito! Que bom que a você gostou espero podermos melhorar para satisfazermos o(a) senhor(a)!")
    else:
        print ("Ok desejo um otimo dia!")
else:
    print ("Ok já estamos enviando!")                                    