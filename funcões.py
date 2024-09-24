def soma(x,y):
    result = x + y
    print (f"O resultado é : {result}")
try:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor: "))
except ValueError:
    print ("Verifique os valores digitados") 

soma(n1,n2)       