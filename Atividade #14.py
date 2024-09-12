# Função de um jogador no campo...

Nome = input ("Digite o nome do jogador: ")
Func = input (f"Digite a função do(a) {Nome} no campo: ")

if Func == "Goleiro" or Func == "Zagueiro" or Func == "Lateral":
    print (f"O(a) {Nome} faz parte da defesa!")
elif Func == "Ala" or Func == "Volante" or Func == "Meia":
    print (f"O(a) {Nome} faz parte do meio-campo!")
elif Func == "Ponta" or Func == "Atacante" or Func == "Cemtroavante":
    print (f"O(a) {Nome} faz parte do ataque!")
else:
    print ("Ele(a) e teimoso!")           