# Declarando variaveis

notas = []
resp = "S"
sn = 0
cont = 0
# Iniciando bloco de repetição
while resp == "S" or resp == "s":
    # Alimentando a lista
    notas.append(float(input("Digite as suas notas: ")))
    resp = input ("Deseja continuar? (S/N)? ")
    cont += 1
# Finalizando o bloco de repetição
# Iniciando bloco de repetição
for i in range(len(notas)):
    print (notas[i])
    sn = sn + notas[i] # Exibindo o conteudo da lista
# Fim do bloco de repetição
# Fim do codigo    
print (f"A sua média de notas e de: {(sn / cont):.1f}")
