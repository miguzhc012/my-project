# Verificação se um número está em ordem descrescente ou crescente...

X = int(input("Digite um número para ver se ele é crescente: "))
Y = int(input("Digite outro número: "))
Z = int(input("Digite mais um número: "))

if X > Y and Y > Z and Z < X:
    print ("Está em ordem decrescente!")
elif X < Y and Y < Z and Z > X:
    print ("Está em ordem crescente!")
else:
    print ("Tá tudo misturado")        