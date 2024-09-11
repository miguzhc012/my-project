# Minhas ações no dia...
print ("---------------------------------------")
print ("O que você vai fazer amanhã de manhã?")
print ("dormir / estudar / planejar")
print ("---------------------------------------")

Morning = input ()
print ("---------------------------------------")
print ("O que você vai fazer amanhã a tarde?")
print ("jogar / treinar / trabalhar")
print ("---------------------------------------")

afternoon = input ()

if not Morning or not afternoon:
    print ("---------------------------------------")
    print ("Você precisa dizer o que vai fazer!")
    print ("---------------------------------------")

else:
    if Morning == "dormir" or afternoon == "jogar":
        print ("---------------------------------------")
        print ("Você está desperdiçando seu dia!")   
        print ("---------------------------------------") 
    elif Morning == "estudar" or afternoon == "treinar":
        print ("---------------------------------------")
        print ("Que bom! Você ira se aperfeiçoar!")
        print ("---------------------------------------") 
    elif Morning == "planejar" and afternoon == "trabalhar":
        print ("---------------------------------------")
        print ("Para trabalhar melhor devo me planejar!")
        print ("---------------------------------------")        
    else:
        print ("---------------------------------------")
        print ("Não combinamos essas ações...")
        print ("---------------------------------------")

print ("Tenha um bom dia! ")
