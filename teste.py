def divsao (n1,n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print ("Não e possivel dividir por 0!")
    else:
        print (f"O resultado da divisão é {result}")
try:        
    n1 = int(input("Digite o valor a ser dividido: "))
    n2 = int(input("Digite o valor a dividir: "))
except ValueError:
    print("Verifique os dados inseridos!")   
divsao (n1,n2)