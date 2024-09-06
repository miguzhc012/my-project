# Temperatura de Celsius para Fahrenheit e de Celsius para Kelvin

C = float(input("Digite uma temperatura: "))

F = C*1.8+32

print ("A temperatura digitada de Celsius para Fahrenheit é: F", F, "°")

K = C + 273.15

print ("A temperatura digitada de Celsius para Kelvin é: K", K, "°")

# Temperatura  de Kelvin para Fahrenheit e de Kelvin para Celsius
C2 = float(input("Digite outra temperatura:"))

K2 = C2 + 273.15

F2 = (K2 - 273.15) * 9 / 5 + 32

print ("A temperatura digitada de Kelvin para Fahrenheit é: F", F2, "°")

C3 = K2 - 273.15

print ("A temperatura digitada de Kelvin para Celsius é: C", C3, "°")

# Temperatura de Fahrenheit para Kelvin e Celsius

C4 = float(input("Digite mais uma temperatura: "))

F3 = C4*1.8+32

K3 = (F3 - 32) * 5 / 9 + 273.15

print ("A temperatura digitada de Fahrenheit para Kelvin é: K", K3, "°")

C5 = (F3 - 32) / 1.8

print ("A temperatura digitada de Fahrenheit para Celsius é: C", C5, "°")