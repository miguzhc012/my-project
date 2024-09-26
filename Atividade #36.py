Idd = []
Curso = []
Sx = []
cont = 1
Cursoz = 0
Cursod = 0
Cursotc = 0
Cursoc = 0
qtd_m = 0
qtd_f = 0
qtd_18 = 0
qtd_17 = 0
print ("Ola aluno do Senac de Campo Grande poderia nos responder uma pesquisa? ")
while True:
    print ("")
    Idd.append(int(input ("Qual e a sua idade? ")))
    Sx.append(input ("Qual e o seu genero? (Masculino = M ou Feminino = F) "))
    Curso.append(int(input("Quantos cursos você ja realiou? ")))
    resp = input ("Você deseja continuar? (S / N) ")
    if resp == "N" or resp == "n":
        break
    cont += 1
for i in range(len(Idd)):
    # Desvio condicional para qtd de Cursos
    if Curso[i] == 0:
        Cursoz += 1
    elif Curso[i] >=1 and Curso[i] <=2:
        Cursod += 1
    elif Curso [i] >= 3 and Curso[i] <= 5:
        Cursotc += 1
    elif Curso[i] > 5:
        Cursoc+= 1
    # Desvio condicional para qtd Genero
    if Sx [i] == "M" or Sx [i] == "m":
        qtd_m += 1
    elif Sx [i] == "F" or Sx [i] == "f":
        qtd_f +=1
    # Desvio condicional para Idade
    if Idd [i] >= 18:
        qtd_18 += 1
    else:
        qtd_17 += 1
# Fim do codigo
print ("---------------------------------------------------------------------------------------------------------------------------------")
print (f"A quantidade de estudantes que não fizeram nenhum curso e: {Cursoz}, compreendendo o percentual de: {(Cursoz*cont/100)*100:.0f}%")
print (f"A quantidade de estudantes que fizeram de 1 a 2 cursos e: {Cursod}, compreendendo o percentual de: {(Cursod*cont)*100:.0f}%")
print (f"A quantidade de estudantes que fizeram de 3 a 5 cursos e: {Cursotc}, compreendendo o percentual de: {(Cursotc*cont)/100:.0f}%")
print (f"A quantidade de estudantes que fizeram mais de 5 cursos e: {Cursoc}, compreendendo o percentual de: {(Cursoc*cont)/100:.0f}%")
print ("")
print (f"A quantidade de estudantes que são do sexo masculino são: {qtd_m}")
print (f"A quantidade de estudantes que são do sexo feminino são: {qtd_f}")
print ("")
print (f"A quantidade de estudantes maiores de 18 é: {qtd_18} e a quantidade de estudantes menores de idade são: {qtd_17}")
print ("")
print (f"Foram um total de: {cont} estudantes que fizeram a pesquisa. ")
print ("---------------------------------------------------------------------------------------------------------------------------------")