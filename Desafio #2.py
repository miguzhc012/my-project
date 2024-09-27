# Programa de IMC

# Declarando os vetores
Username = []
IMC = []
Sx = []
Idd = []
Peso = []
Alt = []
# Declarando as variaveis
qtd_M = 0
qtd_F = 0
Obs = 0
AbxP = 0
qtd_F_PesoIdeal = 0
qtd_M_PesoIdeal = 0
cont = 1
# Inicio do bloco de repetição
while True:
    Username.append(input("Digite o seu nome: "))
    Idd.append(int(input("Digite sua idade: ")))
    Sx.append(input("Digite o seu genero: (M para Masculino ou F para Feminino). "))
    Peso.append(float(input("Digite o seu peso: ")))
    Alt.append(float(input("Digite a sua altura em metro: ")))
    resp = input("Deseja continuar? (S ou N) ")
    if resp == "N" or resp == "n":
        print ("Ok")
        break
    cont += 1
# Fim do bloco de repetição
Pos = Username.index(input("Qual e o seu nome para procurarmos no nosso banco de dados: "))
User = Username[Pos]

for i in range(len(Idd)):
    IMC.append(Peso [i]/(Alt[i])**2)
    # Declarando o IMC:
    # Se o genero for masculino 
    if Sx [i] == "M" or Sx [i] == "m":
        qtd_M += 1
        Pos = Username.index(input("Qual e o seu nome para procurarmos no nosso banco de dados: "))
        User = Username[Pos]
        if IMC [Pos] <= 18.5:
            print (f"Olá {User} seu IMC e de {IMC[Pos]:.1f}Voce está abaixo do peso ")
            AbxP += 1
        elif IMC [Pos] >= 18.5 and IMC [Pos] <= 24.9:
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está no peso ideal. ")
        elif IMC [Pos] >= 25 and IMC [Pos] <= 29.9:
            if Sx [i] == "F" or Sx == "f":
                qtd_F_PesoIdeal += 1
            if Sx [i] == "M" or Sx [i] == "m":
                qtd_M_PesoIdeal += 1
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com sobrepeso. ")
        elif IMC [Pos] >= 30 and IMC [Pos] <= 34.9:
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com Obesidade grau I. ")
            Obs += 1
        elif IMC [Pos] >= 35 and IMC [Pos] <= 39.9:
            Obs += 1
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com Obesidade grau II. ")
        elif IMC [Pos] >= 40:
            Obs += 1
    # Se o genero for feminino
    elif Sx [i] == "F" or Sx [i] == "f":
        qtd_F +=1
        Pos = Username.index(input("Qual e o seu nome para procurarmos no nosso banco de dados: "))
        User = Username[Pos]
        if IMC [Pos] <= 18.5:
            print (f"Olá {User} seu IMC e de {IMC[Pos]:.1f}Voce está abaixo do peso ")
            AbxP += 1
        elif IMC [Pos] >= 18.5 and IMC [Pos] <= 24.9:
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está no peso ideal. ")
        elif IMC [Pos] >= 25 and IMC [Pos] <= 29.9:
            if Sx [i] == "F" or Sx == "f":
                qtd_F_PesoIdeal += 1
            elif Sx [i] == "M" or Sx [i] == "m":
                qtd_M_PesoIdeal += 1
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com sobrepeso. ")
        elif IMC [Pos] >= 30 and IMC [Pos] <= 34.9:
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com Obesidade grau I. ")
            Obs += 1
        elif IMC [Pos] >= 35 and IMC [Pos] <= 39.9:
            Obs += 1
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com Obesidade grau II. ")
        elif IMC [Pos] >= 40:
            Obs += 1
            print (f"Olá {User} seu IMC é de {IMC[Pos]:.1f} e você está com Obesidade grau III. ")
    # Fim do codigo
print ("")
print ("-------------------------------------------------------------------------------------------------------------------------------")
print (f"A quantidade de pessoas abaixo do peso foi de: {AbxP}. ")
print (f"A quantidade de pessoas com Obesidade I, II ou III e de: {Obs}. ")
print (f"A quantidade de Homens que se registraram foi de: {qtd_M} e a quantidade de mulheres que se registraram foi de: {qtd_F}. ")
print (f"O percentual de homens que estão no peso ideal é: {((qtd_M_PesoIdeal+100)/100):.1f}% ")
print (f"O percentual de mulheres que estão no peso ideal é: {((qtd_M_PesoIdeal+100)/100):.1f}% ")
print ("-------------------------------------------------------------------------------------------------------------------------------")