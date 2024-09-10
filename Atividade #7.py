# Calcular a media de um aluno...

print ("Digite suas notas trimestrais: ")
T1 = float(input("Primeiro trimestre: "))
T2 = float(input("Segundo trimestre: "))
T3 = float(input("Terceiro trimestre: "))
T4 = float(input("Quarto trimestre: "))
Soma = T1+T2+T3+T4
Media = Soma/4

print ("Sua media e de:", Media)

if Media < 6:
    print ("Você esta reprovado!")
else:
    print ("Você esta aprovado!")