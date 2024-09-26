# Convertendo cm para m e de m para cm

def calcular (x,y): # Criando a função primcipal
    def m(n): # Criando a função metro
            try:
                return n/100
            except ZeroDivisionError:
                print ("Verifique a entrada de dados!") 
    def cm(n): # Criando a função centimetro
            try:
                return n*100
            except ZeroDivisionError:
                print ("Verifique a entrada de dados!")
                
    if y == "m" or y == "M":
        result = "{} centimetros.".format(cm(x))
    elif y == "cm" or y == "CM":
        result = "{} metros.".format(m(x))
    else:
        result = "Verifique o valor digitado!"
    return result
# Coletando os dados
while True:
    try:
        n = int(input("Informe o valor da medida: "))
        u = input("Informe a unidade de medida (cm ou m): ")
    except ValueError or NameError:
        print ("Verifique o valor digitado!")
    else:
        print (calcular (n,u)) # Chamando a função principal
        break