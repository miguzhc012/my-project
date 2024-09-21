# Declarando as variaveis
Sexo = []
Cor_olhos = []
Cor_cabelo = []
Idade = []
resp = "S"
qtdM = 0
qtdOC = 0
# Inicio do bloco de repetição
while resp == "S" or resp == "s":
    Sexo.append(input("Digite Seu genero: (M)masculino ou (F)feminino: "))
    Cor_olhos.append(input("Digite a cor dos seu olhos: (A)azuis, (V)verdes ou (C)castanhos: "))
    Cor_cabelo.append(input("Diite a cor do seu cabelo: (L)loiro, (C)castanho, ou (P)preto: "))
    Idade.append(int(input("Digite quantos anos você tem: ")))
    resp = input("Digite se deseja continuar: (S/N) ")
Maior_Idd = max (Idade) # Coletando a maior idade
# Iniciando o bloco de repetição
for i in range(len(Idade)):
    # Acumulando os dados
    if (Sexo[i] == "F" or Sexo[i] == "F") and (Idade[i]  >= 18 and Idade[i]  <= 35):
        qtdM += 1  
    if (Cor_olhos[i]  == "V" or Cor_olhos[i]  == "v") and (Cor_cabelo[i]  == "L" or Cor_cabelo[i]  == "l"):
        qtdOC  += 1
# Finalizando o blococ de repetição
print ("")
print ("---------------------------------------------")
print (f"A maior idade dos habitantes é: {Maior_Idd}")
print (f"A quantidade de pessoas do sexo feminino com idades entre 18 e 35 anos foi: {qtdM}.")
print (f"A quantidade de pessoas com cabelos loiros e olhos verdes foi: {qtdOC}")
print ("---------------------------------------------")