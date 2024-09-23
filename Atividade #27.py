# Gabarito de uma prova

#Declarando as variaveis
Gabarito = ["A", "C", "E", "D", "B"]
resp = "S"
# Inicio do bloco de repetição
for i in Gabarito:
    resposta = input ("Digite as respostas  ")
    if resposta == Gabarito [i]:
        print ("Está tudo correto")
    else:
        print ("Tá incorreto")    
#Fim do bloco de repetição