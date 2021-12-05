beatles = []
# paso 1
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# paso 2
print("Paso 2:", beatles)

for i in range(1,3):
    nombre = input("Introduce un nombre: ")
    beatles.append(nombre)
    
# paso 3
print("Paso 3:", beatles)

del(beatles[3])
del(beatles[3])

# etapa 4
print("Paso 4:", beatles)

beatles.insert(0,"Ringo Starr")
# paso 5
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
