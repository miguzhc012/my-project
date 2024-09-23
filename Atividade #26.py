name = [2, 20, 16, 12, 15, 6, 8, 10, 19, 3]
max = max (name)
min = min (name)
print (min, max)
for i in range(1):
    name.sort()
    print (name)
    print (name[0], name [9])
    for i in range(len(name)):
        if name[i] % 2 == 0:
            print ("Par")
        else:
            print ("impar")    