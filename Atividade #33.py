
# Iniciando o codigo
# Converção de Metros para Centimetros

def Calculo (M):
    resultm = Metro * 100
    print (f"A converção de Metro para Centimetro foi de: {Metro:.1f}m para {resultm:.1f}cm")
print ("----------------------------------------------------------------------------------------------")
while True:
    try:
        Metro = float(input("Digite o valor em Metros para fazer a converção para Centimetros: "))
    except ValueError or NameError:
        print ("Verifique o valor digitado! ")
    else:
        Calculo (Metro)
        break
print ("----------------------------------------------------------------------------------------------")
print ("")
def Calculocm (CM):
    resultCM = Centimetros / 100
    print (f"A converção de Centimetros para Metros foi de: {Centimetros:.1f}cm para {resultCM:.1f}m")
print ("----------------------------------------------------------------------------------------------")
while True:
    try:
        Centimetros = float(input("Digite o valor em Centimetros para fazer a converção para Metros: "))
    except ValueError or NameError:
        print ("Verifique o valor digitado! ")
    else:
        Calculocm (Centimetros)
        break
print ("----------------------------------------------------------------------------------------------")