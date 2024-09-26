# Calculadora 2.0
# Declarando as variaveis e funções.
def calcular (z,y,x):
    def soma(N1,N2):
        return N1 + N2
    def sub (N1,N2):
        return N1 - N2
    def multi (N1,N2):
        return N1 * N2
    def div (N1,N2):
        try:
            return N1 / N2
        except ZeroDivisionError:
            print ("Não da para dividir por 0! ")
    if x == "Soma" or x == "soma":
        result = "{} foi o total da soma".format(soma(y,z))
    elif x == "Subtração" or x == "subtração":
        result = "{} foi o total da subtração".format(sub(y,z))
    elif x == "multiplicação" or x == "Multiplicação":
        result = "{} foi o total da multiplicação".format(multi(y,z))
    elif x == "Divisão" or x == "divisão":
        result = "{} foi o total da divisão".format(div(y,z))
    else:
        print ("Verifique a opção desejada!")
    return result
# Coletando os dados.
# Inicio do Bloco de Repetição.
while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        mtd = input("Digite qual vai ser a operação desejada: (Soma / Subtração / Multiplicação ou Divisão) ")

    except ValueError:
        print ("Verifique a entrada de dados! ")
    else:
        print (calcular (n1,n2,mtd))
        break
# Fim do Bloco de Repetição.
