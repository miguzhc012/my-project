# Agenda da semana...

print ("Digite um número de acordo com o dia:")
print ("1. Segunda-feira")
print ("2. Terça-feira")
print ("3. Quarta-feira")
print ("4. Quinta-feira")
print ("5. Sexta-feira")
print ("6. Sabado")
print ("7. Domingo")
MyCallendar = int(input())

match MyCallendar:
    case 1:
        print ("Na Segunda você tem: Aula de yoga, prova de matematica, prova de historia, academia e faculdade")
    case 2:
        print ("Na Terça você tera: prova de quimica, prova de biologia, prova de fisica, academia e faculdade") 
    case 3:
        print ("Na Quarta você tera: Aula de yoga, prova de portugues, prova de ingles, prova de geografia, academia e faculdade")
    case 4:
        print ("Na Quinta você tera: Prova de projeto de vida, prova de eletiva, prova de literatura, academia e faculdade")
    case 5:
        print ("Na Sexta feira você tera: Aula de yoga, academia e faculdade")
    case 6:
        print ("No Sabado você tera: churrasco com seus pais e encontro com sua esposa ") 
    case 7:
        print ("No Domingo você tera: Festa com seus amigos")
