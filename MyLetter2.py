# inserção de dados...

print ("Data de Hoje: ")
Date = input ()
print (" Nome da empresa: ")
Enterprise = input ()
print ("Nome do gestor ou responsavel pelo RH: ")
RH = input ()
print ("Qual e o titulo do seu posto? ")
TitleCarg = input ()
print ("Qual seria o seu cargo atual na empresa? ")
Carg = input ()
print ("Data do inicio do aviso previo: ")
Start =  input ()
print ("Data do termino do aviso previo: ")
Stop = input ()
print ("Local da emissão da carta")
Local = input ()
print ("Sua assinatura: ")
Ass = input ()
print ("Digite seu nome completo: ")
Name = input ()

# Carta de demissão...

print ("A ", Enterprise)
print ("Prezado(a)", RH)
print ("Venho por meio desta carta comunicar formalmente meu pedido de demissão do cargo de ", Carg)
print ("Estarei a disposição da empresa durante o aviso prévio, no periodo de ", Start, "a ", Stop)
print (Local, Date)
print (Ass)
print (Name)