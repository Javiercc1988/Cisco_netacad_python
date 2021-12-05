archivo = input("Introduce el nombre del archivo: ")

diccionario = {}
texto_limpio = ""
valores = []
dicc_limpio = {}

with open(archivo + ".txt", "r") as t:
    texto = t.read().lower()

    for i in texto:
        if i.isalpha():
            if i not in diccionario:
                diccionario[i] = 1
            else:
                diccionario[i] += 1


########### ORDENAR DICCIONARIO ###########

for i in diccionario:
    valores.append(diccionario[i])
valores.sort(reverse=True)

while len(valores) > 0:

    for llave,valor in diccionario.items():
        if valor == valores[0]:
            dicc_limpio[llave] = valor
            del valores[0]
        
        if len(valores) == 0:
            break

########### GRABAR EN ARCHIVO DE TEXTO ###########

grabar = open(archivo+".hist"+".txt", "w")

for i in dicc_limpio:
    linea = str(i) + " --> " + str(dicc_limpio[i]) + "\n"
    grabar.write(linea)