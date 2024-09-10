# Demonstração do uso do if/elif/else...
UAge = int(input ("Digite sua idade:"))

if UAge < 18:
    print ("Você não e maior de idade!")
    print ("Não podera utilizar de nossos serviços!")

elif UAge >= 65:
    print ("Você já está pronto para se aposentar?")
    print ("Poderemos oferecer nossos serviços para você?")
    UOpn = input ()    

else:
    print ("Você e maior de idade!")
    print ("Portanto podera usar nossos serviços!")
    UOpn = input ()      

print ("Obrigado por optar pelo nossos serviços! ")