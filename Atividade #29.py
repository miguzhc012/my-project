#Notas dos alunos

# Declarando as variaveis
Nome = ["Miguel", "João", "Tiago", "Biatriz", "Ronaldo", "Julia", "Maria", "Alicia", "Clara", "Ricardo"]
Nota = [1, 3, 4, 2.3, 6, 8, 3, 7, 4, 5]
media = sum(Nota) / len(Nota)
MaiorNt = max(Nota)
pos = Nota.index(MaiorNt)
alunomlhr = Nome[pos]
qtdm = 0
qtdmnr = 0
# Inicio do bloco de repetição
for i in range(len(Nota)):
    if media > Nota[i]:
        qtdmnr += 1
    else:
        qtdm += 1
# Fim do bloco de repetição        
print (f"A media das notas é {media:.1f}")
print (f"A quantidade de notas acima de: {media:.1f} é {qtdm}")
print (f"A quantidade de notas abaixo de: {media:.1f} é {qtdm}")
print (f"O Aluno: {alunomlhr} tirou a melhor nota que no caso é: {MaiorNt}")