# Login de usuario

# Declarando as variaveis

Name = ["Miguel", "João", "Benjamin", "Eduarda", "Tiago", "Pedro", "Lisa", "Rodrigo", "Erica", "Fabio"]
resp = "S"
# Inicio do bloco de repetição

while resp == "S" or resp == "s":
    pos = Name.index(input ("Digite o nome de Usuario: "))
    if pos == 0 or pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9:
        print ("Usuario encontrado")
    else:
        print ("Usuario não encontrado")
    resp = input ("Deseja continuar? (S/N)")        
#Fim do bloco de repetição