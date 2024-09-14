X = 1
Y = 0
for X1 in range (0, 2000):
    Z = X + Y
    Y = X + Z
    X = Z + Y
    print (X1)