# Pesquisa sobre um produto
# Declarando os vetores

Idd = []
Sx = []
Resp = []
# Declarando as variaveis
cont = 1
qtd_resps = 0
qtd_respn = 0
qtd_mrs18 = 0
qtd_mns18 = 0
qtd_mrn18 = 0
qtd_mnn18 = 0
qtd_SxMasc_Mr18_RespS = 0
qtd_SxFem_Mr18_RespS = 0
qtd_SxMasc_Mnr18_RespS = 0
qtd_SxFem_Mnr18_RespS = 0
qtd_SxMasc_Mnr18_RespN = 0
qtd_SxFem_Mnr18_RespN = 0
qtd_SxMasc_Mr18_RespN = 0
qtd_SxFem_Mr18_RespN = 0
Resp1 = input("Olá bem vindo poderia responder a nossa pesquisa? Não duram nem 1 minuto? ")
if Resp1 == "S" or Resp1 == "s":
    # Inicio do bloco de repetição
    while True:
        Idd.append(int(input("Quantos anos você tem? ")))
        Sx.append(input("Qual e o seu genero biologico? (M para Masculino ou F para Feminino). "))
        Resp.append(input("Você gostou do nosso produto? (S para Sim ou N para Não). "))
        Sn = input("Deseja continuar? (S para Sim ou N para N) ")
        if Sn == "N" or Sn == "n":
            print ("Adeus, foi um prazer lhe conhecer!")
            break
        cont += 1
for i in range(len(Idd)):
    # Quantidade de pessoas que gostaram
    if Resp [i] == "S" or Resp [i] == "s":
        qtd_resps += 1
    # Quantidade de pessoas que não gostaram
    elif Resp [i] == "N" or Resp [i] == "n":
        qtd_respn +=1
    # Quantidade de pessoas que tem mais de 18 anos e gostou
    if Idd [i] >18 and Resp [i] == "s" or Resp == "S":
        qtd_mrs18 += 1
    # Quantidade de pessoas que tem menos de 18 anos e gostou
    elif Idd [i] <18 and Resp [i] == "s" or Resp == "S" :
        qtd_mns18 += 1
    # Quantidade de pessoas que tem mais de 18 anos e não gostou
    if Idd [i] >18 and Resp [i] == "N" or Resp == "n":
        qtd_mrn18 += 1
    # Quantidade de pessoas que tem menos de 18 anos e não gostou
    elif Idd [i] <18 and Resp [i] == "N" or Resp == "n":
        qtd_mnn18 += 1
    # Quantidade de pessoas que tem mais de 18 anos, gostou é e do sexo masculino
    if Idd [i] >18 and Resp [i] == "s" or Resp == "S" and Sx [i] == "M" or Sx [i] == "m":
        qtd_SxMasc_Mr18_RespS += 1
    # Quantidade de pessoas que tem menos de 18 anos, gostou é e do sexo masculino
    elif Idd [i] <18 and Resp [i] == "s" or Resp == "S" and Sx [i] == "M" or Sx [i] == "m":
        qtd_SxMasc_Mnr18_RespS += 1
    # Quantidade de pessoas que tem mais de 18 anos, não gostou e é do sexo masculino
    if Idd [i] >18 and Resp [i] == "N" or Resp == "n" and Sx [i] == "M" or Sx [i] == "m":
        qtd_SxMasc_Mr18_RespN += 1
    # Quantidade de pessoas que tem menos de 18 anos, não gostou é e do sexo masculino
    elif Idd [i] <18 and Resp [i] == "N" or Resp == "n" and Sx [i] == "M" or Sx [i] == "m":
        qtd_SxMasc_Mnr18_RespN += 1
    # Quantidade de pessoas que tem mais de 18 anos, gostou é e do sexo Feminino
    if Idd [i] >18 and Resp [i] == "s" or Resp == "S" and Sx [i] == "F" or Sx [i] == "f":
        qtd_SxFem_Mr18_RespS += 1
    # Quantidade de pessoas que tem menos de 18 anos, gostou é e do sexo Feminino
    elif Idd [i] <18 and Resp [i] == "s" or Resp == "S" and Sx [i] == "F" or Sx [i] == "f":
        qtd_SxFem_Mnr18_RespS += 1
    # Quantidade de pessoas que tem mais de 18 anos, não gostou é e do sexo Feminino
    if Idd [i] >18 and Resp [i] == "n" or Resp == "N" and Sx [i] == "F" or Sx [i] == "f":
        qtd_SxFem_Mr18_RespN += 1
    # Quantidade de pessoas que tem menos de 18 anos, não gostou é e do sexo Feminino
    elif Idd [i] <18 and Resp [i] == "n" or Resp == "N" and Sx [i] == "F" or Sx [i] == "f":
        qtd_SxFem_Mnr18_RespN += 1
print ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print (f"{cont} Pessoas responderam o questionario.")
print ("")
print (f"A quantidade de pessoas que gostaram do produto foi de: {qtd_resps}, e a quantidade de pessoas que não gostaram foi: {qtd_respn}.")
print ("")
print (f"A quantidade de pessoas maiores de idade que gostou do produto foi de: {qtd_mrs18}. A quantidade de pessoas maior de idade que não gostou do produto foi de: {qtd_mrn18}. ")
print ("")
print (f"A quantidade de pessoas menores de idades que gostou do produto foi de: {qtd_mns18}. A quantidade de pessoas menores de idades que não gostou do produto foi de: {qtd_mnn18}. ")
print ("")
print (f"A quantidade de pessoas do sexo masculino com mais de 18 anos que gostou do produto foi de: {qtd_SxMasc_Mr18_RespS}, a quantidade de pessoas do sexo masculino com menos de 18 anos que gostou do produto foi de: {qtd_SxMasc_Mnr18_RespS}. ")
print ("")
print (f"A quantidade de pessoas do sexo masculino com mais de 18 anos que não gostou do produto foi de: {qtd_SxMasc_Mr18_RespN}, a quantidade de pessoas do sexo masculino com menos de 18 anos que não gostou do produto foi de: {qtd_SxMasc_Mnr18_RespN}.")
print ("")
print (f"A quantidade de pessoas do sexo feminino com mais de 18 anos que gostou do produto foi de: {qtd_SxFem_Mr18_RespS}, a quantidade de pessoas do sexo feminino com menos de 18 anos que gostou do produto foi de: {qtd_SxFem_Mnr18_RespS}.")
print ("")
print (f"A quantidade de pessoas do sexo feminino com mais de 18 anos que não gostou do produto foi de: {qtd_SxFem_Mr18_RespN}, a quantidade de pessoas do sexo feminino com menos de 18 anos que não gostou do produto foi de: {qtd_SxFem_Mnr18_RespN}.")
print ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")