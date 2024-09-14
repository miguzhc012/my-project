# Demonstração do uso de estruturas repetitivas

Contador = 0; Senha = ""
while Senha != "S3nh4":
    print ("Digite a senha: ")
    Senha = input ()

    if Senha == "S3nh4":
        print ("Senha correta!")
        print ("Seja Bem vindo!")
        break
    else:
        print ("Senha incorreta!")
        input ()
    Contador = Contador + 1
    if Contador == 3:
        print ("Tentativas exedidas!")
        break