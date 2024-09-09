# Convertor de temperaturas 2.0...

C = float(input("Digite uma temperatura: "))
F = C*1.8+32
K = C + 273.15
K2 = (F - 32) * 5 / 9 + 273.15
C2 = (F - 32) / 1.8
F3 = (K - 273.15) * 9 / 5 + 32
C3 = K - 273.15
print ("Digite um numero para fazer a converção: ")
print ("1. C para F: ")
print ("2. C para K: ")
print ("3. F para C: ")
print ("4. F para K: ")
print ("5. K para C: ")
print ("6. K para F: ")
Op = int(input())
match Op:
    case 1:
        print (f"De C {C}° para F {F}°.")
    case 2:
        print (f"De C {C}° para K {K}°.") 
    case 3:
        print (f"De F {F}° para K {K2}°.")  
    case 4:
        print (f"De F {F}° para C {C2}°.")
    case 5:
        print (f"De K {K}° para C {C3}°.")
    case 6:
        print (f"De K {K}° para F {F3}°.")                 