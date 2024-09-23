nomes = ["João", "Maria", "José"]
idades = [20, 46, 60]

pos = nomes.index("Maria")
#print (pos)

del nomes [pos]
del idades [pos]

for i in range(len(idades)):
    print (nomes[i] + " " + str(idades[i]))