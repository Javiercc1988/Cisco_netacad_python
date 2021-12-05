bloques = int(input("Ingrese el número de bloques:"))
capa = 0

while capa < bloques:
    capa += 1
    bloques -= capa

print("La altura de la pirámide:", capa)