# Calculo de horas extras

# Iniciando codigo
def h (x):
    result = Hora * 50
    print (f"O(a) {Nome} ganhara R${result:.2f} por conta das horas extras trabalhadas. ")
    # Coletando dados
while True:
    Nome = input ("Digite o nome do funcionario: ")
    if Nome != "":
        break
    else:
        print ("Verifique o Nome fornecido! ")
while True:
    try:
        Hora = int(input("Digite quantas horas extras foram trabalhadas: "))
    except ValueError or NameError: # Tratamento de erro
        print ("Parece que algo foi digitado errado! ")
    else:
        h (Hora)
        break
# Fim do codigo