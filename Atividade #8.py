# Calculo do IMC...
print ("Vamos descubrir seu IMC! ")
Peso = float(input("Digite seu peso: "))
Altura = float(input("Agora digite sua altura: "))

IMC = Peso/(Altura**2)

print (f"Seu IMC e de: {IMC}.")
if IMC >25:
    print("Você esta acima do peso!")
elif IMC < 18:    
    print ("Você está abaixo do peso!")
else:
    print ("Você esta ok!")    