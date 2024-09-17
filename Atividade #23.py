#IBGE

# Declarando as variaveis
Soma_Renda = 0
Soma_Qtd_Filhos = 0
Rep = int(input("Digite quantas pessoas responderão esse questionario: "))
MRenda = 0
qtd_Renda = 0
# Inicio do bloco de repetição
for cont in range(Rep):
    # Coletando Dados
    Renda = float(input("Digite a Renda familiar: "))
    Qtd_Filhos = int(input("Digite quantos filhos você tem: "))
    # Acumulando dados
    Soma_Renda = Soma_Renda + Renda
    Soma_Qtd_Filhos = Soma_Qtd_Filhos + Qtd_Filhos
    # Verificando a maior renda
    if Renda > MRenda:
        MRenda = Renda
    # Coletando a porcetagem de pessoas com a renda inferior a 1500
    if Renda < 1500:
        qtd_Renda += 1    
        
# Final do bloco de repetição
print (f"A media das rendas é R${(Soma_Renda/Rep):.2f}")
print (f"A media da quantidade de filhos é {int(Soma_Qtd_Filhos/Rep)}")
print (f"A maior das rendas é R${MRenda:.2f}")
print (f"O percentual de pessoas com renda inferior a R$1500 é {((qtd_Renda/Rep)*100):.1f}%")