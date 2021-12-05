c0 = int(input("Introduce un número: "))
contador = 0

while c0 != 1:
    contador +=1
    if c0 % 2 == 0:
        c0 = c0/2
    else:
        c0 = (3*c0)+1
    
print(contador)