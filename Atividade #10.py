# Qual e o seu time favorito...

print ("Digite um número para caso você seja pra um desses 3: ")
print ("1. Sou Carioca ")
print ("2. Sou Paulista ")
print ("3. Sou Mineiro ")
print ("4. Nenhuma das opções ")

Local = int(input())

if Local == 1:
    print ("Então qual e o seu time carioca favorito? ")
    print ("1. Flamengo ")
    print ("2. Botafogo ")
    print ("3. Vasco ")
    Rj = int(input())
    match Rj:
        case 1:
            print ("Então seu time favorito é o Flamengo😎")
        case 2:
            print ("Então seu time favorito é Botafogo🥵 ")
        case 3:
            print ("Então seu time favorito é Vasco 🥴")

elif Local == 2:
    print ("Então qual e o seu time paulista favorito? ")
    print ("1. São Paulo ")
    print ("2. Corintians ")
    print ("3. Palmeiras ")
    Sp = int(input())
    match Sp:
        case 1:
            print ("Então seu time favorito é São Paulo 🤣")
        case 2:
            print ("Então seu time favorito é Corintians🤢")
        case 3:
            print ("Então seu time favorito é Palmeiras 🥱")

elif Local == 3:
    print ("Então qual e o seu time mineiro favorito ?")
    print ("1. Atletico Mineiro ")
    print ("2. Cruzeiro ")
    print ("3. America MG ")
    Mg= int(input())
    match Mg:
        case 1:
            print ("Então seu time favorito é Atletico Mineiro ")
        case 2:
            print ("Então seu time favorito é Cruzeiro ")
        case 3:
            print ("Então seu time favorito é America MG ")

else:
    Out = input("Então de onde você é? ")
    OutFav = input("É qual e o seu time favorito? ")
    print (f"Então seu time favorito é {OutFav}.")